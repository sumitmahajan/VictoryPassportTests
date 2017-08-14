from behave import Given,When,Then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from features.helpers.browser import Browser as browser


class VpSteps:
    @When("I have vp site open")
    def step(context):
        browser.visit(browser)

    @Then("I can see footer Paid for by Stripe AAN")
    def step(context):
        browser.assert_by_class(browser,"paid-for-by-container","Paid for by Stripe AAN")


