from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/')
def index():
    # Make a request to the website
    response = requests.get('https://sea.mashable.com/')
    soup = BeautifulSoup(response.text, 'lxml')
    headlines1 = [headline.text for headline in soup.find_all(
        'h1', class_="hero_title")]
    url1_elements = soup.find_all('a', class_='hero_title_hover')

    h1url = [element['href'] for element in url1_elements]

    list1 = [(headlines1[i], h1url[i]) for i in range(len(headlines1))]

    headlines2 = [headline.text for headline in soup.find_all(
        'span', class_="hero_story")]
    url2_elements = soup.find_all('a', class_='hero_story_hover')

    h2url = [element['href'] for element in url2_elements]

    assert len(headlines2) == len(h2url)

    list2 = [(headlines2[i], h2url[i]) for i in range(len(headlines2))]

    headlines3 = [headline.text for headline in soup.find_all(
        'a', class_="box_title")]

    url3_elements = soup.find_all('a', class_='box_title')

    h3url = [element['href'] for element in url3_elements]

    list3 = [(headlines3[i], h3url[i]) for i in range(len(headlines3))]

    headlines4 = [headline.text for headline in soup.find_all(
        'a', class_="w-full block text-lg mt-2 text-center font-bold")]

    url4_elements = soup.find_all(
        'a', class_='w-full block text-lg mt-2 text-center font-bold')

    h4url = [element['href'] for element in url4_elements]

    list4 = [(headlines4[i], h4url[i]) for i in range(len(headlines4))]

    headlines5 = [headline.text for headline in soup.find_all(
        'div', class_="caption")]

    url5_list = soup.find_all('li', class_="blogroll ARTICLE")
    url5_elements = []
    for li in url5_list:
        a_tags = li.find_all('a')
        url5_elements.extend(a_tags)

    h5url = [element['href'] for element in url5_elements]

    list5 = [(headlines5[i], h5url[i]) for i in range(len(headlines5))]

    final_headlines = list1 + list2 + list3 + list4 + list5

    return render_template('index.html', headlines=final_headlines)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
