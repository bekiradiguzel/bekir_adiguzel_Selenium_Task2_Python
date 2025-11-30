from pages.base_page import BasePage
from Locators import *

class HomePage(BasePage):
    # --- Locators ---
    # These map the Locators.py variables to the instance for easy access (home_page.COMPANY_BUTTON)
    ACCEPT_COOKIES_BUTTON = ACCEPT_COOKIES_BUTTON
    COMPANY_BUTTON = COMPANY_BUTTON
    CAREERS_BUTTON = CAREERS_BUTTON
    FIND_DREAM_JOB = FIND_DREAM_JOB
    FILTER_BY_LOCATION = FILTER_BY_LOCATION
    FILTER_BY_DEPARTMENT = FILTER_BY_DEPARTMENT
    JOB_LIST = JOB_LIST
    LOCATION_IST = LOCATION_IST
    LOCATION = LOCATION
    LOCATION_CONTAINER = LOCATION_CONTAINER
    
    CLICK_DOWN = CLICK_DOWN
    CLICK_ALL = CLICK_ALL
    REMOVE_ITEM1 = REMOVE_ITEM1
    CLICK_DOWN2 = CLICK_DOWN2
    OPEN_POSITIONS_HEADER = OPEN_POSITIONS_HEADER
    ILGILI_POZISYON = ILGILI_POZISYON
    VIEW_ROLE_BUTTON = VIEW_ROLE_BUTTON
    NEXT_PAGE_ARROW = NEXT_PAGE_ARROW
    # You may need other locators for the next steps (e.g., Department, QA)
    # DEPARTMENT_FILTER = DEPARTMENT_FILTER 
    # QA_DEPARTMENT_OPTION = QA_DEPARTMENT_OPTION


    def __init__(self, driver):
        super().__init__(driver)
        self.URL = "https://useinsider.com/"

    def open(self):
        """Step 1: Visit the Home URL."""
        self.driver.get(self.URL)

    def accept_cookies_if_present(self):
        """Handles the cookie pop-up if it appears."""
        try:
            # Short wait needed here since _click has its own implicit wait
            self.sleep(0.5) 
            self._click(self.ACCEPT_COOKIES_BUTTON)
        except Exception:
            # If the cookie button is not present after a wait, ignore.
            pass