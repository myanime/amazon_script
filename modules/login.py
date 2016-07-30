from selenium import webdriver


def login(email, password):
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get('https://www.amazon.com/gp/sign-in.html')
    driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
    return driver


#driver.get('https://www.amazon.com/ss/help/contact/writeMessage?writeButton=Submit&subject=5&orderID=&sellerID=AI6JWQLGEIWAS&asin=&marketplaceID=ATVPDKIKX0DER&language=en_US')
