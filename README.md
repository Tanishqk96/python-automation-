# Web Scraping with Selenium and Pandas

This project demonstrates how to scrape data from a webpage using `Selenium` and `Pandas` in Python. Specifically, it extracts football headlines, including titles, subtitles, and links, from the website [The Sun - Football](https://www.thesun.co.uk/sport/football/).

## Prerequisites

Before running the script, ensure that you have the following installed:

1. **Python 3.x**  
   You can download it from [python.org](https://www.python.org/downloads/).

2. **Selenium**  
   Install Selenium using pip:
   ```bash
   pip install selenium

3.Pandas Install Pandas using pip:
pip install pandas

4.Safari WebDriver (macOS only) For macOS, the Safari WebDriver is built-in, but you need to enable it. Run the following command in the terminal to enable Safari WebDriver:
safaridriver --enable

--->   How to Find and Replace XPath
XPath is used to locate elements on a webpage. Here's how to find the XPath of elements for your scraping needs:

Steps to Find XPath in Chrome (similar for other browsers):
Open the webpage in Chrome (or your preferred browser).

Right-click on the element you want to scrape (for example, a title).

Click on Inspect to open Developer Tools.

Right-click the highlighted HTML in the Elements tab.

Select Copy > Copy XPath.

5.Changing the File Path Location
output_file = '/Users/tk/Desktop/headlines2.csv'
To change the file location, simply update the path string. For example, to save the file in a different folder:
output_file = '/path/to/your/folder/headlines.csv'


Running the Script
Once everything is set up:

Clone this repository to your local machine (if you haven’t already):

bash
git clone https://github.com/yourusername/your-repo-name.git
Navigate to the project directory:
cd your-repo-name
Run the script:
python sel.py
The script will open Safari (or the browser of your choice), scrape the football headlines, and save the data as a CSV file.
