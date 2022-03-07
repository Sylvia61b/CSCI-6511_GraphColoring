from CSP import CSP, backtracking


class Graph:
    # Basic constructor method
    def __init__(self, edge_list):
        # Convert edge list to adjacency list,
        # represented with a multi-dimensional array

        self.graph_dict = {}

        # Add edges to corresponding nodes of the graph
        for (origin, dest) in edge_list:
            if origin not in self.graph_dict:
                self.graph_dict[origin] = [dest]
                if dest not in self.graph_dict:
                    self.graph_dict[dest] = [origin]
                else:
                    self.graph_dict[dest].append(origin)
            else:
                if dest not in self.graph_dict:
                    self.graph_dict[dest] = [origin]
                else:
                    self.graph_dict[dest].append(origin)
                self.graph_dict[origin].append(dest)


def get_vertices(edge_list):
    vertices_set = set()
    for (origin, dest) in edge_list:
        vertices_set.add(origin)
        vertices_set.add(dest)
    return vertices_set


def read_file(filename):
    edges = []
    num_color = 0
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
    is_color = True
    for line in lines:

        if line.startswith("#"):
            continue
        else:
            if is_color:
                text, num_color = line.strip('\n').split("=")
                num_color = num_color.strip()
                is_color = False
            else:
                index = lines.index(line)
                edges = [(edge.strip().split(",")) for edge in lines[index:]]
                return num_color, edges


def init(num_color, edge_list):
    color_graph = Graph(edge_list)
    domains = {}
    print("The Graph Dictionary- Node: Neighbors ")

    for node in color_graph.graph_dict:
        result = ""
        for neighbour in color_graph.graph_dict[node]:
            result += str(neighbour) + ","
        print(node, ":", result)

    for node in color_graph.graph_dict:
        domains[node] = [color for color in range(int(num_color))]

    csp = CSP(color_graph.graph_dict, domains)
    return csp


if __name__ == '__main__':
    num_color, edge_list = read_file("test0.txt")
    csp = init(num_color, edge_list)
    solution = backtracking(csp, {})
    print("Solution(node,color):{0} ".format(solution))
