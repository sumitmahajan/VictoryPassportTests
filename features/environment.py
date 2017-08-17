from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import json
import pavement

CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'config/parallel.json'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

with open(CONFIG_FILE) as data_file:
    CONFIG = json.load(data_file)


def before_feature(context, taskid):
    taskid = int(TASK_ID)
    desired_capabilities = CONFIG['environments'][taskid]

    for key in CONFIG["capabilities"]:
        if key not in desired_capabilities:
            desired_capabilities[key] = CONFIG["capabilities"][key]

    context.browser = webdriver.Remote(
        command_executor='http://127.0.0.1:4448/wd/hub',
        #desired_capabilities=DesiredCapabilities.EDGE)
        # command_executor='http://sumitmahajan1:Cgvydx3ZyqJBboxGTqWy@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_capabilities)


def after_feature(context, feature):
    context.browser.quit()


