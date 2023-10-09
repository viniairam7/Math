while True:
    n = int(input('Tabuada do :  '))
    if n < 1:
        break
    print('/' * 20)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}.')
    print('/'*20)
    print('Digite 0 (zero) se quiser encerrar.')
    print('/' * 20)
print('TABUADA ENCERRADA!')