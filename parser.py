# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def download_recap_img(url: str):
    browser_options = Options()
    browser_options.add_argument("--headless")

    prefs = {"download.default_directory": "./gamerecap"}
    browser_options.add_experimental_option("prefs", prefs)
    browser_options.add_argument("--headless")
    browser_options.add_argument('--no-sandbox')
    service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
    print('service initialized')
    driver = webdriver.Edge(service=service, options=browser_options)
    print('driver initialized')
    driver.set_window_size(1400, 800)
    driver.get(url)
    print('got url')

    # clicking Download button
    elem = driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary.downloadrecap.text-white')
    elem.click()
    time.sleep(3)
    driver.quit()


def del_recap_img(url):
    time.sleep(4)
    file_path = f'./{url[url.find("gamerecap/"):]}.png'
    print(file_path)
    if os.path.exists(file_path):
        os.remove(file_path)
        print("The file has been removed")
    else:
        print("The file does not exist")
