from Pypeline.Pypes.Sorting.Quicksort import quickSort, partition
import unittest


class QuicksortTest(unittest.TestCase):
    """
	Tests for functions in the Quicksort module.
	"""

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.testarray1 = [7, 6, 4, 3, 5, 2, 13, 8]
        self.testarray2 = [1, 4, 7, -5, 3, 5, 8, 19]

    def tearDown(self):
        pass

    def test_partition(self):
        self.assertEqual(partition(self.testarray1,0,len(self.testarray1)-1, order='ascend'),6)
        self.assertEqual(partition(self.testarray2, 0, len(self.testarray2) - 1, order='ascend'), 7)

    def test_quickSort(self):
        quickSort(self.testarray1,0,len(self.testarray1)-1)
        quickSort(self.testarray2, 0, len(self.testarray2) - 1)
        self.assertListEqual(self.testarray1, [2,3,4,5,6,7,8,13])
        self.assertListEqual(self.testarray2, [-5,1,3,4,5,7,8,19])
