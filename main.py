from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import re

# Specify the URL
url = "https://www.x-kom.pl/g-2/c/1522-notebooki-laptopy-15-6.html?f%5Bprice%5D%5Bfrom%5D=5000&f%5Bprice%5D%5Bto%5D=7000&f4389-przeznaczenie-produktu=66562-do-gier"

# Configure Edge WebDriver
driver = webdriver.Edge()  # Make sure the msedgedriver is in your PATH

# Open the URL
driver.get(url)

try:
    # Find h3 elements with title
    h3_elements = driver.find_elements(By.XPATH, "//h3[@title]")

    # Find span elements with data-name "productPrice"
    span_elements = driver.find_elements(By.XPATH, "//span[@data-name='productPrice']")

    # Create a list to store data
    data = []

    # Iterate through the elements and extract data
    for h3, span in zip(h3_elements, span_elements):
        title = h3.get_attribute("title")
        price_text = span.text
        price_digits = re.sub(r'\D', '', price_text)  # Keep only digits
        formatted_price = f"{price_digits[:-2]},{price_digits[-2:]} PLN"  # Format price
        data.append((title, formatted_price))

    # Save data to a CSV file
    with open("scraped_data.csv", "w", newline="", encoding="utf-8-sig") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Title", "Price"])  # Write header
        csv_writer.writerows(data)

finally:
    # Close the WebDriver
    driver.quit()
