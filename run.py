from flask import Flask, redirect, url_for, request, render_template, jsonify
from keras.models import load_model
from keras import backend
import numpy
import json
import random
check = 0

#model
Hmodel = None
Smodel = None
Rmodel = None

#Note data in json file format
happyJson = None
sadJson = None
relaxJson = None

#networkInputdata
Hnetwork = None
Snetwork = None
Rnetwork = None

#Dict for each moods
Hdict = None
Sdict = None
Rdict = None

def loadModel_jsonNote():
    # Init perplexity function
    def perplexity(y_true, y_pred):
        cross_entropy = backend.categorical_crossentropy(y_true, y_pred)
        perplexity = backend.pow(2.0, cross_entropy)
        return perplexity
    #Load Model
    Hmodel = load_model('./Model_moods/Fmodel_happy.h5',custom_objects={'perplexity': perplexity})
    Smodel = load_model('./Model_moods/Fmodel_sad.h5',custom_objects={'perplexity': perplexity})
    Rmodel = load_model('./Model_moods/Fmodel_relax.h5',custom_objects={'perplexity': perplexity})
    
    #Load Note
    with open("NoteData/happyNote.json") as f:
        happyJson = json.load(f)
    f.close()
    with open("NoteData/sadNote.json") as f:
        sadJson = json.load(f)
    f.close()
    with open("NoteData/relaxNote.json") as f:
        relaxJson = json.load(f)
    f.close()

    #Load networkInput
    with open("./networkInput/Hnetwork.txt", 'r') as f:
        data = f.read()
    f.close
    data1 = data.split("|")
    Hnetwork = []
    for x in range(len(data1)-2):
        test = data1[x].split(",")
        z = []
        for y in test:
            z.append(y)
        Hnetwork.append(z)
    with open("./networkInput/Snetwork.txt", 'r') as f:
        data = f.read()
    f.close
    data1 = data.split("|")
    Snetwork = []
    for x in range(len(data1)-2):
        test = data1[x].split(",")
        z = []
        for y in test:
            z.append(y)
        Snetwork.append(z)
    with open("./networkInput/Rnetwork.txt", 'r') as f:
        data = f.read()
    f.close
    data1 = data.split("|")
    Rnetwork = []
    for x in range(len(data1)-2):
        test = data1[x].split(",")
        z = []
        for y in test:
            z.append(y)
        Rnetwork.append(z)
        
    return Hmodel, Smodel, Rmodel, happyJson, sadJson, relaxJson, Hnetwork, Snetwork, Rnetwork

def getNetworkInput(note, mood):

    def getInput(num, network):
        start = numpy.random.randint(0, len(network)-1)
        pattern = network[start]
        new_pattern = []
        print(pattern)
        for x in range(1,len(pattern)):
            new_pattern.append(pattern[x])
        new_pattern.append(num)
        return new_pattern

    firstNote_number = []
    if mood == "Happy":
        for x in range(len(happyJson)):
            if happyJson[x]["note"] == note:
                print(happyJson[x]["note"], " : ",happyJson[x]["num"])
                firstNote_number.append(happyJson[x]["num"])
        randomNote = firstNote_number[random.randint(0,len(firstNote_number))]
        print("Random Number : ",randomNote)
        network_input = getInput(randomNote, Hnetwork)
    elif mood == "Sad":
        for x in range(len(sadJson)):
            if sadJson[x]["note"] == note:
                print(sadJson[x]["note"], " : ",sadJson[x]["num"])
                firstNote_number.append(sadJson[x]["num"])
        network_input = getInput(firstNote_number, Snetwork)
    elif mood == "Relax":
        for x in range(len(relaxJson)):
            if relaxJson[x]["note"] == note:
                print(relaxJson[x]["note"], " : ",relaxJson[x]["num"])
                firstNote_number.append(relaxJson[x]["num"])
        network_input = getInput(firstNote_number, Rnetwork)
    return network_input

def genSong(pattern,mood):
    def generator(model,pattern,jsonData):
        prediction_output = []
        for prediction_index in range (100):
            prediction_input = numpy.reshape(pattern, (1, len(pattern), 1))
            prediction = model.predict(prediction_input, verbose = 0)
            index=numpy.argmax(prediction,axis=1)
            result = my_dict2[index[0]]
            prediction_output.append(result)
            result=numpy.asarray(result)
            print(result)
            print(index)
            pattern = numpy.append(pattern,[index])
            pattern = pattern[1:len(pattern)]
        return prediction_output
    
    if mood == "Happy":
        predictOutput = generator(Hmodel,pattern,happyJson)
    elif mood == "Sad":
        predictOutput = generator(Smodel,pattern,sadJson)
    elif mood == "Relax":
        predictOutput = generator(Rmodel,pattern,relaxJson)
""" app = Flask(__name__)
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
        else:
            mood = request.form['mood']
            network_input = getNetworkInput(firstNote)
            return render_template("check.html",firstNote = firstNote,mood = mood)

    else:
        firstNote = request.args.get('firstNote')
        mood = request.args.get('mood')
        return url_for('check',data = {"FirstNote": firstNote, "Mood": mood})
        
if __name__ == '__main__':
    print("Server running!!")
    Hmodel, Smodel, Rmodel, happyJson, sadJson, relaxJson = loadModel_jsonNote()
    app.run(debug = True) """
Hmodel, Smodel, Rmodel, happyJson, sadJson, relaxJson, Hnetwork, Snetwork, Rnetwork = loadModel_jsonNote()
#pattern = getNetworkInput("A4","Happy")
#print(network_input)
#print(len(network_input))