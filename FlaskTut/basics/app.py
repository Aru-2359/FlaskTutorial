from flask import Flask, redirect, url_for

#WSGI Application
app = Flask(__name__)

'''
@app.route('/')
def welcome():
    return 'Hello!Bye!'

@app.route('/anotherurl')
def another():
    return 'Wow!Hello again!'
'''

'''@app.route('/status/<int:score>')
def status(score):
    if score >= 55 :
        return f"Congrats, you have passed! Your score is {score}"
    else:
        return f"Sorry, you did not pass. Your score is {score}"
'''

@app.route('/passed/<int:score>')
def passed(score):
    return f"Congrats, you have passed! Your score is {score}"

@app.route('/failed/<int:score>')
def failed(score):
    return f"Sorry, you have failed! Your score is {score}"

@app.route('/result/<int:marks>')
def results(marks):
    result =""
    if marks >= 55:
        result = 'passed'
    else:
        result = 'failed'
    return redirect(url_for(result,score=marks))

if __name__ == '__main__':
    app.run(debug = True)