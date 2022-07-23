from flask import Flask, render_template, url_for, request

# start with this: .venv\Scripts\Activate.ps1

app = Flask(__name__)

todo_list = []


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/name")
def name():
    return "<h1>Behold my power you foolish mortal<h1>"


@app.route("/add")
def add_todo():
    global todo_list
    print(request.args.get("todo-input"))
    todo_list.append(request.args.get("todo-input"))
    return render_template("index.html", todo_list=todo_list)


if __name__ == "__main__":
    app.run(debug=True)
