import requests
from bs4 import BeautifulSoup
import csv

# URL of the e-commerce website to scrape
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

# Find product names and prices
names = soup.find_all("a", class_="title")
prices = soup.find_all("h4", class_="pull-right price")
ratings = soup.find_all("p", class_="pull-right")

# Initialize lists to store data
product_data = []

for name, price, rating in zip(names, prices, ratings):
    product_name = name.text.strip()
    product_price = price.text.strip()
    product_rating = rating.text.strip()
    product_data.append([product_name, product_price, product_rating])

# Specify the filename for the CSV file
csv_filename = "product_data.csv"

# Save data to CSV
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Product Name", "Product Price", "Product Rating"])

    for data in product_data:
        csv_writer.writerow(data)

print(f"Data successfully scraped and saved to {csv_filename}")