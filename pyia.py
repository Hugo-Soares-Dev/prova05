#Crie uma função chamada maior_numero que receberá três números como argumentos. #Esta função deve comparar os três números e identificar qual deles é o maior. Para #isso, utilize uma estrutura de controle que verifique qual número é maior que os #outros dois. A função deve então retornar o maior número encontrado.
cor = lambda valor:f'\033[7;33m{valor}\033[m'
def maior_numerro (n1:int, n2: int, n3:int):
    maior = n1
    if n2 > n1 and n2 > n3:
        maior = n2
    elif n3 > n1 and n3 > n2:
        maior = n3
    return maior

n1 = int(input('digite o 1° numero: '))
n2 = int(input('Digite o 2° numero: '))
n3 = int(input('Digite o 3° numero: '))


valor = maior_numerro(n1,n2,n3)

print(f'O maior numero encontrado foi: {cor(valor)}')