from OsHelper import run_command
from TextHelper import string_starts_with


def check_chrome_driver_exists():
    result = run_command(['chromedriver', '--version'])
    starts = string_starts_with(result.out, 'ChromeDriver')
    return starts


def check_gecko_driver_exists():
    result = run_command(['geckodriver', '--version'])
    starts = string_starts_with(result.out, 'geckodriver')
    return starts