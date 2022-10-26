from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def download_recap_img(url: str):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    prefs = {"download.default_directory": "./gamerecap"}
    chrome_options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    browser.set_window_size(1400, 800)
    browser.get(url)

    # clicking Download button
    elem = browser.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary.downloadrecap.text-white')
    elem.click()
    time.sleep(3)
    browser.close()


def del_recap_img(url):
    time.sleep(4)
    file_path = f'./{url[url.find("gamerecap/"):]}.png'
    print(file_path)
    if os.path.exists(file_path):
        os.remove(file_path)
        print("The file has been removed")
    else:
        print("The file does not exist")
