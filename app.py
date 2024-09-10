from flask import Flask,render_template,request
import random as r
app=Flask(__name__)

def game(user):
    choices=["R","P","S"]
    computer=r.choice(choices)
    user=request.form['choice']
    str="You won this round!!"
    color="green"
    if computer==user:
        color="blue"
        str="Round was a tie"
    elif computer=="P" and user=="R" or computer=="R" and user=="S" or computer=="S" and user=="P":
        str="Computer won this round!!"
        color="red"
    return str,color

@app.route('/',methods=['GET','POST'])
def homepage():
    if request.method=='POST':
        u_choice=request.form.get('choice')
        str,color=game(u_choice)
        return render_template('result.html',color=color,str=str)
    return render_template("home.html")


if __name__=='__main__':
    app.run(debug=True)
