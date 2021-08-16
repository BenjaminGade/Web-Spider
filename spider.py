from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests, argparse
parse = argparse.ArgumentParser()
parse.add_argument('-u', '--url', required=True)
parse.add_argument('-f', '--find', default='', required=False)
parse.add_argument('-o', '--output', required=False)
args = parse.parse_args()
nothing = ""
part = ""
output = ""
url = args.url
find = args.find
links = []
results = []
try:
    print('-'*10,'\nHTTP GET Response Codes:')
    def spider(find, url, part):
        url = args.url + part
        r = requests.get(url)
        print(f"{url}: {r}")
        try:
            url = urlopen(url)
        except:
            nothing = ""
        soup = BeautifulSoup(url, 'html.parser')
        for link in soup.find_all('a'):
            if link.get('herf') not in links:
                if link.get('href').startswith('/') and link.get('href').startswith('/') not in links:
                    links.append(str(args.url + link.get('href')))
                    part = str(link.get('href'))
                elif link.get('href').startswith('http') and link.get('href').startswith('http') not in links:
                    links.append(str(link.get('href')))
                    url = link.get('href')
                    part = ""
                for result in soup.find_all(find):
                    if result not in results:
                        results.append(result)
                spider(find, url, part)
    spider(find, url, part)
    output += f"{'-'*10}\nLinks:\n"
    for link in links:
        output += f"{link}\n"
    if results == []:
        output += f"{'-'*10}\nNumber Of Links: {str(len(links))}"
    else:
        output += f"{'-'*10}\nResults:\n"
        for i in results:
            output += f"{i}\n"
        output += f"{'-'*10}\nNumber Of Links: {len(links)}\nNumber Of Results: {len(results)}"
    if args.output:
        with open(args.output, 'a') as file:
            file.write(output)
    print(output)
except KeyboardInterrupt:
    output += f"{'-'*10}\nLinks:\n"
    for link in links:
        output += f"{link}\n"
    if results == []:
        output += f"{'-'*10}\nNumber Of Links: {str(len(links))}"
    else:
        output += f"{'-'*10}\nResults:\n"
        for i in results:
            output += f"{i}\n"
        output += f"{'-'*10}\nNumber Of Links: {len(links)}\nNumber Of Results: {len(results)}"
    if args.output:
        with open(args.output, 'a') as file:
            file.write(output)
    print(output)