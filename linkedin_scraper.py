from bs4 import BeautifulSoup
# from urllib.request import urlopen
import requests


def main1():
    html_doc = "https://www.linkedin.com/jobs/search/?keywords=software%20engineer"
    page = requests.get(html_doc)
    soup = BeautifulSoup(page.content, "html.parser")
    # print(soup)
    info = []
    positions = soup.find_all("a", {"class": "result-card__full-card-link"})
    # for i in position:
    #     print(i.text)
    companies = soup.find_all(
        "a", {"class": "result-card__subtitle-link job-result-card__subtitle-link"})

    company_list = []
    for i in companies:
        company_list.append(i.text)

    position_list = []
    for i in positions:
        position_list.append(i.text)

    for x in range(len(companies)):
        info.append([company_list[x], position_list[x]])

    return(info)


if __name__ == "__main__":
    main1()
# for inc in range(len(companies)):
#     combined = [companies[inc], positions[inc]]
#     info.append(combined)

# print(info)
