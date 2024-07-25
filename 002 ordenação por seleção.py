from random import randint

def ordenacao_por_selecao(arr):
    novo_arr = [];
    for _ in range(len(arr)):
        menor_indice = busca_menor(arr)
        novo_arr.append(arr.pop(menor_indice))
        
    return novo_arr

def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    
    return menor_indice

def main():
    LENGTH = 20
    arr = list(randint(0, LENGTH) for _ in range(LENGTH))
    print(f"{arr=}")
    arr_ordenado = ordenacao_por_selecao(arr)
    print(f"{arr_ordenado=}")
    
if __name__ == '__main__':
    main()