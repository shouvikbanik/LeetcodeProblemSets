from unittest import TestCase

from LeetcodeProblemSets.two_sum import two_sum


class TwoSumTest(TestCase):

    def test_check_type_of_return_val(self):
        self.assertTrue(
            (type(two_sum([1, 4, 3, 2], 6)) == list) or (type(two_sum([1, 4, 3, 2], 6)) == tuple))

    def test_check_len_of_return_val(self):
        self.assertEqual(len(two_sum([1, 4, 3, 2], 6)), 2)

    def test_check_sum_of_returnVal(self):
        return_val=two_sum([1, 4, 3, 2], 6)
        self.assertTrue((return_val[0]==1 and return_val[1]==3) or (return_val[1]==1 and return_val[0]==3))

    def test_check_sum_of_returnVal2(self):
        return_val=two_sum([1, 4, 4, 2], 8)
        self.assertTrue((return_val[0]==1 and return_val[1]==2) or (return_val[1]==1 and return_val[0]==2))
