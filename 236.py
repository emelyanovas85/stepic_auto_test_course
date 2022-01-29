from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    

    xz = WebDriverWait(browser, 15)
    wait = xz.until(
        EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
 

    btn = browser.find_element_by_css_selector('#book')
    btn.click()

    btn2 = browser.find_element_by_css_selector('#solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn2)

    def calc(x):
        return str(math.log(abs(12*math.sin(x))))

    x_e = browser.find_element_by_css_selector('#input_value')
    x = int(x_e.text)
    y = calc(x)

    input = browser.find_element_by_tag_name("#answer")
    input.send_keys(y)

    btn2.click()



    #input2 = browser.find_element_by_css_selector('.trollface.btn')
    #input2.click()

    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)
    
        
#    confirm = browser.switch_to.alert
#    confirm.accept()

    
    #def calc(x):
    #    return str(math.log(abs(12*math.sin(x))))

    #x_e = browser.find_element_by_css_selector('#input_value')
    #x = int(x_e.text)
    #y = calc(x)
    
    #print(y)
#
    #input = browser.find_element_by_tag_name("#answer")
    #input.send_keys(y)
#
#    input2 = browser.find_element_by_css_selector('input[type="checkbox"]')
#    input2.click()
#
#
#    button2 = browser.find_element_by_css_selector('input[type="radio"]#robotsRule')
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
#    button2.click()
#
#
    #button = browser.find_element_by_css_selector(".btn")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #button.click()


finally:
    
    time.sleep(20)
    browser.quit()