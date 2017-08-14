from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from features.helpers.config import Config as cf
import os,json


class Browser(object):

    base_url = cf.base_url
    driver = webdriver.Chrome(cf.chromeDriverLocation)
    driver.implicitly_wait(10)

    def visit(self, location=''):
        url = self.base_url + location
        self.driver.get(url)
        self.driver.maximize_window()

    def click_by_id(self, selector):
        self.driver.implicitly_wait(10)
        elem =  self.driver.find_element_by_id(selector)
        elem.click()

    def click_by_class(self,selector):
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element_by_class_name(selector)
        elem.click()

    def click_by_css(self,selector):
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element_by_css_selector(selector)
        elem.click()

    def assert_by_id_text(self,selector,expected_text):
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element_by_id(selector).text
        assert expected_text == elem

    def assert_by_cssselector(self,selector,expected_text):
        self.driver.implicitly_wait(10)
        sleep(2)
        elem = self.driver.find_element_by_css_selector(selector).text
        #pdb.set_trace()
        assert expected_text == elem

    def assert_by_class(self,selector,expected_text):
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element_by_class_name(selector).text
        assert expected_text == elem

    def type_in_text_id(self,selector,text):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id(selector).send_keys(text)

    def type_in_text_css(self,selector,text):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector(selector).send_keys(text)

    def type_in_text_name(self,selector,text):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name(selector).send_keys(text)

    def click_on_link_text(self,text):
        elem = self.driver.find_element_by_link_text(text)
        elem.click()

    def click_on_partial_link_text(self,text):
        elem = self.driver.find_element_by_partial_link_text(text)
        elem.click()

    def assert_view_state(self,selector):
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element_by_css_selector(selector).is_displayed()
        assert elem == True

    def enter_return_key(self,selector):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector(selector).send_keys(Keys.RETURN)


    def close(self):
        self.driver.stop_client()
        self.driver.close()