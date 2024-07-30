from copy import deepcopy

graph = {
    "Inicio": {
        "A": 6,
        "B": 2,
    },
    "A": {
        "Fim": 1
    },
    "B": {
        "A": 3,
        "Fim": 5
    },
    "Fim": {}
}

custos = deepcopy(graph["Inicio"])
processados = []

nodo = 