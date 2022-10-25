
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def download_recap_img(url: str):
    edge_options = webdriver.EdgeOptions()


    # define path to download game recap
    prefs = {"download.default_directory" : "/Users/mkoloev/Desktop/mega-bot/gamerecap"}
    edge_options.add_experimental_option("prefs",prefs)
    browser = webdriver.Edge(executable_path='/Users/mkoloev/Desktop/mega-bot/msedgedriver', options=edge_options)
    browser.set_window_size(1400,800)
    browser.get(url)

    # clicking Download button
    elem = browser.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary.downloadrecap.text-white')
    elem.click()
    time.sleep(3)
    browser.close()


def del_recap_img(url):
    time.sleep(4)
    file_path = f'gamerecap/{url[url.find("gamerecap/"):]}.png'
    print(file_path)
    if os.path.exists(file_path):
        os.remove(file_path)
        print("The file has been removed")
    else:
        print("The file does not exist")
