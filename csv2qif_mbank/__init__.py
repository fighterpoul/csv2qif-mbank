import csv
from csv2qif.core import Transaction
import datetime
import re

__price_regex = re.compile('[a-zA-Z ]')
__text_regex = re.compile('[\t ]+')

__mapping = {
    'date': 0,
    'price': 4,
    'recipient': 2,
    'desc': 1,
}


class dialect(csv.Dialect):
    delimiter = ';'
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\r\n'
    quoting = csv.QUOTE_MINIMAL


def row_converter(csv_row) -> Transaction:
    return Transaction(
        date=__get_date(csv_row),
        price=__get_price(csv_row),
        recipient=__text_regex.sub(' ', csv_row[__mapping['recipient']]),
        desc=__text_regex.sub(' ', csv_row[__mapping['desc']])
    )


def row_filter(csv_row) -> bool:
    try:
        __get_price(csv_row)
        __get_date(csv_row)
    except (IndexError, ValueError):
        return False
    else:
        return True


def __get_price(csv_row) -> float:
    price = csv_row[__mapping['price']]
    price = __price_regex.sub('', price)
    price = price.replace(',', '.')
    return float(price)


def __get_date(csv_row) -> datetime.datetime:
    return datetime.datetime.strptime(csv_row[__mapping['date']], '%Y-%m-%d')
