from bs4 import BeautifulSoup
# from urllib.request import urlopen
import requests


def get_html():
    html_doc = "https://www.linkedin.com/jobs/search/?keywords=software%20engineer"
    page = requests.get(html_doc)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_company_list(companies):
    temp_company_list = []
    for i in companies:
        temp_company_list.append(i.text)
    return temp_company_list


def get_position_list(positions):
    temp_position_list = []
    for i in positions:
        temp_position_list.append(i.text)
    return temp_position_list


def info_format(l_companies, l_positions):
    info = []
    for x in range(len(l_companies)):
        info.append([l_companies[x], l_positions[x]])
    return info


def linkedin():
    # info = []
    soup = get_html()
    positions = soup.find_all("a", {"class": "result-card__full-card-link"})
    companies = soup.find_all(
        "a", {"class": "result-card__subtitle-link job-result-card__subtitle-link"})

    company_list = get_company_list(companies)

    position_list = get_position_list(positions)

    finfo = info_format(company_list, position_list)

    return finfo


if __name__ == "__main__":
    linkedin()