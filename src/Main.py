from selenium import webdriver, common
from selenium.webdriver.chrome.options import Options
from PIL import Image
from cStringIO import StringIO
import sys
from FileHelper import check_directory_exists
import time


def main():
    total_arguments = len(sys.argv)
    if total_arguments != 3:
        raise ValueError("Warning: You must give two arguments.\n1) Url \n2) Path/to/save/image")
    url = sys.argv[1]
    path = sys.argv[2]

    exists = check_directory_exists(path)
    if not exists:
        raise Exception("The directory specified doesn't exist.\nPath: " + path)

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    # comment next line if you want chrome to not be headless
    # chrome_options.add_argument("--headless")
    chrome_driver = webdriver.Chrome('chromedriver', 0, chrome_options)
    chrome_driver.implicitly_wait(5)
    # chrome_driver.set_page_load_timeout(5)

    try:
        chrome_driver.get(url)
    except common.exceptions.TimeoutException:
        print "Website didn't fully load"
        print "Trying to stop website from loading"
        try:
            chrome_driver.execute_script("return window.stop;")
        except common.exceptions.TimeoutException:
            print "Failed to stop website from loading.Taking small screenshot"
            chrome_driver.save_screenshot(path)
            chrome_driver.close()
            chrome_driver.quit()
            exit(1)
        time.sleep(2)
    scrollheight = get_scroll_height(chrome_driver)

    screenshot = scroll_and_take_screenshots(chrome_driver, scrollheight)

    screenshot.save(path)

    chrome_driver.close()
    chrome_driver.quit()

    x = 5


def get_scroll_height(chrome_driver):
    """

    :param chrome_driver:
    :return:
    """
    js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,' \
         '  document.documentElement.clientHeight,  document.documentElement.scrollHeight,' \
         '  document.documentElement.offsetHeight);'
    scroll_height = chrome_driver.execute_script(js)
    return scroll_height


def scroll_and_take_screenshots(chrome_driver, scroll_height):
    """

    :param chrome_driver:
    :param scroll_height:
    :return:
    """
    slices = []
    offset = 0
    verbose = 1

    while offset < scroll_height:
        if verbose > 0:
            print offset

        chrome_driver.execute_script("window.scrollTo(0, %s);" % offset)
        img = Image.open(StringIO(chrome_driver.get_screenshot_as_png()))
        offset += img.size[1]
        slices.append(img)

        if verbose > 0:
            chrome_driver.get_screenshot_as_file('%s/screen_%s.png' % ('/tmp', offset))
            print scroll_height

    screenshot = Image.new('RGB', (slices[0].size[0], scroll_height))
    offset = 0
    for img in slices:
        screenshot.paste(img, (0, offset))
        offset += img.size[1]

    return screenshot


if __name__ == "__main__":
    main()
