
from datetime import date, time, datetime, timedelta

def trabalhando_com_date_time():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H/%M/%S')) ## NO "%" PODEMOS PASSAR OS PARÂMETROS QUE QUISERMOS CONFORME DOCUMENTAÇÃO
    print(data_atual.strftime('%c')) ## O "%C" JÁ TRAZ UMA DATA PADÃO COMPLETA
    print(data_atual.day)
    ## PARA FAZER TRADUZIDO
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])

## CONVERTER STRING PARA DATE TIME
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    print(type(data_convertida))
## OPERAÇÕES COM DATAS (TIMEDELTA)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15) ## MENOS UM ANO, DIAS, HORAS E MINUTOS
    print(nova_data)

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))

    data_atual = date.today()
    print(data_atual.strftime('%A %B %Y'))

    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual)) ## EM FORMATO DE DATA. ACESSA OS MÉTODOS DE DATA
    print(data_atual_str)
    print(type(data_atual_str)) ## EM FORMATO DE STRING. ACESSA OS MÉTODOS DE STRING

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_date_time()