#Integrate HTML with Flask
'''
{%...%} conditions, for loops
{{...}} expressions to print output
{#...#} comments
'''
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def resform():
    return render_template('index.html')

'''
@app.route('/passed/<int:score>')
def passed(score):
    return render_template('pass.html', score = score)

@app.route('/failed/<int:score>')
def failed(score):
    return render_template('fail.html', score = score)
'''

@app.route('/result/<int:score>')
def result(score):
    res = ""
    if score >= 50:
        res = "pass"
    else:
        res = "fail"
    exp = {'score' : score, 'result' : res}
    return render_template('result.html',result = exp)
    #return render_template('result.html',result = score)

#Result Checker HTML Page
@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        eng = int(request.form['eng'])
        beng = int(request.form['beng'])
        phy = int(request.form['phy'])
        chem = int(request.form['chem'])
        maths = int(request.form['maths'])
        datasc = int(request.form['datasc'])
        total_score = int((eng + beng + phy + chem + maths + datasc) / 6)
    '''
    result = ""
    if total_score >= 50:
        result = "passed"
    else:
        result = "failed"
    return redirect(url_for(result, score = total_score))
    '''
    return redirect(url_for('result',score = total_score))

if __name__ == '__main__':
    app.run(debug = True)