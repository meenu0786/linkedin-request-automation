import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service = Service('/path/to/chromedriver')

service.start()

# Prompt user to enter email
email = input("Enter your email: ")

# Prompt user to enter password
password = input("Enter your password: ")

network_url = 'https://www.linkedin.com/mynetwork/'
login_url = 'https://www.linkedin.com/login'


driver = webdriver.Chrome()

action = ActionChains(driver)
driver.implicitly_wait(10)


# LinkedIn login page
driver.get(login_url)

# wait for the email input field to appear on the page
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)

# Email input field on the LinkedIn login page
email_input = driver.find_element(By.ID, 'username')
email_input.send_keys(email)

# Password input field on the LinkedIn login page
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys(password)

# Sign-up button
signin_btn = driver.find_element(By.CLASS_NAME, 'btn__primary--large')
signin_btn.click()

# Network Tab page
driver.get(network_url)

sections = driver.find_elements(
    By.XPATH,  # no whitespace after closing parenthesis
    "//ul[contains(@class,'artdeco-card')]/li"
)

req_sent = 0
for sec in sections:
    text = sec.find_element(By.XPATH, './/div/h2').text
    print(text)
    if text in "Software Engineers you may know":
        links = sec.find_elements(By.XPATH, ".//ul/li")
        for card in links:
            if req_sent >= 2:
                break
            time.sleep(2)
            btn = card.find_element(
                By.XPATH,
                ".//button[contains(@aria-label, 'connect')]"
            )
            try:
                btn.click()
                req_sent = req_sent + 1
                print("[+] Request sent ")
            except:
                pass

print("***********************************")
time.sleep(5)
