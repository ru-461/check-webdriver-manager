from time import sleep

from rich.console import Console
from rich.progress import track
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

console = Console()


def main():
    # Default
    driver = None

    console.log("Launch Google Chrome.")

    try:
        # Initialize
        driver = init_webdriver()

        # Access to Google.
        driver.get("https://www.google.com")

        # Wait
        for _ in track(range(5), description="Waiting..."):
            sleep(1)
            pass

    except Exception as e:
        console.log(f"An error occurred: {str(e)}")
    finally:
        if driver:
            # Quit
            driver.quit()
            console.log("Quit Google Chrome.")


def init_webdriver() -> webdriver.Chrome:
    """Initialize ChromeWebDriver

    Returns:
        webdriver.Chrome: ChromeWebDriver
    """
    options = Options()
    service = Service(ChromeDriverManager().install())

    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Create
    driver = webdriver.Chrome(options=options, service=service)

    # Maximize
    driver.maximize_window()

    return driver


if __name__ == "__main__":
    main()
