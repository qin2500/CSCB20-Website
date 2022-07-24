
from datetime import datetime
import email
from functools import reduce
import bcrypt
from flask import Flask, flash, get_flashed_messages, redirect, render_template, session, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# start with this: venv\Scripts\Activate.ps1
# must be in a2 folder

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assignment3.db'
app.config['SECRET_KEY'] = 'ogga bogga'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(35), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    tutorial_attendance_grade = db.Column(db.Float)
    a1_grade = db.Column(db.Float)
    a2_grade = db.Column(db.Float)
    a3_grade = db.Column(db.Float)
    midterm_grade = db.Column(db.Float)
    final_exam_grade = db.Column(db.Float)
    final_grade = db.Column(db.Float)
    instructor = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.username


class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(35))
    last_name = db.Column(db.String(35))

    def __repr__(self):
        return '<Instructor %r>' % self.username


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instructor = db.Column(db.String(80),
                           #                    db.ForeignKey(
                           # "Instructor.id"),
                           nullable=False)
    content1 = db.Column(db.String(720))
    content2 = db.Column(db.String(720))
    content3 = db.Column(db.String(720))
    content4 = db.Column(db.String(720))
    content5 = db.Column(db.String(720))
    date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Feedback %r>' % self.id


class RemarkRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(
        db.Integer, nullable=False)
    remark_item = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(800), nullable=False)

    def __repr__(self):
        return '<Remark %r for %r of %r >' % self.id % self.student_id % self.remark_item


@ app.route("/my_grades", methods=['GET', 'POST'])
def my_grades():
    if not session.get('username'):
        return redirect(url_for('sign_in'))

    print(session['username'])

    print(User.query.filter(User.username == session['username']).first())

    if request.method == 'POST':
        if (request.form.get("item_list") != "option"):
            print("changed item... or so python says")
            # instructor = Instructor.query.filter(
            #     Instructor.username == request.form.get("instructor_list")).first().id
            # print(instructor)

            print("qqq it's a remark")
            print(request.form.get("content"))
            db.session.add(RemarkRequest(

                content=request.form.get("content1"),
                student_id=User.query.filter(
                    User.username == session['username']).first().id,
                remark_item=request.form.get("item_list")
            ))
            db.session.commit()
            flash("You have successfully submitted a remark request. Thanks!")
            return redirect(url_for('hello_world'))
        else:
            flash("Please select an item")
            return redirect(url_for('my_grades'))

    return render_template("my_grades.html", user=User.query.filter(User.username == session['username']).first(), auth=session['auth'])


@app.route("/viewFeedback", methods=['GET', 'POST'])
def viewFeedback():
    if not session.get('username'):
        return redirect(url_for('sign_in'))
    if not Instructor.query.filter(Instructor.id == session['id']).first():
        flash("You are not authorized to view that page")
        return redirect(url_for("hello_world"))
    if request.method == 'POST':
        if (request.form.get("feedback_list") != "feedback"):
            feedback = Feedback.query.filter(
                Feedback.id == request.form.get("feedback_list")).first()
            print(feedback)
            return render_template("view_feedback.html", feedback=feedback, feedbackList=Feedback.query.order_by(Feedback.date).all(), instructor=Instructor.query.filter(Instructor.username == session['username']), auth=session['auth'])

    return render_template("view_feedback.html", feedback=Feedback.query.first(), feedbackList=Feedback.query.order_by(Feedback.date).filter(Feedback.instructor == Instructor.query.filter(Instructor.username == session['username']).first().username), instructor=Instructor.query.filter(Instructor.username == session['username']), auth=session['auth'])


@app.route("/viewRegrade", methods=['GET', 'POST'])
def viewRegrade():
    if not session.get('username'):
        return redirect(url_for("sign_in"))
    if not Instructor.query.filter(Instructor.id == session['id']).first():
        flash("You are not authorized to view that page")
        return redirect(url_for("hello_world"))
    if request.method == 'POST':
        if (request.form.get("feedback_list") != "feedback"):
            feedback = RemarkRequest.query.filter(
                RemarkRequest.id == request.form.get("feedback_list")).first()
            return render_template("view_regrade.html", feedback=feedback, feedbackList=RemarkRequest.query.all(), instructor=Instructor.query.filter(Instructor.username == session['username']), auth=session['auth'])

    return render_template("view_regrade.html", feedback=RemarkRequest.query.first(), feedbackList=RemarkRequest.query.all(), instructor=Instructor.query.filter(Instructor.username == session['username']), auth=session['auth'])


