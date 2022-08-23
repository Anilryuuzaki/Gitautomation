from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import clipboard

#Taking login credentials as input
email = input("enter email")
password = input("Enter password")

repo_name = input('Enter reponame')
branch_name = 'main'
project_name = input('Enter Project name')

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://id.atlassian.com/login?application=bitbucket&continue=https%3A%2F%2Fbitbucket.org%2Faccount%2Fsignin%2F%3Fnext%3D%252F%26redirectCount%3D1")

login_field = driver.find_element(By.ID, "username")
login_field.send_keys(email)
sign = driver.find_element(By.ID,"login-submit")
sign.submit()

time.sleep(3)

login_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div/section/div[2]/form/div[1]/div[2]/div/div/div/div/div/input")
login_field.send_keys(password)
sign = driver.find_element(By.ID,"login-submit")
sign.submit()

time.sleep(7)
createrepo = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/a")
createrepo.click()

time.sleep(3)

# selectproject = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/section/div/form/div[1]/div[1]/div[1]/div[1]/a/span[1]")
# selectproject.click()

# time.sleep(2)

# createNewProject = driver.find_element(By.XPATH,"/html/body/div[21]/ul/li[4]")
# createNewProject.click()


# time.sleep(1)

enterProject_name = driver.find_element(By.ID,'id_project_name')
enterProject_name.send_keys(project_name)


time.sleep(3)


repository_name = driver.find_element(By.ID,'id_name')
repository_name.send_keys(repo_name)

time.sleep(3)

idbranch_name = driver.find_element(By.ID,'id_branch_name')
idbranch_name.send_keys(branch_name)



time.sleep(2)
#click the create repository
createreposubmit = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div/section/div/form/div[2]/div/button")
createreposubmit.submit()

time.sleep(4)

#click the clone button
cloneCode = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div/header/div/div/div/div[2]/div/div[2]/button")
cloneCode.click()

time.sleep(2)

dropdown = driver.find_element(By.XPATH,"/html/body/div[2]/div[4]/div/div[3]/div[2]/section/div/div[1]/div/div/div[2]/div/span")
dropdown.click()

time.sleep(2)

ssh_url = driver.find_element(By.XPATH,"/html/body/div[2]/div[4]/div/div[3]/div[2]/section/div/div[1]/div/div/div[1]/div")
ssh_url.click()

#copy the url of the repo
copytheurl = driver.find_element(By.XPATH,"/html/body/div[2]/div[4]/div/div[3]/div[2]/section/div/div[2]/div/div/div[1]/div[2]/div/button/span/span/span")
copytheurl.click()

time.sleep(2)

#paste the url to clipboard
gitClone_url =  clipboard.paste()
bit_url = gitClone_url.replace('git clone','')
print(bit_url)

time.sleep(2)

#os operations
os.system('git init')
os.system('git add .')
os.system('git status')
os.system('git commit -m "Initial Commit"')
os.system('git remote add origin'+bit_url )
os.system('git push -f origin master')


print('\n task completed')
