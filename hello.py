from flask import Flask
import random
#  # set FLASK_APP=hello.py
#  # $env:FLASK_APP = "hello.py"
#  # flask run
#
# app = Flask(__name__)
# print(__name__)
# print(random.__name__)
#
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
#
# if __name__ == "__main__":
#     app.run()

# python decorators


# def divide(n1, n2):
#     return n1 / n2
#
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# result = calculate(divide, 2, 3)
#

# nested function
#
#
# def outer_function():
#     print("im outer")
#
#     def nested_function():
#         print("im inner")
#
#     nested_function()
#
#
# outer_function()

# function can be returned from other functions
# def outer_function():
#     print("im outer")
#
#     def nested_function():
#         print("im inner")
#
#     return nested_function
#
#
# inner_function = outer_function()
# inner_function()
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # do something before
        function()

        # do something after
    return wrapper_function


@delay_decorator
def say_hello():
    print("hello")


say_hello()

# decorated_function = delay_decorator(say_hello)
# decorated_function()