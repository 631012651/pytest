# pytest
                                                                              pytest测试框架

1、	环境准备
Pytest安装：          pip install pytest==6.0.2
pytest-cov插件安装：  pip install pytest-cov 
分布式测试插件安装：   pip install pytest-xdist
出错立即返回插件：	   pip install pytest-instafail
安装attrs:             pip install attrs==19.1.0
2、	编程
目录结构
		Package
			__init__.py       表明是一个包，import相关类
			conftest.py		@pytest.fixture
			caculator.py		写一个计算器
			test_caculator.py	对计算器进行测试

calculator.py

class cacu:
    def myadd(a,b):
        """
        加法
        :return:
        """
        result = a+b
        return result

    def dividemethod(c,d):
        """
        除法
        :param c:
        :param d:
        :return:
        """
        if d == 0:
            print("分母不能为0")
        else:
            result1 = c/d
            return result1

conftest.py

import pytest

@pytest.fixture(scope='session',autouse=True)
def open():
    print("=========打开计算器，开始测试===========")
    yield
    print("============关闭=================")
    return "teest11111111"

test_caculator.py

import pytest
from caculator import cacu


class Testdivide:

	
    @pytest.mark.parametrize('c,d,e',
                             [(6,2,3),
                              (10,5,2)])
    def test_divide1(self,open,c,d,e):
        cal = cacu
        res = cal.dividemethod(c,d)
        assert res == e
        print(open)

    @pytest.mark.xfail 
    def test_divide2(self):
        cal = cacu
        res = cal.dividemethod(100,0)
        assert res == 0
3.执行
pytest -v -s test_caculator.py::Testdivide::test_divide1
打印出用例初始化和退出过程
pytest –-setup-show test_caculator.py

输出报告（html）
pytest --html=reportname.html
使用xdist分发
pytest -n 3 --html=report.html --self-contained-html

指定路径
Pytest --html=./report/report.html

计算覆盖率
pytest-cov可以自动执行测试文件的全部代码，执行命令pytest --cov=./ 
pytest --cov=./ --cov-report=html


重复执行失败用例
pytest --tb=line --instafail
