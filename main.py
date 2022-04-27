from flask import Flask


app = Flask(__name__)


@app.route("/")
def my_function():
    return "Hello World"





# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
