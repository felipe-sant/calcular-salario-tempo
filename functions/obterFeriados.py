import requests
import datetime

def obterFeriados(ano: int) -> list:
    api_key = "kkep07qEKa4x1VxzOtHXq5fyf9RpYhNp"
    url = f"https://calendarific.com/api/v2/holidays?&api_key={api_key}&country=BR&year={ano}"
    response = requests.get(url)
    data = response.json()
    
    feriados = []
    for holiday in data['response']['holidays']:
        date_str = holiday['date']['iso'].split('T')[0]
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        feriados.append(date)
        
    return feriados

# Path: functions/obterFeriados.py    