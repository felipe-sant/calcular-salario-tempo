import datetime

def obterDiasUteis(mes, ano, diasExcluidos):
    inicio = datetime.date(ano, mes, 1)
    if mes == 12:
        fim = datetime.date(ano + 1, 1, 1)
    else:
        fim = datetime.date(ano, mes + 1, 1)
    
    dias_uteis = 0
    
    while inicio < fim:
        if inicio.weekday() < 5 and inicio not in diasExcluidos:
            dias_uteis += 1
        inicio += datetime.timedelta(days=1)
    
    return dias_uteis

# Path: functions/obterDiasUteis.py