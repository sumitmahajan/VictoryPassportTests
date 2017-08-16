from behave import Given,When,Then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from features.helpers.config import Config as cf
import logging
from time import sleep
log = logging.getLogger(__name__)


class VpSteps:

    @When("I have vp site open")
    def step(context):
        base_url = cf.base_url
        context.browser.get(base_url)

    @Then("I can see footer Paid for by Stripe AAN")
    def step(context):
        context.browser.implicitly_wait(5)
        elem = context.browser.find_element_by_class_name("paid-for-by-container").text
        assert "Paid for by Stripe AAN" == elem.strip()

    @When("I fill all fields on vp page")
    def step(context):
        context.browser.implicitly_wait(5)
        context.browser.switch_to.frame(context.browser.find_element_by_tag_name("iframe"))
        elem = context.browser.find_element_by_xpath("//span[text()='$4']")
        elem.click()
        sleep(1)
        elem = context.browser.find_element_by_css_selector('#first-name')
        elem.send_keys("Sumit")
        sleep(1)
        elem = context.browser.find_element_by_css_selector('#last-name')
        elem.send_keys("Mahajan")
        sleep(1)
        elem = context.browser.find_element_by_css_selector('#street-address')
        elem.send_keys("33 Sheppard Ave E")
        sleep(1)
        elem = context.browser.find_element_by_css_selector('#apartment')
        elem.send_keys("501")
        sleep(5)
        #context.browser.switch_to.default_content()

    @Given("I have vp site open")
    def step(context):
        log.info(context.browser.title)
