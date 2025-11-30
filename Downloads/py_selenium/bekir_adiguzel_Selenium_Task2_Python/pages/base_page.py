from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys # Needed for the new method
from typing import Tuple 
import time

class BasePage:

    HIGHLIGHTED_OPTION = (By.CSS_SELECTOR, ".select2-results__option--highlighted")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 
    
    # --- CORE UTILITY METHODS ---

    def _find_element(self, by_locator: Tuple[By, str]) -> WebElement:
        """Helper to wait for and find an element's visibility."""
        # Using visibility_of_element_located for better reliability
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def _click(self, by_locator: Tuple[By, str]):
        """Helper to wait for clickability and click the element."""
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def _type(self, by_locator: Tuple[By, str], text: str):
        """Helper to find, clear, and send keys to an input field."""
        element: WebElement = self._find_element(by_locator)
        self.sleep(0.2) 
        element.clear()
        element.send_keys(text)
    
    def _is_displayed(self, by_locator: Tuple[By, str], timeout: float = 10.0) -> bool:
        """Checks if an element is present in the DOM and visible on the page."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False

    def sleep(self, seconds: float = 1.0):
        """Convenience method for pauses (use sparingly)."""
        time.sleep(seconds)

    def get_current_url(self) -> str:
        """Retrieves the current URL from the browser."""
        return self.driver.current_url
    
    # --- GENERAL ACTION METHODS ---

    def _get_highlighted_option_text(self) -> str | None:
        """Internal helper to get the text of the currently highlighted list option."""
        try:
            # We use presence_of_element_located here because the element is *highlighted* # within a visible list, and we need a quick check.
            element = self.wait.until(EC.presence_of_element_located(self.HIGHLIGHTED_OPTION))
            return element.text.strip()
        except Exception:
            # If no element is highlighted (or the locator is wrong), return None
            return None

    def select_item_by_arrow_count(self, input_element_locator: Tuple[By, str], arrow_count: int) -> bool:
    
        try:
            # 1. Get the element that receives the key input
            input_element = self._find_element(input_element_locator) 
            
          # 2. Build the key sequence: ArrowDown * N times + Enter
            arrow_downs = [Keys.ARROW_DOWN] * arrow_count
            key_sequence = arrow_downs + [Keys.ENTER]

            # 3. Use ActionChains to ensure the keypress is properly focused on the element.
            print(f"INFO: Attempting to select item by pressing ARROW_DOWN {arrow_count} times.")
            # We send the keys to the element that was initially clicked, as it may be the 
            # host for the Shadow DOM or the element transferring focus.
            ActionChains(self.driver).send_keys_to_element(input_element, key_sequence).perform()
            
            self.sleep(1) # Wait for the selection to register and the list to close
            return True
        except Exception as e:
            print(f"ERROR: Failed to select listbox item via arrow keys. Exception: {e}")
            return False


    def scroll_target(self, by_locator: Tuple[By, str]):

            element = self._find_element(by_locator)
        # Using 'true' (or no argument) aligns the element to the top of the viewport.
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.sleep(0.5) 
         
        
    def hide_floating_container(self):
        """Hides the identified floating HubSpot container using JavaScript."""
        try:
            floating_container_xpath = "//*[@id='hs-web-interactives-floating-container']"
            js_script = f"document.evaluate(\"{floating_container_xpath}\", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.style.display = 'none';"
            self.driver.execute_script(js_script)
            print("INFO: Floating container hidden.")
            self.sleep(0.5)
        except Exception:
            pass

    def hover_and_click(self, hover_locator: Tuple[By, str], click_locator: Tuple[By, str], pause: float = 0.25):
        """Hover over hover_locator, then click click_locator (useful for dropdowns/menus)."""
        element = self._find_element(hover_locator)
        ActionChains(self.driver).move_to_element(element).perform()
        if pause and pause > 0:
            time.sleep(pause)
        self._click(click_locator)