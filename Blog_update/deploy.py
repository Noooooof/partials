#coding:utf-8

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBlog():
  def setup_method(self):
    options = webdriver.ChromeOptions()
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_blog(self):
    self.driver.get("https://gitee.com/Noooooof/Noooooof/pages")
    self.driver.set_window_size(1514, 984)
    self.driver.find_element(By.LINK_TEXT, u"登录").click()
    self.driver.find_element(By.ID, "user_login").click()
    self.driver.find_element(By.ID, "user_login").send_keys("Noooooof")
    self.driver.find_element(By.ID, "user_password").send_keys("t*/N4c7@i+N#U-f")
    self.driver.find_element(By.CSS_SELECTOR, ".two:nth-child(3) label").click()
    self.driver.find_element(By.NAME, "commit").click()
    self.driver.refresh()
    ad = self.driver.find_elements(By.CLASS_NAME, "close-icon")
    if len(ad) == 1:
    	ad[0].click()
    self.driver.find_element(By.CSS_SELECTOR, ".redeploy-button").click()
    assert self.driver.switch_to.alert.text == u"确定重新部署 Gitee Pages 吗?"
    self.driver.switch_to.alert.accept()
    time.sleep(120)
  
test = TestBlog()
test.setup_method()
test.test_blog()
test.teardown_method()
