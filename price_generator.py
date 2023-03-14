import model

#  show how the price is generated, this should not let customers know
#  a business secret

# this will create a table to see how the price is calculated
# and update it to database (pizza final price)....
from model.model import show_pizza_price_calculation

if __name__ == "__main__":
    show_pizza_price_calculation()

