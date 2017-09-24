import unittest
from stack import stack

class testing(unittest.TestCase):

    def test_push(self):
        data=[]
        obj= stack(data)
        obj.push(3)
        obj.push(4)
        obj.push(5)
        obj.push(6)
        res=obj.pop()
        self.assertEqual(res,6)

    def test_underflow(self):
        data=[]
        obj2=stack(data)
        b=stack(data)
        print b.isEmpty()
        res=obj2.pop()
        self.assertFalse(res)






unittest.main()
