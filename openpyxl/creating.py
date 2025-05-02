from pathlib import Path
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

ROOT_FOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOT_FOLDER / 'workbook.xlsx'

workbook = Workbook()
workbook.create_sheet('Teste', 0)
worksheet: Worksheet = workbook['Teste']

workbook.remove(workbook['Sheet'])

# Headers
worksheet.cell(1, 1, 'Nome')
worksheet.cell(1, 2, 'Idade')
worksheet.cell(1, 3, 'Nota')

students = [
    # nome      idade   nota
    ['João',    14,     5.5],
    ['Maria',   13,     9.7],
    ['Luiz',    15,     8.8],
    ['Alberto', 16,     10],
]

# for r, students_row in enumerate(students, start=2):
#     for c, stundets_col in enumerate(students_row, start=1):
#         worksheet.cell(r, c, stundets_col)

# Simplificado
for student in students:
    worksheet.append(student)

workbook.save(WORKBOOK_PATH)