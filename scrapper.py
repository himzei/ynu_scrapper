import requests
from bs4 import BeautifulSoup

keyword = "간호사"
response = requests.get(
    f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno=0")

soup = BeautifulSoup(response.text, "html.parser")
lis = soup.find_all("li", class_="c_col")

jobs = []

for li in lis: 
    company = li.find("a", class_="cpname").text
    title = li.find("div", class_="cell_mid").find("a").text
    location = li.find("div", class_="cell_mid").find_all("span")[3].text
    link = li.find("div", class_="cell_mid").find("a").get("href")
    
    job_data = {
        "title": title, 
        "company": company, 
        "location": location, 
        "link": link
    }

    jobs.append(job_data)

print(jobs)
