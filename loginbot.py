from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the web driver (in this example, we're using Chrome)
# Replace with your own path to chromedriver
driver = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver')

# Navigate to the login page
driver.get('file:///C:/Users/ganes/OneDrive/Documents/Coding/WEB%20DEV%20PROGRAMMING/websites/instagram%20clone/loginpage.html')  # Replace with the actual login page URL

# Find the username and password input fields by their HTML attributes (e.g., name, id, class)
username_field = driver.find_element_by_name('uname')  # Replace with the actual field name
password_field = driver.find_element_by_name('pword')  # Replace with the actual field name

# Input your login credentials
username_field.send_keys('ganesh')  # Replace with your username
password_field.send_keys('renuse')  # Replace with your password

# Submit the login form (assuming there's a "Login" button)
login_button = driver.find_element_by_id('login')  # Replace with the actual button element
login_button.click()

# Optionally, you can add a delay or wait for a specific element to confirm successful login
# For example, wait for a "Welcome" message to appear on the next page
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# wait = WebDriverWait(driver, 10)
# welcome_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Welcome')]")))
#
# if "Welcome" in welcome_message.text:
#     print("Login successful!")
# else:
#     print("Login failed!")

# Close the web browser when done
driver.quit()
