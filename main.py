import requests
from bs4 import BeautifulSoup
from time import sleep
from fake_useragent import UserAgent
from headers import headers
from undetected import undetected
from xml_writter import create_xml
from json_writer import update_json

ua = UserAgent(browsers=['edge', 'chrome'])
# headers = {'user-agent': ua.random}


def get_urls_carts():
    for i in range(1, 16):
        sleep(5)
        url = f'https://www.farfetch.com/ca/shopping/women/dresses-1/items.aspx?page={i}&view=8&sort=3'
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("li", {"data-testid": "productCard"})

        for url in data:
            src = "https://www.farfetch.com/" + url.find("a").get("href")
            with open(f"urls.txt", "a", encoding='utf-8') as file:
                file.write(src + "\n")


def selen_parse():
    with open(f"urls2.html", "r", encoding='utf-8') as file:
        urls = file.read()
        for index, link in enumerate(urls.split()):
            sleep(5)
            soup = BeautifulSoup(undetected(link), "lxml")

            color, material = [i.text for i in soup.find("ul", class_="_fdc1e5").find_all("li")][:2]

            item_group_id = soup.find(
                "div", class_="ltr-15eja7h exjav152"
                      ).find_all("div", class_="ltr-92qs1a")[-1].find_all("span", {"dir": "ltr"})[0].text.strip()

            id = f"{item_group_id}_{'_'.join(color.split())}_{'_'.join(material.split())}"

            mpn = soup.find(
                "div", class_="ltr-15eja7h exjav152"
                      ).find_all("div", class_="ltr-92qs1a")[-1].find_all("span", {"dir": "ltr"})[-1].text.strip()

            title = soup.find(class_="ltr-13ze6d5-Body efhm1m90").text

            description = "None"

            image_link = soup.find("div", class_="ltr-bjn8wh ed0fyxo0").find("img").get("src")

            additional_image_link = "None"

            g = link.split("/")[6]
            gender_dict = {"women": "female", "men": "male", "kids": "plural"}
            gender = gender_dict.get(g)

            age_group = "None"
            brand = soup.find("h1", class_="ltr-i980jo el610qn0").find("a").text
            size = 'None'
            availability = soup.find("meta", {"property": "og:availability"}).get("content")
            price = soup.find("p", class_="ltr-194u1uv-Heading").text
            condition = "None"
            product_type = '>'.join([i.text for i in soup.find_all(class_="ltr-1h8w6zn-Footnote")])
            google_product_category = 2271

            new_data = [
                id,
                item_group_id,
                mpn,
                title,
                description,
                image_link,
                additional_image_link,
                link,
                gender,
                age_group,
                brand,
                color,
                size,
                availability,
                price,
                condition,
                product_type,
                google_product_category
            ]
            update_json("F:\\project PyCharm\\Jooble_test\\data.json", new_data)


if __name__ == "__main__":
    get_urls_carts()
    selen_parse()
    create_xml()
