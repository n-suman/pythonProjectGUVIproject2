from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import msedgedriver
import time

from selenium.webdriver.support.wait import WebDriverWait

msedgedriver.install()

# Initialize the Edge Webdriver
driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)

# TestCaseID: TC_PIM_01
# Locate the "Forgot Password" link and click it
forgot_password_link = driver.find_element(By.Link_TEXT, 'forgot your password')
forgot_password_link.click()

# Find the email input field and enter the email address
email_input = driver.find_element(By.NAME, 'username')
email_input.send_keys('Admin')

# Locate and click the "Reset Password" button
reset_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]')
reset_button.click()
print("Reset password link sent successfully")

driver.quit()

# TestCaseID:TC_PIM_02
# Launch url
driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)

# Login as Admin
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
# Submit the login form
driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

#  the dashboard page  gets loaded  and then click the Admin tab
admin_tab = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
admin_tab.click()

# Locate the header elements on the admin page
admin_header = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[1]/a/div[2]/img')


# Validate the page title
page_title = driver.title
expected_title = 'Orange HRM'
actual_title = page_title.text.strip()

if actual_title == expected_title:
    print(f"Header title is correct: {actual_title}")
else:
    print(f"Header title is incorrect. Expected: {expected_title}, Actual: {actual_title}")

dropdown = driver.find_element(By.XPATH, 'y/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')

# Extract the options from the dropdown
dropdown_options = dropdown.find_elements(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span/i')
# Define the expected labels in the dropdown
expected_labels = ['User Management', 'Job', 'Organisation','Qualifications', 'Nationalities', 'Corporate Banking','Configuration']


# TCCaseID: TC_PIM_03
# Wait for the admin page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/aside')))

# Locate the side pane element (the element that contains the options)
side_pane = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav')

# Extract the options from the side pane
side_pane_options = side_pane.find_elements(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]')
side_pane_options = side_pane.find_elements(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]')
side_pane_options = side_pane.find_elements(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]')
side_pane_options = side_pane.find_elements(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]')
side_pane_options = side_pane.find_elements(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]')
side_pane_options = side_pane.find_elements(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]')

# Define the expected side pane option texts
expected_options = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance']

# Extract the actual option texts and compare them with the expected texts
actual_options = [option.text.strip() for option in side_pane_options]

for option in expected_options:
    if option in actual_options:
        print(f"Option '{option}' is present in the side pane.")
    else:
        print(f"Option '{option}' is not found in the side pane.")


# Close the browser window
driver.quit()


