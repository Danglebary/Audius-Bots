# IMPORT SELENIUM DEPENDENCIES
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# CONFIGURE HEADLESS BROWSER OPTIONS
opt_headless = Options()
opt_headless.add_argument('--headless')

# CREATE HEADLESS BROWSER INSTANCE FOR BOTS
def init_browser_headless():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=opt_headless)
    return browser

# CREATE HEADFUL BROWSER INSTANCE FOR BOTS
def init_browser_headful():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    return browser
