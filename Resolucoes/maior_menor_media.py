import math

#Recebe quatro números do usuario e guarda em um array
#depois imprime o maior número, o menor número e a media entre os números do array.
def main():
    arr = []
    menor = 0
    maior = 0

    for i in range(4):
        arr.append(int(input(f"Digite o {i + 1}º numero: ")))

        if menor > arr[i] or menor == 0:
            menor = arr[i]

        if maior < arr[i]:
            maior = arr[i]

    if arr.__contains__(0):
        menor = 0

    print(f'O arry de numeros é {arr}')
    print(f'O menor numero é {menor}')
    print(f'O maior numero é {maior}')

    # Forma simplificada de resolver utilizando a biblioteca math
    # "print(f'min {min(arr)}')"
    # "print(f'max {max(arr)}')"

    print(f'A media é {math.fsum(arr) / len(arr)}')


if __name__ == '__main__':
    main()