from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_feature(context, feature):
    context.browser = webdriver.Remote(
        command_executor='http://sumitmahajan1:Cgvydx3ZyqJBboxGTqWy@hub.browserstack.com:80/wd/hub',
        desired_capabilities=DesiredCapabilities.FIREFOX)


def after_feature(context, feature):
    context.browser.quit()


