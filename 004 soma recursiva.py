def main():
    arr = [1, 2, 3]
    print(f"{arr=}")
    soma = soma_recursiva(arr)
    print(f"{soma=}")
    
    arr = []
    print(f"{arr=}")
    soma = soma_recursiva(arr)
    print(f"{soma=}")

def soma_recursiva(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + soma_recursiva(arr[1:])
    
if __name__ == '__main__':
    main()