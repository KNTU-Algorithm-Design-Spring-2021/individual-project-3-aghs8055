MAX_VALUE = 22

class node:
    def __init__(self, value):
        self.neighbors = []
        self.value = value
        self.visit = False
    def add_neighbors(self, value):
        self.neighbors.append(value)
    def change_visit(self):
        self.visit = not self.visit
    def visited(self):
        return self.visit
    def get_neighbors(self):
        return self.neighbors
    def get_value(self):
        return self.value

class graph:
    def __init__(self):
        self.v = MAX_VALUE
        self.nodes = [node(i) for i in range(self.v)]
    def add_edge(self, node1, node2):
        self.nodes[node1].add_neighbors(self.nodes[node2])
        self.nodes[node2].add_neighbors(self.nodes[node1])
    def get_node(self, value):
        return self.nodes[value]

def promising(maps, cur_node):
    return not cur_node.visited()

def paths(maps, cur_node, path, k):
    if cur_node.get_value() == k:
        path.append(k)
        print("-".join([str(i) for i in path]))
        path.pop()
        return
    if not promising(maps, cur_node):
        return
    cur_node.change_visit()
    path.append(cur_node.get_value())
    for i in cur_node.get_neighbors():
        paths(maps, i, path, k)
    cur_node.change_visit()
    path.pop()

if __name__ == "__main__":
        case = int(input("Enter count of cases: "))
        for i in range(case):
            k = int(input("Enter value of destination: "))
            print("Enter edges: ")
            maps = graph()
            while True:
                node1, node2 = map(int,input().split())
                if (node1, node2) == (0, 0):
                    break
                maps.add_edge(node1, node2)
            print("Case #{}:".format(i+1))
            paths(maps, maps.get_node(1), [], k)
