import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

class TestHomePage:
    @classmethod
    def setup_class(cls):
        # Start virtual display
        cls.display = Display(visible=0, size=(800, 800))
        cls.display.start()

        # Install ChromeDriver
        chromedriver_autoinstaller.install()

        # Set up Chrome options
        cls.chrome_options = webdriver.ChromeOptions()
        cls.chrome_options.add_argument("--window-size=1200,1200")
        cls.chrome_options.add_argument("--ignore-certificate-errors")
        cls.chrome_options.add_argument("--headless")  # Add headless option

        # Initialize WebDriver
        cls.driver = webdriver.Chrome(options=cls.chrome_options)

    @classmethod
    def teardown_class(cls):
        # Close the browser and stop virtual display
        cls.driver.quit()
        cls.display.stop()

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
