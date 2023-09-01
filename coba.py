from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://app.jubelio.com/login")

driver.find_element("name","email").send_keys("qa.rakamin.jubelio@gmail.com")
driver.find_element("name","password").send_keys("Jubelio123!")
driver.find_element("xpath",'/html/body/div[1]/div/div/div[1]/div/div[2]/div/form/button').click()