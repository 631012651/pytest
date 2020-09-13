import pytest
from caculator import cacu

class Testdivide:
    #参数化
    @pytest.mark.parametrize('c,d,e',
                             [(6,2,3),
                              (10,5,2)])
    def test_divide1(self,open,c,d,e):
        cal = cacu
        res = cal.dividemethod(c,d)
        #断言
        assert res == e
        print(open)
    #预计失败
    @pytest.mark.xfail
    def test_divide2(self):
        cal = cacu
        res = cal.dividemethod(100,0)
        assert res == 0

    #跳过该测试
    @pytest.mark.skip
    def test_divide3(self):
        pass

'''
if '__name__' == '__main__':
    pytest.main(['-m smoke','--result-log = reports/test.log',
                 '--junit-xml = reports/test.xml',
                 '--html = reports/test.html'])
'''