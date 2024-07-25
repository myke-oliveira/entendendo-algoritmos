def main():
    arr = [1, 2, 3]
    print(f"{arr=}")
    soma = soma_recursiva(arr)
    contagem = conta_items_recursiva(arr)
    maior = maior_valor_recursiva(arr)
    print(f"{soma=}")
    print(f"{contagem=}")
    print(f"{maior=}")
    
    arr = []
    print(f"{arr=}")
    soma = soma_recursiva(arr)
    contagem = conta_items_recursiva(arr)
    maior = maior_valor_recursiva(arr)
    print(f"{soma=}")
    print(f"{contagem=}")
    print(f"{maior=}")

def soma_recursiva(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + soma_recursiva(arr[1:])
    
def conta_items_recursiva(arr):
    if arr == []:
        return 0
    else:
        return 1 + conta_items_recursiva(arr[1:])
    
def maior_valor_recursiva(arr):
    if len(arr) == 0:
        return None
    
    if len(arr) == 1:
        return arr[0]

    item = arr[0]
    recurcao = maior_valor_recursiva(arr[1:])
    return item if item > recurcao else recurcao
    
if __name__ == '__main__':
    main()