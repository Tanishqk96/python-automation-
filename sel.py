import pandas as pd
from selenium import webdriver

driver = webdriver.Safari()
driver.get("https://www.thesun.co.uk/sport/football/")

print("Current URL:", driver.current_url)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')
print(f"Number of containers found: {len(containers)}")

titles = []
subtitles = []
links = []

for container in containers:
    try:
        title = container.find_element(by="xpath", value='./a/h3').text
        subtitle = container.find_element(by="xpath", value='./a/p').text
        link = container.find_element(by="xpath", value='./a').get_attribute("href")

        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)

        print(f"Title: {title}")
        print(f"Subtitle: {subtitle}")
        print(f"Link: {link}")
    except Exception as e:
        print(f"Error extracting data for a container: {e}")

driver.quit()

my_dict = {'Title': titles, 'Subtitle': subtitles, 'Link': links}

if len(titles) == 0:
    print("No data extracted. Please check the XPath or the website structure.")
else:
    output_file = '/Users/tk/Desktop/headlines2.csv'
    headlines_df = pd.DataFrame(my_dict)
    headlines_df.to_csv(output_file, index=False)
    print(f"Headlines successfully saved to {output_file}")
