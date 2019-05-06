from bs4 import BeautifulSoup
import requests

from url_checker import url_checker

url_site = 'https://scrapethissite.com/pages'

url_site_disallowed_path = ['/ ', '/lessons', '/faq'] # That could be dynamically

validated_url = url_checker(url_site, url_site_disallowed_path)

if validated_url:

    # TODO: handle exceptions 
    site_response = requests.get(url_site, timeout=5).content

    site_content = BeautifulSoup(site_response, "html.parser")

    site_content_urls = site_content.find_all('a')

    # just show link in the console
    counter = 1
    for path in site_content_urls:
        path = path.attrs["href"] if "href" in path.attrs else ''

        print("{} ==> {}".format(counter, path))

        counter += 1
else:

    print("Sorry, the path you trying to access is disallowed")
