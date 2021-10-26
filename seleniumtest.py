from time import sleep
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = EdgeOptions()
options.use_chromium = True
options.add_extension('C:/edgedriver_win64/extension_1_32_4_0.crx')
driver = Edge(executable_path='C:/edgedriver_win64/msedgedriver.exe', options=options)
driver.get('https://play2048.co/')
driver.maximize_window()
elem = driver.find_element_by_class_name('container')
for i in range(10):
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()
    sleep(1)
driver.close()
