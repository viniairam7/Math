ind = str(input('Você se identifica como? [M/F]  ')).strip().upper()[0]
while ind not in 'MmFf':
    ind = str(input('Por favor, escolha uma opção válida! Você se identifica como? [M/F]  ')).strip().upper()[0]
print('Sexo registrado com sucesso!')

