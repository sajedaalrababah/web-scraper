import requests
from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/History_of_Mexico"


def get_citations_needed_count(url):
    """
    Count the number of citations needed in the given Wikipedia URL.

    Args:
        url (str): The URL of the Wikipedia page.

    Returns:
        int: The count of citations needed.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    citations = soup.find_all("sup", class_="noprint")
    return len(citations)


def get_citations_needed_report(url):
    """
    Generate a report of the citations needed in the given Wikipedia URL.

    Args:
        url (str): The URL of the Wikipedia page.

    Returns:
        str: The report containing the relevant passages with citations needed.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    citations_needed = []

    for paragraph in paragraphs:
        if paragraph.find("sup", class_="noprint"):
            citation_text = paragraph.text.strip()
            citations_needed.append(citation_text)

    report = "\n\n".join(citations_needed)
    report = f"Citations needed:\n{report}"
    return report


print("Number of citations needed:", get_citations_needed_count(URL))
print("")
print(get_citations_needed_report(URL))