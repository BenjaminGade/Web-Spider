from bs4 import BeautifulSoup
from urllib.request import urlopen
import argparse, threading, time
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
links.append(url)
print('''********************
This Program Is Buggy.
To Make Sure That It\'s Completely Finished Crawling Then Give It A Moment After It Said It\'s Finished.
Also, The Find Tag Feature Might Not Work In Some Cases.
********************''')
time.sleep(5)
try:
    def spider( url, part):
        global links
        global results
        global find
        try:
            url = urlopen(url)
            soup = BeautifulSoup(url, 'html.parser')
            for result in soup.find_all(find):
                if result not in results:
                    results.append(result)
            for link in soup.find_all('a'):
                try:
                    if link.get('href') not in links:
                        if link.get('href').startswith('/') and link.get('href').startswith('/') not in links:
                            links.append(str(args.url + link.get('href')))
                            part = str(link.get('href'))
                        elif link.get('href').startswith('http') and link.get('href').startswith('http') not in links:
                            print(link.get('href'))
                            links.append(str(link.get('href')))
                            url = link.get('href')
                            part = ""
                        threading.Thread(target=spider, args=(url, part)).start()
                except:
                    continue
        except:
            pass
    print(url)
    spider( url, part)
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
            file.close()
    print(output)
    print("Ctrl + C To Exit")
    exit()
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
            file.close()
    print(output)
    print("Ctrl + C To Exit")
    exit()
