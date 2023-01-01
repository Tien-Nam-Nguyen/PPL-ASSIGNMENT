import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_2(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    def test_3(self):
        self.assertTrue(TestLexer.test("aAsVN32","aAsVN32,<EOF>",103))
    def test_4(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",104))