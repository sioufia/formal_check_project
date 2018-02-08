from itertools import product
from collections import defaultdict

from constraint_programming import constraint_programming as CSP
from control_graph import Graph, find_vertice_with_label

from Control_Graphs.CG_Project_Example import CG_Project_Example

def test_generation(graph,path):
    """Generate test data's predicate from a given path and graph

    :param path: list of labels
    :param graph:
    :return:
    """

    variables_domains = {}  # de la forme : variables_domains['X']={1,2,3}
    variable_names = list(variables_domains.keys())

    # Larger Domain possible
    general_domain = set(range(-10, 11))
    for var in graph.var:
        variables_domains[var] = set(general_domain)

    constraints = {}  # de la forme : constraints[('X','Y')]={(1,2),(2,3),(3,4)}

    iter_path = iter(reversed(path))
    cur_label = next(iter_path)
    cur_vert = find_vertice_with_label(graph, cur_label)

    # How compute each label from the given path in reverse
    for previous_label in iter_path:

        # Corresponding vertice to the label
        previous_vert = find_vertice_with_label(graph, previous_label)

        # edge from previous vert to cur_vert
        edge = [n_e for n_e in previous_vert.next_edges if n_e.next_label == cur_label][0]

        # Apply reverse command of the edge on variables
        command = edge.command
        previous_variables_domains_1 = defaultdict(set)

        for possible_variable in possible_variables(variables_domains, constraints):
            previous_variables = command.reverse_execute(possible_variable)

            for var, value in previous_variables.items():
                previous_variables_domains_1[var].add(value)

        # We now have an intermediary variables domains
        # Always going backward in our symbolic execution
        # We apply reverse condition on the edge

        condition = edge.condition
        previous_variables_domains_2 = defaultdict(set)
        for possible_variable in possible_variables(previous_variables_domains_1, constraints):
            if condition.evaluate(possible_variable):
                for var, value in possible_variable.items():
                    previous_variables_domains_2[var].add(value)

        # We assign the variables domains with the expected variables domain computed
        variables_domains = previous_variables_domains_2

        # We move one step backward
        cur_label = previous_label
        cur_vert = previous_vert

    # Our Constraint Problem
    P = CSP(variables_domains)

    # We add to the probelm binary constraint
    for (x, y), constraints_x_y in constraints.items():
        P.addConstraint(x, y, constraints_x_y)

    # We return the solution of our problem
    return P.solve()


def possible_variables(variables_domains, constraints):
    """compute the possible values of our variables in a given state and a set of constraints"""
    result = []
    variable_names = list(variables_domains.keys())
    for possible_values in product(*(variables_domains.values())):
        buffer_vars = dict()
        for i, var in enumerate(variable_names):
            buffer_vars[var] = possible_values[i]
        if all((buffer_vars[var1], buffer_vars[var2]) in constraint for (var1, var2), constraint in
               constraints.items()):
            result.append(buffer_vars)
    return result

if __name__=="__main__":
    CG=CG_Project_Example()

    print(test_generation(CG,[1,2,4,5,'exit']))

    print(test_generation(CG,[1,2,4,6,'exit']))
