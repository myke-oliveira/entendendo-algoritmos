from sys import setrecursionlimit

def estourando_a_pilha_de_chamada(i):
    print(i)
    estourando_a_pilha_de_chamada(i+1)
    
setrecursionlimit(10**6)

estourando_a_pilha_de_chamada(0)