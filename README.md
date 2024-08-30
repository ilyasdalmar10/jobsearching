                                                                                Job Searching Project  
Overview
This project is a job searching application designed to automate the process of searching for job listings from various websites.
The application utilizes Selenium for web scraping, allowing users to extract job postings, filter them based on certain criteria, and save the results for further review.

Features
Automated Job Search: Automatically search for job listings on certain websites.
Filtering Options: Filter job listings based on keywords, location, company, etc.
Data Extraction: Extract job details such as title, company, location, and job description.
Data Storage: Save the extracted job listings to a file for later review.
Browser Automation: Uses Selenium with ChromeDriver to handle browser interactions.


Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.x: This project requires Python 3.6 or later.
Selenium: Selenium WebDriver is used for browser automation.
ChromeDriver: ChromeDriver is required for interacting with the Chrome browser or Brave browser.
BeautifulSoup: Used for parsing HTML and extracting information.

Installation
Clone the repository:

bash

git clone https://github.com/ilyasdalmar10/jobsearching.git
cd jobsearching
Install dependencies: Use pip to install the necessary Python packages:

pip install -r requirements.txt

Download ChromeDriver:

Download ChromeDriver from https://developer.chrome.com/docs/chromedriver/downloads and place it in your project directory or add it to your system PATH. 
Make sure the chromedriver is compatible with your chrome or other search engines

Configure Paths:

Update the chrome_driver_path and options.binary_location in your script to reflect the correct paths on your system.
Usage
Run the Job Search Script: Execute the Python script to start the job searching process:

bash

python main.py

Specify Search Criteria: Modify the script to include your desired search criteria such as job title, location, or company.

View Extracted Data: The extracted job listings will be saved to a specified output file (e.g. .txt) for easy review.

Example
Here’s an example of how to run the script:

python:

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_driver_path = r"C:\path\to\chromedriver.exe"
brave_browser_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

service = Service(executable_path=chrome_driver_path)
options = Options()
options.binary_location = brave_browser_path

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.example-job-site.com")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Example data extraction
jobs = soup.find_all('div', class_='job-listing')
for job in jobs:
    title = job.find('h2').text
    company = job.find('div', class_='company').text
    location = job.find('div', class_='location').text
    print(f"Title: {title}, Company: {company}, Location: {location}")

driver.quit()


Troubleshooting
If you encounter issues with ChromeDriver not being found, ensure that:

The chrome_driver_path is correct.
ChromeDriver is compatible with your browser version.
ChromeDriver is in your system's PATH.
Refer to the Selenium documentation for more detailed troubleshooting tips.

Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.

License
This project is open-source and available under the MIT License.

Acknowledgements
Selenium
BeautifulSoup
ChromeDriver
