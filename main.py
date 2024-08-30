from bs4 import BeautifulSoup
from jobswebsite import websites
import traceback
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


print("Hello and Welcome to the Job Alerter")
users_job = input("Type in the job you are searching for: ")
users_location = input("Type in the location you are interested in working: ")

print("Answer the next two questions with numbers")

number_of_web = int(input("Do you want to search at:\n1.) Indeed\n2.) TotalJobs\n3.) Both\n"))
write_to = int(input("Do you want to save this information into a text file:\n1.) Yes\n2.) No\n"))


users_job = users_job.replace(" ", "")
users_location = users_location.replace(" ", "")


indeed = websites(
    f"https://uk.indeed.com/jobs?q={users_job}&l={users_location}",
    "css-9446fg",
    "jobTitle",
    "salary-snippet-container",
    "company_location"
)

total_jobs = websites(
    f"https://www.totaljobs.com/jobs/{users_job}/in-{users_location}?radius=10",
    "res-1d1eotm",
    "res-nehv70",
    "res-1fad2gj",
    "res-btchsq"
)

job_data = []

# Function to get information
def get_info_(website):
    try:

                
        chrome_driver_path = r"C:path_to_chromedriver"
        brave_browser_path = r"C:path_to_brave" # For me I used this option becuase I like brave
        service = Service(executable_path=chrome_driver_path)
        options = Options()
        options.binary_location = brave_browser_path
        driver = webdriver.Chrome(service=service, options=options)


        driver.get(website.url)
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        job_titles = [element.get_text().strip() for element in soup.find_all(class_=website.title_div)]
        salaries = soup.find_all(class_=website.salary_div)
        locations = soup.find_all(class_=website.location_div)
        contents = soup.find_all(class_=website.content_div)

        for i, title in enumerate(job_titles):
            salary = salaries[i].get_text().strip() if i < len(salaries) else "N/A"
            location = locations[i].get_text().strip() if i < len(locations) else f"In {users_location}"
            content = contents[i].get_text().strip() if i < len(contents) else "Learn more by visiting our website"
            
            job_data.append((title, salary, location, content))

        for title, salary, location, content in job_data:
            underline = "-" * len(title)
            title_display = f"Job Title: -> {title}"
            print(title_display.center(50))
            print(underline.center(50))
            print(f"Salary: {salary} | Location: {location} |\nInformation: {content}\n")
        
        driver.quit()
        return job_data

    except Exception as e:
        print(f"An Error Occurred: {e}")
        traceback.print_exc()

# Function to save data to file
def save_in_file(job_data):
    with open("jobsearches.txt", "w") as file:
        for title, salary, location, content in job_data:
            underline = "-" * len(title)
            title_display = f"Job Title: -> {title}\n"
            file.write(title_display.center(50) + "\n")
            file.write(underline.center(50) + "\n")
            file.write(f"Salary: {salary} | Location: {location} |\nInformation: {content}\n\n\n")


if number_of_web == 1:
    print("Results From Indeed: ")
    get_info_(indeed)
elif number_of_web == 2:
    print("Results From TotalJobs")
    get_info_(total_jobs)
elif number_of_web == 3:
    print("Results From Indeed and TotalJobs")
    get_info_(indeed)
    get_info_(total_jobs)
else:
    print("Error: Please select a valid option")

time.sleep(2)  


if write_to == 1:
    save_in_file(job_data)
elif write_to == 2:
    feedback = input("Thank You For Accessing The Job Alerter:\nCan you provide any feedback?\n")
    with open("Feedback.txt", "a") as feedback_file:
        feedback_file.write("\n" + feedback + "\n")
else:
    print("Error: Please select a valid option")
