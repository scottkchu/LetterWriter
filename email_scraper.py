from bs4 import BeautifulSoup
import requests
from googlesearch import search
job_info = []

def info(job_info, company, title):
    for name in company:
        job_info.append([name.text.strip('\n')])
    counter = 0
    for position in title:
        job_info[counter].append(position.text.strip('\n'))
        counter += 1


def main():
#Job search website
    job_name = "programming"
    site = None
    for i in search(("indeed" + job_name + "job"),  tld="com", lang='en', num = 1 , start = 0, stop = 1, pause = 2):
        site = i
    print(site)

    r = requests.get(site)
    site_content = BeautifulSoup(r.content,'html.parser')
    title = site_content.find_all('a', {'class':'jobtitle turnstileLink'})
    company = site_content.find_all('span', {'class':'company'})

    info(job_info, company, title)
    print(job_info)
    return job_info
main()





