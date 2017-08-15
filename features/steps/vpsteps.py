from behave import Given,When,Then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from features.helpers.config import Config as cf


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


