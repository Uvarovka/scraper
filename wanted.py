import data_input
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import time
import pickle

def read_dict():
    with open("dict.pickle", "rb") as handle:
        my_dict = pickle.load(handle)
    return my_dict

my_dict = read_dict()

def parse_wanted():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    browser = webdriver.Chrome(options=chrome_options)

    name = my_dict["fio"]

    stealth(browser,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    browser.get('https://fsin.gov.ru/criminal/')  # Открываем сайт

    try:
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, '[size="20"]').click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, '[size="20"]').send_keys(name)
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, '[name="set_filter"]').click()
        time.sleep(5)
        
        
        path_link = str("//*[@class= 'sl-item-image']/a")
        path_tab = str("//*[@class= 'section-list type-6']/div['sl-item']")

        links = browser.find_elements(By.XPATH, path_link)
        tabs = browser.find_elements(By.XPATH, path_tab)

        len_link_tabs = len(links)

        urls = []
        delo = []
        for url in links:
            urls.append(url.get_attribute('href'))
        for d in tabs:
            delo.append(d.text)
        y = 1
        for i in range(0, len_link_tabs):
            delo.insert(y, urls[i])
            y +=2
        if delo == []:
            wanted_array = ['Информация в списке розыска не найдена', 'https://fsin.gov.ru/criminal/']
        else:
            wanted_array = delo

    except Exception as e:
        print(e)
        wanted_array = ['Информация в списке розыска не найдена', 'https://fsin.gov.ru/criminal/']

    time.sleep(2)
    browser.close()

    print(wanted_array)
    return wanted_array

wanted_result = parse_wanted()

with open("parse_wanted.pickle", "wb") as handle:
    pickle.dump(wanted_result, handle)