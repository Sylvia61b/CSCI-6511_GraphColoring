import unittest
from CSP import CSP, is_complete, minimum_remaining_values, least_constraining_value, remove_inconsistent_value, AC3


class MyTestCase(unittest.TestCase):
    def test1_is_complete(self):
        graph_dict = {'1': ['2'], '2': ['1', '3'], '3': ['2']}
        solution = {'1': 0, '2': 1, '3': 2}
        result = is_complete(graph_dict, solution)
        self.assertEqual(result, True)

    def test2_is_complete(self):
        graph_dict = {'1': ['2'], '2': ['1', '3'], '3': ['2']}
        solution = {'1': 0, '2': 1}
        result = is_complete(graph_dict, solution)
        self.assertEqual(result, False)

    def test3_minimum_remaining_values(self):
        domains = {'1': [0, 1], '2': [0, 1], '3': [0, 1]}
        graph_dict = {'1': ['2'], '2': ['1', '3'], '3': ['2']}
        csp = CSP(graph_dict, domains)
        assignment = {}
        result = minimum_remaining_values(csp, assignment)
        self.assertEqual(result, '2')

    def test4_minimum_remaining_values(self):
        domains = {'1': [0, 1], '2': [0, 1, 2], '3': [0, 1, 2]}
        graph_dict = {'1': ['2'], '2': ['1', '3'], '3': ['2']}
        csp = CSP(graph_dict, domains)
        assignment = {}
        result = minimum_remaining_values(csp, assignment)
        self.assertEqual(result, '1')

    def test5_least_constraining_value(self):
        print("Test1 LCV :")
        domains = {'1': [0, 1, 2], '2': [0, 1], '3': [0, 1]}
        graph_dict = {'1': ['2'], '2': ['1', '3'], '3': ['2']}
        csp = CSP(graph_dict, domains)
        assignment = {}
        current_node = '1'
        result = list(least_constraining_value(csp, current_node, assignment))
        self.assertEqual(result, [2, 0, 1])

    def test6_least_constraining_value(self):
        print("Test2 LCV :")
        domains = {'1': [0, 1, 2], '2': [0, 1, 2], '3': [0, 2]}
        graph_dict = {'1': ['2'], '2': ['1', '3'], '3': ['2']}
        csp = CSP(graph_dict, domains)
        assignment = {}
        current_node = '2'
        result = list(least_constraining_value(csp, current_node, assignment))
        self.assertEqual(result, [1, 0, 2])

    def test7_remove_inconsistent_value(self):
        print("Test1 remove_inconsistent_value :")
        domains = {'1': [0, 1, 2], '2': [0], '3': [0, 1]}
        graph_dict = {'1': ['2'], '2': ['1', '3'], '3': ['2']}
        csp = CSP(graph_dict, domains)
        xi = '1'
        xj = '2'
        result = remove_inconsistent_value(xi, xj, csp)
        self.assertEqual(result, True)

    def test8_remove_inconsistent_value(self):
        print("Test2 remove_inconsistent_value :")
        domains = {'1': [0, 1], '2': [2], '3': [0, 1]}
        graph_dict = {'1': ['2'], '2': ['1', '3'], '3': ['2']}
        csp = CSP(graph_dict, domains)
        xi = '1'
        xj = '2'
        result = remove_inconsistent_value(xi, xj, csp)
        self.assertEqual(result, False)

    def test_9_AC3(self):
        print("Test1 AC3:")
        domains = {'1': [0, 1, 2], '2': [0], '3': [0, 1]}
        graph_dict = {'1': ['2'], '2': ['1', '3'], '3': ['2']}
        csp = CSP(graph_dict, domains)
        result = AC3(csp)
        self.assertEqual(result, True)

    def test_9_AC3_2(self):
        print("Test2 AC3:")
        domains = {'1': [0, 1], '2': [0], '3': [0, 1]}
        graph_dict = {'1': ['2', '3'], '2': ['1', '3'], '3': ['1', '2']}
        csp = CSP(graph_dict, domains)
        result = AC3(csp)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
