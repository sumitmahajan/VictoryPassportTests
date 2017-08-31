from behave import Given,When,Then
import features.helpers.vppage as vp
import logging
from time import sleep
log = logging.getLogger(__name__)

class AdminSteps:
    @When("I visit Admin Page")
    def step(context):
        vp.visit_admin_url(context)

    @When('I login as Google+ User')
    def step(context):
        vp.click_by_css(context, "a.red")
        vp.type_by_css(context, 'input[type="email"]', "worldwide.sumit@gmail.com")
        vp.click_by_id(context, 'identifierNext')
        sleep(3)
        vp.type_by_css(context, 'input[type="password"]', 'Chetna123')
        vp.click_by_id(context, 'passwordNext')

    @Given("I am on donation page")
    @Then('I should be able to see new donation page button')
    def step(context):
        sleep(2)
        vp.assert_by_xpath(context, "//div//a[1]", "Donation Pages")

    @When('I go to new donation page')
    def step(context):
        vp.click_by_css(context, 'a.green')

    @When('I Fill all the values')
    def step(context):
        sleep(5)
        vp.type_by_css(context,'input[name="donation_page[name]"]', "TestPage")
        vp.type_by_css(context,'input[name="donation_page[title]"]', "TestPage")
        vp.click_by_css(context,"div#donation_page_business_unit_id_chosen.chosen-container.chosen-container-single")
        vp.select_dropdownoption(context, '//*[@id="donation_page_business_unit_id_chosen"]/div/ul/li[2]', '2')
        vp.select_dropdownclickoption(context,'//*[@id="donation_page_campaign_id_chosen"]',
                                      '//*[@id="donation_page_campaign_id_chosen"]/div/ul/li[2]', '2')
        vp.select_dropdownclickoption(context, '//*[@id="donation_page_issues_chosen"]',
                                      '//*[@id="donation_page_issues_chosen"]/div/ul/li[3]', '2')
        vp.click_by_xpath(context,'//*[@id="new_donation_page"]/div[16]/div[1]/div')
        vp.type_by_css(context, '#donation_page_custom_donation_amount',
                       "10:25:50:100:250:1000:2700:3000")
        vp.click_by_css(context, 'img[data-layout="single"]')
        vp.click_by_xpath(context,'//*[@id="new_donation_page"]/table/tbody/tr[1]/td[1]/div/div')
        vp.select_dropdownclickoption(context, '//*[@id="new_donation_page"]/div[15]/div',
                                      '//*[@id="new_donation_page"]/div[15]/div/div[2]/div[2]', '2')
        vp.click_by_css(context, 'button.green')
        sleep(15)