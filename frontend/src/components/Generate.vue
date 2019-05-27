<template>
    <div id="main">
        {{checkLogin}}
        Testing Piano<br>
        <div class="right">
            <div class="containerOuter">
                <div class="container">
                    <input type="radio" class="hidden" id="input1" name="inputs" v-model="mood" value="Happy">
                    <label class="entry" for="input1"><div class="circle"></div><div class="entry-label">Happy</div></label>
                    <input type="radio" class="hidden" id="input2" name="inputs" v-model="mood" value="Sad">
                    <label class="entry" for="input2"><div class="circle"></div><div class="entry-label" >Sad</div></label>
                    <input type="radio" class="hidden" id="input3" name="inputs" v-model="mood" value="Relax">
                    <label class="entry" for="input3" ><div class="circle"></div><div class="entry-label">Relax</div></label>
                    <div class="highlight"></div>
                    <div class="overlay"></div>
                </div>
                <br>
                <b-field label="Duration (Second)" >
                    <select v-model="songDuration">
                        <option>5</option> sec.
                        <option>10</option> sec.
                        <option>15</option> sec.
                        <option>20</option> sec.
                    </select>
                </b-field>
                <button v-on:click=startrecord>Record</button> <button v-on:click=stoprecord>Stop</button>  <button v-on:click=resetNote>Reset</button> <br>
                <button v-on:click=gensong>Generate Song</button> <br>
                <button v-if="fileName != ''" v-on:click=playSong>Play</button>
                <button v-if="fileName != ''" v-on:click=stopSong>Stop</button>
                <br>
            </div>
        </div>
        <div class="bottom">
            <div id="piano">
                <div id="white">
                    <div id="a49d" class="w" @mousedown="start('a49')" @mouseup="stop('a49')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a50d" class="w" @mousedown="start('a50')" @mouseup="stop('a50')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a51d" class="w" @mousedown="start('a51')" @mouseup="stop('a51')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a52d" class="w" @mousedown="start('a52')" @mouseup="stop('a52')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a53d" class="w" @mousedown="start('a53')" @mouseup="stop('a53')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a54d" class="w" @mousedown="start('a54')" @mouseup="stop('a54')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a55d" class="w" @mousedown="start('a55')" @mouseup="stop('a55')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a56d" class="w" @mousedown="start('a56')" @mouseup="stop('a56')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a57d" class="w" @mousedown="start('a57')" @mouseup="stop('a57')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a48d" class="w" @mousedown="start('a48')" @mouseup="stop('a48')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a81d" class="w" @mousedown="start('a81')" @mouseup="stop('a81')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a87d" class="w" @mousedown="start('a87')" @mouseup="stop('a87')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a69d" class="w" @mousedown="start('a69')" @mouseup="stop('a69')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a82d" class="w" @mousedown="start('a82')" @mouseup="stop('a82')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a84d" class="w" @mousedown="start('a84')" @mouseup="stop('a84')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a89d" class="w" @mousedown="start('a89')" @mouseup="stop('a89')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a85d" class="w" @mousedown="start('a85')" @mouseup="stop('a85')"></div>
                    <div id="a73d" class="w" @mousedown="start('a73')" @mouseup="stop('a73')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a79d" class="w" @mousedown="start('a79')" @mouseup="stop('a79')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a80d" class="w" @mousedown="start('a80')" @mouseup="stop('a80')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a65d" class="w" @mousedown="start('a65')" @mouseup="stop('a65')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a83d" class="w" @mousedown="start('a83')" @mouseup="stop('a83')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a68d" class="w" @mousedown="start('a68')" @mouseup="stop('a68')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a70d" class="w" @mousedown="start('a70')" @mouseup="stop('a70')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a71d" class="w" @mousedown="start('a71')" @mouseup="stop('a71')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a72d" class="w" @mousedown="start('a72')" @mouseup="stop('a72')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a74d" class="w" @mousedown="start('a74')" @mouseup="stop('a74')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a75d" class="w" @mousedown="start('a75')" @mouseup="stop('a75')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                    <div id="a76d" class="w" @mousedown="start('a76')" @mouseup="stop('a76')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                </div>
                <div id="black">
                    <div id="b49d" class="b" @mousedown="start('b49')" @mouseup="stop('b49')" style="left: 26px;"></div>
                    <div id="b50d" class="b" @mousedown="start('b50')" @mouseup="stop('b50')" style="left: 40px;"></div>
                    <div id="b52d" class="b" @mousedown="start('b52')" @mouseup="stop('b52')" style="left: 88px;"></div>
                    <div id="b53d" class="b" @mousedown="start('b53')" @mouseup="stop('b53')" style="left: 102px;"></div>
                    <div id="b54d" class="b" @mousedown="start('b54')" @mouseup="stop('b54')" style="left: 116px;"></div>
                    <div id="b56d" class="b" @mousedown="start('b56')" @mouseup="stop('b56')" style="left: 164px;"></div>
                    <div id="b57d" class="b" @mousedown="start('b57')" @mouseup="stop('b57')" style="left: 178px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                    <div id="b81d" class="b" @mousedown="start('b81')" @mouseup="stop('b81')" style="left: 226px;"></div>
                    <div id="b87d" class="b" @mousedown="start('b87')" @mouseup="stop('b87')" style="left: 240px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                    <div id="b69d" class="b" @mousedown="start('b69')" @mouseup="stop('b69')" style="left: 254px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                    <div id="b84d" class="b" @mousedown="start('b84')" @mouseup="stop('b84')" style="left: 302px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                    <div id="b89d" class="b" @mousedown="start('b89')" @mouseup="stop('b89')" style="left: 316px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                    <div id="b73d" class="b" @mousedown="start('b73')" @mouseup="stop('b73')" style="left: 364px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                    <div id="b79d" class="b" @mousedown="start('b79')" @mouseup="stop('b79')" style="left: 378px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                    <div id="b80d" class="b" @mousedown="start('b80')" @mouseup="stop('b80')" style="left: 392px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                    <div id="b83d" class="b" @mousedown="start('b83')" @mouseup="stop('b83')" style="left: 440px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                    <div id="b68d" class="b" @mousedown="start('b68')" @mouseup="stop('b68')" style="left: 454px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                    <div id="b71d" class="b" @mousedown="start('b71')" @mouseup="stop('b71')" style="left: 502px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                    <div id="b72d" class="b" @mousedown="start('b72')" @mouseup="stop('b72')" style="left: 516px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                    <div id="b74d" class="b" @mousedown="start('b74')" @mouseup="stop('b74')" style="left: 530px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                </div>
            </div>
        </div>
        <b-loading :is-full-page="true" :active.sync="loadingPage" :can-cancel="true"></b-loading>
        {{midiController}} <br> {{notes.length}}:{{velocities.length}}:{{duration.length}}:{{offset.length}} <br>
        Current Note: {{currentNote}}<br>
        Note: {{notes}} <br> Velocity: {{velocities}} <br> Duration: {{duration}} <br> Offset: {{offset}} <br>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
