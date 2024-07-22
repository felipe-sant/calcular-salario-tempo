from functions.obterFeriados import obterFeriados
from functions.obterDiasUteis import obterDiasUteis
from utils.limparTerminal import limparTerminal

mes = int(input("Digite o mês (MM): "))
ano = int(input("Digite o ano (YYYY): "))

feriados = obterFeriados(ano)
diasUteis = obterDiasUteis(mes, ano, feriados)

print(diasUteis)
input()

limparTerminal()