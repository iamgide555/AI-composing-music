from flask import Flask, redirect, url_for, request, render_template, jsonify
from flask_cors import CORS
from keras.models import load_model
from keras import backend
import tensorflow as tf
import math
import numpy
import json
from music21 import *
from music21.midi import *
import random
import os
import pygame

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
    Hmodel = load_model('./Model_moods/model_happy_more_padding_1.h5',custom_objects={'perplexity': perplexity})
    Smodel = load_model('./Model_moods/model_sad_more_padding_1.h5',custom_objects={'perplexity': perplexity})
    Rmodel = load_model('./Model_moods/model_relax_more_padding_1.h5',custom_objects={'perplexity': perplexity})
    
    #Load Note
    with open("./NoteData/happy_dict_morePedding.json") as f:
        happyJson = json.load(f)
    Hdict = getDict(happyJson)
    f.close()
    with open("./NoteData/sad_dict_morePedding.json") as f:
        sadJson = json.load(f)
    Sdict = getDict(sadJson)
    f.close()
    with open("./NoteData/relax_dict_morePedding.json") as f:
        relaxJson = json.load(f)
    Rdict = getDict(relaxJson)
    f.close()

    # #Load networkInput
    # with open("./networkInput/Hnetwork.txt", 'r') as f:
    #     data = f.read()
    # f.close
    # data1 = data.split("|")
    # Hnetwork = []
    # for x in range(len(data1)-2):
    #     test = data1[x].split(",")
    #     z = []
    #     for y in test:
    #         z.append(y)
    #     Hnetwork.append(z)
    # with open("./networkInput/Snetwork.txt", 'r') as f:
    #     data = f.read()
    # f.close
    # data1 = data.split("|")
    # Snetwork = []
    # for x in range(len(data1)-2):
    #     test = data1[x].split(",")
    #     z = []
    #     for y in test:
    #         z.append(y)
    #     Snetwork.append(z)
    # with open("./networkInput/Rnetwork.txt", 'r') as f:
    #     data = f.read()
    # f.close
    # data1 = data.split("|")
    # Rnetwork = []
    # for x in range(len(data1)-2):
    #     test = data1[x].split(",")
    #     z = []
    #     for y in test:
    #         z.append(y)
    #     Rnetwork.append(z)
        
    return Hmodel, Smodel, Rmodel, Hdict, Sdict, Rdict

def generateSong(pattern,mood,my_dict2,sDuration):
    predictOutput = None
    def generator(genPattern,mood,my_dict2,duration):
        totalDuration = 0
        if(mood == "Happy"):
            barCalculate = 60/117.83
        elif(mood == "Sad"):
            barCalculate = 60/97
        elif(mood == "Relax"):
            barCalculate = 60/103.375
        if mood == "Happy":
            model1 = Hmodel
        elif mood == "Sad":
            model1 = Smodel
        elif mood == "Relax":
            model1 = Rmodel
        global graph
        with graph.as_default():
            prediction_output = []
            for x in genPattern:
                prediction_output.append(my_dict2[x])
            if(len(genPattern) < 50):
                newPattern = genPattern
                genPattern = []
                for y in range(50-len(newPattern)):
                    genPattern.append(0)
                for y in newPattern:
                    genPattern.append(y)
            elif(len(genPattern) > 50):
                genPattern = genPattern[len(genPattern)-50:]
            while(totalDuration < float(duration)):
                prediction_input = numpy.reshape(genPattern, (1, len(genPattern), 1))
                prediction = model1.predict(prediction_input, verbose = 0)
                index=numpy.argmax(prediction,axis=1)
                print(index[0])
                result = my_dict2[index[0]]
                totalDuration = totalDuration + (float(result[2])*barCalculate)
                print("+",float(result[2])*barCalculate)
                print("TotalDuration :",totalDuration)
                prediction_output.append(result)
                result=numpy.asarray(result)
                genPattern = numpy.append(genPattern,[index])
                genPattern = genPattern[1:len(genPattern)]
            return prediction_output
    print("Start")
    predictOutput = generator(pattern,mood,my_dict2,sDuration)
    print("Done")
    return predictOutput

