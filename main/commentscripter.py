from collections import namedtuple
from operator import attrgetter

import requests
from bs4 import BeautifulSoup


class CommentScripter:
    def __init__(self, base_url):
        self.__base_url = base_url
        self.comment_data = []
        self.__comment = namedtuple('comment', 'date, vote, value')

    def get_comment_data(self):
        for i in range(1, 1000):
            url = self.__base_url + str(i)
            page = self.__get_page(url)
            if page is None:
                break
            self.__analyze_page(page)
        print("Collected {0} comments".format(len(self.comment_data)))
        self.__sort_by_plus_vote()

    def __get_page(self, url):
        page = requests.get(url)
        if page.status_code != 200:
            print("scipting has been done")
            return None
        return page.text

    def __analyze_page(self, page):
        soup = BeautifulSoup(page, 'html.parser')
        entry_ic = soup.find_all('ul', class_='sub')
        for div in entry_ic:
            vote = int(div.find('p', class_='vC').text.strip())
            date = div.find('time').get('datetime')
            value = div.find(class_='text').find('p').text.strip()
            self.comment_data.append(self.__comment(date, vote, value))

        print("{0} comments".format(len(self.comment_data)))

    def __sort_by_plus_vote(self):
        self.comment_data = sorted(self.comment_data, key=attrgetter('vote'))
