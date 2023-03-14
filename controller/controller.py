from model import model
from view import view


def process_pizza_choice(pizza_answer):
    if pizza_answer == "-Margherita":
        model.add_food_to_order(1, "Margherita")
        print("------------------------------------")
        print("~~Margherita pizza added to your order~~")
        print("------------------------------------")

    if pizza_answer == "-Tuna":
        model.add_food_to_order(2, "Tuna")
        print("------------------------------------")
        print("~~Tuna pizza added to your order~~")
        print("------------------------------------")

    if pizza_answer == "-Pepperoni":
        model.add_food_to_order(3, "Pepperoni")
        print("------------------------------------")
        print("~~Pepperoni pizza added to your order~~")
        print("------------------------------------")

    if pizza_answer == "-Vegetaria":
        model.add_food_to_order(4, "Vegetaria")
        print("------------------------------------")
        print("~~Vegetaria pizza added to your order~~")
        print("------------------------------------")

    if pizza_answer == "-Salami":
        model.add_food_to_order(5, "Salami")
        print("------------------------------------")
        print("~~Salami pizza added to your order~~")
        print("------------------------------------")

    if pizza_answer == "-Chicken":
        model.add_food_to_order(6, "Chicken")
        print("------------------------------------")
        print("~~Chicken pizza added to your order~~")
        print("------------------------------------")

    if pizza_answer == "-Hawaii":
        model.add_food_to_order(7, "Hawaii")
        print("------------------------------------")
        print("~~Hawaii pizza added to your order~~")
        print("------------------------------------")

    if pizza_answer == "-Meat Lover":
        model.add_food_to_order(8, "Meat Lover")
        print("------------------------------------")
        print("~~Meat Lover pizza added to your order~~")
        print("------------------------------------")

    if pizza_answer == "-Salmon":
        model.add_food_to_order(9, "Salmon")
        print("------------------------------------")
        print("~~Salmon pizza added to your order~~")
        print("------------------------------------")

    if pizza_answer == "-Fruit":
        model.add_food_to_order(10, "Fruit")
        print("------------------------------------")
        print("~~Fruit pizza added to your order~~")
        print("------------------------------------")

    return


def process_dessert_and_drink_choice(dessert_and_drink_answer):
    if dessert_and_drink_answer == "-Coke":
        model.add_food_to_order(11, "Coke")
        print("------------------------------------")
        print("~~Coke added to your order~~")
        print("------------------------------------")

    if dessert_and_drink_answer == "-Fanta":
        model.add_food_to_order(12, "Fanta")
        print("------------------------------------")
        print("~~Fanta added to your order~~")
        print("------------------------------------")

    if dessert_and_drink_answer == "-Ice Tea":
        model.add_food_to_order(13, "Ice Tea")
        print("------------------------------------")
        print("~~Ice Tea added to your order~~")
        print("------------------------------------")

    if dessert_and_drink_answer == "-Sprite":
        model.add_food_to_order(14, "Sprite")
        print("------------------------------------")
        print("~~Sprite added to your order~~")
        print("------------------------------------")

    if dessert_and_drink_answer == "-Cheese Cake":
        model.add_food_to_order(15, "Cheese Cake")
        print("------------------------------------")
        print("~~Cheese Cake added to your order~~")
        print("------------------------------------")

    if dessert_and_drink_answer == "-Apple Pie":
        model.add_food_to_order(16, "Apple Pie")
        print("------------------------------------")
        print("~~Apple Pie added to your order~~")
        print("------------------------------------")

    return


def process_postcode_choice(postcode_answer):
    postcode = 0
    if postcode_answer == "-6219":
        postcode = 6219

    if postcode_answer == "-6221":
        postcode = 6221

    if postcode_answer == "-6222":
        postcode = 6222

    if postcode_answer == "-6223":
        postcode = 6223

    if postcode_answer == "-6224":
        postcode = 6224

    postcode_text = str(postcode)
    print("Postcode: " + postcode_text)
    print("------------------------------------")
    return postcode


def ensure_user_id(username, phone_number, address):
    print("------------------------------------")
    print("-------Confirm your info here-------")
    print("------------------------------------")
    print("Username: " + username)
    print("Phone number: " + phone_number)
    print("Address: " + address)


def ensure_user_postcode(postcode_answer):
    process_postcode_choice(postcode_answer)


def begin():
    view.start()
