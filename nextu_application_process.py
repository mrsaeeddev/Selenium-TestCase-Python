import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


#  Setting Up And Getting the job
driver = webdriver.Chrome(executable_path=r'/Users/saadpasta/Documents/chromedriver')

# Click On Start Button On Job Info Page

driver.get("http://localhost:3000/job/5a57baea-3072-4699-99c3-55775520eb43/info")
elem = driver.find_element_by_id("main-button")
elem.click()

# Fill Application Start Form

name = driver.find_element_by_name("name")
name.clear()
name.send_keys("Saad")

email = driver.find_element_by_name("email")
email.clear()
email.send_keys("saad@gmail.com")

country_code = Select(driver.find_element_by_id('countryPrefixCode'))

# select by value 
country_code.select_by_value('92')

# driver.find_element_by_xpath("//select[@name='select']/option[text()='PK (+92)']").click()


number = driver.find_element_by_name("mobileNumber")
number.clear()
number.send_keys("3243454077")

checkbox = driver.find_element_by_class_name("terms-condition-checkbox")
checkbox.click()

# Click Application Start Button To Proceed


button = driver.find_element_by_id("sumbit-button")
button.click()

# Getting job journey url from a tag

wait = WebDriverWait(driver, 20)
job_journey_url = wait.until(EC.element_to_be_clickable((By.ID, 'job_journey_url')))
job_journey_url.click()

# click on job journey buisness question start main button
job_journey_start_button = wait.until(EC.element_to_be_clickable((By.ID, 'main-button')))
job_journey_start_button.click()

# click on quiz option button
quiz_list_options = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'quiz-list-item')))
quiz_list_options.click()

# wait for success result and then quit
success_result = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'status')))
driver.close()

# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
