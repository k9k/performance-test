__author__ = 'ubuntu'

import unittest
import multiply_my_way
import multiply_with_numpy

scripts = [multiply_my_way, multiply_with_numpy]

class KnownValues(unittest.TestCase):
    known_values = (
        (([[1,2],[3,4]], [[1,2],[3,4]]), [[7,10], [15,22]]),
        (([[1,2],[1,2]], [[1,1],[1,1]]), [[3,3], [3,3]]),
        (([[1,2],[3,4]], [[0,0],[0,0]]), [[0,0], [0,0]])
    )

    def testKnownValues(self):
        for data_in, correct_value in self.known_values:
            for script in scripts:
                result = script.multiply(data_in[0], data_in[1])
                self.assertEqual(result, correct_value)

class toMatrixBadInput(unittest.TestCase):
    def testNotMatrix(self):
        """should fail with input other than matrix"""
        for script in scripts:
            self.assertRaises(script.NotMatrixError, script.multiply, 99, 11)

    def testWrongSizeMatrix(self):
        """matrix multiplying is allowed only if A[i x j] and B[j x k]"""
        for script in scripts:
            self.assertRaises(script.DifferentSizeMatriXError, script.multiply, [[1],[1]], [[1],[1],[1]])

if __name__ == '__main__':
    unittest.main()