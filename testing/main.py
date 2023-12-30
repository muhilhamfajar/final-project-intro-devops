import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestHomePage:
    @classmethod
    def setup_class(cls):
        # Initialize WebDriver with headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        # Close the browser after the test
        cls.driver.quit()

    def test_open_page(self):
        # Open homepage
        self.driver.get("http://frontend:8080/")

        # Wait for the results page to load
        time.sleep(2)

        # Get the title of the page
        page_title = self.driver.title

        expected_title = "Tweet App" 
        assert expected_title in page_title, f"Expected title '{expected_title}' not found in actual title '{page_title}'"

# Run the test if the script is executed directly
if __name__ == "__main__":
    pytest.main(["-v", "main.py"])
