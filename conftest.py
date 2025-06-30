import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose interface language: en, ru, fr, etc.")

@pytest.fixture()
def get_browser_name(request):
    return request.config.getoption("--browser_name")

@pytest.fixture()
def language(request):
    """Фикстура, возвращающая язык интерфейса (по умолчанию 'en')."""
    return request.config.getoption("--language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        ## options = webdriver.ChromeOptions()
        ## options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless=new")
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=chrome_options)
        ## browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
    
