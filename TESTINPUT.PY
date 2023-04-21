import csv
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service = Service("/path/to/chromedriver")

service.start()


login_url = "https://www.linkedin.com/login"

# Prompt user to enter email
email = input("Enter your email: ")

# Prompt user to enter password
password = input("Enter your password: ")


# Function to login to LinkedIn
def login(driver):
    action = ActionChains(driver)
    driver.implicitly_wait(10)

    # Navigate to LinkedIn login page
    driver.get(login_url)

    # wait for the email input field to appear on the page
    email_field = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    # Email input field on the LinkedIn login page
    email_input = driver.find_element(By.ID, "username")
    email_input.send_keys(email)

    # Password input field on the LinkedIn login page
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    # Sign-up button
    signin_btn = driver.find_element(By.CLASS_NAME, "btn__primary--large")
    signin_btn.click()


# Function to extract LinkedIn URLs from file
def extract_urls_from_file(filename):
    with open(filename, "r") as f:
        urls = [line.strip() for line in f]
    return urls


# Function for sending invitation
def send_invitation(driver, msg_column):
    # Navigate to user's LinkedIn page
    driver.get(url_column)
    if (
        driver.find_elements(
            By.XPATH, "//div[contains(@class,'pvs-profile-actions')]/button"
        )[1].text
        == "Pending"
    ):
        print("Connection request already sent")
    else:
        connect_btn = find_connect_btn(driver)
        if connect_btn:
            connect_btn.click()
            # Check if the message length is less than or equal to 300
            if msg_column:
                if len(msg_column) <= 300:
                    add_note = driver.find_elements(
                        By.XPATH,
                        "//div[contains(@class,'artdeco-modal__actionbar')]/button",
                    )[0]
                    add_note.click()
                    msg_box = driver.find_element(
                        By.XPATH, "//textarea[contains(@class,'ember-text-area')]"
                    )
                    msg_box.send_keys(msg_column)
            send_btn = driver.find_elements(
                By.XPATH, "//div[contains(@class,'artdeco-modal__actionbar')]/button"
            )[1]
            send_btn.click()
            print("Connection request sent")
        else:
            print("connect button not found.")


# Function for finding connect button on user's profile url
def find_connect_btn(driver):
    connect_btn = driver.find_elements(
        By.XPATH, "//div[contains(@class,'pvs-profile-actions')]/button"
    )[0]
    # Condition checks if the Connect button found visible directly on user's profile page.
    if connect_btn.text == "Connect":
        return connect_btn
    else:
        # Click the "More..." button to expand and find the Connect options
        more_button = driver.find_elements(
            By.XPATH, "//div[contains(@class,'pvs-profile-actions')]/div"
        )[2]
        if more_button:
            more_button.click()
            connect_btn = more_button.find_elements(By.TAG_NAME, "li")[2]
            return connect_btn
            print("Connection request sent")


# Ask user to input their choice
choice = input("Enter 1 to input LinkedIn user URL or 2 to input file path: ")

# Check user's choice
if choice == "1":
    # Ask user to input the LinkedIn URL
    url = input("Enter user's LinkedIn URL: ")

    driver = webdriver.Chrome()

    # driver.get(login_url)
    login(driver)

    # Navigate to user's LinkedIn profile
    driver.get(url)

    # Code to send connection request for single URL goes here

elif choice == "2":
    filename = "/home/developer/prospects.csv"
    driver = webdriver.Chrome()
    # Check if file exists
    if os.path.isfile(filename):
        urls = extract_urls_from_file(filename)
        reader = csv.DictReader(urls)
    else:
        print("File does not exist.")
        exit()

    # Loop through the URLs and send connection requests
    login(driver)
    time.sleep(30)
    for row in reader:
        url_column = row["URL"]
        name_column = row["NAME"]
        msg_column = row["MSG"]
        send_invitation(driver, msg_column)
else:
    print("Invalid choice.")
    exit()

# Close the Selenium WebDriver
driver.quit()
