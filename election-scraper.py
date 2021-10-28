import requests
from bs4 import BeautifulSoup as BS
import csv
import sys
import os
import traceback


def verification_of_arguments(arguments):
    soup = make_soup(URL_REGION)
    if len(sys.argv) < 3:
        print(f"File: {sys.argv[0]} has a lack of arguments.")
        quit()
    elif len(sys.argv) > 3:
        print(f"File: {sys.argv[0]} has too many arguments.")
        quit()
    elif not requests.get(sys.argv[1]).status_code == 200:
        print(f" {sys.argv[1]} address is not valid.")
        quit()
    elif "Page not found!" in soup.getText():
        print(f"Page {sys.argv[1]} not found.")
        quit()
    elif not "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=" in sys.argv[1]:
        print(f" {sys.argv[1]} address is not correct")
        quit()
    elif not sys.argv[2].endswith(".csv"):
        print(f"File: {sys.argv[2]} is not csv file.!")
        quit()
    else:
        return f"Downloading data from URL:{sys.argv[1]}"


def make_soup(URL):
    r = requests.get(URL)
    soup = BS(r.text, "html.parser")
    return soup


def town_selection(soup):
    results = []
    table_tag = soup.find_all("table", {"class": "table"})
    for table in table_tag:
        all_tr = table.find_all("tr")
        for tr in all_tr[2:]:
            td_row = tr.find_all("td")
            if not td_row[0].getText() == "-":
                data = select_attributes(td_row)
                results.append(data)

    return results


def url_town(URL, dic):
    URL = os.path.split(URL)
    spilt_url = URL[1].split("=")
    code_of_location = dic.setdefault("Code")
    URL_TOWN = URL[0] + f"/ps311?xjazyk=CZ&xkraj={spilt_url[2].strip('&xnumnuts')}&xobec={code_of_location}&xvyber={spilt_url[-1]}"
    return URL_TOWN


def info_town(URL, results):
    res2 = []
    res3 = []
    for dic in results:
        URL_TOWN = url_town(URL, dic)
        soup = make_soup(URL_TOWN)
        results_of_parties = nominating_parties(soup)
        results_of_town = town_election(soup)
        res2.append(results_of_town)
        res3.append(results_of_parties)

    return res2, res3


def town_election(soup):
    parties = []
    table_tag = soup.find("table", {"class": "table"})
    all_tr = table_tag.find_all("tr")
    for tr in all_tr[2:]:
        td_row = tr.find_all("td")
        results = select_attributes(td_row)
        parties.append(results)

    return results


def nominating_parties(soup):
    parties = []
    table_tag = soup.find_all('table')
    for table in table_tag:
        all_tr = table.find_all("tr")
        for tr in all_tr[2:]:
            td_row = tr.find_all("td")
            if not td_row[0].getText() == "-":
                results = select_attributes(td_row)
                parties.append(results)

    return parties


def select_attributes(td_row):
    if len(td_row) == 3:
        if not td_row[0].getText() == "-":
            return {
                "Code": td_row[0].getText(),
                "Location": td_row[1].getText(),
            }
    elif len(td_row) == 5:
        return {
            td_row[1].getText(): td_row[2].getText()
            }
    else:
        return {
            "Registred voters": td_row[3].getText(),
            "Envelopes": td_row[4].getText(),
            "Valid cotes": td_row[7].getText()
        }


def make_dic(res1, res2, res3):
    dic = []
    while res1:
        for i in list(range(len(res1))):
            p1 = res1.pop(0)
            p2 = res2.pop(0)
            p3 = res3.pop(0)
            dic.append(p1)
            dic[i].update(p2)
            for party in p3:
                dic[i].update(party)

    return dic


def make_csv_file(file_name, results):
    try:
        csv_file = open(file_name, mode="w", encoding="utf-8")
        columns = results[0].keys()
    except FileNotFoundError:
        return traceback.format_exc()
    except IndexError:
        return traceback.format_exc()
    else:
        writer = csv.DictWriter(csv_file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(results)
        print(f"Saving results to file: {file_name}")
    finally:
        csv_file.close()
        return f"Finishing {sys.argv[0]}"

URL_REGION = sys.argv[1]
file_name = sys.argv[2]
print(verification_of_arguments(sys.argv))
soup = make_soup(URL_REGION)
list_of_towns = town_selection(soup)
results_of_town, results_of_parties = info_town(URL_REGION, list_of_towns)
all_results = make_dic(list_of_towns, results_of_town, results_of_parties)
print(make_csv_file(file_name, all_results))