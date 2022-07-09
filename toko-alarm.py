from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

extension_path = '/your crx file path'
profile_path = 'chrome profile path'
options = webdriver.ChromeOptions()
options.add_argument(f'--user-data-dir={profile_path}, --profile-directory=Profile1, --no-sandbox, --disable-infobars')
options.add_extension(extension_path)
driver_path = Service('/usr/local/bin/chromedriver')
url = "the home page of youtuber"
driver = webdriver.Chrome(options = options, service = driver_path)
driver.implicitly_wait(30)

for _ in range(3):

    try:

        driver.get(url)
#        title_container = driver.find_element(By.ID, "title-container")
        play_button = driver.find_element(By.LINK_TEXT, "すべて再生")

        play_button.click()
    except Exception as e:
        print(e)
    else:
        break

ct = 2*60*60
time.sleep(ct)

driver.quit()

