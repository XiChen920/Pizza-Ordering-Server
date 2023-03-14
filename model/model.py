import pymysql.cursors
from tabulate import tabulate
from view import view

# connect to database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='920920',
    db='pizza'
)
cursor = connection.cursor()


# return the id of the last row from table order (the id of current order)
def get_order_id():
    sql = 'SELECT MAX(order_id) FROM orders'
    cursor.execute(sql)
    result = list(cursor.fetchone())
    current_id = result[0]
    return int(current_id)


# return the name of customer
def get_order_name():
    current_id = get_order_id()
    sql = 'SELECT order_customer_name FROM orders WHERE order_id = %s;'
    cursor.execute(sql, current_id)
    result = list(cursor.fetchone())
    customer_name = result[0]
    return customer_name


# method to create a new order using customer name, number, address
def create_new_order(postcode, username, phone_number, address):
    sql1 = "INSERT INTO `orders` (`order_customer_name`, `order_phone_number`, `order_postcode`,`order_address`, `order_pizza_amount`) " \
           "VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql1, (username, phone_number, postcode, address, 0))
    connection.commit()


# method to add a food to food_order table
# +1 to order pizza amount
def add_food_to_order(food_id, food_name):
    current_id = get_order_id()

    sql1 = "INSERT INTO `food_order` (`order_id`, `food_id`,`food_name`) " \
           "VALUES (%s,%s,%s)"
    cursor.execute(sql1, (current_id, food_id, food_name))

    if food_id <= 10:
        sql2 = "UPDATE `pizza`.`orders` SET `order_pizza_amount` = `order_pizza_amount`+1 WHERE (`order_id` = %s);"
        cursor.execute(sql2, current_id)

    connection.commit()
    if int(food_id)<=10:
        view.money = view.money + get_pizza_money(food_id)
    else:
        view.money = view.money + get_sweet_money(food_id)


#  delete food id from food_order table, if is pizza, then pizza amount from order-1
def delete_food_from_order(delete_food):
    current_id = get_order_id()

    sql = 'DELETE FROM `food_order` WHERE order_id = %s AND food_id = %s;'
    cursor.execute(sql, [current_id, str(delete_food)])
    print("-------------------------------")
    print("Food id " + str(delete_food) + " has already removed from your menu")
    print("-------------------------------")
    if int(delete_food) <= 10:
        sql2 = "UPDATE `pizza`.`orders` SET `order_pizza_amount` = `order_pizza_amount`-1 WHERE (`order_id` = %s);"
        cursor.execute(sql2, current_id)

    connection.commit()
    if int(delete_food) <= 10:
        view.money = view.money - get_pizza_money(delete_food)
    else:
        view.money = view.money - get_sweet_money(delete_food)


# get how many pizza has been ordered in an order
def get_pizza_amount_from_order(order_id):
    sql = 'SELECT order_pizza_amount FROM orders WHERE order_id = %s;'
    cursor.execute(sql, order_id)
    result = list(cursor.fetchone())
    pizza_amount = result[0]
    return pizza_amount


def cancel_order():
    current_id = get_order_id()
    sql1 = 'DELETE FROM orders WHERE orders.order_id = %s;'
    cursor.execute(sql1, [current_id])
    connection.commit()
    sql2 = 'DELETE FROM food_order WHERE order_id = %s;'
    cursor.execute(sql2, [current_id])
    connection.commit()


def show_pizza_menu():
    sql = 'select * from pizzas'
    cursor.execute(sql)
    result = list(cursor.fetchall())
    index = 0
    for rows in result:
        rows = list(rows)
        if rows[3] == 0:
            rows[3] = "no"
        elif rows[3] == 1:
            rows[3] = "yes"
        result[index] = rows
        index += 1
    print(tabulate(result, headers=['id', 'name', 'price', 'vegetarian', 'ingredient'], tablefmt="pretty"))


def show_dessert_and_drink_menu():
    sql = 'select * from desserts_and_drinks'
    cursor.execute(sql)
    result = cursor.fetchall()
    print(tabulate(result, headers=['id', 'name', 'price'], tablefmt="pretty"))


def show_current_order():
    current_id = get_order_id()
    sql = 'SELECT food_name,food_id FROM food_order WHERE order_id = %s;'
    cursor.execute(sql, current_id)
    result = list(cursor.fetchall())
    print(tabulate(result, headers=['your food', 'food id'], tablefmt="pretty"))


