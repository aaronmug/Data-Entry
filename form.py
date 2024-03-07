from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdCF0B1DFMlauvp7dL9s_JIThfNzWZVcBsYN_qUlBv5UWtoNw/viewform"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class Form:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url=FORM_URL)

    def input_info(self, address, price, link):
        sleep(2)
        inputs = self.driver.find_elements(By.CLASS_NAME, value="whsOnd")
        inputs[0].send_keys(address)
        inputs[1].send_keys(price)
        inputs[2].send_keys(link)
        submit_button = self.driver.find_element(By.CLASS_NAME, value="l4V7wb")
        submit_button.click()
        sleep(2)
        another_response = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        another_response.click()
