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


@given('que esteja na pagina de Preferencias')
def go_to_page(context):
    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    time.sleep(15)
    TouchAction(context.driver).tap(x=521, y=489).perform()
    time.sleep(5)

    el1 = context.driver.find_element_by_id("com.jogatina.tranca:id/buttonOptions")
    time.sleep(10)
    el1.click()
    time.sleep(5)


@when('eu escolho o Nível de Dificuldade Normal')
def create_todo(context):
    el6 = context.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[8]/android.widget.RelativeLayout")
    el6.click()
    time.sleep(5)
    el7 = context.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]")
    el7.click()
    time.sleep(5)


@then('verifico se "{texto}" está selecionado')
def check_todo(context, texto):
    el5 = context.driver.find_element_by_id("android:id/button2")
    el5.click()  
    time.sleep(5)

    time.sleep(10)
    el5 = context.driver.find_element_by_id("android:id/button2")
    el5.click() 
    time.sleep(5)

    context.driver.quit()