@app.route("/giveFeedback", methods=['GET', 'POST'])
def giveFeedback():
    if not session.get('username'):
        return redirect(url_for('sign_in'))
    if request.method == 'POST':
        if (request.form.get("instructor_list") != "instructor"):
            print("changed instructor... or so python says")
            instructor = Instructor.query.filter(
                Instructor.username == request.form.get("instructor_list")).first().id
            print(instructor)

            print("qqq it's feedback")
            db.session.add(Feedback(
                instructor=instructor,
                content1=request.form.get("feedback1"),
                content2=request.form.get("feedback2"),
                content3=request.form.get("feedback3"),
                content4=request.form.get("feedback4"),
                content5=request.form.get("feedback5"),
                date=datetime.now()
            ))
            db.session.commit()
            flash("You have successfully given feedback. Thanks!")
            return redirect(url_for('hello_world'))
        else:
            flash("Please select an instructor")
            return redirect(url_for('giveFeedback'))
    return render_template("give_feedback.html", instructor=Instructor.query.first(), instructorList=Instructor.query.all(), auth=session['auth'])


@app.route("/editGrades", methods=['GET', 'POST'])
def editGrades():
    if not session.get('username'):
        return redirect(url_for('signUp'))
    if request.method == 'POST':

        # get student or something idk
        # if (request.form.get("student_list") != "student"):
        #     student = User.query.filter(
        #         User.username == request.form.get("student_list")).first()
        #     print(student)
        #     return render_template("edit_grades.html", student=student, studentList=User.query.all(), auth=session['auth'])

        # update grades
        print("supposed to submit")
        for i in User.query.all():
            j = request.form.get("tutorial_attendance_grade - " + str(i.id))
            i.tutorial_attendance_grade = j
            i.a1_grade = request.form.get("a1_grade - " + str(i.id))
            i.a2_grade = request.form.get("a2_grade - " + str(i.id))
            i.a3_grade = request.form.get("a3_grade - " + str(i.id))
            i.midterm_grade = request.form.get("midterm_grade - " + str(i.id))
            i.final_exam_grade = request.form.get(
                "final_exam_grade - " + str(i.id))
            i.final_grade = request.form.get("final_grade - " + str(i.id))

            if not (i.tutorial_attendance_grade == None or i.tutorial_attendance_grade == ""):
                j = float(i.tutorial_attendance_grade)
                i.tutorial_attendance_grade = j
            else:
                i.tutorial_attendance_grade = None
            if not (i.a1_grade == None or i.a1_grade == ""):
                i.a1_grade = float(i.a1_grade)
            else:
                i.a1_grade = None
            if not (i.a2_grade == None or i.a2_grade == ""):
                i.a2_grade = float(i.a2_grade)
            else:
                i.a2_grade = None
            if not (i.a3_grade == None or i.a3_grade == ""):
                i.a3_grade = float(i.a3_grade)
            else:
                i.a3_grade = None
            if not (i.midterm_grade == None or i.midterm_grade == ""):
                i.midterm_grade = float(i.midterm_grade)
            else:
                i.midterm_grade = None
            if not (i.final_exam_grade == None or i.final_exam_grade == ""):
                i.final_exam_grade = float(i.final_exam_grade)
            else:
                i.final_exam_grade = None
            if not (i.final_grade == None or i.final_grade == ""):
                i.final_grade = float(i.final_grade)
            else:
                i.final_grade = None
            print(i)
            print(request.form.get('tutorial_attendance_grade - ' + str(i.id)))
            print("^^^")
            j = request.form.get('tutorial_attendance_grade - ' + str(i.id))
            print(j)
            print("^^^")
            i.tutorial_attendance_grade = j
            print(i.tutorial_attendance_grade)
            print(i.final_grade)
            print('a1_grade - ' + str(i.id))
            print(request.form.get('a1_grade - ' + str(i.id)))
            db.session.commit()
        print("Updated grades.-----------------------------------------------------------------------------")
        flash("You have succesfully edited the grades.")
        return redirect(url_for('editGrades'))

    return render_template("edit_grades.html", student=User.query.first(), studentList=User.query.all(), auth=session['auth'])


