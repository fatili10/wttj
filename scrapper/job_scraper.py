from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd
from .utils import get_page_time

def head_info():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    return chrome_options

def get_all_data(keyword, country, country_code):
    driver = webdriver.Chrome(options=head_info())
    p = 1
    results = []

    while True:
        url = f'https://www.welcometothejungle.com/en/jobs?refinementList%5Boffices.country_code%5D%5B%5D={country_code}&query={keyword}&page={p}&aroundQuery={country}&searchTitle=True'
        driver.get(url)
        driver.implicitly_wait(10)

        jobs = driver.find_elements(By.CSS_SELECTOR, '[data-testid="search-results-list-item-wrapper"]')
        if not jobs:
            break

        for job in jobs:
            try:
                link = job.find_element(By.CSS_SELECTOR, 'a[href^="/en/companies"]').get_attribute('href')
                date_annonce = get_page_time(link)
                results.append({
                    "link": link,
                    "date_annonce": date_annonce,
                    "date_extract": datetime.today().strftime("%Y-%m-%dT%H:%M:%SZ")
                })
            except Exception as e:
                print(f"Erreur sur une annonce : {e}")

        p += 1

    driver.quit()
    return pd.DataFrame(results)
