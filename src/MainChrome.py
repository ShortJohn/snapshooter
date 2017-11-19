import sys

from selenium import webdriver, common
from selenium.webdriver.chrome.options import Options

from src.Helpers.ArgumentsHelper import *
from src.Helpers.ScrollHelper import get_scroll_height, scroll_and_take_screenshots


def main():
    total_arguments = len(sys.argv)
    if total_arguments != 3:
        raise ValueError("Warning: You must give two arguments.\n1) Url \n2) Path/to/save/image")
    url = get_url_from_command_line()
    path = get_screenshot_save_path_from_command_line()

    exists = check_directory_exists(path)
    if not exists:
        raise Exception("The directory specified doesn't exist.\nPath: " + path)

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    # comment next line if you want chrome to not be headless
    # chrome_options.add_argument("--headless")
    chrome_driver = webdriver.Chrome('chromedriver', 0, chrome_options)
    chrome_driver.implicitly_wait(30)
    chrome_driver.set_page_load_timeout(30)
    chrome_driver.set_script_timeout(30)

    try:
        chrome_driver.get(url)
    except common.exceptions.TimeoutException:
        # todo find a way for chrome to not crash when tryint go take screenshots if timeout is exceeded
        print "Exiting. Failed to load " + url + ". Exiting"
        chrome_driver.quit()
        exit(1)

    scroll_height = get_scroll_height(chrome_driver)

    screenshot = scroll_and_take_screenshots(chrome_driver, scroll_height)

    screenshot.save(path)

    chrome_driver.quit()

    exit(0)


if __name__ == "__main__":
    main()
