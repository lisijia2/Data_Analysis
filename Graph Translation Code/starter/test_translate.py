import unittest

class TestGraphTranslate(unittest.TestCase):

    # ================================================================= list2matrix
    def test_list2matrix_A(self):
        import numpy as np
        from translate import graph_list2matrix
        graph = [(1,0), (2,1), (1,2), (2,3), (3,4)]
        num_nodes = 5
        expected = np.array([  [0, 0, 0, 0, 0],
                                [1, 0, 1, 0, 0],
                                [0, 1, 0, 1, 0],
                                [0, 0, 0, 0, 1],
                                [0, 0, 0, 0, 0]])
        result = graph_list2matrix(graph, num_nodes)
        self.assertTrue(np.array_equal(expected, result))


    def test_list2matrix_B(self):
        import numpy as np
        from translate import graph_list2matrix
        graph = [
                    (1,2),
                    (2,1),
                    (2,3),
                    (3,2),
                    (3,5),
                    (5,3),
                    (5,4),
                    (4,5),
                    (4,0),
                    (0,4),
                    (2,0),
                    (3,4)
                ]
        num_nodes = 6
        expected = np.array([[0, 0, 0, 0, 1, 0],
                            [0, 0, 1, 0, 0, 0],
                            [1, 1, 0, 1, 0, 0],
                            [0, 0, 1, 0, 1, 1],
                            [1, 0, 0, 0, 0, 1],
                            [0, 0, 0, 1, 1, 0]])
        result = graph_list2matrix(graph, num_nodes)
        self.assertTrue(np.array_equal(expected, result))


    # ================================================================= list2dict
    def test_list2dict_A(self):
        import numpy as np
        from translate import graph_list2dict
        graph = [
                    (0,2),
                    (2,0),
                    (3,0),
                    (3,1),
                    (3,2)
                ]
        num_nodes = 4
        expected = {0: [2], 2: [0], 3: [0, 1, 2]}
        result = graph_list2dict(graph, num_nodes)
        self.assertEquals(expected, result)


    def test_list2dict_B(self):
        import numpy as np
        from translate import graph_list2dict
        graph = [
                    (0,0),
                    (0,1),
                    (1,0),
                    (3,1),
                    (1,3),
                    (0,2),
                    (2,5)
                ]
        num_nodes = 6
        expected = {0: [0, 1, 2], 1: [0, 3], 3: [1], 2: [5]}
        result = graph_list2dict(graph, num_nodes)
        self.assertEquals(expected, result)


    # ================================================================= matrix2list

    def test_matrix2list_A(self):
        import numpy as np
        from translate import graph_matrix2list
        graph = np.array([  [0, 1, 0, 0, 0],
                            [0, 0, 1, 0, 0],
                            [0, 0, 0, 1, 0],
                            [0, 0, 0, 0, 1],
                            [0, 0, 0, 0, 1]])
        num_nodes = 5
        expected = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 4)]
        result = graph_matrix2list(graph, num_nodes)
        self.assertEquals(set(expected), set(result))


    def test_matrix2list_B(self):
        import numpy as np
        from translate import graph_matrix2list
        graph = np.array([  [0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 0, 1, 1],
                            [0, 0, 0, 1, 0, 0],
                            [0, 0, 0, 0, 1, 0],
                            [1, 0, 0, 0, 0, 0]])
        num_nodes = 6
        expected = [(0,3), (2,1), (2,4), (2,5), (3,3), (4,4), (5,0)]
        result = graph_matrix2list(graph, num_nodes)
        self.assertEquals(set(expected), set(result))


    # ================================================================= matrix2dict

    def test_matrix2dict_A(self):
        import numpy as np
        from translate import graph_matrix2dict
        graph = np.array([  [0, 1, 1, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1],
                            [1, 0, 0, 0]])
        num_nodes = 4
        expected = {0: [1, 2], 1: [2], 2: [3], 3: [0]}
        result = graph_matrix2dict(graph, num_nodes)
        self.assertEquals(expected, result)


    def test_matrix2dict_B(self):
        import numpy as np
        from translate import graph_matrix2dict
        graph = np.array([  [0, 0, 0, 0, 1, 0],
                            [0, 0, 1, 0, 0, 0],
                            [1, 1, 0, 1, 0, 0],
                            [0, 0, 1, 0, 1, 1],
                            [1, 0, 0, 0, 0, 1],
                            [0, 0, 0, 1, 1, 0]])
        num_nodes = 6
        expected = {0: [4], 1: [2], 2: [0, 1, 3], 3: [2, 4, 5], 4: [0, 5], 5: [3, 4]}
        result = graph_matrix2dict(graph, num_nodes)
        self.assertEquals(expected, result)


    # ================================================================= dict2list

    def test_dict2list_A(self):
        import numpy as np
        from translate import graph_dict2list
        graph = {
                    0:[2,3],
                    1:[3],
                    2:[0],
                    3:[1]
                }
        num_nodes = 4
        expected = [(0,2), (0,3), (1,3), (2,0), (3,1)]
        result = graph_dict2list(graph, num_nodes)
        self.assertEquals(set(expected), set(result))


    def test_dict2list_B(self):
        import numpy as np
        from translate import graph_dict2list
        graph = {
                0:[0,2],
                1:[3],
                2:[3],
                3:[4],
                4:[1,5]
                }
        num_nodes = 6
        expected = [(0,0), (0,2), (1,3), (2,3), (3,4), (4,1), (4,5)]
        result = graph_dict2list(graph, num_nodes)
        self.assertEquals(set(expected), set(result))


    # ================================================================= dict2matrix

    def test_dict2matrix_A(self):
        import numpy as np
        from translate import graph_dict2matrix
        graph = {
                    0:[0,1],
                    1:[2,3],
                    2:[0,1],
                    3:[1,2]
                }
        num_nodes = 4
        expected = np.array([   [1, 1, 0, 0],
                                [0, 0, 1, 1],
                                [1, 1, 0, 0],
                                [0, 1, 1, 0]])
        result = graph_dict2matrix(graph, num_nodes)
        self.assertTrue(np.array_equal(expected, result))


    def test_dict2matrix_B(self):
        import numpy as np
        from translate import graph_dict2matrix
        graph = {
                0:[0,4],
                1:[0,4],
                2:[3,4],
                3:[1,4],
                4:[2,3,4]
                }
        num_nodes = 5
        expected = np.array([   [1, 0, 0, 0, 1],
                                [1, 0, 0, 0, 1],
                                [0, 0, 0, 1, 1],
                                [0, 1, 0, 0, 1],
                                [0, 0, 1, 1, 1]])
        result = graph_dict2matrix(graph, num_nodes)
        self.assertTrue(np.array_equal(expected, result))
