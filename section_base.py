from abc import ABCMeta
from stratboxcore.library.variables.constants import Currencies
from stratboxcore.library.csv_fields import FieldName
from stratboxcore.library.etl.raw_data.constants import (
    OTHER_SEGMENT_NAME,
    TemplateConfig,
    DEFAULT_ALL_PERIODS_VALUE,
)
from stratboxcore.library.etl.raw_data.file_configs import ConfigLine
from stratboxcore.library.metric_datatypes import METRIC_DATATYPES

class SectionBase(metaclass=ABCMeta):
    def __init__(
        self, scenario, exercise, config: ConfigLine, template_config: TemplateConfig
    ):
        self.scenario = scenario
        self.exercise = exercise
        self.config = config
        self.template_config = template_config
        self.is_business_unit_active = {
            bu["name"]: bu.get("isActive", True)
            for bu in exercise.get("business_units", {}).get("last_level", [])
        }
        self.is_scenario_active = {
            sc["name"]: sc.get("isActive", True)
            for sc in exercise.get("alternative_scenarios", [])
            if isinstance(sc, dict)
        }
        self.data = []
        self.issues = []
        self.warnings = []
        self.SAME_ROW_SEGMENTATION = set(["SAME_ROW"])
        self.NORMAL_MODULE_SEGMENTATION = set(
            ["TRUE", "MARKET_RISK", "CCR_SWITCHBOARD"]
        )
        self.STANDARD_SEGMENTATION = (
            set(["TRUE_AGGREGATE"])
            | self.SAME_ROW_SEGMENTATION
            | self.NORMAL_MODULE_SEGMENTATION
        )
        self.BUSINESS_UNIT_SEGMENTATION = set(["BU-COMPLEX", "BU-AGGREGATE"])

    def _aggregate_business_units(self):
        if self.exercise and self.exercise["business_units"]:
            return [
                bu["name"] if isinstance(bu, dict) else bu
                for bu in self.exercise["business_units"]["level_0"]
            ]
        return []

    def _complex_business_units(self):
        if self.exercise and self.exercise["business_units"]:
            return [
                bu["name"] if isinstance(bu, dict) else bu
                for bu in self.exercise["business_units"]["last_level"]
            ]
        return []

    def _parse_row(self, values_by_column, row_number, segment):
        raise NotImplementedError("_parse_row must be implemented by child class")

    def parse_row_templates_complex_bus(self, values_by_column, row_number, segment):
        row_name = values_by_column.get(3) if values_by_column.get(3) else values_by_column.get(2)
        if not row_name:
            self.issues.append("Row {}: missing row name".format(row_number))

        for bu_index, business_unit in enumerate(self._complex_business_units()):
            bu_column = self.template_config.first_data_column + bu_index * self.template_config.columns_between_groups
            for period_index, period in enumerate(self.exercise["periods"]):
                self._add_value_to_data(
                    self.scenario,
                    segment,
                    business_unit,
                    period,
                    self.config.metric,
                    values_by_column.get(bu_column + period_index),
                )

    def _parse_row_business_units(
        self, values_by_column, row_number, business_units, segment
    ):
        raise Exception("_parse_row_business_units must be implemented by child class")

    def _parse_row_business_unit(
        self, values_by_column, row_number, business_unit, segment
    ):
        raise Exception("_parse_row_business_unit must be implemented by child class")

    def _format_business_unit(self, business_unit):
        formatted_bu = business_unit.replace("España", "Espana")
        return formatted_bu.replace("ESPAÑA", "ESPANA")

    def _format_period(self, period):
        return period.replace("E", "")

    def _add_value_to_data(
        self, scenario, segment, business_unit, period, metric_name, value
    ):
        if not self.is_scenario_active.get(scenario, True):
            return
        if not self.is_business_unit_active.get(business_unit, True):
            return
        if (period == self.exercise["periods"][0] and not self.config.first_period) or (
            period != DEFAULT_ALL_PERIODS_VALUE
            and period != self.exercise["periods"][0]
            and not self.config.subsequent_periods
        ):
            return
        if not value:
            self.warnings.append(
                (
                    self.config.row_number,
                    self.config.primary_methodology,
                    segment,
                    metric_name,
                    business_unit,
                    period,
                )
            )
        data_type = METRIC_DATATYPES[metric_name].type
        if data_type == object:
            data_type = str
        if value:
            if value == "#REF!":
                value = 0
            if value == "#NAME?":
                value = 0
            try:
                data_type(value)
            except (TypeError, ValueError) as ex:
                self.issues.append(
                    "Incorrect data type detected for subsegment {}, business unit {}, period {}: {}".format(
                        segment, business_unit, period, str(ex)
                    )
                )
                return
        self.data.append(
            {
                FieldName.SCENARIO: scenario,
                FieldName.CURRENCY: Currencies.LOCAL,
                FieldName.PERIOD: self._format_period(period),
                FieldName.PRIMARY_METHODOLOGY: self.config.primary_methodology,
                FieldName.SUBSEGMENT: segment,
                FieldName.METRIC: metric_name,
                FieldName.BUSINESS_UNIT: self._format_business_unit(business_unit),
                FieldName.VALUE: value,
            }
        )

    def extract_data(self):
        return self.data


class SectionValidationException(Exception):
    def __init__(self, *args, section: SectionBase):
        super().__init__(*args)
        self.section = section

    def __str__(self):
        result = 'Section starting on row {} for primary methodology "{}" and metric "{}": {}'.format(
            self.section.config.row_number,
            self.section.config.primary_methodology,
            self.section.config.metric,
            str(self.args[0]) if self.args else "",
        )
        if self.section.issues:
            result += "".join([f"\n\t\t{ex}" for ex in self.section.issues])
        return result