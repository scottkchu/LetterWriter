from bs4 import BeautifulSoup
# from urllib.request import urlopen
import requests

html_doc = "https://www.linkedin.com/jobs/search/?keywords=software%20engineer"

page = requests.get(html_doc)
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)
position = soup.find_all("a", {"class": "result-card__full-card-link"})
for i in positions:
    print(i.text)
companies = soup.find_all(
    "a", {"class": "result-card__subtitle-link job-result-card__subtitle-link"})
# for i in companies:
#     print(i.text)
# second = soup.find({'class': "jobs-search-results__list artdeco-list"})
# # print(soup.find(class_="jobs-search-results__list artdeco-list"))
# print(first)
# print(second)
# items = []

# for i in range(5):

# test = soup.find_all(
# "div", {'class': "jobs-details-top-card__content-container"})
# print(test)
# test1 = soup.find_all("data-job-id")
# print(test1)
# for i in test1:
#     print(i)

# cnp = soup.find_all(class_="display-flex")

# print(cnp)

# items = companynamepos.find_all(class_="display-flex")
# print(items)


# info = clean_page.find_all(class_="jobs-details-top-card__content-container")
# print(tryfind)


# info = soup.find_all(class_="jobs-details-top-card__content-container")

# print(info)
# print(soup.find_all(class_="jobs-details-top-card__job-title t-20 t-black t-normal"))
