from Módulos2 import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {moedas.moedas(p)} é R$ {moedas.metade(p, True)}')
print(f'O dobro de R$ {moedas.moedas(p)} é R$ {moedas.dobro(p, True)}')
print(f'Aumentando 10%, é igual a R$ {moedas.aumentar(p, 10, True)}')