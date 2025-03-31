from bs4 import BeautifulSoup
from urllib.request import urlopen
import argparse
import threading
import time

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=True)
parser.add_argument('-f', '--find', default='', required=False)
parser.add_argument('-o', '--output', required=False)
args = parser.parse_args()

# Global variables
links = [args.url]
results = []
lock = threading.Lock()
output = ""

print('''********************
This Program Is Buggy.
To Make Sure That It\'s Completely Finished Crawling Then Give It A Moment After It Said It\'s Finished.
Also, The Find Tag Feature Might Not Work In Some Cases.
********************''')
# Ignore unessesary wait time
# time.sleep(5)

def spider(url, part=""):
    global links, results, output
    
    try:
        with urlopen(url) as response:
            soup = BeautifulSoup(response, 'html.parser')
            
            # Find requested elements set in the --find argument and save them to the results array
            if args.find:
                with lock:
                    for result in soup.find_all(args.find):
                        if result not in results:
                            results.append(result)
            
            # Find all links in the current webpage and recursively crawl them
            for link in soup.find_all('a'):
                try:
                    href = link.get('href')
                    if not href:
                        continue
                        
                    with lock:
                        if href not in links:
                            if href.startswith('/'):
                                new_url = args.url.rstrip('/') + href
                                if new_url not in links:
                                    links.append(new_url)
                                    threading.Thread(target=spider, args=(new_url, href)).start()
                            elif href.startswith('http'):
                                links.append(href)
                                print(href)
                                threading.Thread(target=spider, args=(href, "")).start()
                except:
                    continue
    except:
        pass

def main():
    global output
    
    try:
        print(f"Starting crawl from: {args.url}")
        spider(args.url)
        
        # Wait for all threads to complete
        while threading.active_count() > 1:
            time.sleep(1)
        
        # Generate output and print to console
        output += f"{'-'*10}\nLinks:\n"
        output += "\n".join(links) + "\n"
        
        if results:
            output += f"{'-'*10}\nResults:\n"
            output += "\n".join(str(r) for r in results) + "\n"
        
        output += f"{'-'*10}\nNumber Of Links: {len(links)}"
        if results:
            output += f"\nNumber Of Results: {len(results)}"
        
        # Write to links and results to a specified output if the --output argument is set
        if args.output:
            with open(args.output, 'w') as file:
                file.write(output)
        
        print(output)
        print("Crawling completed. Press Ctrl+C to exit.")
        
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received. Saving current results...")
        
        output = f"{'-'*10}\nLinks (partial results):\n"
        output += "\n".join(links) + "\n"
        
        if results:
            output += f"{'-'*10}\nResults (partial):\n"
            output += "\n".join(str(r) for r in results) + "\n"
        
        output += f"{'-'*10}\nNumber Of Links: {len(links)}"
        if results:
            output += f"\nNumber Of Results: {len(results)}"
        
        if args.output:
            with open(args.output, 'w') as file:
                file.write(output)
        
        print(output)
        print("Partial results saved. Exiting.")

if __name__ == "__main__":
    main()
