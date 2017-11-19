# <center>Snapshooter</center>
### Takes screenshots from websites based on url!

> The first argument is the url that we want to take screenshot
>> e.g. http://facebook.com

> The second argument is where we want to save the image. This argument should also contain the name of the file
>> e.g. /path/to/save/image/filename.jpg


## Requirements:

1)For google chrome

    i) Download google chrome (version 60 or higher).
       Version used on this project (62.0.3202.94)
       To install: dpkg -i <name/of/deb/file>

[Download latest version of google chrome](https://www.google.com/chrome/browser/desktop/index.html)

    ii) Download chrome driver
        Version used on this project (2.33.506092)
        Copy chrome driver to /usr/bin

[Download latest version of chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

2)For firefox

    i) Download mozilla firefox (version 55 or higher).
       Version used on this project (57.0)
       To install: dpkg -i <name/of/deb/file>

[Download latest version of mozilla firefox](https://www.mozilla.org/en-US/firefox/new/)

    ii) Download gecko driver
        Version used on this project (0.19.1)
        Copy gecko driver to /usr/bin

[Download latest version of gecko driver](https://github.com/mozilla/geckodriver/releases)



# TODO

* Add security check that the website is a valid website
* Create custom Exceptions
* Create helper for chrome that is responsible to setup chrome correctly

# DONE

* The user should be able to define where he wants to save the screenshot
* Add  check that the directory exists

