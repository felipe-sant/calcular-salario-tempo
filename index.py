from functions.obterFeriados import obterFeriados
from functions.obterDiasUteis import obterDiasUteis
from utils.limparTerminal import limparTerminal
from utils.formatarTexto import formatarTexto_azul, formatarTexto_italico, formatarTexto_negrito

salario = float(input(f"Digite o seu {formatarTexto_negrito("salário:")} "))
mes = int(input(f"Digite o {formatarTexto_negrito("mês")} {formatarTexto_italico("(MM)")}: "))
ano = int(input(f"Digite o {formatarTexto_negrito("ano")} {formatarTexto_italico("(YYYY)")}: "))

feriados = obterFeriados(ano)
diasUteis = obterDiasUteis(mes, ano, feriados)
salario_por_dia = round((salario / diasUteis), 2)

print("\nDias úteis no mês:", formatarTexto_azul(diasUteis))
print("Salário por dia:", formatarTexto_azul(salario_por_dia))
input()

limparTerminal()