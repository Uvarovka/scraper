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

def parse_arbitr():
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

    browser.get('https://kad.arbitr.ru')  # Открываем сайт

    try:
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, "textarea[class=g-ph]").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, '[placeholder="название, ИНН или ОГРН"]').send_keys(name)
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, '[alt="Найти"]').click()
        time.sleep(5)

        path_link = str("//*[@class= 'b-cases']/tbody/tr/td/div/a")
        path_tab = str("//*[@class= 'b-cases']/tbody/tr")

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
            arbiter_array = ['Информация в картотеке арбитражных дел в качестве ответчика не найдена', 'https://kad.arbitr.ru/']
        else:
            arbiter_array = delo

    except Exception as e:
        print(e)
        arbiter_array = ['Информация в картотеке арбитражных дел не найдена', 'https://kad.arbitr.ru/']

    time.sleep(2)
    browser.close()

    print(arbiter_array)
    return arbiter_array

arbitr_result = parse_arbitr()

with open("parse_arbitr.pickle", "wb") as handle:
    pickle.dump(arbitr_result, handle)