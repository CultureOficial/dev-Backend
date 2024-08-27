maior_numero = 0 

for i in range(5):
    numero = int(input("Digite um número: "))
    if numero > maior_numero:
        maior_numero = numero

print("O maior número é:", maior_numero)
