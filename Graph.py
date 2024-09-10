class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_adj_list(self):
        for vertex, value in self.adj_list.items():
            print(vertex, ':', value)

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edges(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for edge in self.adj_list[vertex]:
                self.adj_list[edge].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.print_adj_list()

my_graph.add_edges('A', 'B')
my_graph.add_edges('A', 'C')
my_graph.add_edges('A', 'D')
my_graph.add_edges('B', 'D')
my_graph.add_edges('C', 'D')
print('\nafter adding edges')
my_graph.print_adj_list()

my_graph.remove_edges('A', 'D')
print('\nafter removing edges')
my_graph.print_adj_list()

my_graph.remove_vertex('D')
print('\nafter removing the vertex D')
my_graph.print_adj_list()