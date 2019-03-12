from flask import Flask, redirect, url_for, request, render_template, jsonify
from keras.models import load_model
from keras import backend
import tensorflow as tf
import numpy
import json
import random

check = 0

graph = tf.get_default_graph()

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
    # Get Data dict for each mood
    def getDict(dataJson):
        set_of_data = []
        for x in range(len(dataJson)):
            data_for_set = []
            data_for_set.append(dataJson[x]["note"])
            data_for_set.append(dataJson[x]["duration"])
            data_for_set.append(dataJson[x]["offset"])
            data_for_set.append(dataJson[x]["velocity"])
            set_of_data.append(data_for_set)
        list1a = [ tuple(x) for x in set_of_data ]
        dictTest = dict()
        dictTest = dict(enumerate(x for x in list1a))
        data_dict = dict(zip(dictTest.values(), dictTest.keys()))
        my_dict2 = dict((y,x) for x,y in data_dict.items())
        return my_dict2


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
    Hdict = getDict(happyJson)
    f.close()
    with open("NoteData/sadNote.json") as f:
        sadJson = json.load(f)
    Sdict = getDict(sadJson)
    f.close()
    with open("NoteData/relaxNote.json") as f:
        relaxJson = json.load(f)
    Rdict = getDict(relaxJson)
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
        
    return Hmodel, Smodel, Rmodel, happyJson, sadJson, relaxJson, Hnetwork, Snetwork, Rnetwork, Hdict, Sdict, Rdict

def getNetworkInput(note, mood):

    def getInput(num, network):
        start = numpy.random.randint(0, len(network)-1)
        pattern = network[start]
        new_pattern = []
        for x in range(1,len(pattern)):
            new_pattern.append(pattern[x])
        new_pattern.append(num)
        return new_pattern

    firstNote_number = []
    if mood == "Happy":
        for x in range(len(happyJson)):
            if happyJson[x]["note"] == note:
                firstNote_number.append(happyJson[x]["num"])
        print("All number: ",firstNote_number)
        randomNote = firstNote_number[random.randint(0,len(firstNote_number))]
        print("Random: ",randomNote)
        network_input = getInput(randomNote, Hnetwork)
    elif mood == "Sad":
        for x in range(len(sadJson)):
            if sadJson[x]["note"] == note:
                firstNote_number.append(sadJson[x]["num"])
        randomNote = firstNote_number[random.randint(0,len(firstNote_number))]
        network_input = getInput(randomNote, Snetwork)
    elif mood == "Relax":
        for x in range(len(relaxJson)):
            if relaxJson[x]["note"] == note:
                firstNote_number.append(relaxJson[x]["num"])
        randomNote = firstNote_number[random.randint(0,len(firstNote_number))]
        network_input = getInput(randomNote, Rnetwork)
    return network_input, randomNote

def generateSong(firstNote,pattern,mood,my_dict2, firstIndexNote):
    predictOutput = None
    def generator(genPattern):
        if mood == "Happy":
            model1 = Hmodel
        elif mood == "Sad":
            model1 = Smodel
        elif mood == "Relax":
            model1 = Rmodel
        global graph
        with graph.as_default():
            prediction_output = []
            for x in my_dict2.keys():
                if my_dict2[x][0] == firstNote:
                    print("Hi")
                    prediction_output.append(my_dict2[x])
                    break
            print("FirstNote : ",firstNote)
            print("FirstIndex : ",firstIndexNote)
            print("Note : ",prediction_output)
            for prediction_index in range (100):
                prediction_input = numpy.reshape(genPattern, (1, len(genPattern), 1))
                prediction = model1.predict(prediction_input, verbose = 0)
                index=numpy.argmax(prediction,axis=1)
                result = my_dict2[index[0]]
                prediction_output.append(result)
                result=numpy.asarray(result)
                genPattern = numpy.append(genPattern,[index])
                genPattern = genPattern[1:len(genPattern)]
            return prediction_output
    print("Start")
    predictOutput = generator(pattern)
    return predictOutput

#Load everyData
Hmodel, Smodel, Rmodel, happyJson, sadJson, relaxJson, Hnetwork, Snetwork, Rnetwork, Hdict, Sdict, Rdict = loadModel_jsonNote()
print("Server Start!!!!")

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html",check = check)


@app.route('/genSong',methods = ['POST', 'GET'])
def genSong():
    allNote =  ["A1","A2","A3","A4","A5","A6","A7","A8",
                "B1","B2","B3","B4","B5","B6","B7","B8",
                "C1","C2","C3","C4","C5","C6","C7","C8",
                "D1","D2","D3","D4","D5","D6","D7","D8",
                "E1","E2","E3","E4","E5","E6","E7","E8",
                "F1","F2","F3","F4","F5","F6","F7","F8",
                "G1","G2","G3","G4","G5","G6","G7","G8"]
    if request.method == 'POST':
        firstNote = request.form['firstNote']
        if firstNote not in allNote:
            check = 1
            return render_template("index.html",check = check)
        else:
            mood = request.form['mood']
            print(firstNote)
            print(mood)
            if mood == "Happy":
                dataDict = Hdict
            elif mood == "Sad":
                dataDict = Sdict
            elif mood == "Relax":
                dataDict = Rdict
            pattern,firstIndexNote = getNetworkInput(firstNote,mood)
            print("Len dict :",len(dataDict))
            prediction_output = generateSong(firstNote,pattern,mood,dataDict, firstIndexNote)
            return render_template("output.html",checkaa = prediction_output)
            #return render_template("output.html",checkaa = test)
        
if __name__ == '__main__':
    #Hmodel, Smodel, Rmodel, happyJson, sadJson, relaxJson, Hnetwork, Snetwork, Rnetwork, Hdict, Sdict, Rdict = loadModel_jsonNote()
    app.run(debug = True)

# firstNote = "A5"
# mood = "Relax"
# pattern = getNetworkInput(firstNote,mood)
# if mood == "Happy":
#     dataDict = Hdict
# elif mood == "Sad":
#     dataDict = Sdict
# elif mood == "Relax":
#     dataDict = Rdict
# print(len(pattern))
# prediction_output = generateSong(pattern,mood,dataDict)
# print(prediction_output)
#print(network_input)
#print(len(network_input))