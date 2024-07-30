from collections import deque

def main():
    graph = {}
    graph['Myke'] = ['Alice', 'Bob', 'Claire']
    graph['Alice'] = ['Peggy']
    graph['Bob'] = ['Peggy', 'Anuj']
    graph['Claire'] = ['Thom', 'Jonny']
    graph['Peggy'] = []
    graph['Anuj'] = []
    graph['Thom'] = []
    graph['Jonny'] = []
    
    check_end = lambda element: element.endswith('n')
    
    result = search_width(graph=graph, start="Myke", check_end=check_end)
    print(f"{result=}")

def search_width(graph, start, check_end):
    deq = deque(graph[start])
    visited = set()

    while deq:
        current = deq.popleft()
        print(f"{current=}")
        print(f"{deq=}")
        if current in visited:
            continue
        
        if check_end(current):
            return True
        
        visited.add(current)
        deq += graph[current]
            
    return False

if __name__ == "__main__":
    main()