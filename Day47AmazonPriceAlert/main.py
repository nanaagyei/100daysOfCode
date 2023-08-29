import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

AMAZON_URL = "https://www.amazon.com/dp/B0BCPCSTNB/ref=sspa_dk_detail_" \
             "2?psc=1&pd_rd_i=B0BCPCSTNB&pd_rd_w=QYzE1&content-id=amzn1.sym." \
             "386c274b-4bfe-4421-9052-a1a56db557ab&pf_rd_p=386c274b-4bfe-4421-9052-a1a56db557ab&pf_" \
             "rd_r=46Z5DJKGCZ2WJQVK4VFZ&pd_rd_wg=iFF1m&pd_rd_r=073b5435-0070-4b99-adcc-b9f943b7010f&s=" \
             "electronics&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&smid=A2IDDUZRWUPK5L&spLa=" \
             "ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQ0VPRUhCSlVDVzVFJmVuY3J5cHRlZElkPUEwMTgzMTUzMTc2MlpZQTRSV0tWOSZ" \
             "lbmNyeXB0ZWRBZElkPUEwMDczMjkzOTRYTDNDVlI4TDlVJndpZGdldE5hbWU9c3BfZGV0YWlsX3RoZW1hdGljJmFjdGlvbj" \
             "1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

amazon_webpage_response = requests.get(url=AMAZON_URL, headers=header)
amazon_webpage = amazon_webpage_response.text

soup = BeautifulSoup(amazon_webpage, "lxml")
item_price_html = soup.find(name="span", class_="a-offscreen")
item_price = item_price_html.getText()[1:]
item_price = float(item_price)
