import time
from selenium import webdriver

from selenium.webdriver.common.by import By


#class for opening and closing the browser
class TestSetupTeardown():
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    @classmethod
    def tearDown (cls):
        cls.driver.close()
        cls.driver.quit()

#class for testing websites url
class TestBrowser(TestSetupTeardown):

    def test_01_website(self, url_01):
        self.driver.get(url_01)
        time.sleep(2)

#class for testing login validation
class TestLogin(TestSetupTeardown):

    def test_02_login_username(self, username):                                                 #writing username
        self.driver.find_element(By.ID, Locators.username_textbox_id).clear()
        self.driver.find_element(By.ID, Locators.username_textbox_id).send_keys(username)
        time.sleep(2)

    def test_03_login_password(self, password):                                                 #writing password
        self.driver.find_element(By.ID, Locators.password_textbox_id).clear()
        self.driver.find_element(By.ID, Locators.password_textbox_id).send_keys(password)
        time.sleep(2)

    def test_04_login_btn(self):                                                                #clicking login button
        self.driver.find_element(By.ID, Locators.login_button_id).click()
        time.sleep(2)

    def test_05_logout_btn(self):                                                               #clicking logout button
        self.driver.find_element(By.ID, Locators.welcome_link_id).click()
        time.sleep(2)
        self.driver.find_element(By.ID, Locators.logout_link_linkText).click()
        time.sleep(2)

    def test_06_check_invalid_login_message(self):                                              #checking for invalid user id and invalid password
        msg = self.driver.find_element(By.XPATH, Locators.invalid_login_message_xpath).text
        return msg


#class for testing adding  items to cart
class TestAddToCart(TestSetupTeardown):
        
    def test_02_add_one_item(self, item):                                                       #adding one item to cart
        self.driver.find_element(By.ID, item).click()
        time.sleep(2)
        
    def test_03_go_to_cart(self):                                                               #for going to the my cart page 
        self.driver.find_element(By.ID, Locators.shopping_cart_id).click()
        time.sleep(2)
        
    def test_04_checkout(self):                                                                 #for going to the checkout page
        self.driver.find_element(By.ID, Locators.checkout_btn_id).click()
        time.sleep(2)
    
    def test_05_checkout_page(self, firstname, lastname, postalcode):                           #filling up the check out page 
        self.driver.find_element(By.ID, Locators.user_first_name_id).clear()
        self.driver.find_element(By.ID, Locators.user_first_name_id).send_keys(firstname)
        time.sleep(2)

        self.driver.find_element(By.ID, Locators.user_last_name_id).clear()
        self.driver.find_element(By.ID, Locators.user_last_name_id).send_keys(lastname)
        time.sleep(2)

        self.driver.find_element(By.ID, Locators.user_postal_code_id).clear()
        self.driver.find_element(By.ID, Locators.user_postal_code_id).send_keys(postalcode)
        time.sleep(2)

        self.driver.find_element(By.ID, Locators.continue_btn_id).click()
        time.sleep(2)
        
    def test_06_overview_page(self):                                                            #for finishing up the shoping in the overview page
        self.driver.find_element(By.ID, Locators.finish_btn_id).click()
        time.sleep(2)

    def test_07_checkout_complete_page(self):                                                   #for completing the checkout and going back user inventory page
        self.driver.find_element(By.ID, Locators.back_home_btn_id).click()
        time.sleep(2)


            


class Locators :                                                                                #websites information

    HomePage_url = "https://saucedemo.com"
    UserPage_url = "https://www.saucedemo.com/inventory.html"
    cartPage_url = "https://www.saucedemo.com/cart.html"

    username_textbox_id = "user-name"
    password_textbox_id = "password"
    login_button_id = "login-button"
    welcome_link_id = "react-burger-menu-btn"
    logout_link_linkText = "logout_sidebar_link"
    invalid_login_message_xpath = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/h3[1]"
    user_first_name_id = "first-name"
    user_last_name_id = "last-name"
    user_postal_code_id = "postal-code"
    continue_btn_id = "continue"
    shopping_cart_id = "shopping_cart_container"
    add_to_cart_backpack_id ="add-to-cart-sauce-labs-backpack"
    add_to_cart_bikelight_id = "add-to-cart-sauce-labs-bike-light"
    checkout_btn_id = "checkout"
    finish_btn_id = "finish"
    back_home_btn_id = "back-to-products"

    valid_user_01 = "standard_user"
    valid_passord_01 = "secret_sauce"

    invalid_user_01 ="user"
    invalid_password_01 = "pass"

    invalid_message = "Epic sadface: Username and password do not match any user in this service"

    user_firstname = "Roy"
    user_lastname = "Joy"
    user_postalcode = "000"

    


if __name__ == "__main__":

        #Data  
    url_01 = Locators.HomePage_url
    url_02 = Locators.UserPage_url
    user_01 = Locators.valid_user_01
    pass_01 = Locators.valid_passord_01
    user_02 = Locators.invalid_user_01
    pass_02 = Locators.invalid_password_01
    item_01 = Locators.add_to_cart_backpack_id
    userfirstname = Locators.user_firstname
    userlastname = Locators.user_lastname
    userpostalcode = Locators.user_postalcode
    invalid_msg_01 = Locators.invalid_message

        #Calling the classes
    test_00 = TestSetupTeardown()
    test_01 = TestBrowser()
    test_02 = TestLogin()
    test_03 = TestAddToCart()

        #valid login 
    test_00.setUp()
    test_01.test_01_website(url_01)
    test_02.test_02_login_username(user_01)
    test_02.test_03_login_password(pass_01)
    test_02.test_04_login_btn()
    if test_00.driver.current_url == url_02:
        print("login valid")
    else : 
        print("something went wrong")
    test_02.test_05_logout_btn()
    test_00.tearDown()

        #invalid login   
    test_00.setUp()
    test_01.test_01_website(url_01)
    test_02.test_02_login_username(user_02)
    test_02.test_03_login_password(pass_02)
    test_02.test_04_login_btn()
    if invalid_msg_01 == test_02.test_06_check_invalid_login_message():
        print("login invalid")
    else : 
        print("something went wrong")
    test_00.tearDown()

        #Add 1 item
    test_00.setUp()
    test_01.test_01_website(url_01)
    test_02.test_02_login_username(user_01)
    test_02.test_03_login_password(pass_01)
    test_02.test_04_login_btn()
    test_03.test_02_add_one_item(item_01)
    test_03.test_03_go_to_cart()
    test_03.test_04_checkout()
    test_03.test_05_checkout_page(userfirstname, userlastname, userpostalcode)
    test_03.test_06_overview_page()
    test_03.test_07_checkout_complete_page()
    if test_00.driver.current_url == url_02:
        print("success")
    else:
        print("fishy")
    test_02.test_05_logout_btn()
    test_00.tearDown()


    