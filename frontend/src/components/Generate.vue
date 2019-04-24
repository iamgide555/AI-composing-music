<template>
    <div>
        Testing Piano<br>
        <div id="piano">
            <div id="btns">
                <div id="assistd" class="text" onclick="piano.assist()">Key assist Off</div>
            </div>
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
                <div id="a90d" class="w" @mousedown="start('a90')" @mouseup="stop('a90')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a88d" class="w" @mousedown="start('a88')" @mouseup="stop('a88')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a67d" class="w" @mousedown="start('a67')" @mouseup="stop('a67')" style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a86d" class="w" @mousedown="start('a86')" @mouseup="stop('a86')"></div>
                <div id="a66d" class="w" @mousedown="start('a66')" @mouseup="stop('a66')"></div>
                <div id="a78d" class="w" @mousedown="start('a78')" @mouseup="stop('a78')"></div>
                <div id="a77d" class="w" @mousedown="start('a77')" @mouseup="stop('a77')"></div>
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
                <div id="b76d" class="b" @mousedown="start('b76')" @mouseup="stop('b76')" style="left: 578px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b90d" class="b" @mousedown="start('b90')" @mouseup="stop('b90')" style="left: 592px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b67d" class="b" @mousedown="start('b67')" @mouseup="stop('b67')" style="left: 640px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b86d" class="b" @mousedown="start('b86')" @mouseup="stop('b86')" style="left: 654px;"></div>
                <div id="b66d" class="b" @mousedown="start('b66')" @mouseup="stop('b66')" style="left: 668px;"></div>
            </div>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
require('howler');
import axios from 'axios';
export default {
    data() {
        return {
            startTime: [],
            stopTime: [],
            timeUsed: [],
            checkClick: false,
            noteList: {'a49':'C1','a50':'D1','a51':'E1','a52':'F1','a53':'G1','a54':'A1','a55':'B1','a56':'C2','a57':'D2','a48':'E2','a81':'F2','a87':'G2','a69':'A2','a82':'B2','a84':'C3','a89':'D3','a85':'E3','a73':'F3','a79':'G3','a80':'A3','a65':'B3','a83':'C4','a68':'D4','a70':'E4','a71':'F4','a72':'G4','a74':'A4','a75':'B4','a76':'C5','a90':'D5','a88':'E5','a67':'F5','a86':'G5','a66':'A5','a78':'B5','a77':'C6','b49':'C#1','b50':'D#1','b52':'F#1','b53':'G#1','b54':'A#1','b56':'C#2' ,'b57':'D#2','b81':'F#2','b87':'G#2','b69':'A#2','b84':'C#3','b89':'D#3','b73':'F#3','b79':'G#3','b80':'A#3','b83':'C#4','b68':'D#4','b71':'F#4','b72':'G#4','b74':'A#4','b76':'C#5','b90':'D#5','b67':'F#5','b86':'G#5','b66':'A#5'},
            note: ''
        }
    },
    methods: {
        start(rawNote) {
            this.pianoclick(rawNote)
            this.noteOn(this.noteList[rawNote])
        },
        stop(rawNote) {
            this.noteOff(this.noteList[rawNote])
            console.log("NoteOff")
        },
        noteOn(note) {
            this.startTimer(note)
        },
        noteOff(note,velocity) {
            this.stopTimer(note,velocity)
        },

        startTimer(note) {
            this.startTime[note] = new Date();
        },
        stopTimer(note) {
            this.stopTime[note] = new Date();
            this.timeUsed[note] = (this.stopTime[note] - this.startTime[note])/1000;
            console.log(note," used : ",this.timeUsed[note])
        },
        pianoclick(note) {
            var sound = new Howl({
                src: ['/static/notes/' +note + '.mp3']
            });
            sound.play()
            // console.log(note)
            var check = note.split('')
            this.note = this.noteList[note]
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
        }
    }
}

</script>

<style>
@keyframes fading {
    from {filter: brightness(50%);}
    to {filter: brightness(100%);}
}
body {
  background-image: linear-gradient(#24234D,#241428);
}

#piano {
    z-index: 3;
    margin: 0 auto;
    width: 1236px;
    height: 220px;
}
.w,
.b,
.text,
input[type="button"] {
    cursor: pointer;
}
.text,
#white,
#btns {
    -moz-border-radius: 5px;
    -webkit-border-radius: 5px;
    border-radius: 5px;
}
#btns {
    position: absolute;
    z-index: 4;
    margin: 0 auto;
    margin-top: 3px;
    margin-left: 393px;
    padding-left: 40px;
    width: 450px;
    height: 40px;
    border: 1px solid #303030;
    background-color: #404040;
    font-size: 20px;
}
#assistd {
    width: 164px;
}
.text {
    float: left;
    text-align: center;
}
#white {
    z-index: 1;
    padding-left: 10px;
    width: 1236px;
    height: 220px;
    background-image: linear-gradient(#454545 -10px,#000 200px);
}

#black {
    position: relative;
    top: -210px;
    padding-left: 9px;
    width: 1236px;
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
    animation: fading 1000ms;
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

</style>