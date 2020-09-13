import pytest
#import allure
from caculator import cacu

class Testcaculator:
    def test_myadd1(self):
        cal =  cacu
        res = cal.myadd(1,1)
        assert res == 2

    #@pytest.mark.usefixtures("open")
    def test_myadd2(open):
        #print('显示出来: %s' %s open)
        print('test_data: %s' % open)
        cal = cacu
        res = cal.myadd(1,99)
        assert res == 100

    @pytest.mark.usefixtures("open")
    def test_myadd3(open):
        cal = cacu
        res = cal.myadd(3,3)
        assert res == 6