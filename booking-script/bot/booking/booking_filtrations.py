from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltrations:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self, star_values):
        for star_value in star_values:
            self.driver.find_element(By.CSS_SELECTOR, f'[data-filters-item="class:class={star_value}"]').click()