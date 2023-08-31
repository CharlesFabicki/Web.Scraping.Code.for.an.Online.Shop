# Web Scraping with Selenium

This Python script utilizes Selenium to scrape data from a webpage and save it to a CSV file. The script is designed to extract information about laptops within a specific price range and intended for gaming, from the x-kom.pl website.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your system.
- Microsoft Edge WebDriver (`msedgedriver`) installed and added to your system's PATH.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/CharlesFabicki/Web.Scraping.Code.for.an.Online.Shop.git
```
Install the required Python packages:
```bash
pip install selenium
```
## Usage

Open web_scraping_script.py and locate the url variable to set the target URL.

Run the script:
python web_scraping_script.py

The script will open Microsoft Edge, navigate to the URL, extract data, and save it as scraped_data.csv.
Output
Extracted data includes:

Title: Laptop name.
Price: Laptop price in PLN.
Data is saved in a CSV format for analysis.

## Customization
Modify the url variable to scrape from a different webpage.
Adjust the data extraction logic as needed.
Contributing
Contributions are welcome! For issues or enhancements, open an issue or pull request.

## Acknowledgements
Thanks to the Selenium team for the powerful web automation library.

## License
License. See LICENSE.





