from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from typing import TypedDict
from bs4 import BeautifulSoup, ResultSet, Tag


class Cards(TypedDict):
    question: str
    answer: str


cards_in_set: list[Cards] = []
url_file_name: str = "url.txt"
export_file_name: str = "quizlet.txt"
separation_character: str = "\t"


def export_set() -> None:
    """
    Purpose:    Export the contents of 'cards_in_set' to a text file.
    Modifies:   Nothing
    Returns:    None
    """
    try:
        with open(export_file_name, "w", encoding="utf-8") as file:
            for card in cards_in_set:
                file.write(
                    card["question"].strip()
                    + separation_character
                    + card["answer"].strip()
                    + "\n"
                )
        print(f"\nSuccessfully exported to: {export_file_name}")
    except Exception as e:
        print("Error occurred when exporting cards:", e)


def format_content(elements: ResultSet[Tag]) -> None:
    """
    Purpose:    Properly format the card content removing special characters and whitespace
    Modifies:   Elements in 'cards_in_set'
    Returns:    None
    """
    print('Formatting content...')
    try:
        for element in elements:
            element.string = element.text.strip()
            #print(element.string)
    except Exception as e:
        print("Exception occurred when formatting content:", e)


def scrape_cards(driver) -> None:
    """
    Purpose:    Scrape quizlet set, properly format content and populate 'cards_in_set'.
    Modifies:   Populates 'cards_in_set'
    Returns:    None
    """
    html_content: str = load_html(driver=driver)
    print("Scraping the quizlet set...")
    try:
        soup: BeautifulSoup = BeautifulSoup(html_content, "html.parser")

        # Find all <span> elements with class "TermText"
        elements: ResultSet[Tag] = soup.find_all("span", class_="TermText")
        format_content(elements=elements)

        for i in range(0, len(elements), 2):
            question: str = elements[i].string
            answer: str = elements[i + 1].string
            card: dict[str, str] = {"question": question, "answer": answer}
            cards_in_set.append(card)
    except Exception as e:
        print("Error occurred when scraping cards:", e)


def load_html(driver) -> str:
    """
    Purpose:    Loads the HTML content from the provided web page
    Modifies:   Nothing
    Returns:    source_html (string object)
    """
    print("Loading the html...")
    try:
        source_html: str = driver.page_source
        return source_html
    except Exception as e:
        print("Error occurred when loading html:", e)


def main() -> None:
    """
    Purpose:    w
    Modifies:   Nothing
    Returns:    None
    """
    try:
        with open(url_file_name, "r") as file:
            url = file.readline()
        print("Quizlet link:", url)
        try:
            opts = Options()
            opts.headless = True
            geckodriver_path = (
                "geckodriver.exe"  # Assumes geckdriver is in the same directory
            )
            service = Service(geckodriver_path)

            driver = webdriver.Firefox(service=service, options=opts)
            driver.get(url)

            try:
                scrape_cards(driver=driver)
                driver.quit()
                export_set()
            except:
                driver.quit()
        except Exception as e:
            driver.quit()
            print("Error occurred when connecting driver:", e)
    except Exception as e:
        print("Error occurred when loading url:", url)


if __name__ == "__main__":
    main()
