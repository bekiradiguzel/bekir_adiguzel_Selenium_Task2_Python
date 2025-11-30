from pages.home_page import HomePage
from Locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys # REQUIRED FOR KEYBOARD NAVIGATION

def test_job_application_flow(driver):
    """
    E2E test: Opens Insider, navigates to Careers, filters by Location (Istanbul),
    and verifies the job listing.
    """

    home_page = HomePage(driver)
    wait = WebDriverWait(driver, 15)

    # 1) Open Home and accept cookies
    home_page.open()
    home_page.sleep(2) 
    home_page.accept_cookies_if_present()
    home_page.hide_floating_container() 

    # 2) Basic page title check
    assert "Insider" in home_page.driver.title, "Home page title does not contain 'Insider'."

    # 3) Navigate to Careers page
    home_page._click(home_page.COMPANY_BUTTON)
    home_page.hover_and_click(home_page.CAREERS_BUTTON, home_page.CAREERS_BUTTON)
    home_page.sleep(2)

    # Verification: Check title and a key element on the Careers page
    assert "Insider" in home_page.driver.title, "Careers page title does not contain 'Insider'."
    assert home_page._is_displayed(home_page.FIND_DREAM_JOB), "Find your dream job element is not displayed."
    
    # 4) Click on "Find your dream job" to scroll/jump to job list section
    home_page._click(home_page.FIND_DREAM_JOB) 
    
    # Verification: Check if URL contains 'careers' (usually true) and ensure job list is visible
    assert "careers" in home_page.get_current_url(), "Did not navigate correctly to the Careers section."
    home_page.hover_and_click(home_page.JOB_LIST, home_page.JOB_LIST)
    assert home_page._is_displayed(home_page.JOB_LIST), "Job list container is not visible after clicking Find job."
    home_page.sleep(2)

    # 5.1. Click the main filter dropdown to open the list
    home_page._click(home_page.FILTER_BY_LOCATION)
    home_page._click(home_page.FILTER_BY_LOCATION)
    home_page.sleep(10)
    #home_page._click(home_page.CLICK_DOWN) 
    
     

    
    # 5) Filter by Location: Istanbul, Turkiye (USING KEYBOARD NAVIGATION METHOD)
    # ----------------------------------------------------------------------
    arrow_press_count = 12 
    target_city = "Istanbul, Turkiye" 
 
    
    # 5.2. Select the item using the new count-based method
    # We send the key sequence to the main filter element, leveraging ActionChains for robust focus.
    selection_successful = home_page.select_item_by_arrow_count(
        home_page.FILTER_BY_LOCATION, 
        arrow_press_count
    )

    assert selection_successful, f"Failed to select the location '{target_city}' via keyboard navigation."
    
    print(f"INFO: Location '{target_city}' successfully selected.")
    home_page._click(home_page.OPEN_POSITIONS_HEADER)
    home_page.sleep(5) # Wait for job list results to update
    

    dept_arrow_count = 10
    target_department = "Quality Assurance" 
    # 6.1. Click the department filter dropdown to open the list
    # NOTE: FILTER_BY_DEPARTMENT locator must be defined in Locators.py
    home_page._click(home_page.CLICK_DOWN2) 
    home_page._click(home_page.FILTER_BY_DEPARTMENT) 
    home_page.sleep(5) 
    # 6.2. Highlight the item using the count-based method
    selection_successful_dept = home_page.select_item_by_arrow_count(
        home_page.FILTER_BY_DEPARTMENT, 
        dept_arrow_count
    )
    assert selection_successful_dept, f"Failed to highlight the department '{target_department}' via keyboard navigation after {dept_arrow_count} attempts."
    home_page.sleep(5)
    original_window = driver.current_window_handle

    
    home_page.scroll_target(home_page.JOB_LIST)

    assert home_page._is_displayed(home_page.ILGILI_POZISYON), "İş bulunamadı"
    
    
    home_page.hover_and_click(home_page.JOB_LIST, home_page.VIEW_ROLE_BUTTON)
    home_page.sleep(5)

        # --- MANDATORY WINDOW SWITCHING CODE ---
    # Wait for a new window or tab to be opened
    wait.until(EC.number_of_windows_to_be(2))
    
    # Loop through all window handles
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
            
    # Now that the driver is focused on the new tab, perform the URL check
    new_url = home_page.get_current_url()
    print(f"INFO: Switched to new window. New URL is: {new_url}")

    # Check if the URL has changed correctly
    assert "https://jobs.lever.co/" in new_url, "Did not navigate correctly to the Lever application page."

    print("INFO: Successfully navigated to the external job application page.")
    home_page.sleep(5) # Final pause for visibility

    
    
    

