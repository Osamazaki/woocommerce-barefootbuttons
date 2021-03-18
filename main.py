from requests_html import HTMLSession
import csv
session = HTMLSession()
url = "https://barefootbuttons.com/product-category/version-1/"


def get_links(url):
    response = session.get(url)
    products = response.html.find("div.product-small.box")
    links = []
    for product in products:
        link = product.find("a", first=True).attrs["href"]
        links.append(link)
    return links


def product_info(links_list):
    for link in links_list:
        response = session.get(link).html
        info = {
            "title": response.find("h1.product-title.product_title.entry-title", first=True).text.replace("(Please Tighten Lightly)",""),
            "sku": response.find("span.sku_wrapper", first=True).text,
            "price": response.find("span.woocommerce-Price-amount.amount bdi")[1].full_text,
            "tag": response.find("a[rel=tag]", first=True).text
        }
        products.append(info)


products = []

links = get_links(url)
product_info(links)
with open("products.csv", "w", encoding="utf8", newline="") as file:
    wr = csv.DictWriter(file, fieldnames=products[0].keys())
    wr.writeheader()
    wr.writerows(products)