@ app.route("/signUp", methods=['GET', 'POST'])
def signUp():
    if session.get('username'):
        return redirect(url_for('hello_world'))
    if request.method == 'POST':
        if request.form.get("auth") == "s":
            print("may/may not add student")
            id = User.query.filter(User.id == request.form.get("id")).first()
            name = User.query.filter(
                User.username == request.form.get("username")).first()
            mail = User.query.filter(
                User.email == request.form.get("email")).first()

            if id is None and name is None and mail is None:
                print("unique user")
                pw = request.form.get('password')
                uname = request.form.get('username')
                if pw == "":
                    flash("Please enter a password")
                    return redirect(url_for('signUp'))
                if uname == "":
                    flash("Please enter a username")
                    return redirect(url_for('signUp'))
                if request.form.get('email') == "" or request.form.get('first_name') == "" or request.form.get('last_name') == "" or request.form.get('id') == "":
                    flash("Please fill in each box")
                    return redirect(url_for('signUp'))

                if (" ") in pw:
                    flash(
                        "No spaces are allowed in password. Please construct an alternative one.")
                    return redirect(url_for("signUp"))
                if (" ") in uname:
                    flash(
                        "No spaces are allowed in username. Please construct an alternative one.")
                    return redirect(url_for("signUp"))

                hashed_pw = bcrypt.generate_password_hash(
                    request.form.get('password')).decode('utf-8')

                db.session.add(User(
                    id=request.form.get("id"),
                    username=uname,
                    password=hashed_pw,
                    email=request.form.get("email"),
                    first_name=request.form.get("fname"),
                    last_name=request.form.get("lname"),
                    tutorial_attendance_grade=None,
                    a1_grade=None,
                    a2_grade=None,
                    a3_grade=None,
                    midterm_grade=None,
                    final_exam_grade=None,
                    final_grade=None
                ))
            else:
                print("Did not add user")
                flash("Email/username/student# already taken")
                return redirect(url_for('signUp'))

        else:
            print("trying to find instructor")
            name2 = Instructor.query.filter(
                Instructor.username == request.form.get("username2")).first()
            mail2 = Instructor.query.filter(
                Instructor.email == request.form.get("email2")).first()

            print("username form: ", request.form.get("username2"))
            print("username match: ", name2)
            print("email form: ", request.form.get("email2"))
            print("mail match:", mail2)
            print((name2 is None) and (mail2 is None))

            print(name2 is None)
            print(mail2 is None)
            if name2 == None and mail2 == None:
                pw = request.form.get('password2')
                uname = request.form.get('username2')

                if pw == "":
                    flash("Please enter a password")
                    return redirect(url_for('signUp'))
                if uname == "":
                    flash("Please enter a username")
                    return redirect(url_for('signUp'))
                if request.form.get('email2') == "" or request.form.get('first_name2') == "" or request.form.get('last_name2') == "":
                    flash("Please fill in each box")
                    return redirect(url_for('signUp'))

                if (" ") in pw:
                    flash(
                        "No spaces are allowed in password. Please construct an alternative one.")
                    return redirect(url_for('hello_world'))
                if (" ") in uname:
                    flash(
                        "No spaces are allowed in username. Please construct an alternative one.")
                    return redirect(url_for('signUp'))
                hashed_pw = bcrypt.generate_password_hash(
                    request.form.get('password2')).decode('utf-8')

                db.session.add(Instructor(

                    first_name=request.form.get("fname2"),
                    last_name=request.form.get("lname2"),
                    password=hashed_pw,
                    username=request.form.get("username2"),
                    email=request.form.get("email2"),

                ))
            else:
                print("Did not add instructor")
                flash("Username/email is already being used.")
                return redirect(url_for('signUp'))
        db.session.commit()
        flash("Account succesfully created. Please Sign in.")
        return redirect(url_for('sign_in'))
    return render_template("sign_up.html", auth=2)


