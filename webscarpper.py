#webscarpper 
#
#Shell
#1.)python -m pip install requests
#2.)python -m pip install beautifulsoup4
#
import requests
#2
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#2
soup = BeautifulSoup(page.content,"html.parser")

results= soup.find(id="ResultsContainer")

print(results.prettufy())

job_elements = results.find_all("div",class_="card-content")

for job_element in job_elements:
    #print(job_element,end="\n"*2)
    title_element =job_element.find("h2", class_="title")
    company_element = job_element.find("h3",class_="company")
    location_element = job_element.find("p",class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

python_jobs = results.find_all(
    "h2",string = lambda text: "python" in text.lower()
)
#Access Parent Elements
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

#Extract Attributes from HTML Elements
for job_element in python_job_elements:
    #-- snip --
    links = job_element.find_all("a")
    for link in links:
        #print(link.text.strip())
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
print(page.text)
