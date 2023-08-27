import pytest
from time import sleep

from bla.settings import USERS, PASSWORDS

from selenium import webdriver as selenium_webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session') #работа драйвера
def driver(request):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    """как обойти антибота-противоскриптера """
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = selenium_webdriver.Chrome(service=service, options=options)
    yield driver

    sleep(2)
    driver.quit()

