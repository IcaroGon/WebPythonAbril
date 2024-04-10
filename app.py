from flask import Flask,render_template
app = Flask("Ola")

@app.route('/')
def ola():
    return render_template("ola.html")


@app.route('/aluno')
def aluno():
    return "Alunos"