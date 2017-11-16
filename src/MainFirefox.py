from selenium import webdriver, common
import sys
from src.Helpers.ArgumentsHelper import *
from src.Helpers.ScrollHelper import *


def main():
    total_arguments = len(sys.argv)
    if total_arguments != 3:
        raise ValueError("Warning: You must give two arguments.\n1) Url \n2) Path/to/save/image")
    url = get_url_from_command_line()
    path = get_screenshot_save_path_from_command_line()

    exists = check_directory_exists(path)
    if not exists:
        raise Exception("The directory specified doesn't exist.\nPath: " + path)
    firefox_driver = webdriver.Firefox()
    firefox_driver.set_page_load_timeout(2)

    try:
        firefox_driver.get(url)
    except common.exceptions.TimeoutException:
        print "Failed to load in time"

    scroll_height = get_scroll_height(firefox_driver)

    screenshot = scroll_and_take_screenshots(firefox_driver, scroll_height)

    screenshot.save(path)

    # in firefox i should only use quit
    # if i use close and the quit it will fail
    firefox_driver.quit()


if __name__ == "__main__":
    main()
