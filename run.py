from flask import Flask, redirect, url_for, request, render_template
from keras.models import load_model
from keras import backend
check = 0

data = {
    "firstNote": None,
    "mood": None
}

# Init perplexity function
def perplexity(y_true, y_pred):
    cross_entropy = backend.categorical_crossentropy(y_true, y_pred)
    perplexity = backend.pow(2.0, cross_entropy)
    return perplexity

def loadModel():
    Hmodel = load_model('Fmodel_happy.h5',custom_objects={'perplexity': perplexity})
    Smodel = load_model('Fmodel_sad.h5',custom_objects={'perplexity': perplexity})
    Rmodel = load_model('Fmodel_relax.h5',custom_objects={'perplexity': perplexity})


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
    loadModel()
    app.run(debug = True)