import unittest
from Examples import Example

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('runs once before everything')

    @classmethod
    def tearDownClass(cls) -> None:
        print('runs after everything has completed')

    def setUp(self):
        print('runs before every method')

    def tearDown(self):
        print('runs after very method')

    def test_add(self):
        result = Example.add(self,10,20)
        self.assertEqual(result,30)
    def test_sub(self):
        result = Example.sub(self,50,20)
        self.assertEqual(result,30)
    def test_anotherWayToTestAdd(self):
        self.assertEqual(Example.add(self,0,0),0)
        self.assertEqual(Example.add(self,-1,1),0)

if __name__ == '__main__':
    unittest.main()
