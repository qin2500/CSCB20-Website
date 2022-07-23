function outputHeader(title, auth) {
    if (auth == 0) {
        //Student Access
        document.write('\
        <head>\
            <link rel="stylesheet" href="static/css/header.css" />\
        </head>\
        <div id = "popnav1" class= "popnav" >\
        <div id="popnav1links" class="links">\
            <a class="exit" href="#">&times;</a>\
            <a href="\\">Home</a>\
            <a href="\\calendar">Calendar</a>\
            <a href="\\announcements">Announcements</a>\
            <a href="https://piazza.com/class/kxj5alixpjg4ft" target="blank">Piazza</a>\
            <a href="\\lectures">Lectures</a>\
            <a href="\\labs">Labs</a>\
            <a href="\\assignments">Assignments</a>\
            <a href="\\tests">Tests</a>\
            <a href="\\resources">Resources</a>\
            <a href="\\about">About</a>\
            <a href="/my_grades">My Grades</a>\
            <a href="/giveFeedback">Anonymous FeedBack</a>\
            <a href="/logout">Logout    </a>\
            <br>\
        </div>\
    </div >\
\
\
        <div id="topnav1" class="topnav">\
\
            <txt><a class="mobile" href="#popnav1">&#9776;</a>CSCB20 - '+ title + '</txt>\
            \
            <div class="dropdown">\
                <button class="signIn">Special</button>\
                    <div class="dropdown-content">\
                        <a href="/my_grades">My Grades</a>\
                        <a href="/giveFeedback">Anonymous FeedBack</a>\
                        <a href="/logout">Logout    </a>\
                    </div>\
            </div>\
            \
            <div id="topnav1links" class="links">\
                <a href="\\">Home</a>\
                <a href="\\calendar">Calendar</a>\
                <a href="\\announcements">Announcements</a>\
                <a href="https://piazza.com/class/kxj5alixpjg4ft" target="blank">Piazza</a>\
                <a href="\\lectures">Lectures</a>\
                <a href="\\labs">Labs</a>\
                <a href="\\assignments">Assignments</a>\
                <a href="\\tests">Tests</a>\
                <a href="\\resources">Resources</a>\
                <a href="\\about">About</a>\
            </div>\
        </div>\
        ');
    }
    else if (auth == 1) {
        //instructor access
        document.write('\
        <head>\
            <link rel="stylesheet" href="static/css/header.css" />\
        </head>\
        <div id = "popnav1" class= "popnav" >\
        <div id="popnav1links" class="links">\
            <a class="exit" href="#">&times;</a>\
            <a href="\\">Home</a>\
            <a href="\\calendar">Calendar</a>\
            <a href="\\announcements">Announcements</a>\
            <a href="https://piazza.com/class/kxj5alixpjg4ft" target="blank">Piazza</a>\
            <a href="\\lectures">Lectures</a>\
            <a href="\\labs">Labs</a>\
            <a href="\\assignments">Assignments</a>\
            <a href="\\tests">Tests</a>\
            <a href="\\resources">Resources</a>\
            <a href="\\about">About</a>\
            <a href="/my_grades">My Grades</a>\
            <a href="/giveFeedback">Anonymous FeedBack</a>\
            <a href="/logout">Logout    </a>\
            <br>\
        </div>\
    </div >\
\
\
        <div id="topnav1" class="topnav">\
\
            <txt><a class="mobile" href="#popnav1">&#9776;</a>CSCB20 - '+ title + '</txt>\
            \
            <div class="dropdown">\
                <button class="signIn">Special</button>\
                    <div class="dropdown-content">\
                        <a href="/editGrades">Edit Grades</a>\
                        <a href="/viewFeedback">View FeedBack</a>\
                        <a href="/viewRegrade">View Regrade</a>\
                        <a href="/logout">Logout</a>\
                    </div>\
            </div>\
            \
            <div id="topnav1links" class="links">\
                <a href="\\">Home</a>\
                <a href="\\calendar">Calendar</a>\
                <a href="\\announcements">Announcements</a>\
                <a href="https://piazza.com/class/kxj5alixpjg4ft" target="blank">Piazza</a>\
                <a href="\\lectures">Lectures</a>\
                <a href="\\labs">Labs</a>\
                <a href="\\assignments">Assignments</a>\
                <a href="\\tests">Tests</a>\
                <a href="\\resources">Resources</a>\
                <a href="\\about">About</a>\
            </div>\
        </div>\
        ');
    }
    else {
        document.write('\
        <head>\
            <link rel="stylesheet" href="static/css/header.css" />\
        </head>\
        <div id = "popnav1" class= "popnav" >\
        <div id="popnav1links" class="links">\
\           <a class="exit" href="#">&times;</a>\
        </div>\
    </div >\
\
\
        <div id="topnav1" class="topnav">\
\
            <txt><a class="mobile" href="#popnav1">&#9776;</a>CSCB20 - '+ title + '</txt>\
            \
            <div class="dropdown">\
            <button class="signIn"><a href="/sign_in">Sign In</a></button>\
\
            </div>\
            \
            <div id="topnav1links" class="links">\
\
            </div>\
        </div>\
        ');
    }

}