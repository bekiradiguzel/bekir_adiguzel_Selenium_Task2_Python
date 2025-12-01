import os
import sys
# ensure project root is on sys.path so "from pages..." imports work reliably
ROOT = os.path.abspath(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(scope="session")
def driver():
    options = Options()
    # Start maximized — safe default for local debugging
    options.add_argument("--start-maximized")
    # disable Chrome browser notifications so they don't interfere with tests
    # Use both argument and prefs to be robust across Chrome versions
    options.add_argument("--disable-notifications")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    # options.add_argument("--headless=new")  # uncomment to run headless
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()