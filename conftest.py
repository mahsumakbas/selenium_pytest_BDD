from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    wd = webdriver.Chrome()
    wd.implicitly_wait(30)
    wd.set_page_load_timeout(30)
    wd.set_script_timeout(30)
    wd.maximize_window()
    wd.get("https://testpages.herokuapp.com/styled/index.html")
    yield wd
    wd.quit()