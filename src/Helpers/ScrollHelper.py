from PIL import Image
from cStringIO import StringIO


def get_scroll_height(web_driver):
    """

    :param web_driver:
    :return:
    """
    js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,' \
         '  document.documentElement.clientHeight,  document.documentElement.scrollHeight,' \
         '  document.documentElement.offsetHeight);'
    scroll_height = web_driver.execute_script(js)
    return scroll_height


def scroll_and_take_screenshots(web_driver, scroll_height):
    """

    :param web_driver:
    :param scroll_height:
    :return:
    """
    slices = []
    offset = 0
    verbose = 1

    while offset < scroll_height:
        if verbose > 0:
            print offset

        web_driver.execute_script("window.scrollTo(0, %s);" % offset)
        img = Image.open(StringIO(web_driver.get_screenshot_as_png()))
        offset += img.size[1]
        slices.append(img)

        if verbose > 0:
            # chrome_driver.get_screenshot_as_file('%s/screen_%s.png' % ('/tmp', offset))
            print scroll_height

    screenshot = Image.new('RGB', (slices[0].size[0], scroll_height))
    offset = 0
    for img in slices:
        screenshot.paste(img, (0, offset))
        offset += img.size[1]

    return screenshot
