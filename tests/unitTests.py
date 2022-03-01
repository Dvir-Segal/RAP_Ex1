import unittest
from src.ex_1 import find_root, safe_call


class MyTestCase(unittest.TestCase):
    def testFindRoot(self):
        eps = 1*10**(-10)
        self.assertTrue(abs(find_root(lambda x: x**2-49, 1, 11)-7.0)<= eps)
        self.assertTrue(abs(find_root(lambda x: x**2+5*x+6, -2.5, 0)+2.0) <= eps)
        self.assertTrue(abs(find_root(lambda x: 3 * x ** 2 + 10 * x + 8, -1.5, 0)+4.0/3.0) <= eps)
        self.assertTrue(abs(find_root(lambda x: 2 * x ** 3 - 7 * x ** 2 + 7 * x - 2, 1.5, 10)-2.0) <= eps)
        self.assertTrue(abs(find_root(lambda x: 2 * x ** 3 + 5 * x ** 2 - 2 * x - 5, -80, 1)-1.0)<=eps)

    def testSafeCall(self):
        def f(x: int, y: float, z):
            return x + y + z

        def g(x: str, y: str):
            return x + y

        self.assertEqual(safe_call(f, x=5, y=7.0, z=3), 15.0)
        self.assertEqual(safe_call(f, x=5, y="abc", z=3), "raises an exception")
        self.assertEqual(safe_call(f, x=9, y=5.8, z=5, w=54), "raises an exception")
        self.assertEqual(safe_call(g, x=5, y="abc", z=3), "raises an exception")
        self.assertEqual(safe_call(g, x="no", y="abc", z=3), "raises an exception")
        self.assertEqual(safe_call(g, x="no ", y="exception"), "no exception")









