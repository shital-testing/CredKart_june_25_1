import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pageObjects.Login_Page import Login_Page_Class
from utilities.read_config import ReadConfig


class Test004:

    def test_CredKart_Title_001(self, driver_setup):
        driver = driver_setup
        url = ReadConfig.get_login_url()
        driver.get(url)
        driver.maximize_window()

        if driver.title == "CredKart":
            print("You are landed on correct page and its title is:", driver.title)
            assert True
        else:
            print("You are landed on wrong page and its title is:", driver.title)
            assert False

    def test_CredKart_Login_002(self, driver_setup):
        driver = driver_setup
        url = ReadConfig.get_login_url()
        email = ReadConfig.get_email()
        password = ReadConfig.get_password()

        driver.get(url)
        self.lp = Login_Page_Class(driver)

        self.lp.Enter_Email(email)
        self.lp.Enter_Password(password)
        self.lp.Click_Login_Button()

        if self.lp.verify_menu() == "Pass":
            driver.save_screenshot(r"Screenshots\User_login_Successfully.png")
            assert True
        else:
            driver.save_screenshot(r"Screenshots\User_login_Failed.png")
            assert False
