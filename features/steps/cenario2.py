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


@given('que eu esteja na pagina de Preferences')
def step_impl(context):
    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    time.sleep(20)
    TouchAction(context.driver).tap(x=537, y=436).perform()
    time.sleep(10)

    el1 = context.driver.find_element_by_id("com.jogatina.tranca:id/buttonOptions")
    time.sleep(10)
    el1.click()
    time.sleep(10)


@given('desmarque os checkbox de configuração')
def step_impl(context):
    el4 = context.driver.find_element_by_xpath("/hierarchy/  android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.CheckBox")
    time.sleep(5)
    el4.click()
    el5 = context.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.CheckBox")
    time.sleep(5)
    el5.click()
    el6 = context.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.CheckBox")
    time.sleep(5)
    el6.click()
    time.sleep(10)
    el8 = context.driver.find_element_by_accessibility_id("Navigate up")
    time.sleep(5)
    el8.click() 


@when('estiver desmarcado')
def step_impl(context):
    el5 = context.driver.find_element_by_id("com.jogatina.tranca:id/buttonOptions")
    time.sleep(5)
    el5.click()
    time.sleep(5)
     
    

@then('foi feita a troca')
def step_impl(context):
    el8 = context.driver.find_element_by_accessibility_id("Navigate up")
    el8.click()
    time.sleep(5)
    context.driver.quit()
  