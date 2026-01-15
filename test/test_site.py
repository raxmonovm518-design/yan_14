
from selenium.webdriver.common.by import By
import time

from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open_homepage()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is("Samsung galaxy s6")


def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open_homepage()
    homepage.click_monitor()
    # browser.get('https://www.demoblaze.com/')
    # monitor_link = browser.find_element(By.CSS_SELECTOR, 'a[onclick="byCat(\'monitor\')"]')
    # monitor_link.click()
    time.sleep(5)
    homepage.check_that_products_counts(2)
    monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    assert len(monitors) == 2