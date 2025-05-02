# pip install python-dateutil
from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

for data in data_parcelas:
    print(data)

print(f'Número de parcelas: {numero_parcelas}')

# print(f'Valor de parcela: R$ {valor_parcela:,.2f}')

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
print(f'Valor de parcela: {locale.currency(valor_parcela, grouping=True)}')

