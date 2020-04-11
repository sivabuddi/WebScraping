import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama

# init the colorama module
colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET


# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()


# Since not all links in anchor tags (a tags) are valid (I've experimented with this),
# some are links to parts of the website, some are javascript, so let's write a function to validate URLs:

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


# Now let's build a function to return all the valid URLs of a web page:

def get_all_website_links(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    # all URLs of `url`
    urls = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")


# First, I initialized the urls set variable, I've used Python sets here because we don't want redundant links.
#
# Second, I've extracted the domain name from the URL, we gonna need it to check whether the link we grabbed is external or internal.
#
# Third, I've downloaded the HTML content of the web page and wrapped it with a soup object to ease HTML parsing.

# Let's get all HTML a tags (anchor tags that contains all the links of the web page):

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue

    # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)


# Now we need to remove HTTP GET parameters from the URLs, since this will cause redundancy in the set, the below code handles that:

        parsed_href = urlparse(href)
    # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

        if not is_valid(href):
            continue

        if href in internal_urls:
        # already in the set
            continue
        # if domain_name not in href:
        # # external link
        #     if href not in external_urls:
        #         print(f"{GRAY}[!] External link: {href}{RESET}")
        #         external_urls.add(href)
        #         continue

        print(f"{GREEN}[*] Internal link: {href}{RESET}")
        with open("medicinenet.txt", "a") as f:
            f.write(href+"\n")
        urls.add(href)
        #print(urls)
        internal_urls.add(href)

    return urls


# Finally, after all checks, the URL will be an internal link, we print it and add it to our urls and internal_urls sets.

# number of urls visited so far will be stored here
total_urls_visited = 0

def crawl(url, max_urls=40):
    """
    Crawls a web page and extracts all links.
    You'll find all links in `external_urls` and `internal_urls` global set variables.
    params:
        max_urls (int): number of max urls to crawl, default is 30.
    """
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    #print(links)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)

if __name__ == "__main__":
    listvar = ["https://www.cancer.gov/", "https://www.cdc.gov/cancer/","https://www.cancer.org/cancer/all-cancer-types.html", "https://www.cancer.net/navigating-cancer-care/cancer-basics/what-cancer","https://www.cancercenter.com/cancer-types","https://medlineplus.gov/cancer.html","https://www.medicalnewstoday.com/articles/323648.php","https://www.who.int/health-topics/cancer#tab=tab_1","https://www.who.int/news-room/fact-sheets/detail/cancer","https://www.cancerresearchuk.org/about-cancer/what-is-cancer","https://www.medicinenet.com/cancer/article.htm"]

    for index, value in enumerate(listvar):
        print(index, value)

        crawl(value)
    #print("[+] Total External links:", len(external_urls))
        print("[+] Total Internal links:", len(internal_urls))
    #print("[+] Total:", len(external_urls) + len(internal_urls))

