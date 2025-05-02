# python -m pip install pytz types-pytz
from datetime import datetime, timedelta
from pytz import timezone

format = '%d/%m/%Y'
data1 = datetime.now(timezone('America/Sao_Paulo'))
data2 = datetime.strptime('12/12/2000', format)
data3 = datetime.strptime('12/12/1990', format)

print(f'Data1: {data1}')
print(f'Data2: {data2}')

print ('Timestamp: ', data1.timestamp())
print(f'Timestamp convertido: {datetime.fromtimestamp(data1.timestamp())}')

print(f'Diferença em dias: {(data2 - data3).days}')

delta = timedelta(days=10)
print(f'Adicionando {delta.days} dias em {data2.strftime(format)}: {(data2 + delta).strftime(format)}')

