import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pageObjects.Login_Page import Login_Page_Class
class Test004:


    def test_CredKart_Title_001(self, driver_setup):
        driver = driver_setup
        driver.get("https://automation.credence.in/login")
        driver.maximize_window()

        if driver.title == "CredKart":
            print("you are landed on correct page and it's title is:", driver.title)
            assert True
        else:
            print("you are landed on wrong page and it's title is:", driver.title)
            assert False

    def test_CredKart_Login_002(self, driver_setup):
        driver = driver_setup
        driver.get("https://automation.credence.in/login")
        self.lp = Login_Page_Class(driver) # Object Creation

    #     # Field - Email
    # email_field.send_keys(f"Credencejune{value}@credence.in")
        self.lp.Enter_Email("Credencejune01@credence.in")

    #
    #     # Field - Password
    #     password_field = driver.find_element(By.ID, "password")
    #     password_field.send_keys("Credence@123")
        self.lp.Enter_Password("Credence@123")

    #
    #     # Button - Login Now
    #     login_now_button = driver.find_element(By.CLASS_NAME, "btn")
    #     login_now_button.click()
        self.lp.Click_Login_Button()

    #
    #     # Verify the User login Successfully
    #     wait = WebDriverWait(driver, 5)
    #     try:
    #         wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
    #         driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
    #         print("User login Successfully")
    #         #driver.save_screenshot("User login Successfully.png")
    #     except:
    #         print("User login Failed")
    #         #driver.save_screenshot("User login Failed.png")
    # else:
    #     print("you are landed on wrong page and it's title is:", driver.title)

        if self.lp.verify_menu() == "Pass":
            driver.save_screenshot(r"D:\Batch Notes\Automation Testing may 2025\04. CredKart_Pytest_Framework\Screenshots\User login Successfully.png")
            assert True
        else:
            driver.save_screenshot(r"D:\Batch Notes\Automation Testing may 2025\04. CredKart_Pytest_Framework\Screenshots\User login Failed.png")
            assert False

