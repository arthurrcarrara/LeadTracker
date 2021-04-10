def sequenciaFibonacci(n):
    count = 1
    penultimo = 1
    ultimo = 1
    proximo = 0
    while ( count <= n):

        if( count == 1) or (count == 2):
            print("1")
            count = count + 1
        else:
            proximo = penultimo + ultimo
            penultimo = ultimo
            ultimo = proximo
            print(proximo)
            count = count + 1

n = input("Quantos elementos da sequencia Fibonacci voce deseja:")

n = int(n)

sequenciaFibonacci(n)