from flask import Flask,redirect,url_for
from flask import render_template,request

'''
It will create an instance of the flask class,
which will be your WSGI(web server gateway interface) application
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this Flask course.This should be an amazing course"

@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')

# @app.route("/form",methods=['GET','POST'])
# def form():
#     if request.method=='POST':
#         name = request.form['name']
#         return f'Hello{name}!'
#     return render_template('form.html')

# @app.route("/submit",methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name = request.form['name']
#         return f'Hello{name}!'
#     return render_template('form.html')


##Variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('results.html',results=res)


@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score':score,'res':res}
    return render_template('result1.html',results=res)


@app.route('/successif/<int:score>')
def successif(score):
    return render_template('results.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('results.html',results=score)

@app.route('/submit',methods =['GET','POST'])
def submit():
    total_score =0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        data_science =float(request.form['datascience'])
    
        total_score=(science+maths+data_science)/3
        return redirect(url_for('successres',score =total_score))
    return render_template('submit.html')





if __name__=="__main__":
    app.run(debug=True)