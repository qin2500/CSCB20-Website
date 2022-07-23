from flask import Flask, render_template, url_for, request

# start with this: venv\Scripts\Activate.ps1
# must be in a2 folder

app = Flask(__name__)


# def user(name: str) -> str:
#     if name.isupper() or name.islower():
#         name.swapcase()

#     return name.strip()


@app.route("/<name>")
def user(name: str) -> str:
    # not name.isnumeric):
    if ((name.isupper() or name.islower()) and name.isalpha()):
        name = name.swapcase()

    if (not name.isalpha):
        name = name.capitalize()

    else:
        name2 = ""
        for i in range(len(name)):
            if name[i].isalpha():
                name2 += name[i]
        name = name2

    # print(name.isalpha())

    return "Welcome, " + name.strip() + ", to my CSCB20 Website!"


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=False)
