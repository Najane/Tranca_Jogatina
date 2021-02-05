from behave import given, when, then
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time


caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "11"
caps["deviceName"] = "NNIV140030"
caps["appPackage"] = "com.jogatina.tranca"
caps["appActivity"] = "com.jogatina.menu.Splash"
caps["automationName"] = "UiAutomator2"
caps["AppWaitpackage"] = "com.jogatina.MainMenu"
caps["ensureWebviewsHavePages"] = True
caps["locale"] = "US"
caps["language"] = "en"


@given('que eu esteja na pagina MainMenu')
def go_to_page(context):
    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    print("awaint 15s before skipping google accounts")
    time.sleep(15)
    TouchAction(context.driver).tap(x=521, y=489).perform()
    print("\n Google Account skipped await 5 seconds to next step")
    time.sleep(5)


@when('o idioma do device esta em Ingles')
def create_todo(context):
    assert caps["language"] == "en"


@then('existe um botao com o texto "{texto}"')
def check_todo(context, texto):

    el1 = context.driver.find_element_by_id("com.jogatina.tranca:id/buttonSinglePlayer")

    time.sleep(15)
    result = el1.text
    el1.click()
    context.driver.quit()
    assert texto == result
