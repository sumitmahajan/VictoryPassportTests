from behave import Given,When,Then
import features.helpers.vppage as vp
import logging
from time import sleep
log = logging.getLogger(__name__)

class VpSteps:

    @When("I have vp site open")
    def step(context):
        vp.visit_url(context)

    @Then("I can see footer Paid for by Stripe AAN")
    def step(context):
        vp.assert_by_class(context,"paid-for-by-container","Paid for by Stripe AAN")

    @When("I fill all fields on vp page")
    def step(context):
        vp.switch_to_iframe(context,"iframe")
        vp.click_by_xpath(context,"//span[text()='$4']")
        vp.type_by_css(context, "#first-name", "Sumit")
        vp.type_by_css(context, "#last-name", "Mahajan")
        vp.type_by_css(context, "#street-address", "33 Sheppard Ave E")
        vp.type_by_css(context, "#apartment", "501")
        vp.type_by_css(context, "#city", "Toronto")
        vp.type_by_css(context, "#zip-code", "12345")
        vp.type_by_css(context, "#email-address", "sumit@stagwell.tech")
        vp.type_by_css(context, "#phone", "647-973-8258")
        vp.type_by_css(context, "#employer", "Stagwell")
        vp.select_dropdown(context,"","")
        vp.type_by_css(context, "#occupation", "Analyst")
        if context.browser.capabilities["browserName"] == "MicrosoftEdge":
            vp.switch_to_inner_frame(context, "")
            sleep(4)
            vp.click_by_css(context, '#card-element')
            vp.type_by_css(context, 'iframe[title = "Secure payment input frame"]', "4242424242424242")
        else:
            vp.switch_to_inner_frame(context, "")
            vp.click_by_xpath(context, '//*[@id="root"]/form/div/div[2]/span[1]/span[2]/label')
            vp.type_by_xpath(context, '//*[@id="root"]/form/div/div[2]/span[1]/span[2]/label/input',
                             "42424242424242420121123")
        vp.switch_to_default(context)
        vp.switch_to_iframe(context, "iframe")
        #context.browser.switch_to.default_content()

    @Given("I have vp site open")
    def step(context):
        log.info(context.browser.title)

    @When("I click on contribute button")
    def step(context):
        vp.click_by_css_script(context, "#contribute-button")

    @Then("I can make contribution")
    def step(context):
        log.info("You")
