import unittest

import statzcw


class test_statzcw(unittest.TestCase):

    def test_zcount(self):
        test_in = [1, 2, 4, 6, 88, 1, 2]
        expected_out = 7
        actual = statzcw.zcount(test_in)
        assert actual == expected_out

    def test_zmode(self):
        test_in = [1, 1, 1, 1, 2, 2, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 8]
        expected_out = 6
        actual = statzcw.zmode(test_in)
        assert actual == expected_out

    def test_zmean(self):
        test_in = [1, 1, 1, 1, 2, 2, 4, 4, 6, 6]
        expected_out = 2.8
        actual = statzcw.zmean(test_in)
        assert actual == expected_out

    # def test_zrannge(self):
    #     test_in = [1,2,3,4,1,2,100,4,5]
    #     expected_out = 99
    #     actual = statzcw.zrange(test_in)
    #     assert actual == expected_out

    def test_zmedian(self):
        test_ins = ([1, 1, 1, 2, 5, 5, 5], [1, 1, 1, 2, 2, 2])
        expected_outs = [2, 1.5]
        actuals = []
        for test_in in test_ins:
            actuals += [statzcw.zmedian(test_in)]
        assert actuals == expected_outs

    def test_zvariance(self):
        test_ins = ([1, 2, 3, 4, 5], [1, 1, 1, 1, 1, 1])
        expected_outs = [2.5, 0]
        actuals = []
        for test_in in test_ins:
            actuals += [statzcw.zvariance(test_in)]
        assert actuals == expected_outs

    def test_zstddev(self):
        test_ins = ([0, 4.5, 9], [1, 1, 1, 1, 1, 1])
        expected_outs = [4.5, 0]
        actuals = []
        for test_in in test_ins:
            actuals += [statzcw.zstddev(test_in)]
        assert actuals == expected_outs

    def test_zstderr(self):
        test_ins = ([0, 0, 0, 0, 3, 6, 6, 6, 6], [1, 1, 1, 1, 1, 1])
        expected_outs = [1, 0]
        actuals = []
        for test_in in test_ins:
            actuals += [statzcw.zstderr(test_in)]
        assert actuals == expected_outs

    def test_zcorr(self):
        test_ins = (([1,2,3],[1,2,3]), ([1,2,3],[3,2,1]))
        expected_outs = [1, -1]
        actuals = []
        for test_in in test_ins:
            listx, listy = test_in
            actuals += [statzcw.zcorr(listx, listy)]
        assert actuals == expected_outs
