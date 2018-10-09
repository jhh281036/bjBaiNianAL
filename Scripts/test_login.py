import os,sys
import allure
sys.path.append(os.getcwd())
from Page.page_login import PageLogin
from Base.get_driver import get_driver
class TestLogin():

    def setup_class(self):
        # 实例化 登录页面类
        self.login=PageLogin(get_driver())
    def teardown_class(self):
        # 退出driver驱动
        self.login.driver.quit()
    def test_login(self):
        # 登录操作
        self.login.page_login("18610453007","123456")
        try:
            assert "itheima" in self.login.page_get_nickname()
            allure.attach('断言成功描述')
            # 退出操作
            self.login.page_login_logout()
        except:
            # 截图
            self.login.base_getImage()
            with open("./Image/faild.png","rb") as f:
                allure.attach("失败描述：",f.read(),allure.attach_type.PNG)

            # 抛异常
            raise