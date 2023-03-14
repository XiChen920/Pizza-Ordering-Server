# use this to create the question: How can I help you?
# select from order, see menu, quit all
main_list = {
    "type": "list",
    "name": "main_choice",
    "message": "How can I help you?",
    "choices": ["Order my meals", "See the menus", "Quit"],

}

# choose which menu to see (pizza / desserts_drinks)
sub_list = {
    "type": "list",
    "name": "sub_choice",
    "message": "Which menu to see?",
    "choices": ["Pizzas Menu", "Desserts and Drinks Menu"],
}

postcode_question = {
    "type": "list",
    "name": "postcode_choice",
    "message": "Please chose your postcode here: (if is not listed below, please pick up yourself) ",
    "choices": ["-6219", "-6221", "-6222", "-6223", "-6224"],
}
# ask personal info of the client
id_questions = [
    {"type": "input", "message": "Enter your username", "name": "username"},
    {"type": "input", "message": "Enter your phone number", "name": "phone_number"},
    {"type": "input", "message": "Enter your address", "name": "address"}
]

# ask user if the info is correct
ensure_list = {
    "type": "list",
    "name": "ensure_choice",
    "message": "Is your personal information recorded right?",
    "choices": ["Yes, it's correct", "No!"],
}

# !!!this is not connect to database yet, might later or never
pizza_list = {
    "type": "list",
    "name": "pizza_choice",
    "message": "Select your pizza (Note: you must choose at least one pizza!)",
    "choices": ["-Margherita", "-Tuna", "-Pepperoni", "-Vegetaria", "-Salami",
                "-Chicken", "-Hawaii", "-Meat Lover", "-Salmon", "-Fruit",
                "-That's all (then let's order desserts and drinks)",
                "-See my current order"],
}

# !!!this is not connect to database yet, might later or never
dessert_and_drink_list = {
    "type": "list",
    "name": "dessert_and_drink_choice",
    "message": "Select your drinks and desserts! (This is optional)",
    "choices": ["-Coke", "-Fanta", "-Ice Tea", "-Sprite",
                "-Cheese Cake", "-Apple Pie", "-That's all (nothing I want more)",
                "-See my current order"],
}

menu_ensure_question = {
    "type": "list",
    "name": "menu_ensure_choice",
    "message": "This is what you ordered so far. Do you want to make some change?",
    "choices": ["Yes, I want to delete something", "No!"],
}

menu_delete_question = [
    {"type": "input", "message": "Enter the id of the food you want to delete", "name": "delete_food"},

]

deliver_list = {
    "type": "list",
    "name": "deliver_choice",
    "message": "Select your option",
    "choices": ["See status of order", "Cancel my order", "check when the pizza will arrive", "Quit"],
}


history_pizza_order_list = {
    "type": "list",
    "name": "history_choice",
    "message": "Have you ordered using the same username before? Choose here to win a discount!",
    "choices": ["Yes! I've ordered before!", "No"],
}

