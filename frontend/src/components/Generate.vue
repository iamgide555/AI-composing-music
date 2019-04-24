<template>
    <div>
        Testing Piano <br>
        <button v-on:click="gensong">Click Me for generate song</button> <br>
        <section>
        <div class="block">
            <b-radio v-model="mood"
                native-value="Happy">
                Happy
            </b-radio>
            <b-radio v-model="mood"
                native-value="Sad">
                Sad
            </b-radio>
            <b-radio v-model="mood"
                native-value="Relax">
                Relax
            </b-radio>

        </div>
        <p class="content">
            <b>Selection:</b>
            {{ mood }}
        </p>
    </section>
        {{note.length}} : {{velocity.length}} : {{duration.length}} : {{offset.length}} <br>
        {{predictData}}
        <div id="piano">
            <div id="btns">
                <div id="assistd" class="text" onclick="piano.assist()">Key assist Off</div>
            </div>
            <div id="white">
                <div id="a49d" class="w" v-on:click="pianoclick('a49')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a50d" class="w" v-on:click="pianoclick('a50')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a51d" class="w" v-on:click="pianoclick('a51')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a52d" class="w" v-on:click="pianoclick('a52')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a53d" class="w" v-on:click="pianoclick('a53')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a54d" class="w" v-on:click="pianoclick('a54')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a55d" class="w" v-on:click="pianoclick('a55')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a56d" class="w" v-on:click="pianoclick('a56')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a57d" class="w" v-on:click="pianoclick('a57')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a48d" class="w" v-on:click="pianoclick('a48')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a81d" class="w" v-on:click="pianoclick('a81')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a87d" class="w" v-on:click="pianoclick('a87')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a69d" class="w" v-on:click="pianoclick('a69')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a82d" class="w" v-on:click="pianoclick('a82')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a84d" class="w" v-on:click="pianoclick('a84')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a89d" class="w" v-on:click="pianoclick('a89')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a85d" class="w" v-on:click="pianoclick('a85')" ></div>
                <div id="a73d" class="w" v-on:click="pianoclick('a73')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a79d" class="w" v-on:click="pianoclick('a79')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a80d" class="w" v-on:click="pianoclick('a80')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a65d" class="w" v-on:click="pianoclick('a65')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a83d" class="w" v-on:click="pianoclick('a83')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a68d" class="w" v-on:click="pianoclick('a68')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a70d" class="w" v-on:click="pianoclick('a70')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a71d" class="w" v-on:click="pianoclick('a71')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a72d" class="w" v-on:click="pianoclick('a72')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a74d" class="w" v-on:click="pianoclick('a74')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a75d" class="w" v-on:click="pianoclick('a75')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a76d" class="w" v-on:click="pianoclick('a76')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a90d" class="w" v-on:click="pianoclick('a90')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a88d" class="w" v-on:click="pianoclick('a88')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a67d" class="w" v-on:click="pianoclick('a67')"  style="background-image: linear-gradient(0deg, rgb(0, 0, 0) -20px, rgb(255, 255, 255) 8%);"></div>
                <div id="a86d" class="w" v-on:click="pianoclick('a86')" ></div>
                <div id="a66d" class="w" v-on:click="pianoclick('a66')" ></div>
                <div id="a78d" class="w" v-on:click="pianoclick('a78')" ></div>
                <div id="a77d" class="w" v-on:click="pianoclick('a77')" ></div>
            </div>
            <div id="black">
                <div id="b49d" class="b" v-on:click="pianoclick('b49')"  style="left: 26px;"></div>
                <div id="b50d" class="b" v-on:click="pianoclick('b50')"  style="left: 40px;"></div>
                <div id="b52d" class="b" v-on:click="pianoclick('b52')"  style="left: 88px;"></div>
                <div id="b53d" class="b" v-on:click="pianoclick('b53')"  style="left: 102px;"></div>
                <div id="b54d" class="b" v-on:click="pianoclick('b54')"  style="left: 116px;"></div>
                <div id="b56d" class="b" v-on:click="pianoclick('b56')"  style="left: 164px;"></div>
                <div id="b57d" class="b" v-on:click="pianoclick('b57')"  style="left: 178px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b81d" class="b" v-on:click="pianoclick('b81')"  style="left: 226px;"></div>
                <div id="b87d" class="b" v-on:click="pianoclick('b87')"  style="left: 240px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b69d" class="b" v-on:click="pianoclick('b69')"  style="left: 254px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b84d" class="b" v-on:click="pianoclick('b84')"  style="left: 302px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b89d" class="b" v-on:click="pianoclick('b89')"  style="left: 316px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b73d" class="b" v-on:click="pianoclick('b73')"  style="left: 364px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b79d" class="b" v-on:click="pianoclick('b79')"  style="left: 378px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b80d" class="b" v-on:click="pianoclick('b80')"  style="left: 392px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b83d" class="b" v-on:click="pianoclick('b83')"  style="left: 440px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b68d" class="b" v-on:click="pianoclick('b68')"  style="left: 454px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b71d" class="b" v-on:click="pianoclick('b71')"  style="left: 502px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b72d" class="b" v-on:click="pianoclick('b72')"  style="left: 516px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b74d" class="b" v-on:click="pianoclick('b74')"  style="left: 530px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b76d" class="b" v-on:click="pianoclick('b76')"  style="left: 578px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b90d" class="b" v-on:click="pianoclick('b90')"  style="left: 592px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b67d" class="b" v-on:click="pianoclick('b67')"  style="left: 640px; background-image: linear-gradient(0deg, rgb(200, 200, 200) -10px, rgb(15, 15, 15) 12%);"></div>
                <div id="b86d" class="b" v-on:click="pianoclick('b86')"  style="left: 654px;"></div>
                <div id="b66d" class="b" v-on:click="pianoclick('b66')"  style="left: 668px;"></div>
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
            noteList: {'a49':'C1','a50':'D1','a51':'E1','a53':'F1','a53':'G1','a54':'A1','a55':'B1','a56':'C2','a57':'D2','a48':'E2','a81':'F2','a87':'G2','a69':'A2','a82':'B2','a84':'C3','a89':'D3','a85':'E3','a73':'F3','a79':'G3','a80':'A3','a65':'B3','a83':'C4','a68':'D4','a70':'E4','a71':'F4','a72':'G4','a74':'A4','a75':'B4','a76':'C5','a90':'D5','a88':'E5','a67':'F5','a86':'G5','a66':'A5','a78':'B5','a77':'C6','b49':'C#1','b50':'D#1','b52':'F#1','b53':'G#1','b54':'A#1','b56':'C#2' ,'b57':'D#2','b81':'F#2','b87':'G#2','b69':'A#2','b84':'C#3','b89':'D#3','b73':'F#3','b79':'G#3','b80':'A#3','b83':'C#4','b68':'D#4','b71':'F#4','b72':'G#4','b74':'A#4','b76':'C#5','b90':'D#5','b67':'F#5','b86':'G#5','b66':'A#5'},
            predictData : '',
            note: ['E4', '7.0', 'E4', 'F4', 'G4', 'G4', '7.11', 'F4', 'E4', 'D4', 'C4', '4.7', 'C4', 'D4', 'D3', 'E4', 'C3', 'E4', 'G3', 'D4', 'D4', 'E4', '7.0', 'E4', 'F4', 'G4', 'G4', '7.11', 'F4', 'E4', 'D4', 'C4', '4.7', 'C4', 'D4', 'D3', 'E4', 'C3', 'D4', '5.7', 'C4', '4.7', 'C4', '4.7', 'D4', '7.11', 'D4', 'E4', '7.0', 'C4', 'D4', '7.11', 'E4', 'F4', 'E4', '7.0', 'C4', 'D4', '7.11', 'E4', 'F4', 'E4', 'G#3', 'D4', 'C4', 'A3', 'D4', 'F#3', 'G3', 'G3', 'E4', '7.0', 'E4', 'F4', 'G4', 'G4', '7.11', 'F4', 'E4', 'D4', 'C4', '4.7', 'C4', 'D4', 'D3', 'E4', 'C3', 'D4', '5.7', 'C4', '4.7', 'C4', '4.7'],
            velocity: [121.0, 110.0, 123.0, 115.0, 118.0, 122.0, 116.0, 114.0, 116.0, 115.0, 116.0, 121.0, 121.0, 115.0, 117.0, 121.0, 112.0, 123.0, 116.0, 107.0, 117.0, 121.0, 116.0, 121.0, 114.0, 119.0, 122.0, 116.0, 107.0, 111.0, 117.0, 114.0, 106.0, 118.0, 117.0, 121.0, 117.0, 95.0, 118.0, 110.0, 116.0, 111.0, 124.0, 114.0, 121.0, 108.0, 119.0, 119.0, 113.0, 115.0, 117.0, 115.0, 122.0, 104.0, 119.0, 116.0, 115.0, 115.0, 115.0, 119.0, 112.0, 122.0, 100.0, 116.0, 118.0, 100.0, 109.0, 100.0, 117.0, 116.0, 124.0, 110.0, 124.0, 99.0, 114.0, 115.0, 116.0, 108.0, 114.0, 113.0, 115.0, 106.0, 117.0, 113.0, 121.0, 121.0, 95.0, 122.0, 110.0, 115.0, 111.0, 126.0, 114.0],
            duration: [1.0, 4.0, 1.0, 1.0, 1.0, 1.0, 4.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5, 4.0, 0.5, 2.0, 1.0, 4.0, 1.0, 1.0, 1.0, 1.0, 4.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5, 1.5, 0.5, 0.5, 2.0, 2.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 0.5, 0.5, 1.0, 2.0, 1.0, 1.0, 2.0, 0.5, 0.5, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 4.0, 1.0, 1.0, 1.0, 1.0, 4.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.5, 1.5, 0.5, 0.5, 2.0, 2.0],
            offset: [1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.5, 0.5, 2.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.5, 0.0, 0.5, 0.0, 2.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.5, 0.5, 0.0, 1.0, 1.0, 0.0, 1.0, 0.5, 0.5, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.5, 0.0, 0.5, 0.0],
            mood: ''
        }
    },
    methods: {
        gensong() {
            const path = 'http://localhost:5000/genSong'
            const payload = {
                note: this.note,
                velocity: this.velocity,
                duration: this.duration,
                offset: this.offset,
                mood: this.mood,
            }
            axios.post(path,payload)
                .then((res) =>{
                    console.log(res)
                })
                .catch((error) => {
                    console.log(error)
                })
            console.log("postDone")
            },
        pianoclick(note) {
            
            var sound = new Howl({
                src: ['/static/notes/' +note + '.mp3']
            });
            sound.play()
            console.log(note)
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