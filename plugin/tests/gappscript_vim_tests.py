import unittest
import gappscript_vim as sut


@unittest.skip("Don't forget to test!")
class GappscriptVimTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.gappscript_vim_example()
        self.assertEqual("Happy Hacking", result)
