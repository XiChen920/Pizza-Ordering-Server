import sys

from PyInquirer import prompt

from controller import calculation
from controller import controller
from model import model
import datetime
from datetime import datetime
from datetime import timedelta
from termcolor import colored

from view.terminal_list import menu_ensure_question, menu_delete_question, main_list, sub_list, postcode_question, \
    id_questions, ensure_list, pizza_list, dessert_and_drink_list, history_pizza_order_list, deliver_list

# instance variable used in calculation
order_time = datetime.fromtimestamp(datetime.timestamp(datetime.now()))
money = 0


def menu_operation():
    model.show_current_order()
    print("-------------------------------")
    print("current total price is: " + str(money) + " euro")
    print("-------------------------------")
    menu_answers = prompt(menu_ensure_question)
    menu_answer = menu_answers["menu_ensure_choice"]
    if menu_answer == "Yes, I want to delete something":
        # get the input
        menu_delete_answer = prompt(menu_delete_question)
        model.delete_food_from_order(**menu_delete_answer)
        model.show_current_order()
        print("-------------------------------")
        print("current total price is: " + str(money) + " euro")
        print("-------------------------------")
        return

    if menu_answer == "No!":
        return


def start():
    isFinished_order = False  # True if the user have done ordering , false if he's still adding food
    while not isFinished_order:
        answers = prompt(main_list)
        answer = answers["main_choice"]

        if answer == "See the menus":
            sub_answers = prompt(sub_list)
            sub_answer = sub_answers["sub_choice"]

            # see the menu of pizzas
            if sub_answer == "Pizzas Menu":
                model.show_pizza_menu()

            # see the menu of desserts and drinks
            if sub_answer == "Desserts and Drinks Menu":
                model.show_dessert_and_drink_menu()

        if answer == "Order my meals":
            isCorrect_id = False
            while not isCorrect_id:
                # get post code input
                postcode_answers = prompt(postcode_question)
                postcode_answer = postcode_answers["postcode_choice"]
                postcode = controller.process_postcode_choice(postcode_answer)
                print("------------------------------------")
                postcode_record = postcode

                # get the input
                ensure_id_answers = prompt(id_questions)

                # use ensure_user_id method to print the personal info
                controller.ensure_user_id(**ensure_id_answers)
                controller.ensure_user_postcode(postcode_answer)

                print("------------------------------------")

                # ask user if your info is correct
                ensure_answers = prompt(ensure_list)

                # get user answer
                ensure_answer = ensure_answers["ensure_choice"]

                print("------------------------------------")

                # if the user confirm the info, end while loop
                if ensure_answer == "Yes, it's correct":
                    isCorrect_id = True

                    model.create_new_order(postcode_record, **ensure_id_answers)
                    # check if this name order before

                    isFinished_only_pizza = False  # pizza part is finished
                    while not isFinished_only_pizza:
                        pizza_answers = prompt(pizza_list)
                        pizza_answer = pizza_answers["pizza_choice"]

                        controller.process_pizza_choice(pizza_answer)

                        if pizza_answer == "-That's all (then let's order desserts and drinks)":
                            isFinished_only_pizza = True

                        if pizza_answer == "-See my current order":
                            menu_operation()

                    print("------------------------------------")

                    isFinished_other = False
                    while not isFinished_other:
                        dessert_and_drink_answers = prompt(dessert_and_drink_list)
                        dessert_and_drink_answer = dessert_and_drink_answers["dessert_and_drink_choice"]

                        controller.process_dessert_and_drink_choice(dessert_and_drink_answer)

                        if dessert_and_drink_answer == "-See my current order":
                            menu_operation()

                        if dessert_and_drink_answer == "-That's all (nothing I want more)":
                            if model.less_than_one_pizza():
                                model.show_current_order()

                                print("------------------------------------")
                                print('You should order at least one pizza.')
                                print('Sorry, but your order is cancelled...')
                                model.cancel_order()
                                print("------------------------------------")

                                sys.exit(0)

                            else:
                                model.show_current_order()
                                print("------------------------------------")
                                print("Total price is: " + str(money) + " euro")
                                print("------------------------------------")
                                history_pizza_answers = prompt(history_pizza_order_list)
                                history_pizza_answer = history_pizza_answers["history_choice"]

                                if history_pizza_answer == "Yes! I've ordered before!":
                                    model.record_pizza_amount_old_customer()
                                    if model.has_ordered_ten_pizzas():

                                        print("------------------------------------")
                                        print("Nice! you will have 10% discount!")
                                        m = 0.9 * money
                                        print("Total price now is: " + str(m) + " euro")
                                        left_pizza_amount = model.get_history_pizza_amount()
                                        expected_pizza_amount = 10 - int(left_pizza_amount)
                                        print("Order " + str(
                                            expected_pizza_amount) + " more pizzas next time, you will gain another 10% discount!")
                                        print("------------------------------------")
                                    else:
                                        print("------------------------------------")
                                        print("You don't order enough pizza to win a discount.")
                                        left_pizza_amount = model.get_history_pizza_amount()
                                        expected_pizza_amount = 10 - int(left_pizza_amount)
                                        print("Order " + str(
                                            expected_pizza_amount) + " more pizzas next time, you will gain a 10% discount!")
                                        print("------------------------------------")
                                if history_pizza_answer == "No":
                                    model.record_pizza_amount_new_customer()
                                    left_pizza_amount = model.get_history_pizza_amount()
                                    expected_pizza_amount = 10 - int(left_pizza_amount)
                                    print("------------------------------------")

                                    print("We will record your this time pizza record")
                                    print("Order " + str(
                                        expected_pizza_amount) + " more pizzas next time, you will gain a 10% discount!")
                                    print("------------------------------------")

                                model.show_current_order()
                                print("------------------------------------")
                                print("Overall price is: " + str(money) + " euro")
                                print("------------------------------------")
                                print("------------------------------------")

                                print("You've ordered all you want")
                                print("we'll start delivering soon")

                                print("------------------------------------")
                                isFinished_other = True
                                isFinished_order = True

                    # timer is set when the order is confirmed
                    order_time = datetime.fromtimestamp(datetime.timestamp(datetime.now()))
        if answer == "Quit":
            sys.exit(0)

    # above is the ordering part
    # below is the delivery part

    # TODO: (yyq)timer

    # within 5 mins allow to be cancelled
    # estimated_time = 30mins - timer

    # TODO: delivery person should be assigned to the order
    # 5 mins later it has to be out for delivery, status: in process -> out for delivery

    '''
    !!!!timer start!!!!!!

    '''
    isArrived = False  # True if the pizza has been delivered
    isCancelled = False  # True if the order is cancelled
    isDelivering = False  # True if the pizza is out for delivering (> 5 min)

    while not isArrived & isFinished_order:
        deliver_answers = prompt(deliver_list)
        deliver_answer = deliver_answers["deliver_choice"]
        now = datetime.fromtimestamp(datetime.timestamp(datetime.now()))

        if deliver_answer == "See status of order":
            if (now - order_time) >= timedelta(minutes=15):
                isArrived = True
            if isArrived:
                print("------------------------------------")
                print("Your pizza has already arrived!")
                print("------------------------------------")

            if isCancelled:
                print("------------------------------------")
                print("Your order is cancelled")
                print("------------------------------------")
                break
            # if 现在时间<5min
            # print("Your order is in process")
            # if 现在时间>5min
            # print("Your order is out for delivery")
            if (now - order_time) < timedelta(minutes=5):
                print("------------------------------------")
                print("Your order is in process")
                print("------------------------------------")
            else:
                print("------------------------------------")
                print("Your order is out for delivery")
                print("------------------------------------")

        if deliver_answer == "Cancel my order":
            # if 现在时间>5 min:
            # print("Sorry, You cannot cancel your order now.")
            # print("You may only cancel it within 5 mins after you order.")
            if (now - order_time) > timedelta(minutes=5):
                print("------------------------------------")
                print("Sorry, You cannot cancel your order now.")
                print("You may only cancel it within 5 mins after you order.")
                print("------------------------------------")
            # else
            # print("Now your order is cancelled, you will get refund soon.")
            # print("Welcome to order next time:)")

            else:
                model.cancel_order()
                print("------------------------------------")
                print("Now your order is cancelled, you will get refund soon.")
                print("Welcome to order next time:)")
                print("------------------------------------")
            isCancelled = True
            # delete everything from the database (order, order_food）
            # delete pizza number he order this time

        if deliver_answer == "check when the pizza will arrive":
            if (now - order_time) >= timedelta(minutes=15):
                isArrived = True
            if isArrived:
                print("------------------------------------")
                print("Your pizza has already arrived!")
                print("------------------------------------")
            else:
                time_text = str(calculation.calculate_deliver_time())
                print("------------------------------------")
                print("Your pizza will arrive in " + time_text + " minutes! Please wait patiently")
                print("------------------------------------")

        if deliver_answer == "Quit":
            sys.exit(0)
