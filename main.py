from application.salary import calculate_salary
import application.db.people as people
import datetime as dt
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    # Собираем факты дня
    response = requests.get('https://xn--80af2bld5d.xn--p1ai/studlife/home/10565/')
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all('div', class_='col col-mb-12 col-12')

    day_facts = []

    if len(divs) >= 3:
        div = divs[2]
        p_tags = div.find_all('p')
        for i in range(1, len(p_tags), 2):
            day_facts.append(p_tags[i].text)

    count = 0
    while True:
        employees_names = people.get_employees()
        print(f'Выбери работника: ')
        for i in range(len(employees_names)):
            print(f'{i + 1}. {employees_names[i]}')
        name = input()

        print(f'Заработано: {calculate_salary(people.salaries[employees_names[int(name) - 1]])} рублей. '
              f'Сегодня: {dt.datetime.now().strftime("%H:%M:%S %Y-%m-%d")}')

        print(f'А Вы знали: {day_facts[count]}')
        if count == len(day_facts) - 1:
            count = 0
        count += 1
