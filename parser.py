from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import os

def download_recap_img(url: str):
    browser_options = Options()
    browser_options.add_argument("--headless")
    browser_options.add_argument('--no-sandbox')
    browser_options.add_argument('–headless')
    browser_options.add_argument('–no - sandbox')
    browser_options.add_argument('–disable - gpu')
    browser_options.add_argument('–window - size = 1280×1696')
    browser_options.add_argument('–user - data - dir = / tmp / user - data')
    browser_options.add_argument('–hide - scrollbars')
    browser_options.add_argument('–enable - logging')
    browser_options.add_argument('–log - level = 0')
    browser_options.add_argument('–v = 99')
    browser_options.add_argument('–single - process')
    browser_options.add_argument('–data - path = / tmp / data - path')
    browser_options.add_argument('–ignore - certificate - errors')
    browser_options.add_argument('–homedir = / tmp')
    browser_options.add_argument('–disk - cache - dir = / tmp / cache - dir')
    browser_options.add_argument('user - agent = Mozilla / 5.0(X11;Linuxx86_64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 61.0.3163.100Safari / 537.36')
    
    
    prefs = {"download.default_directory": "./gamerecap"}
    browser_options.add_experimental_option("prefs", prefs)
    service = ChromeService(executable_path=ChromeDriverManager().install())
    print('service initialized')
    driver = Chrome(service=service, options=browser_options)
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