@ app.route("/sign_in", methods=['GET', 'POST'])
def sign_in():
    print("we are on sign in page")
    session.pop('_flashes', None)
    if session.get('username'):
        if User.query.filter(User.username == session['username']):
            session['auth'] = 0
        elif Instructor.query.filter(Instructor.username == session['username']):
            session['auth'] = 1
        else:
            return render_template("sign_in.html", auth=2)
        flash(session['username'])
        return redirect(url_for('hello_world'))
    if request.method == 'POST':
        input_usr = request.form.get("username")
        input_pword = request.form.get("password")
        auth = request.form.get("auth")
        print(input_usr)

        if auth == "s":
            print("trying student")
            usr_attempt = User.query.filter(
                User.username == input_usr).first()

            if usr_attempt == None:
                session.pop('_flashes', None)
                flash("Invalid combination of Username and Password")
                return render_template("sign_in.html", showError="TRUE", auth=2)
            if bcrypt.check_password_hash(
                    usr_attempt.password, input_pword):
                session['username'] = input_usr
                session['id'] = usr_attempt.id
                session['auth'] = 0
                print("WHO KNOWS")
                return redirect(url_for("hello_world"))

            else:
                print("wrong password")
                flash("Invalid combination of Username and Password")
                return render_template("sign_in.html", showError="TRUE", auth=2)
        else:
            usr_attempt = Instructor.query.filter(
                Instructor.username == input_usr).first()

            if usr_attempt == None:
                flash("Invalid combination of Username and Password")
                return render_template("sign_in.html", showError="TRUE", auth=2)
            if bcrypt.check_password_hash(
                    usr_attempt.password, input_pword):
                session['username'] = input_usr
                session['id'] = usr_attempt.id
                session['auth'] = 1

                print("WHO KNOWS")

                return redirect(url_for("hello_world"))

            else:
                flash("Invalid combination of Username and Password")
                return redirect(url_for("sign_in"))

    return render_template("sign_in.html", auth=2)


@ app.route("/")
def hello_world():
    print("we are on home page")
    print(session.get('username'))
    print(session.get('auth'))
    if (session.get('username') and not session.get('auth')):
        if User.query.filter(User.username == session['username']):
            session['auth'] = 0
        else:
            session['auth'] = 1

    if (not session.get('username') or (session.get('auth') > 1)):
        return redirect(url_for('sign_in'))

    if not User.query.filter(
            User.username == session['username']).first():
        print("how are we here??")
        return redirect(url_for('sign_in'))

    if session['auth'] == 1:
        ins = Instructor.query.filter(
            Instructor.username == session['username']).first()
        if ins != None:
            fname = ins.first_name
            flash(fname)
        return render_template("index.html", auth=session['auth'])

    if session['auth'] == 0:
        fname = User.query.filter(
            User.username == session['username']).first().first_name
        if fname != None:
            flash(fname)
        return render_template("index.html", auth=session['auth'])

    print(session.get("KEY"))
    fname = User.query.filter(
        User.username == session['username']).first().first_name
    if fname != None:
        flash(fname)
    return render_template("index.html", auth=session['auth'])


@ app.route("/about")
def idk():
    if not session.get('username'):
        return redirect(url_for('sign_in'))
    return render_template("about.html", auth=session['auth'])


@ app.route("/tests")
def tests():
    if not session.get('username'):
        return redirect(url_for('sign_in'))
    return render_template("tests.html", auth=session['auth'])


@ app.route("/assignments")
def assignments():
    if not session.get('username'):
        return redirect(url_for('sign_in'))
    return render_template("assignments.html", auth=session['auth'])


@ app.route("/announcements")
def announcements():
    if not session.get('username'):
        return redirect(url_for('sign_in'))
    return render_template("announcements.html", auth=session['auth'])


@ app.route("/lectures")
def lectures():
    if not session.get('username'):
        return redirect(url_for('sign_in'))
    return render_template("lectures.html", auth=session['auth'])


@ app.route("/calendar")
def calendar():
    if not session.get('username'):
        return redirect(url_for('sign_in'))
    return render_template("calendar.html", auth=session['auth'])


@ app.route("/labs")
def labs():
    if not session.get('username'):
        return redirect(url_for('sign_in'))
    return render_template("labs.html", auth=session['auth'])


@ app.route("/resources")
def resources():
    if not session.get('username'):
        return redirect(url_for('sign_in'))
    return render_template("resources.html", auth=session['auth'])


@ app.route('/logout')
def logout():

    session.pop('username', None)
    session.pop('auth', None)
    session.pop('id', None)
    return redirect(url_for('sign_in'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    app.run(debug=True)
