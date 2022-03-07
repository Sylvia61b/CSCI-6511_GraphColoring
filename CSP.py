from copy import deepcopy
from operator import itemgetter


class CSP:
    def __init__(self, graph_dict, domains):
        self.graph_dict = graph_dict
        self.domains = domains


def backtracking(csp, assignment: {}):
    # assignment complete
    if is_complete(csp.graph_dict, assignment):
        return assignment
    # get all the unassigned nodes
    # unassigned = [node for node in csp.graph_dict if node not in assignment]
    # current_node = unassigned[0]

    # select node with min values left in domain
    current_node = minimum_remaining_values(csp, assignment)
    print("Select Node {}".format(current_node))

    # try to assign a possible value in domains for current node
    # select value which will rule out the least values in neighbor domains
    for value in least_constraining_value(csp, current_node, assignment):
        print("before")
        print(csp.domains)
        temp_assignment = assignment.copy()
        temp_assignment[current_node] = value
        temp_csp = deepcopy(csp)
        csp.domains[current_node] = [value]
        print("Select Color " + str(value) + " for Node " + str(current_node))
        if is_consistent(current_node, value, temp_assignment, csp.graph_dict):
            # if csp.forward_checking(current_node, value, assignment):
            # check consistent among all domains
            if AC3(csp):
                print("after")
                print(csp.domains)
                result = backtracking(csp, temp_assignment)
                # if there is a result , return it
                if result is not None:
                    return result
        else:
            print("after")
            print(csp.domains)
        print("Not consistent")
        print("{} for node {} fails, Reselect color for node{}".format(value, current_node, current_node))
        # if not consistent, unassigned csp
        csp = temp_csp
    print("Failure for Node {}".format(current_node))
    return None


def is_consistent(current_node, value, assignment, graph_dict):
    # if there is no value can be assigned to the current node
    if assignment is None:
        return False
    # check if neighbors has already been assigned to the color
    for neighbor in graph_dict[current_node]:
        # if the neighbor has been assigned
        if neighbor in assignment:
            # if the value conflict with neighbor's value
            if value == assignment[neighbor]:
                print(str(current_node) + ":" + str(value) + " conflicts with " + str(neighbor) + ":" + str(
                    assignment[neighbor]))
                return False
    # all the values of neighbors don't conflict with the new assignment
    return True


def forward_checking(csp, current_node, value, assignment):
    unassigned_neighbors = [neighbor for neighbor in csp.graph_dict[current_node] if neighbor not in assignment]
    for neighbor in unassigned_neighbors:
        if value in csp.domains[neighbor]:
            print("Remove " + str(value) + " from " + str(neighbor))
            csp.domains[neighbor].remove(value)
            if len(csp.domains[neighbor]) == 0:
                print("There is no value can be selected for " + str(neighbor))
                return False
    return True


def minimum_remaining_values(csp, assignment):
    unassigned_nodes = [node for node in csp.graph_dict if node not in assignment]
    # get the nodes with minimum remaining value
    min_count = min([len(csp.domains[node]) for node in unassigned_nodes])
    min_nodes = [node for node in unassigned_nodes if len(csp.domains[node]) == min_count]
    # get the nodes that are most constraint
    most_constraint_count = max([len(csp.graph_dict[node]) for node in min_nodes])
    select_nodes = [node for node in min_nodes if len(csp.graph_dict[node]) == most_constraint_count]
    return select_nodes[0]


def least_constraining_value(csp, current_node, assignment):
    neighbors = csp.graph_dict[current_node]
    value_count = []
    for value in csp.domains[current_node]:
        count = 0
        for neighbor in neighbors:
            if neighbor not in assignment:
                if value in csp.domains[neighbor]:
                    count = count + 1
        value_count.append((value, count))
    sorted_count = sorted(value_count, key=itemgetter(1))
    print("Neighbors domain(color, count): {}".format(sorted_count))
    for value, count in sorted_count:
        yield value


def AC3(csp):
    # print("The domain before AC3 is {}".format(csp.domains))
    queue = []
    for node in csp.graph_dict:
        for neighbor in csp.graph_dict[node]:
            queue.append((node, neighbor))

    while len(queue) != 0:
        xi, xj = queue.pop()
        # once removed the value from the node,keep checking inconsistent for its neighbors
        if remove_inconsistent_value(xi, xj, csp):
            # if the domains is empty after removal
            if len(csp.domains[xi]) == 0:
                print("no value")
                return False
            else:
                for xk in csp.graph_dict[xi]:
                    queue.append((xk, xi))

    # print("The domain after AC3 is {}".format(csp.domains))
    return True


def remove_inconsistent_value(xi, xj, csp):
    removed = False

    for value in csp.domains[xi]:
        if all(y == value for y in csp.domains[xj]):
            csp.domains[xi].remove(value)
            print("\t Color {} is removed for node {}, contradicts with node {}".format(value, xi, xj))
            removed = True
    return removed


def is_complete(graph_dict, solution):
    return True if len(graph_dict) == len(solution) else False
