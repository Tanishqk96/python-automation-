# Web Scraping with Selenium and Pandas

This project demonstrates how to scrape data from a webpage using `Selenium` and `Pandas` in Python. Specifically, it extracts football headlines, including titles, subtitles, and links, from the website [The Sun - Football](https://www.thesun.co.uk/sport/football/).

## Prerequisites

Before running the script, ensure that you have the following installed:

A. **Python 3.x**  
   You can download it from [python.org](https://www.python.org/downloads/).

B. **Selenium**  
   Install Selenium using pip:
   ```bash
   pip install selenium

Finding and Replacing XPath
XPath is used to locate elements on a webpage. Here’s how to find the XPath of elements for your scraping needs:

Steps to Find XPath in Chrome (similar for other browsers):

1. Open the webpage in Chrome (or your preferred browser).

2. Right-click on the element you want to scrape (e.g., a title).

3. Click Inspect to open Developer Tools.

4. Right-click the highlighted HTML in the Elements tab.

5. Select Copy > Copy XPath.

For example, the XPath to extract a title could look like:

//div[@class="teaser__copy-container"]/a/h3

6. In your Python script, replace the XPath strings when the page structure changes or for different data extraction:

7. Locate the XPath in the script:

title = container.find_element(by="xpath", value='./a/h3').text

8. Replace './a/h3' with your newly copied XPath from the browser’s Developer Tools.

** Repeat this process for other elements like subtitles or links.

9. Changing the File Path Location
--> By default, the script saves the scraped data as a CSV file on your desktop:

** output_file = '/Users/tk/Desktop/headlines2.csv'

To save the file in a different folder, simply update the path string:

10. output_file = '/path/to/your/folder/headlines.csv'
Ensure that the specified path exists and that you have write permissions for that location.

Running the Script:
````
Clone the repository to your local machine (if you haven’t already):
````bash
git clone https://github.com/yourusername/your-repo-name.git
````
Navigate to the project directory:

````bash
cd your-repo-name
````

Run the script:
````bash
python scrape_headlines.py
````
The script will open Safari (or the browser of your choice), scrape the football headlines, and save the data as a CSV file.

