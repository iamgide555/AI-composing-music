from flask import Flask, redirect, url_for, request, render_template

check = 0

data = {
    "firstNote": None,
    "mood": None
}


app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html",check = check)


@app.route('/genSong',methods = ['POST', 'GET'])
def genSong():
    if request.method == 'POST':
        firstNote = request.form['firstNote']
        if firstNote not in ["A","B","C","D","E","F","G"]:
            check = 1
            return render_template("index.html",check = check)
        mood = request.form['mood']
        return render_template("check.html",firstNote = firstNote,mood = mood)
    else:
        firstNote = request.args.get('firstNote')
        mood = request.args.get('mood')
        return url_for('check',data = {"FirstNote": firstNote, "Mood": mood})
        
if __name__ == '__main__':
    print("Server running!!")
    app.run(debug = True)