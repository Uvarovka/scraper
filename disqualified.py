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

def parse_disqualified():
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

    browser.get('https://service.nalog.ru/disqualified.do')  # Открываем сайт

    try:
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, '[name="query"]').click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, '[name="query"]').send_keys(name)
        time.sleep(1)
        browser.find_element(By.ID, "btnSearch").click()
        time.sleep(5)
        
        
        path_link = str("//*[@class= 'prop prop--number']/dl/dt/a")
        path_tab = str("//*[@class= 'search-results__data']/div['search-result ']")

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
            disqualified_array = ['Информация в реестре дисквалифицированных лиц (рдл) не найдена', 'https://service.nalog.ru/disqualified.do']
        else:
            disqualified_array = delo

    except Exception as e:
        print(e)
        disqualified_array = ['Информация в реестре дисквалифицированных лиц (рдл) не найдена', 'https://service.nalog.ru/disqualified.do']

    time.sleep(2)
    browser.close()

    print(disqualified_array)
    return disqualified_array

disqualified_result = parse_disqualified()

with open("parse_disqualified.pickle", "wb") as handle:
    pickle.dump(disqualified_result, handle)