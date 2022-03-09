# https://docs.python.org/3/library/datetime.html

from datetime import date, time, datetime, timedelta
# date = data, time = horário, datetime = data com horário, timedelta = subtração e soma com datas


def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y'))  # para formatar a data como string usando as diretivas do Python
    # pode ser colocado /, - ou qualquer outra coisa. O que importa é a diretiva
    print(data_atual.strftime('%A %B %Y'))

    # Uma vez convertido date para string, não é possível reconvertê-lo.


def trabalhando_com_time():
    # criar um horário usando time:
    horario = time(hour=15, minute=10, second=30)
    print(horario)
    print(horario.strftime('%Hh%Mmin%Ss'))


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.month)
    print(data_atual.minute)
    print(data_atual.weekday())
    tupla_dias_semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla_dias_semana[data_atual.weekday()])
    data_criada = datetime(2010, 1, 1, 7, 0, 10)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/02/2000 10:49:12'
    data_convertida = datetime.strptime(data_string, '%m/%d/%Y %H:%M:%S')
    print(data_convertida)
    print(data_convertida.strftime('%c'))
    subtracao_data = data_convertida - timedelta(days=365)
    print(subtracao_data)
    soma_data = data_criada + timedelta(weeks=7, hours=10, seconds=30, minutes=55)
    print(soma_data)


if __name__ == '__main__':
    # working_with_date()
    # working_with_time()
    trabalhando_com_datetime()