def preData(rawData):
    def round_of_rating(number):
        return round(number * 4) / 4

    def round_of_rating_two(number):
        return round(number * 2) / 2

    def round_of_rating_three(number):
        return int(math.ceil(number / 16))* 16

    def getDictData(notes,duration,offset,velocities,dataNote,dataDuration,dataOffset,dataVelocity):
        predData = []
        yoyo = 0
        for x in range(len(notes)):
            listCheck = []
            checkD = {}
            checkO = {}
            checkV = {}
            for y in range(len(dataNote)):
                if(notes[x] == dataNote[y]):
                    if(str(duration[x]) == dataDuration[y]):
                        if(str(offset[x]) == dataOffset[y]):
                            if(str(velocities[x]) == dataVelocity[y]):
                                predData.append(y)
                                checkD = {}
                                checkO = {}
                                checkV = {}
                                break;
                            else:
                                listCheck.append("V")
                                checkV[dataVelocity[y]] = y
                        else:
                            listCheck.append("O")
                            checkO[dataOffset[y]] = y
                    else:
                        listCheck.append("D")
                        checkD[dataDuration[y]] = y
            if("V" in listCheck):
                yoyo += 1
                if(len(checkV) == 1):
                    listKey = list(checkV.values())
                    predData.append(listKey[0])
                elif(len(checkV) > 1):
                    nearestVelocity = []
                    checkVelocity = 200
                    for z in checkV:
                        if(abs(float(velocities[x]) - float(z)) < float(checkVelocity)):
                            nearestVelocity = []
                            nearestVelocity.append(z)
                            checkVelocity = abs(float(velocities[x]) - float(z))
                        elif(abs(float(velocities[x]) - float(z)) == float(checkVelocity)):
                            nearestVelocity.append(z)
                    predData.append(checkV[nearestVelocity[0]])
            elif("O" in listCheck):
                yoyo += 1
                if(len(checkO) == 1):
                    listKey = list(checkO.values())
                    predData.append(listKey[0])
                elif(len(checkO) > 1):
                    nearestOffset = []
                    checkOffset = 200
                    for z in checkO:
                        if(abs(float(offset[x]) - float(z)) < float(checkOffset)):
                            nearestOffset = []
                            nearestOffset.append(z)
                            checkOffset = abs(float(offset[x]) - float(z))
                        elif(abs(float(offset[x]) - float(z)) == float(checkOffset)):
                            nearestOffset.append(z)
                    predData.append(checkO[nearestOffset[0]])
            elif("D" in listCheck):
                yoyo += 1
                if(len(checkD) == 1):
                    listKey = list(checkD.values())
                    print(listKey[0])
                    predData.append(listKey[0])
                elif(len(checkD) > 1):
                    nearestDuration = []
                    checkDuration = 200
                    for z in checkD:
                        if(abs(float(duration[x]) - float(z)) < float(checkDuration)):
                            nearestDuration = []
                            nearestDuration.append(z)
                            checkDuration = abs(float(duration[x]) - float(z))
                        elif(abs(float(duration[x]) - float(z)) == float(checkDuration)):
                            nearestDuration.append(z)
                    predData.append(checkD[nearestDuration[0]])
        print(yoyo," : ",len(predData))
            # if(len(checkV) == 1):
            #     listKey = list(checkV.values())
            #     predData.append(listKey[0][0])
            # elif(len(checkV) > 1):
            #     nearestVelocity = []
            #     checkVelocity = 200
            #     for z in checkV:
            #         if(abs(float(velocities[x]) - float(z)) < float(checkVelocity)):
            #             nearestVelocity = []
            #             nearestVelocity.append(z)
            #             checkVelocity = abs(float(velocities[x]) - float(z))
            #         elif(abs(float(velocities[x]) - float(z)) == float(checkVelocity)):
            #             nearestVelocity.append(z)
            #     predData.append(checkV[nearestVelocity[0]])
        return predData

    predData = []
    notes = rawData["note"]
    duration = rawData["duration"]
    offset = rawData["offset"]
    velocities = rawData["velocity"]
    mood = rawData["mood"]
    for x in range (len(duration)):
        if duration [x] != -1:        
            if duration[x] > 5:
                duration[x] = round_of_rating_two(duration[x])
            else:
                duration[x] = round_of_rating(duration[x]) 
            offset[x] = round_of_rating(offset[x])
            velocities[x] = round_of_rating_three(velocities[x])
            if velocities[x] > 128:
                velocities[x] = 128
    if(mood == "Happy"):
        my_dict2 = Hdict
    elif(mood == "Sad"):
        my_dict2 = Sdict
    elif(mood == "Relax"):
        my_dict2 = Rdict
    data = my_dict2.values()
    dataNote = []
    dataDuration = []
    dataOffset = []
    dataVelocity = []
    for x in list(data):
        dataNote.append(x[0])
        dataDuration.append(x[1])
        dataOffset.append(x[2])
        dataVelocity.append(x[3])
    predData = getDictData(notes,duration,offset,velocities,dataNote,dataDuration,dataOffset,dataVelocity)
    for x in range(len(predData)):
        print(notes[x],",",duration[x],",",offset[x],",",velocities[x]," --> ",my_dict2[predData[x]])
    return predData,my_dict2,mood
    
