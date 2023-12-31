# Quizlet-set-scraper
Quizlet-set-scraper is a command line program designed to pull a quizlet set from a url in one file and export the quizlet set to another file.

This program currently supports URLs which point directly to a study set - folders, classes, and premium content are not supported.

# Usage
Copy the url of the set into url.txt, save the file then run:
```python main.py```

You can edit the file name it exports to, the url file name it pulls from, and the separation character between the question and answer near the top of the code.

# Dependencies
- Python 3.12+ (older versions may work, v3.12.0 was used), which can be downloaded [here.](https://www.python.org/downloads/) It's recommended to check "Add Python 3.x to PATH" during installation.
- Selenium, which can be installed by running: ```pip install selenium``` (v4.14.0 was used)
- BeautifulSoup4, which can be installed by running: ```pip install beautifulsoup4``` (v4.12.2 was used)
- Firefox (v199.0 was used), can be downloaded [here.](https://www.mozilla.org/en-US/firefox/new/)
- Geckodriver, which is distributed with Quizlet-set-scraper (v0.33.0 was used). In the case that an updated version is required, Geckodriver can be downloaded [here.](https://github.com/mozilla/geckodriver/releases) Please ensure geckodriver.exe is located in the same directory as main.py  

---

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
This project is licensed under the MIT License. See the [LICENSE.txt](LICENSE.txt) file for details.
main.py also contains a brief license notice.
