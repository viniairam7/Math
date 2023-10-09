print('Gerador de P.A.')
print('°' * 20)
primeiro = int(input('Primeiro Termo:  '))
razão = int(input('Razão de P.A.:  '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('//PAUSA DA P.A.//')
    mais = int(input('Quantos termos você quer mostrar a mais?  '))
print('FIM DA P.A. COM {} TERMOS MOSTRADOS.'.format(total))