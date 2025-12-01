from selenium.webdriver.common.by import By

# Shared test constants
FILTER_LOCATION = "Istanbul, Turkey"
FILTER_DEPARTMENT = "Quality Assurance"
EXPECTED_APP_URL_PART = "jobs.lever.co"

# Page locators (make these tuples so page objects can use them directly)
ACCEPT_COOKIES_BUTTON = (By.XPATH, "//*[contains(text(),'Accept All')]")
OPEN_POSITIONS_HEADER = (By.XPATH, "//label[@for='filter-by-department']")   
COMPANY_BUTTON = (By.XPATH, "//*[@id='navbarDropdownMenuLink' and contains(normalize-space(.), 'Company')]")
CAREERS_BUTTON = (By.XPATH, "//a[normalize-space()='Careers' and contains(@href,'/careers')]")
FIND_DREAM_JOB = (By.XPATH, "//a[contains(text(),'Find your dream job')]")
FILTER_BY_LOCATION = (By.XPATH, "//span[@data-select2-id='1']")
FILTER_BY_DEPARTMENT = (By.XPATH, "//span[@id='select2-filter-by-department-container']")

FILTER_BY_LOCATION2 = (By.XPATH, "(//span[@class='select2-selection__rendered'])[2]")
REMOVE_ITEM1 = (By.XPATH, "(//span[@title='Remove all items'])[1]")
LOCATION = (By.XPATH, "//*[@id='select2-filter-by-location-result-43ud-Istanbul, Turkiye']")
JOB_LIST = (By.XPATH, "//div[@id='jobs-list']")
CLICK_DOWN = (By.XPATH, "//b[@role='presentation']")
CLICK_DOWN2 = (By.XPATH, "(//b[@role='presentation'])[2]")
CLICK_ALL = (By.XPATH, "(//span[@title='All'])[1]")
DROPDOWN = (By.XPATH, "(//span[@dir='ltr'])[3]")
LOCATION_CONTAINER = (By.XPATH, "//ul[@class='select2-results__options']")
ILGILI_POZISYON = (By.XPATH, "//div[@data-location='istanbul-turkiye']")
VIEW_ROLE_BUTTON = (By.XPATH, "//a[contains(text(),'View Role')]")
NEXT_PAGE_ARROW = (By.XPATH, "//a[contains(text(),'View Role')]")



id="select2-filter-by-location-result-43ud-Istanbul, Turkiye"
LOCATION_IST = (By.ID, 'select2-filter-by-location-result-blq1-Istanbul, Turkiye')

# XPaths used by the search helper (can be string or tuple; we keep string here)
NEXT_PAGE_ARROW = "//i[@class='icon-arrow-right']"
