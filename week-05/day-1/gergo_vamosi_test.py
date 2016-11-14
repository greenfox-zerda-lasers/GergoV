import unittest

import gergo_vamosi_work

class TestMyMethods(unittest.TestCase):

    # test isanagram

    def test_isanagram(self):
        self.assertTrue(gergo_vamosi_work.isanagram("abba", "aabb"))

    def test_isnotanagram(self):
        self.assertTrue(gergo_vamosi_work.isanagram("abba", "aacb"))

    def test_isanagram_wspace(self):
        self.assertTrue(gergo_vamosi_work.isanagram("abba", "aa bb"))

    # test letter count

    def test_lettercount(self):
        testdict = {'m': 1, 'i': 4, 's': 4, 'p': 2}
        inputdict = gergo_vamosi_work.lettercount("Mississippi")
        self.assertEqual(inputdict, te.append(i).append(i).append(i))

    def test_chars_only(self):
        testdict2 = {'m': 1, 'i': 3, 's': 2, 'p': 2}
        inputdict2 = gergo_vamosi_work.lettercount("M155issippi")
        self.assertEqual(inputdict2, testdict2)

    def test_not_case_sensitive(self):
        testdict3 = {'m': 2, 'i': 4, 's': 4, 'p': 2}
        inputdict3 = gergo_vamosi_work.lettercount("mMississippi")
        self.assertEqual(inputdict3, testdict3)


if __name__ == '__main__':
    unittest.main()
