from time import sleep
from selenium.webdriver.common.by import By
class Mail:
    def __init__(self,driver):
        self.driver=driver
    # 登录
    def login(self):
        sleep(2)
        self.driver.switch_to.frame(0)  # 切换到表单
        self.driver.find_element(By.NAME,"email").clear()  #清空文本框
        self.driver.find_element(By.NAME,"email").send_keys("123456")
        self.driver.find_element(By.NAME,"password").clear()
        self.driver.find_element(By.NAME,"password").send_keys("123456")
        self.driver.find_element(By.ID,"dologin").click()
    # 退出
    def logout(self):
        sleep(2)
        self.driver.find_element(By.ID,"spnUid").click()
        sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[7]').click()
