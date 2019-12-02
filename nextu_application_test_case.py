import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NextUApplicationProcess(unittest.TestCase):

    #  Setting Up And Getting the job
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/Users/saadpasta/Documents/chromedriver')
        

    # Click On Start Button On Job Info Page
    def test_click_button_job_info(self):
        driver = self.driver
        driver.get("http://localhost:3000/job/5a57baea-3072-4699-99c3-55775520eb43/info")
        elem = driver.find_element_by_id("main-button")
        elem.click()

    # Fill Application Start Form
    def fill_application_start_form(self):
        driver = self.driver
        name = driver.find_element_by_name("name")
        name.clear()
        name.send_keys("Saad")

        email = driver.find_element_by_name("email")
        email.clear()
        email.send_keys("saad@gmail.com")

        number = driver.find_element_by_name("mobileNumber")
        number.clear()
        number.send_keys("3243454077")
        
        checkbox = driver.find_element_by_class_name("terms-condition-checkbox")
        checkbox.click()

    # Click Application Start Button To Proceed
    def click_application_submit_button(self):
        driver = self.driver
        button = driver.find_element_by_id("sumbit-button")
        button.click()

    # Getting job journey url from a tag
    def click_job_journey_url(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        job_journey_url = wait.until(EC.element_to_be_clickable((By.ID, 'job_journey_url')))
        job_journey_url.click()

    # click on job journey buisness question start main button
    def click_buisness_question_start_button(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        job_journey_start_button = wait.until(EC.element_to_be_clickable((By.ID, 'main-button')))
        job_journey_start_button.click()

    # click on quiz option button
    def click_buiness_question_option(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        quiz_list_options = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'quiz-list-item')))
        quiz_list_options.click()

    # wait for success result and then quit
    def tearDown(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        success_result = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'status')))
        driver.close()

# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
if __name__ == "__main__":
    unittest.main()
