num = int(input('Digite um número e verifique se ele pertence aos 10 primeiros números da sequência de Fibonacci: '))
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

while num not in fibonacci:
    print('O número não pertence aos 10 primeiros números da lista de Fibonacci')
    num = int(input('Digite um número e verifique se ele pertence aos 10 primeiros números da sequência de Fibonacci: '))
print('O número pertence a sequência de Fibonacci')
