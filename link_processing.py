import urllib.request
from urllib.parse import urljoin
import re


HREF_PATTERN = 'href[ ]{0,1}=[ ]{0,1}"([^\"]{0,})"'


def get_html_code(url: str) -> str:
    try:
        with urllib.request.urlopen(url) as response:
            encoding = response.headers.get_content_charset()
            html = response.read().decode(encoding)
        return html
    except:
       return ""


def find_links(html: str) -> list[str]:    
    return re.findall(HREF_PATTERN, html)


def is_wiki_link(url: str, baseurl) -> bool:
    return url.startswith(('/wiki', baseurl))


def to_full_link(url: str, baseurl: str):
    return urljoin(baseurl, url) if url.startswith("/wiki") else url


def get_wiki_links(url: str, baseurl: str) -> set[str]:
    html = get_html_code(url)
    links = find_links(html)
    full_wiki_links = set([
        to_full_link(link, baseurl)
        for link in links if is_wiki_link(link, baseurl)
    ])

    if url in full_wiki_links:
        full_wiki_links.remove(url)

    return full_wiki_links