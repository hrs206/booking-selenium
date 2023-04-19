from selenium import webdriver
import booking.constants as const
import os
from selenium.webdriver.common.by import By
import time
from booking.booking_filtrations import BookingFiltrations
from prettytable import PrettyTable



class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"D:\Selenium Projects\Selenium Drivers") -> None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)
        self.driver_path = driver_path
        os.environ["PATH"] += self.driver_path
        super().__init__(options=options)
        self.implicitly_wait(15)


    def land_first_page(self):
        self.get(const.BASE_URL)
        
    def dismiss_sign_in(self):
        button = self.find_element(By.CSS_SELECTOR, '[aria-label="Dismiss sign-in info."]')
        button.click()
                
    def change_currency(self, currency="INR"):
        change_button = self.find_element(By.CSS_SELECTOR, '[aria-label="Prices in Indian Rupee"]')
        change_button.click()
        elements = self.find_elements(By.CSS_SELECTOR, '[data-testid="selection-item"]')
        for element in elements:
            if currency in element.text:
                element.click()
                break
            
    def select_place(self, place):
        search_bar = self.find_element(By.NAME, "ss")
        search_bar.clear()
        search_bar.send_keys(place)
        time.sleep(2)
        elements = self.find_elements(By.CLASS_NAME, "a40619bfbe")
        for element in elements:
             if place in element.text:
                element.click()
                break
    
    def choose_date(self, start_date, end_date):
        s_date = self.find_elements(By.CSS_SELECTOR, f'[data-date="{start_date}"]')
        e_date = self.find_elements(By.CSS_SELECTOR, f'[data-date="{end_date}"]')
        nxt = self.find_element(By.CSS_SELECTOR, '[class="fc63351294 a822bdf511 e3c025e003 fa565176a8 cfb238afa1 c334e6f658 ae1678b153 c9fa5fc96d be298b15fa"]')
        date_not_changed = True
        s_date_not_changed = True
        e_date_not_changed = True
        while date_not_changed:
            if s_date_not_changed:
                if s_date:
                    s_date[0].click()
                    s_date_not_changed = False
                else:
                    nxt.click()
                    s_date = self.find_elements(By.CSS_SELECTOR, f'[data-date="{start_date}"]')
            if e_date_not_changed:
                if e_date:
                    e_date[0].click()
                    e_date_not_changed  = False
                else:
                    nxt.click()
                    e_date = self.find_elements(By.CSS_SELECTOR, f'[data-date="{end_date}"]')
            if not e_date_not_changed and not s_date_not_changed:
                date_not_changed = False
                
            
                
                
    def total_persons(self, adults, children, age, rooms):
        time.sleep(2)
        occupancy_btn = self.find_element(By.CSS_SELECTOR, '[data-testid="occupancy-config"]')
        occupancy_btn.click()
        time.sleep(2)
        minus_btn = self.find_element(By.CSS_SELECTOR, '[class="fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 cd7aa7c891"]')
        minus_btn.click()

        plus_btns = self.find_elements(By.CSS_SELECTOR, '[class="fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 d64a4ea64d"]')

        for _ in range(adults-1):
            plus_btns[0].click()
        for _ in range(children):
            plus_btns[1].click()
        i = 0
        c = 0
        for each in age:
            c = i
            kids = self.find_elements(By.CSS_SELECTOR, '[data-testid="kids-ages-select"]')
            kids[i].click()
            i = i+1
            age_options = self.find_elements(By.TAG_NAME, "option")
            for option in age_options:
                if f"{each} years old" == option.text or f"{each} year old" == option.text:
                    if c>0:
                        c = c -1
                        continue
                    option.click()
                    break
            
        for _ in range(rooms-1):
            plus_btns[2].click()
            
        self.find_element(By.CSS_SELECTOR, '[class="fc63351294 a822bdf511 e2b4ffd73d f7db01295e c938084447 a9a04704ee d285d0ebe9"]').click()
        
    def search(self):
        self.find_element(By.CSS_SELECTOR, '[class="fc63351294 a822bdf511 d4b6b7a9e7 cfb238afa1 c938084447 f4605622ad aa11d0d5cd"]').click()

    
    def apply_filtrations(self, star_values):
        filtration = BookingFiltrations(driver=self)
        filtration.apply_star_rating(star_values)
        time.sleep(3)

    def report(self):
        price_list=[]
        title_list=[]
        rating_list=[]
        final = []
        titles = self.find_elements(By.CSS_SELECTOR,'[data-testid="title"]')
        for title in titles:
            title_list.append(title.text)
        prices = self.find_elements(By.CSS_SELECTOR, '[data-testid="price-and-discounted-price"]')
        for price in prices:
            price_list.append(price.text)
        ratings = self.find_elements(By.CSS_SELECTOR, '[class="b5cd09854e d10a6220b4"]')
        for rating in ratings:
            rating_list.append(rating.text)
            final = zip(title_list, price_list, rating_list)

        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(final)
        print(table)
            
            


                

             
    