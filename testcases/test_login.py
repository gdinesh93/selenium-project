import pytest
from selenium import webdriver
from pageobject.loginpage import Login
from utilities.readproperties import Readconfig
from utilities.customlogger import Loggen

class Test_001_login:
    baseURL=Readconfig.getapplicationURL()
    username=Readconfig.getusername()
    password=Readconfig.getpassword()
    logger=Loggen.loggen()

    def test_homepagetitle(self):
        self.logger.info("++++++++++++Test_001_login+++++++++++++++")
        self.logger.info("++++++++++++verifying homepage title+++++++++++++++")
        self.driver = webdriver.Chrome(executable_path="E:\chromedriver_win32\chromedriver.exe")
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("+++++++++++homepage title success+++++++++++++++")
        else:
            assert False
            self.logger.error("+++++++++++homepage title failed+++++++++++++++")

    def test_login(self):
        self.driver = webdriver.Chrome(executable_path="E:\chromedriver_win32\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("+++++++++++test login successful+++++++++++++++")
        else:
            assert False
            self.logger.error("+++++++++++test login failed+++++++++++++++")