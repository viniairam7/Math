from moedas import metade, dobro, aumentar

p = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {p} é R$ {metade(p)}')
print(f'O dobro de R$ {p} é R$ {dobro(p)}')
print(f'Aumentando 10%, é igual a R$ {aumentar(p, 10)}')