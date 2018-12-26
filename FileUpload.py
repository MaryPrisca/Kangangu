# from selenium import webdriver
#
#
# address = "http://127.0.0.1:8000/upload"
#
# # your executable path is wherever you saved the chrome webdriver
# chromedriver = "uploads/chromedriver-v2.42.exe"
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--no-sandbox')
#
# # browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
# browser = webdriver.Chrome(executable_path=chromedriver)
#
# # url = "https://www.duckduckgo.com"
# url = "http://127.0.0.1:8000/upload"
# browser.get(url)

import os
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('headless')

# set the window size
options.add_argument('window-size=1200x600')

# your executable path is wherever you saved the chrome webdriver
chromedriver = "uploads/chromedriver-v2.42.exe"

# initialize the driver
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

url = "http://127.0.0.1:8000/upload"
browser.get(url)

names_field = browser.find_element_by_name('name')
upload_field = browser.find_element_by_id('file')

db_tables1 = ['classes', 'events', 'exams']
db_tables2 = ['exam_results', 'subjects', 'system_setup']
db_tables3 = ['users']
table_file_paths1 = os.getcwd() + '/uploads/classes.xml \n' + os.getcwd() + '/uploads/events.xml \n'+ os.getcwd() + '/uploads/exams.xml'
table_file_paths2 = os.getcwd() + '/uploads/exam_results.xml \n' + os.getcwd() + '/uploads/subjects.xml \n'+ os.getcwd() + '/uploads/system_setup.xml'
table_file_paths3 = os.getcwd() + '/uploads/users.xml'

table_names_string = ",".join(db_tables1)  # Comma separated string

names_field.send_keys(table_names_string)
upload_field.send_keys(table_file_paths1)

submit_button = browser.find_element_by_id('submit-btn')
submit_button.click()