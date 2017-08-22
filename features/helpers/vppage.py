from features.helpers.config import Config as cf
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging
log = logging.getLogger(__name__)

def type_by_css(context,selector,text):
    context.browser.implicitly_wait(5)
    elem = context.browser.find_element_by_css_selector(selector)
    elem.send_keys(text)


def type_by_xpath(context,selector,text):
    context.browser.implicitly_wait(5)
    elem = context.browser.find_element_by_xpath(selector)
    elem.send_keys(text)


def switch_to_iframe(context,iframetag):
    context.browser.implicitly_wait(5)
    context.browser.switch_to.frame(context.browser.find_element_by_tag_name(iframetag))


def click_by_xpath(context,xpath):
    context.browser.implicitly_wait(5)
    elem = context.browser.find_element_by_xpath(xpath)
    elem.click()


def click_by_css(context,selector):
    context.browser.implicitly_wait(5)
    elem = context.browser.find_element_by_css_selector(selector)
    elem.click()


def assert_by_class(context,classname,expectedtext):
    context.browser.implicitly_wait(5)
    elem = context.browser.find_element_by_class_name(classname).text
    assert expectedtext == elem.strip()


def visit_url(context):
    base_url = cf.base_url
    context.browser.get(base_url)


def select_dropdown(context,selector,selection):
    context.browser.implicitly_wait(5)
    elem=context.browser.find_element_by_css_selector('div.five.wide.field')
    elem.click()
    if context.browser.capabilities['browserName'] == "MicrosoftEdge" or \
                    context.browser.capabilities['browserName'] == "internet explorer":
        select = Select(context.browser.find_element_by_css_selector('#state'))
        select.select_by_visible_text("Alabama")
    else:
        #type_by_xpath(context, '//*[@id="cc-billing-information"]/div[3]/div[2]/div/input', "Alabama")
        click_by_css(context, "div.item")
        #click_by_css(context, ".menu")



def switch_to_inner_frame(context,selector):
    context.browser.implicitly_wait(5)
    if context.browser.capabilities['browserName'] != "MicrosoftEdge":
        frame = context.browser.find_element_by_xpath('//*[@id="card-element"]/div/iframe')
        context.browser.switch_to.frame(frame)
    else:
        sleep(5)
        frame = context.browser.find_elements_by_tag_name('iframe')
        log.info("Length is : "+str(len(frame)))
        iframe = frame[0]
        context.browser.switch_to.frame(iframe)


def switch_to_default(context):
    context.browser.implicitly_wait(5)
    context.browser.switch_to.default_content()

def type_by_name(context,selector,text):
    context.browser.implicitly_wait(5)
    elem = context.browser.find_element_by_css_selector(selector)
    elem.send_keys(text)

def click_by_css_script(context,selector):
    context.browser.implicitly_wait(5)
    elem = context.browser.find_element_by_css_selector(selector)
    context.browser.execute_script("arguments[0].scrollIntoView(true);", elem)
    sleep(2)
    elem.click()

def assert_by_css(context,css,expectedtext):
    context.browser.implicitly_wait(5)
    elem = context.browser.find_element_by_css_selector(css).text
    assert expectedtext == elem.strip()

def click_by_css_jscript(context,selector):
    context.browser.implicitly_wait(5)
    elem = context.browser.find_element_by_css_selector(selector)
    context.browser.execute_script("arguments[0].click();", elem)
    sleep(2)