export default {
    data() {
        return {
            loadingPage: false,
            indexNote:0,
            checkRecord: 0,
            chordOrnot: null,
            notes: [],
            velocities: [],
            duration: [],
            offset: [1],
            mood: '',
            songDuration: 5,
            currentNote: [],
            wholeNote: [],
            timeUsed: [],
            startTime: [],
            stopTime: [],
            noteSound: {'a49':'C1','a50':'D1','a51':'E1','a52':'F1','a53':'G1','a54':'A1','a55':'B1','a56':'C2','a57':'D2','a48':'E2','a81':'F2','a87':'G2','a69':'A2','a82':'B2','a84':'C3','a89':'D3','a85':'E3','a73':'F3','a79':'G3','a80':'A3','a65':'B3','a83':'C4','a68':'D4','a70':'E4','a71':'F4','a72':'G4','a74':'A4','a75':'B4','a76':'C5','a90':'D5','a88':'E5','a67':'F5','a86':'G5','a66':'A5','a78':'B5','a77':'C6','b49':'C#1','b50':'D#1','b52':'F#1','b53':'G#1','b54':'A#1','b56':'C#2' ,'b57':'D#2','b81':'F#2','b87':'G#2','b69':'A#2','b84':'C#3','b89':'D#3','b73':'F#3','b79':'G#3','b80':'A#3','b83':'C#4','b68':'D#4','b71':'F#4','b72':'G#4','b74':'A#4','b76':'C#5','b90':'D#5','b67':'F#5','b86':'G#5','b66':'A#5'},
            // Chord: C,Cm,D,Dm,E,Em,F,Fm,G,Gm,A,Am,B,Bm
            chordList: {'0.4.7':['C','E','G'],'0.3.7':['C','D#','G'],'2.6.7':['D','F#','A'],'2.5.7':['D','F','A'],'4.8.11':['E','G#','B'],'4.7.11':['E','G','B'],'5.9':['F','A','C'],'5.8':['F','G#','C'],'7.11.2':['G','B','D'],'7.10.2':['G','A#','D'],'9.1.4':['A','C#','E'],'9.0.4':['A','C','E'],'11.3.6':['B','D#','F#'],'11.2.6':['B','D','F#']},
            noteList : {36: 'C1', 48: 'C2', 60: 'C3', 72: 'C4', 37: 'C#1', 49: 'C#2', 61: 'C#3', 73: 'C#4', 38: 'D1', 50: 'D2', 62: 'D3', 74: 'D4', 39: 'D#1', 51: 'D#2', 63: 'D#3', 75: 'D#4', 40: 'E1', 52: 'E2', 64: 'E3', 76: 'E4', 41: 'F1', 53: 'F2', 65: 'F3', 77: 'F4', 42: 'F#1', 54: 'F#2', 66: 'F#3', 78: 'F#4', 43: 'G1', 55: 'G2', 67: 'G3', 79: 'G4', 44: 'G#1', 56: 'G#2', 68: 'G#3', 80: 'G#4', 45: 'A1', 57: 'A2', 69: 'A3', 81: 'A4', 46: 'A#1', 58: 'A#2', 70: 'A#3', 82: 'A#4', 47: 'B1', 59: 'B2', 71: 'B3', 83: 'B4', 84: 'C5', '0.4.7': '0.4.7', '0.3.7': '0.3.7', '2.6.7': '2.6.7', '2.5.7': '2.5.7', '4.8.11': '4.8.11', '4.7.11': '4.7.11', '5.9':'5.9','5.8':'5.8','7.11.2':'7.11.2','7.10.2':'7.10.2','9.1.4':'9.1.4','9.0.4':'9.0.4','11.3.6':'11.3.6','11.2.6':'11.2.6'},
            // chordList: {['C','E','G']:'0.4.7',['C','D#','G']:'0.3.7',['D','F#','A']:'2.6.7',['D','F','A']:'2.5.7',['E','G#','B']:'4.8.11',['E','G','B']:'4.7.11',['F','A','C']:'5.9',['F','G#','C']:'5.8',['G','B','D']:'7.11.2',['G','A#','D']:'7.10.2',['A','C#','E']:'9.1.4',['A','C','E']:'9.0.4',['B','D#','F#']:'11.3.6',['B','D','F#']:'11.2.6'},
            fileName: '',
        }
    },
    methods: {
        stopSong() {
            const path = 'http://localhost:5000/stopSong'
            axios.post(path)
                .then((res) =>{
                    console.log(res.data)
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        playSong() {
            const path = 'http://localhost:5000/playSong'
            const payload = {
                fileName: this.fileName
            }
            console.log(payload)
            axios.post(path,payload)
                .then((res) =>{
                    console.log(res.data)
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        resetNote() {
            this.wholeNote = []
            this.indexNote = 0
            this.notes = []
            this.velocities = []
            this.duration = []
            this.offset = [1]
            this.startTime = []
            this.stopTime = []
            this.timeUsed = []
            this.fileName = ''
        },
        gensong() {
            const path = 'http://localhost:5000/genSong'
            const payload = {
                note: this.notes,
                velocity: this.velocities,
                duration: this.duration,
                offset: this.offset,
                mood: this.mood,
                user: this.$store.state.user.id_user,
                songDuration: this.songDuration,
            }
            this.loadingPage = true
            axios.post(path,payload)
                .then((res) =>{
                    console.log("Gen Song Done")
                    this.loadingPage = false
                    // this.fileName = res.data
                    var file = res.data.split(" ")
                    file.push(this.duration)
                    this.$store.commit('getFilename',file)
                    // {"ID_song": "2", "username": "lnw", "nameSong": "testOutput2", "mood": "Relax", "path": "../frontend/static/fileSong/testOutput2.mid", "duration": "20"}
                    var songData = {
                        ID_song: file[1],
                        username: this.$store.state.user.username,
                        nameSong: file[2],
                        mood: this.mood,
                        path: this.$store.state.path,
                        duration: this.duration,
                    }
                    this.saveSongData(songData)
                    this.$router.push('/PlaySound')
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        saveSongData(songData) {
            const path = 'http://localhost:5000/addSong'
            axios.post(path,songData)
                .then((res) =>{
                    console.log("Done Add song")
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        startrecord() {
            this.checkRecord = 1
        },
        stoprecord() {
            this.checkRecord = 0
        },
        start(rawNote) {
            this.pianoclick(rawNote)
            if(this.checkRecord == 1){
                var noteto = this.noteSound[rawNote]
                for (var i in this.noteList){
                    if(noteto == this.noteList[i]){
                        noteto = i
                        break;
                    }
                }
                var message = {'data':[144,noteto,60]}
                this.getMIDIMessage(message)
            }
        },
        stop(rawNote) {
            if(this.checkRecord == 1){
                var noteto = this.noteSound[rawNote]
                for (var i in this.noteList){
                    if(noteto == this.noteList[i]){
                        noteto = i
                        break;
                    }
                }
                var message = {'data':[128,noteto,0]}
                this.getMIDIMessage(message)
            }
        },
        noteOn() {
            this.startTimer()
        },
        noteOff(index) {
            this.stopTimer(index)
        },

        startTimer() {
            this.startTime[this.indexNote] = new Date();
        },
        stopTimer(index) {
            this.stopTime[index] = new Date();
            this.timeUsed[index] = (this.stopTime[index] - this.startTime[index])/1000;
        },
        checkChord(currentNote){
            var chordCheck = 0
            var chordFromNote = []
            var noteFromChord = []
            var notee = currentNote.sort()
            var currentIndex = []
            for(var i=0;i<notee.length;i++){
                chordFromNote.push(notee[i].slice(0,-1))
                currentIndex.push(notee[i].slice(-1))
            }
            var a = chordFromNote.sort()
            var map = new Object()
            for(var x in this.chordList){
                if(this.chordList[x].every(val => a.includes(val))){
                    for(var i = 0; i < currentIndex.length; i++) {
                        if(map[currentIndex[i]] != null) {
                            map[currentIndex[i]] += 1;
                        } else {
                            map[currentIndex[i]] = 1;
                            }
                        }
                    for(var y in map){
                        if(map[y] == 3){
                            for(var z in this.chordList[x]){
                                noteFromChord.push(this.chordList[x][z]+y)
                            }
                        }
                    }
                    return [x, noteFromChord]
                }
            }
            return chordCheck
        },
        getMIDIMessage(message) {
            var barCalculate
            var command = message.data[0];
            var note = message.data[1];
            var velocity = (message.data.length > 2) ? message.data[2] : 0; // a velocity value might not be included with a noteOff command
            if(this.mood == "Happy"){
                barCalculate = 117.83/60
            }
            else if(this.mood == "Sad"){
                barCalculate = 97/60
            }
            else if(this.mood == "Relax"){
                barCalculate = 103.375/60
            }
            if(command == 144){
                var keySound = this.playSound(this.noteList[note])
                this.pianoclick(keySound)
                this.currentNote.push(this.noteList[note])
            }
            if(this.currentNote.length >= 3){
                this.chordOrnot = this.checkChord(this.currentNote)
                console.log(this.chordOrnot)
                // var PlayerOne = ['C','E','G','D'];
                // var PlayerTwo = ['C','E','G'];
                // console.log(PlayerTwo.every(val => PlayerOne.includes(val)))
            }
            if(command == 128){
                for( var i = 0; i < this.currentNote.length; i++){ 
                        if ( this.currentNote[i] == this.noteList[note]) {
                            this.currentNote.splice(i, 1); 
                            i--;
                        }
                    }
            }
            if(this.checkRecord == 1){
                switch (command) {
                    case 144: // note on
                        this.wholeNote[this.indexNote] = this.noteList[note]
                        this.notes[this.indexNote] = this.noteList[note]
                        this.velocities[this.indexNote] = velocity
                        this.noteOn()
                        if(this.indexNote > 0){
                            this.offset[this.indexNote] = ((this.startTime[this.indexNote]-this.startTime[this.indexNote-1])/1000)*barCalculate
                        }
                        this.indexNote += 1
                        break;
                    case 128: // note off
                        for(var i=0;i<this.wholeNote.length;i++){
                            if(this.wholeNote[i] == this.noteList[note]){
                                this.noteOff(i)
                                this.wholeNote[i] = "Used"
                                this.duration[i] = (this.timeUsed[i])*barCalculate
                                break;                            
                            }
                        }
                        break;
                    // we could easily expand this switch statement to cover other types of commands such as controllers or sysex
                }
            }
        },
        pianoclick(note) {
            var sound = new Howl({
                src: ['/static/notes/' +note + '.mp3']
            });
            sound.play()
            var check = note.split('')
            if(check[0] == 'a'){
                document.getElementById(note+'d').className = 'w fade_delay'
                setTimeout(function(){
                document.getElementById(note+'d').className = 'w'    
                }, 2000)
            }
            else if(check[0] == 'b'){
                document.getElementById(note+'d').className = 'b fade_delay'
                setTimeout(function(){
                    document.getElementById(note+'d').className = 'b'    
                }, 2000)
            }
        },
        onMIDISuccess(midiAccess) {
            for (var input of midiAccess.inputs.values())
                input.onmidimessage = this.getMIDIMessage;
            var inputs = midiAccess.inputs;
            var outputs = midiAccess.outputs;
        },
        playSound(note) {
            for(var keys in this.noteSound){
                if(note == this.noteSound[keys]){
                    return keys
                }
            }
        },
    },
    computed: {
        checkLogin(){
            if(this.$store.state.user == null){
                this.$router.push('/')
            }
        },
         midiController() {
            navigator.requestMIDIAccess()
                .then(this.onMIDISuccess, this.onMIDIFailure);
         },
     },
}

</script>

<style>
@keyframes fading {
    from {filter: brightness(50%);}
    to {filter: brightness(100%);}
}
html,body {
  background-attachment:fixed;
  background-origin: initial;
  background-repeat:no-repeat;
  min-height: 106%;
  background: -webkit-linear-gradient(#24234D 0%,#241428 100%); 
  font-family: "Open Sans", sans-serif;
}
button {
  background-color: #24234D;
  border: rgb(220, 212, 243) solid 1px;
  padding: 8px 18px;
  margin: 4px 2px;
  color: white;
  border-radius: 5px;
  font-size: bold 12px;
  transition-duration: 0.2s;
  cursor: pointer;
}
button:hover {
  background-color: rgb(220, 212, 243);
  color: rgb(3, 3, 3);
  border: #0f0f0f 1px solid; 
}
#piano {
    z-index: 3;
    margin: 50px auto;
    width: 900px;
    height: 220px;
    position: absolute;
    padding-left: 140px;

}
.w,
.b,
.text,
input[type="button"] {
    cursor: pointer;
}
.text,
#white
 {
    -moz-border-radius: 5px;
    -webkit-border-radius: 5px;
    border-radius: 5px;
}
.text {
    float: left;
    text-align: center;
}
#white {
    z-index: 1;
    padding-left: 10px;
    width: 1006px;
    height: 220px;
    background-image: linear-gradient(#454545 -10px,#000 200px);
}

#black {
    position: relative;
    top: -200px;
    padding-left: 9px;
    width: 900px;
}

.w,
.b {
    float: left;
    text-align: center;
}

.w {
    margin: 4% auto;
    margin-left: 2px;
    width: 32px;
    height: 160px;
    -moz-border-radius: 2px 2px 5px 5px;
    -webkit-border-radius: 2px 2px 5px 5px;
    border-radius: 2px 2px 5px 5px;
    background-image: linear-gradient(0,#000 -20px,#fff 8%);
    color: #000;
    font-weight: 700;
}

.fade_delay{
    animation: fading 2000ms;
}

.b {
    position: relative;
    width: 20px;
    height: 100px;
    -moz-border-radius: 0 0 5px 5px;
    -webkit-border-radius: 0 0 5px 5px;
    border-radius: 0 0 5px 5px;
    background-image: linear-gradient(0,#c8c8c8 -10px,#0f0f0f 12%);
    color: #fff;
}
div.right {
  position: absolute;
  right: 30px;
} 

@import url('https://fonts.googleapis.com/css?family=Open+Sans:600');

.containerOuter {
  background: rgba(251, 250, 255, 0.766) ;
  border-radius: 8px;
  width: 260px;
  box-shadow: 2px 6px 10px 2px rgba(119, 119, 219, 0.15);
  font-size: 18px;
}
.container {
  position: relative;
  margin : 20px;
  overflow: hidden;
  width: 260px;
}
.hidden {
  display: none;
}

.entry {
  height: 25px;
  position: absolute;
  width: 160px;
}

.entry:nth-child(2) {
  left: 10px;
  top: 10px;
}
.entry:nth-child(4) {
  left: 10px;
  top: 60px;
}
.entry:nth-child(6) {
  left: 10px;
  top: 110px;
}
.circle {
  border: 2px solid #545556;
  border-radius: 100%;
  cursor: pointer;
  height: 20px;
  position: absolute;
  transition: border-color 100ms;
  width: 20px;
}
.entry-label {
  cursor: pointer;
  margin-top: -3px;
  padding-left: 40px;
  user-select: none;
  -moz-user-select: none;
}
.overlay {
  height: 140px;
  pointer-events: none;
  transition: background 300ms;
  width: 40px;
}
.highlight {
  background: #4D98EF;
  border-radius: 50%;
  height: 12px;
  left: 14px;
  pointer-events: none;
  position: absolute;
  top: 14px;
  transition: transform 400ms cubic-bezier(0.175, 0.885, 0.32, 1.2);
  transform: translateY(-50px);
  width: 12px;
}
.hidden:nth-child(1):checked ~ .highlight {
  transform: translateY(0);
}
.hidden:nth-child(3):checked ~ .highlight {
  transform: translateY(50px);
}
.hidden:nth-child(5):checked ~ .highlight {
  transform: translateY(100px);
}
.hidden:nth-child(1):checked + .entry .circle {
  border-color: #4D98EF;
}
.hidden:nth-child(3):checked + .entry .circle {
  border-color: #4D98EF;
}
.hidden:nth-child(5):checked + .entry .circle {
  border-color: #4D98EF;
}
div.bottom {
  position: absolute;
  bottom: 300px;
  left: 30px;
} 
#main {
    align-items: center;
    display: flex 1;
}
</style>