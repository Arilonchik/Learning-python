import requests
from bs4 import BeautifulSoup
from decimal import *


def convert(amount, cur_from, cur_to, date, requests):
    xml = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}')
    soup = BeautifulSoup(xml.content, 'lxml')
    required = ('value', 'nominal')
    if cur_from != 'RUB':
        value_from, nominal_from = map(float, (
            soup.find('charcode', text=cur_from).find_next_sibling(i).string.replace(',', '.')
            for i in required))
    else:
        value_from, nominal_from = 1, 1
    if cur_to != 'RUB':
        value_to, nominal_to = map(float, (
            soup.find('charcode', text=cur_to).find_next_sibling(i).string.replace(',', '.')
            for i in required))
    else:
        value_to, nominal_to = 1, 1
    amount_in_rub = (Decimal(value_from) / Decimal(nominal_from)) * Decimal(amount)
    converted = amount_in_rub / (Decimal(value_to) / Decimal(nominal_to))
    return converted.quantize(Decimal('.0001'))


if __name__ == '__main__':
    print(convert(40, 'RUB', 'BYN', '12.05.2020', requests))
