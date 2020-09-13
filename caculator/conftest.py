import pytest

#固件fixture;scope注明作用域；autouse表明自动化执行
@pytest.fixture(scope='session',autouse=True)
def open():
    print("=========打开计算器，开始测试===========")
    #预处理签，后处理；相当于unittest的setup和teardown
    yield
    print("============关闭=================")
    return "teest11111111"


