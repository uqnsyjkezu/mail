from selenium import webdriver
from module import Mail
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.126.com")
mail=Mail(driver)
#登录
mail.login()
#退出
mail.logout()
driver.close()
