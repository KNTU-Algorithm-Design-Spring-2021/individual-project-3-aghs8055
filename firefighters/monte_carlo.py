from random import randint

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
    def get_nodes(self):
        return self.nodes

def estimate(m, t, level):
    result=1
    coefficient=1
    for i in range(level):
        result+=coefficient*t[i]
        coefficient*=m[i]
    return result

def promising(maps, cur_node):
    return not cur_node.visited()

def paths(maps, cur_node, m, t , k, level):
    t[level]=len(cur_node.get_neighbors())
    if cur_node.get_value() == k:
        return estimate(m, t, level)
    if not promising(maps, cur_node):
        return estimate(m, t, level)
    promising_nodes=[]
    for i in cur_node.get_neighbors():
        if promising(maps, i):
            promising_nodes.append(i)
    m[level]=len(promising_nodes)
    if m[level]==0:
        return estimate(m, t, level)
    promising_node=promising_nodes[randint(0,m[level]-1)]
    cur_node.change_visit()
    return paths(maps, promising_node, m, t, k, level+1)

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
            result=0
            for i in range(200):
                for i in maps.get_nodes():
                    i.visit=False
                m,t,level=[0 for i in range(23)],[0 for i in range(23)],0
                result+=paths(maps, maps.get_node(1), m, t, k, 0)
            print("The estimated count of promising nodes is: {}".format(result//200))
