import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d['key'], 'value')

    def test_attr(self):
        d = Dict()
        d['key'] = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    # 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。
    # 这两个方法会分别在每调用一个测试方法的前后分别被执行。
    # 设想你的测试需要启动一个数据库，这时，
    # 就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，
    # 这样，不必在每个测试方法中重复相同的代码 

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...\n')
if __name__ == '__main__':
    unittest.main()

# 在命令行通过参数-m unittest直接运行单元测试：
# python -m unittest mydict_test