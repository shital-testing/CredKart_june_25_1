import sys
import os
import time

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from faker import Faker
from pageObjects.Registration_Page import Registration_Page_Class
from pageObjects.Login_Page import Login_Page_Class
from utilities.ReadConfig import ReadConfigClass

@pytest.mark.usefixtures("driver_setup")
class Test_User_Profile_Class:
    driver = None
    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()
    login_url = ReadConfigClass.get_data_for_login_url()
    register_url = ReadConfigClass.get_data_for_register_url()



    def test_CredKart_Title_001(self):
        self.driver.get(self.login_url)
        self.driver.maximize_window()

        if self.driver.title == "CredKart":
            print("you are landed on correct page and it's title is:", self.driver.title)
            assert True
        else:
            print("you are landed on wrong page and it's title is:", self.driver.title)
            assert False




    def test_CredKart_Login_002(self):
        self.driver.get(self.login_url)
        self.lp = Login_Page_Class(self.driver) # Object Creation

    #     # Field - Email
    #     email_field = self.driver.find_element(By.ID, "email")
    #     email_field.send_keys(f"Credencejune{value}@credence.in")
        self.lp.Enter_Email(self.email) # hard coding

    #
    #     # Field - Password
    #     password_field = self.driver.find_element(By.ID, "password")
    #     password_field.send_keys("Credence@123")
        self.lp.Enter_Password(self.password) # hard coding

    #
    #     # Button - Login Now
    #     login_now_button = self.driver.find_element(By.CLASS_NAME, "btn")
    #     login_now_button.click()
        self.lp.Click_Submit_Button()

    #
    #     # Verify the User login Successfully
    #     wait = WebDriverWait(self.driver, 5)
    #     try:
    #         wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
    #         self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
    #         print("User login Successfully")
    #         #self.driver.save_screenshot("User login Successfully.png")
    #     except:
    #         print("User login Failed")
    #         #self.driver.save_screenshot("User login Failed.png")
    # else:
    #     print("you are landed on wrong page and it's title is:", self.driver.title)

        if self.lp.verify_menu() == "Pass":
            #self.driver.save_screenshot(r"D:\Batch Notes\Automation Testing may 2025\04. CredKart_Pytest_Framework\Screenshots\User login Successfully.png")
            self.lp.Click_Menu_Button()
            self.lp.Click_Logout_Link()
            assert True
        else:
            self.driver.save_screenshot(r"D:\Batch Notes\Automation Testing may 2025\04. CredKart_Pytest_Framework\Screenshots\User login Failed.png")
            assert False


    def test_CredKart_Registration_003(self):
        self.driver.get(self.register_url)
        self.rp = Registration_Page_Class(self.driver) # Object Creation
        name = Faker().name()
        email = Faker().email()
        print(f"Name: {name}, Email: {email}")
        # Field - Name
        self.rp.Enter_Name(name)

        # Field - Email
        self.rp.Enter_Email(email)

        # Field - Password
        self.rp.Enter_Password("Credence@123")

        # Field - Confirm Password
        self.rp.Enter_Confirm_Password("Credence@123")

        # Button - Submit
        self.rp.Click_Submit_Button() # registration button

        # Verify Registration Successfully
        if self.rp.verify_menu() == "Pass":
            # self.driver.save_screenshot(r"D:\Batch Notes\Automation Testing may 2025\04. CredKart_Pytest_Framework\Screenshots\User login Successfully.png")
            self.rp.Click_Menu_Button()
            self.rp.Click_Logout_Link()
            assert True
        else:
            self.driver.save_screenshot(r"D:\Batch Notes\Automation Testing may 2025\04. CredKart_Pytest_Framework\Screenshots\User Registration Failed.png")
            assert False


# added registration
# common value--> config.ini
# driver_setup implemented at class level
# driver_setup, driver attached to class
# logger class, and method


# log
# rerun failed testcases
# allure report
# params, excel
# add test cases
