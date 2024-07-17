#! /usr/bin/env python

my_list = list(range(100))

def main():
    target = int(input("Type a target as integer:"))
    index, value, number_of_interations = binary_search(my_list, target)
    print(f"{index=}, {value=}, {number_of_interations=}")

def binary_search(data, target):
    '''
    # Tamanho do array para testar a cada iteração

    f(i) = n/(2**i)

    # Ao finalizar f(i) = 1, então o total de iterações

    1 = n / (2**i)

    2**i = n

    i = log_2(n)

    # Complexidade de tempo: O(log(n))
    '''
    start_index = 0
    end_index = len(data) - 1
    number_of_interations = 0
    while True:
        number_of_interations += 1
        i = (start_index + end_index) // 2
        if data[i] == target:
            return i, data[i], number_of_interations

        if start_index >= end_index:
            return None, None, number_of_interations

        if target < data[i]:
            end_index = i
            continue

        start_index = i

if __name__ == "__main__":
    main()

