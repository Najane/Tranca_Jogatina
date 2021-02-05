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


@given('que eu clique em Play Now!')
def step_impl(context):
    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    time.sleep(20)
    TouchAction(context.driver).tap(x=537, y=436).perform()
    time.sleep(10)

    el1 = context. driver.find_element_by_id("com.jogatina.tranca:id/buttonSinglePlayer")
    el1.click()
    time.sleep(10)


@given('escolha 2 Playeres')
def step_impl(context):
    el2 = context.driver.find_element_by_id("com.jogatina.tranca:id/btn2Players")
    el2.click()
    time.sleep(10)
    

@given('decida sair da jogada')
def step_impl(context):
    context.driver.back()
    time.sleep(5)  
    el3 = context.driver.find_element_by_id("com.jogatina.tranca:id/textViewButton") 
    el3.click()
    time.sleep(10)
    context.driver.back() 
    time.sleep(5)
    el4 = context.driver.find_element_by_id("com.jogatina.tranca:id/textViewButtonExtra")
    el4.click() 
    time.sleep(5)

@when('eu estiver fora da jogada, retomo a jogada')
def step_impl(context):
    el9 = context.driver.find_element_by_id("com.jogatina.tranca:id/buttonSinglePlayer")
    el9.click()
    time.sleep(5)


@then('aceito continuar com a jogada anterior')
def step_impl(context):
    el10 = context.driver.find_element_by_id("com.jogatina.tranca:id/textViewButton")
    el10.click() 
    time.sleep(5)
    context.driver.back()
    time.sleep(5)
    el11 = context.driver.find_element_by_id("com.jogatina.tranca:id/textViewButtonExtra")
    el11.click() 
    time.sleep(5)
    context.driver.quit()
