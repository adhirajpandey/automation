"""

author: @endormi

Automated private repository creation and github desktop URL clone

"""

from selenium import webdriver
import pyautogui
import time


"""
Install browser driver:
https://www.seleniumhq.org/download/
"""

browser = webdriver.Chrome(r'file/to/chromedriver/if/needed')
browser.get('https://github.com/login')

user = ''
pw = ''
repo = ''
desc = ''

username = browser.find_element_by_id('login_field')
username.send_keys(user)
password = browser.find_element_by_id('password')
password.send_keys(pw)
log_in = browser.find_element_by_class_name('btn-block')
log_in.click()
new_repo = browser.find_element_by_link_text('New')
new_repo.click()
repo_name = browser.find_element_by_id('repository_name')
repo_name.send_keys(repo)
repo_desc = browser.find_element_by_id('repository_description')
repo_desc.send_keys(desc)
priv_repo = browser.find_element_by_id('repository_visibility_private')
priv_repo.click()
init = browser.find_element_by_id('repository_auto_init')
init.click()

"""
Additional for marketplace apps:
app = browser.find_element_by_name('quick_install[your_name][number]')
app.click()
"""

time.sleep(1)
create_repo = browser.find_element_by_class_name('first-in-line')
create_repo.click()
time.sleep(1)
clone = browser.find_element_by_class_name('get-repo-select-menu')
clone.click()
github_desktop = browser.find_element_by_class_name('js-get-repo')
github_desktop.click()
time.sleep(1)

"""
Depends on your computer, check where is your github desktop click point using
print(pyautogui.position())
"""
pyautogui.click(x=552, y=193)
time.sleep(3)
pyautogui.click(x=802, y=770)