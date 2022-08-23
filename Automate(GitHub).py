import email
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import clipboard
import pyperclip
import sys

email = input("Enter the email")
password = input("Enter the password")

repo_name = input('Enter repo name')

# try:
#     repo_name = sys.argv[1]
# except:
#     print('Please provide repo name.')
#     sys.exit()

# try:
#     visibility = sys.argv[2]
# except:
#     visibility = 'public'

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://github.com/login")

login_field = driver.find_element(By.ID, "login_field")
login_field.send_keys(email)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)

sign = driver.find_element(By.XPATH,"/html/body/div[3]/main/div/div[4]/form/div/input[12]")
sign.submit()

driver.get('https://github.com/new')

repository_name = driver.find_element(By.NAME,'repository[name]')
repository_name.send_keys(repo_name)

time.sleep(3)

# visibility_radio_input = driver.find_element(By.XPATH,
#     f'//input[@name="repository[visibility]"][@value="{visibility}"]')
# visibility_radio_input.click()

# repository_name.submit()

visibility_radio_input = driver.find_element(By.ID,
    'repository_visibility_private')
visibility_radio_input.click()

addReademe = driver.find_element(By.ID, "repository_auto_init")
addReademe .click()

createreposubmit = driver.find_element(By.XPATH, "/html/body/div[5]/main/div/form/div[5]/button")
createreposubmit.submit()

try:
    content = driver.find_element(By.XPATH,
        '//clipboard-copy[@for="empty-setup-push-repo-echo"]')
    content.click()
    time.sleep(1)
    print('****Repository created successfully****', end="\n\n")
    # print(pyperclip.paste())
    print(f"git remote add origin https://github.com/llawliet4723/{repo_name}.git")
    print("git branch -M master")
    print("git push -u origin master")
except:
    print('Repository cannot be created. (Confirm the repo name is unique)')