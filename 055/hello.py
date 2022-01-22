from flask import Flask

app = Flask(__name__)



def make_bold(function):
    def wrapper_function():
        return_string = function()
        formatted_string = "<b>{0}</b>".format(return_string)
        return formatted_string
    return wrapper_function

def html_tag_wrap(tag):
    def with_html_tag(function):
        def wrapper_function(*args, **kwargs):
            return_string = function(*args, **kwargs)
            formatted_string = "<{tag}>{0}</{tag}>".format(return_string, tag=tag)
            return formatted_string
        return wrapper_function
    return with_html_tag

@app.route("/")
@html_tag_wrap("em")
@html_tag_wrap("b")
@html_tag_wrap("u")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bold")
@make_bold
def hello_world():
    return "<p>Bold!</p>"

if __name__ == "__main__":
    app.run()
