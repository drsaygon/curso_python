from pathlib import Path
from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell import Cell

ROOT_FOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOT_FOLDER / 'workbook.xlsx'

workbook: Workbook = load_workbook(WORKBOOK_PATH)
worksheet: Worksheet = workbook['Teste']

r: tuple[Cell]

for r in worksheet.iter_rows(min_row=1):
    for c in r:
        if c.value == 'Maria':
            r[1].value = 30 
        print(c.value, end='\t')
    print()


# B3 = worksheet['B3']
# VALOR_ATUAL = B3.value
# VALOR_NOVO = B3.value = 14

workbook.save(WORKBOOK_PATH)

# print(f'Mudando a célula B3 de {VALOR_ATUAL} para {VALOR_NOVO}')

