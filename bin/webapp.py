# Mircoframework
# Bottle   .tmp STE
#  Template location needs to update in TEMPLATE_PATH
# in bottle for python code needs to start with
# % stmt1
### FOR BLOCKS
# %for
# %end
# to print a variable
# {{variable}}


# Flask    .html JINJA2
#
# MVT ==> Model View Template
# Django .html OWN
# for bottle and Django needs to put the template in templates folder
# for statements
# {% stmt1 %}
## For blocks we can use as below
# {% for %}
# {% endfor %}
# to print a variable
# {{variable}}

import bottle

app = bottle.Bottle()


@app.error(404)
def errorpage(err):
    return "PAGE UNDER DEVELOPMENT"


@app.route("/")
def indexpage():
    return "Welcome Page"


@app.route("/about")
def aboutpage():
    return "About Page"


@app.route("/login")
def loginpage():
    bottle.TEMPLATE_PATH.append(r'C:\Users\Rajat.Goel1\Desktop\training\bin')
    return bottle.template("login.tpl")


@app.route("/verify", method="POST")
def verifypage():
    u = bottle.request.forms.get("uname")
    p = bottle.request.forms.get("pw")
    if not (u == "abc" and p == "xyz"):
        return bottle.abort(403, "ACCESS Denied")
    else:
        # return "LOGIN  SUCCESS"
        import sqlite3
        con = sqlite3.connect("mydb.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT * from LOGDATA")
        result = cur.fetchall()
        bottle.TEMPLATE_PATH.append(r'C:\Users\Rajat.Goel1\Desktop\training\bin')
        return bottle.template("report.tpl", res=result)


@app.route("/download/<f>")
def downloadpage(f):
    bottle.TEMPLATE_PATH.append(r'C:\Users\Rajat.Goel1\Desktop\training\bin')
    return bottle.static_file(root=r'C:\Users\Rajat.Goel1\Desktop\training\bin', filename=f, download=True)


@app.route("/json")
def jsonpage():
    F = open("data.json", "w")
    import json
    D = {"A": 10, "B": 21}
    json.dump(D, F)
    F.close()
    F = open("data.json")
    E = json.load(F)
    F.close()
    return E


@app.route("/api2", method="GET")
def myapi2():
    D = {"api1": "THIS IS API 1"}
    return D


@app.route("/api3", method="POST")
def myapi3():
    res = bottle.request.params
    res = dict(res)
    return res


app.run(debug=True)
