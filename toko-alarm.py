from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

extension_path = '/home/uzuki/.config/google-chrome-beta/Default/Extensions/cfhdojbkjhnklbpkdaibdccddilifddb/3.14_0.crx'
profile_path = '/home/uzuki/.config/google-chrome-beta/Default'
options = webdriver.ChromeOptions()
options.add_argument(f'--user-data-dir={profile_path}, --profile-directory=Profile1, --no-sandbox, --disable-infobars')
options.add_extension(extension_path)
driver_path = Service('/usr/local/bin/chromedriver')
url = "https://www.youtube.com/channel/UCXRlIK3Cw_TJIQC5kSJJQMg"
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