def less_than_one_pizza():
    current_id = get_order_id()
    sql = 'SELECT order_pizza_amount FROM orders WHERE order_id = %s;'
    cursor.execute(sql, current_id)
    result = list(cursor.fetchone())
    pizza_amount = result[0]
    if pizza_amount < 1:
        return True


# update pizza amount (if ordered before)
def record_pizza_amount_old_customer():
    current_id = get_order_id()
    customer_name = get_order_name()
    new_ordered_pizza_amount = get_pizza_amount_from_order(current_id)

    sql = "UPDATE `pizza`.`customer` SET `pizza_amount` = `pizza_amount`+%s WHERE (`name` = %s);"
    cursor.execute(sql, [new_ordered_pizza_amount, customer_name])
    connection.commit()


# record this time pizza amount (if he has not ordered before)
def record_pizza_amount_new_customer():
    current_id = get_order_id()
    customer_name = get_order_name()
    pizza_amount = get_pizza_amount_from_order(current_id)

    sql = "INSERT INTO `customer` (`name`, `pizza_amount`) " \
          "VALUES (%s,%s)"
    cursor.execute(sql, (customer_name, pizza_amount))
    connection.commit()


# get (current)customer's history pizza amount
# !!!!have to be someone ordered before!!!!!!
def get_history_pizza_amount():
    customer_name = get_order_name()

    sql = 'SELECT pizza_amount FROM customer WHERE name = %s;'
    cursor.execute(sql, customer_name)
    result = list(cursor.fetchone())
    history_amount = result[0]
    return history_amount


# return true if we can give this customer 10% discount
# whether he has >10 amount in history pizza ordered amount
# if yes, -10 and return true
# only applies to people ordered before
def has_ordered_ten_pizzas():
    history_amount = int(get_history_pizza_amount())
    customer_name = get_order_name()

    if history_amount >= 10:
        sql = "UPDATE `pizza`.`customer` SET `pizza_amount` = `pizza_amount`-10 WHERE (`name` = %s);"
        cursor.execute(sql, customer_name)
        connection.commit()
        return True

    return False


def get_ingredient_price(ingredient_id):
    sql = 'SELECT price FROM ingredient WHERE ingredient_id = %s;'
    cursor.execute(sql, ingredient_id)
    result = list(cursor.fetchone())
    ingredient_price = result[0]
    return int(ingredient_price)


def show_pizza_price_calculation():
    # get ingredient price
    price1 = get_ingredient_price(1)
    price2 = get_ingredient_price(2)
    price3 = get_ingredient_price(3)
    price4 = get_ingredient_price(4)
    price5 = get_ingredient_price(5)
    price6 = get_ingredient_price(6)
    price7 = get_ingredient_price(7)
    price8 = get_ingredient_price(8)
    price9 = get_ingredient_price(9)
    price10 = get_ingredient_price(10)
    price11 = get_ingredient_price(11)
    price12 = get_ingredient_price(12)

    # get ingredient price
    price_11 = price1 + price2
    price_22 = price1 + price2 + price3
    price_33 = price1 + price2 + price4
    price_44 = price1 + price2 + price8
    price_55 = price1 + price2 + price9
    price_66 = price1 + price2 + price5
    price_77 = price1 + price2 + price6
    price_88 = price1 + price11 + price12 + price9 + price2
    price_99 = price1 + price2 + price7
    price_00 = price1 + price2 + price6 + price10

    # calculate price after margin
    sql1 = "UPDATE `pizza`.`pizza_price` SET `price_after_margin` = `ingredient_price`*1.4;"
    cursor.execute(sql1)
    connection.commit()

    # calculate price after VAT
    sql2 = "UPDATE `pizza`.`pizza_price` SET `price_after_vat` = `price_after_margin`*1.09;"
    cursor.execute(sql2)
    connection.commit()

    sql = 'select * from pizza_price'
    cursor.execute(sql)
    result = cursor.fetchall()

    print(tabulate(result, headers=['pizza id', 'pizza', 'ingredients',
                                    'ingredients cost', 'price after margin(40%)', 'price after VAT(9%)'],
                   tablefmt="pretty"))


def get_pizza_money(pizza_id):
    sql = 'SELECT pizza_price FROM pizzas WHERE pizza_id = %s;'
    cursor.execute(sql, pizza_id)
    result = list(cursor.fetchone())
    pizza_price = result[0]
    return float(pizza_price)


def get_sweet_money(other_id):
    sql = 'SELECT food_price FROM desserts_and_drinks WHERE food_id = %s;'
    cursor.execute(sql, other_id)
    result = list(cursor.fetchone())
    price = result[0]
    return float(price)
