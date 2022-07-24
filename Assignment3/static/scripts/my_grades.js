var name = '{{user.name}}'
var tut_att = '{{user.tutorial_attendance_grade}}'
var a1_gr = '{{user.a1_grade}}'
var a2_gr = '{{user.a2_grade}}'
var a3_gr = '{{user.a3_grade}}'
var midt_gr = '{{user.midterm_grade}}'
var finex_gr = '{{user.final_exam_grade}}'
var fin_gr = '{{user.final_grade}}'
console.log('{{user}}')


function output_grades(username, first_name, tut_att, a1_gr, a2_gr, a3_gr, midt_gr, finex_gr, fin_gr) {

  //console.log(user);
  console.log("oh no");
  document.write('\
  <head>\
  <link rel="stylesheet" href="static/css/my_grades.css">\
  </head>\
  <div class="container">\
  {% block content %}\
            {% with messages = get_flashed_messages() %}\
            {% if messages %}\
            {% for msg in messages %}\
            <h1 class="error">{{msg}}</h1>\
            {% endfor %}\
            {% endif %}\
            {% endwith %}\
            {% endblock %}\
    <h1>Grades for '+ first_name + '</h>\
    <table>\
        <tr>\
          <th>Item</th>\
          <th>Grade</th>\
        </tr>\
        <tr>\
          <td>Tutorial Attendance</td>\
          <td>'+ tut_att + '</td>\
        </tr>\
        <tr>\
          <td>Assignment 1</td>\
          <td>'+ a1_gr + '</td>\
        </tr>\
        <tr>\
          <td>Assignment 2</td>\
          <td>'+ a2_gr + '</td>\
        </tr>\
        <tr>\
          <td>Assignment 3</td>\
          <td>'+ a3_gr + '</td>\
        </tr>\
        <tr>\
          <td>Midterm</td>\
          <td>'+ midt_gr + '</td>\
        </tr>\
        <tr>\
          <td>Final Exam</td>\
          <td>'+ finex_gr + '</td>\
        </tr>\
        <tr>\
          <td>Final</td>\
          <td>'+ fin_gr + '</td>\
        </tr>\
    </table>\
  </div>\
  <br>\
          ');
}