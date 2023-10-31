from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from typing import TypedDict
from bs4 import BeautifulSoup


class Cards(TypedDict):
    question: str
    answer: str


def export_set(cards_in_set):
    export_file_name = "quizlet.txt"
    separation_character = "\t"
    try:
        with open(export_file_name, 'w', encoding='utf-8') as file: 
            for card in cards_in_set:
                file.write(card['question'].strip() + separation_character + card['answer'].strip() + "\n")
        print(f"\nSuccessfully exported to: {export_file_name}")
    except Exception as e:
        print("Error occurred when exporting cards:", e)


def scrape_cards(cards_in_set, driver):
    html_content = load_html(driver)
    print("Scraping the quizlet set...")
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find all <span> elements with class "TermText"
        elements = soup.find_all('span', class_='TermText')
        
        for i in range(0, len(elements), 2):
            question = elements[i].text.replace('<br>', ' ')
            answer = elements[i + 1].text.replace('<br>', ' ')
            card = {'question': question, 'answer': answer}
            cards_in_set.append(card)
    except Exception as e:
        print("Error occurred when scraping cards:", e)


def load_html(driver):
    print("Loading the html...")
    try:
        source_html = driver.page_source
        return source_html
    except Exception as e:
        print("Error occurred when loading html:", e)


def main():
    url_file_name = "url.txt"
    try:
        with open(url_file_name, 'r') as file:
            url = file.readline()
        print("Quizlet link:", url)
        try:
            opts = Options()
            opts.headless = True
            geckodriver_path = 'geckodriver.exe' # Assumes geckdriver is in the same directory
            service = Service(geckodriver_path)

            driver = webdriver.Firefox(service=service, options=opts)
            driver.get(url)
            # Might need to insert time.sleep() here
            
            cards_in_set: Cards = []
            try:
                scrape_cards(cards_in_set, driver)
                driver.quit()
                export_set(cards_in_set)
            except:
                driver.quit()
        except Exception as e:
            driver.quit()
            print("Error occurred when connecting driver:", e)
    except Exception as e:
        print("Error occurred when loading url:", url)

if __name__ == '__main__':
    main()