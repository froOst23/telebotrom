import requests
from bs4 import BeautifulSoup

from utils import get_logger

url = requests.get(
    url='https://rsport.ria.ru/organization_football_roma/calendar/'
)
soup = BeautifulSoup(url.content, 'html.parser')
logger = get_logger(__name__)


def parse_content(content: soup) -> list:
    content = list(content.find_all('tr'))
    result = []

    for element in content:
        date = element.find(class_='m-date m-tac').contents

        try:
            tournament = element.find(class_='m-tournament').a.contents
        except AttributeError as e:
            tournament = element.find(class_='m-tournament').contents
            logger.exception(e)

        team_1 = element.find(class_='m-team m-team-1').a.contents

        try:
            team_2 = element.find(class_='m-team m-team-2').a.contents
        except AttributeError as e:
            team_2 = element.find(class_='m-team m-team-2').span.span.contents
            logger.exception(e)

        result.append([date[0], tournament[0], team_1[0], team_2[0]])
    return result


if __name__ == '__main__':
    data = soup.find('tbody')
    game = parse_content(data)
    for i in game:
        logger.info(f'Дата: {i[0]}, Турнир: {i[1]}, {i[2]} vs {i[3]}')
