from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
from base.BasePage import  SeleniumDriver
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.sd.getElement(locator="user_email").clear()
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyPageTitle("Let's Kode It")
        self.ts.mark(result1, "Title is Incorrect")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was not successful")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True