def getMidi(prediction_output):
    prediction_output = numpy.asarray(prediction_output)
    predict_note = []
    predict_duration = []
    predict_offset = []
    predict_velo = []
    for x in prediction_output:
        predict_note.append(x[0])
        predict_duration.append(x[1])
        predict_offset.append(x[2])
        predict_velo.append(x[3])
    for x in range(len(predict_duration)):
        predict_duration[x] = float(predict_duration[x])
    for x in range(len(predict_velo)):
        predict_velo[x] = float(predict_velo[x])
    for x in range(len(predict_offset)):
        predict_offset[x] = float(predict_offset[x])
    offset = 0
    output_notes = []
    for x in range(len(predict_note)):
        if ('.' in predict_note[x]) or predict_note[x].isdigit():
            notes_in_chord = predict_note[x].split('.')
            notes = []
            for current_note in notes_in_chord:
                new_note = note.Note(int(current_note))
                new_note.storedInstrument = instrument.Piano()
                new_note.duration.quarterLength = predict_duration[x]
                new_note.volume.velocity = predict_velo[x]
                notes.append(new_note)
            new_chord = chord.Chord(notes)
            new_chord.offset = offset
            output_notes.append(new_chord)
        else:
            new_note = note.Note(predict_note[x])
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            new_note.duration.quarterLength = predict_duration[x]
            new_note.volume.velocity = predict_velo[x]
            output_notes.append(new_note)
        offset += predict_offset[x]
        midi_stream = stream.Stream(output_notes)
    path, dirs, files = next(os.walk('../frontend/static/fileSong'))
    file_count = len(files)
    print(file_count)
    path = '../frontend/static/fileSong/testOutput'+ str(file_count) + '.mid'
    midi_stream.write('midi', fp=path)
    return path,str(file_count),"testOutput"+ str(file_count)
        
# Load everyData
Hmodel, Smodel, Rmodel, Hdict, Sdict, Rdict = loadModel_jsonNote()
print("Server Start!!")

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


@app.route('/')
def index():
    return render_template("index.html",check = check)

@app.route('/getUser', methods = ['GET'])
def getUser():
    with open('./data/user.json') as json_file:  
        data = json.load(json_file)
    return jsonify(data)

@app.route('/addUser', methods = ['POST'])
def addUser():
    if request.method == 'POST':
        post_data = request.get_json()
        with open('./data/user.json') as json_file:  
            data = json.load(json_file)
        json_file.close()
        pushdata = {
            "id_user": len(data)+1,
            "username": post_data['username'],
            "password": post_data['password'],
            "email": post_data['email']
        }
        data.append(pushdata)
        with open('./data/user.json', 'w') as outfile:  
            json.dump(data, outfile)
        outfile.close()
        return "Add Done"

@app.route('/genSong',methods = ['POST', 'GET'])
def genSong():
    usedData = []
    predictOutput = []
    finalPredictData = []
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        print(len(post_data))
        for x in range(len(post_data['note'])):
            print((post_data["note"][x],post_data["duration"][x],post_data["offset"][x],post_data["velocity"][x]))
            finalPredictData.append((post_data["note"][x],post_data["duration"][x],post_data["offset"][x],post_data["velocity"][x]))
        usedData,my_dict2, mood = preData(post_data)
        predictOutput = generateSong(usedData,mood,my_dict2,post_data["songDuration"])
        for x in predictOutput:
            finalPredictData.append(x)
        print(finalPredictData)
        filePath,file_id,fileName = getMidi(predictOutput)
        # filePath = "Hi"
        for x in predictOutput:
            print(x)
        returnData = filePath + " " + file_id + " " + fileName
        return str(returnData)
    if request.method == 'GET':
        print(predictOutput)
        data = {"data": predictOutput}
        return jsonify(data)

@app.route('/playSong',methods = ['POST','GET'])
def playSong():
    post_data = request.get_json()
    print(post_data)
    pygame.mixer.init()
    pygame.mixer.music.load(post_data['fileName'])
    pygame.mixer.music.play()
    return "play song"

@app.route('/stopSong',methods = ['POST','GET'])
def stopSong():
    post_data = request.get_json()
    pygame.mixer.music.stop()
    return "stop"

@app.route('/addSong', methods = ['POST','GET'])
def addSong():
    if request.method == 'POST':
        post_data = request.get_json()
        with open('./data/song.json') as json_file:  
            data = json.load(json_file)
        json_file.close()
        data.append(post_data)
        with open('./data/song.json', 'w') as outfile:  
            json.dump(data, outfile)
        outfile.close()
        return "Done"

if __name__ == '__main__':
    app.run()





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