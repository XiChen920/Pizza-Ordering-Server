from view import view
import datetime
from datetime import datetime
from datetime import timedelta


def calculate_deliver_time():
    now = datetime.fromtimestamp(datetime.timestamp(datetime.now()))
    return int((timedelta(minutes=15) - (now - view.order_time)).seconds / 60)


# profit 40%
def add_pizza_profit(pizza_price):
    pizza_price = 1.4 * pizza_price
    return pizza_price


# VAT 9%
def add_pizza_vat(price):
    price = 1.09 * price
    return price
