<template>
    <div>
        <button v-on:click=playSong>Play</button>
        <button v-on:click=stopSong>Stop</button>
        <div class="holder">
            <div class="audio green-audio-player">
                <div class="loading">
                    <div class="spinner"></div>
                </div>
                <div class="play-pause-btn">
                     <svg xmlns="http://www.w3.org/2000/svg" width="18" height="24" viewBox="0 0 18 24">
                        <path fill="#566574" fill-rule="evenodd" d="M18 12L0 24V0" class="play-pause-icon" id="playPause"/>
                    </svg>
                </div>
                <div class="controls">
                <span class="current-time">0:00</span>
                <div class="slider" data-direction="horizontal">
                    <div class="progress">
                    <div class="pin" id="progress-pin" data-method="rewind"></div>
                    </div>
                </div>
                <span class="total-time">0:00</span>
                </div>

                <div class="volume">
                <div class="volume-btn">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                    <path fill="#566574" fill-rule="evenodd" d="M14.667 0v2.747c3.853 1.146 6.666 4.72 6.666 8.946 0 4.227-2.813 7.787-6.666 8.934v2.76C20 22.173 24 17.4 24 11.693 24 5.987 20 1.213 14.667 0zM18 11.693c0-2.36-1.333-4.386-3.333-5.373v10.707c2-.947 3.333-2.987 3.333-5.334zm-18-4v8h5.333L12 22.36V1.027L5.333 7.693H0z" id="speaker"/>
                    </svg>
                </div>
                <div class="volume-controls hidden">
                    <div class="slider" data-direction="vertical">
                    <div class="progress">
                        <div class="pin" id="volume-pin" data-method="changeVolume"></div>
                    </div>
                    </div>
                </div>
                </div>

                <audio crossorigin>
                <source src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/355309/Swing_Jazz_Drum.mp3" type="audio/mpeg">
                </audio>
            </div>
        </div>
    </div>    
</template>

<script>
/* eslint-disable */
import axios from 'axios';
export default {
    data() {
        return {
            test: 10,
            test2: 20,
            user: this.$store.state.user,
            fileName: this.$store.state.fileName,
            duration: this.$store.state.duration
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
        countDown() {
            console.log("In countdown")
        }
    },
}
</script>
<style>
/* UI: Green Audio Player
A PEN BY Greg Hovanesyan*/

body {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
.holder {
  display: flex;
  flex-direction: column;
  align-items: center;
}
 .audio.green-audio-player {
  width: 400px;
  min-width: 300px;
  height: 56px;
  box-shadow: 0 4px 16px 0 rgba(0, 0, 0, .07);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-left: 24px;
  padding-right: 24px;
  border-radius: 4px;
  user-select: none;
  -webkit-user-select: none;
  background-color: rgb(209, 214, 253);
}
.audio.green-audio-player.play-pause-btn {
    display: none;
    cursor: pointer;
} 
.spinner {
    width: 18px;
    height: 18px;
    background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/355309/loading.png);
    background-size: cover;
    background-repeat: no-repeat;
    animation: spin 0.4s linear infinite;
}
.slider {
    flex-grow: 1;
    background-color: rgb(255, 27, 27);
    cursor: pointer;
    position: relative;
}
.slider.progress {
    background-color: #44BFA3;
    border-radius: inherit;
    position: absolute;
    pointer-events: none;
}
.slider.progress.pin {
    height: 16px;
    width: 16px;
    border-radius: 8px;
    background-color: #44BFA3;
    position: absolute;
    pointer-events: all;
    box-shadow: 0px 1px 1px 0px rgba(0,0,0,0.32);
}
.controls {
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
    line-height: 18px;
    color: #55606E;
    display: flex;
    flex-grow: 1;
    justify-content: space-between;
    align-items: center;
    margin-left: 24px;
    margin-right: 24px;
}
.controls.span{
    cursor: default;
}
.controls.slider {
    margin-left: 16px;
    margin-right: 16px;
    border-radius: 2px;
    height: 4px;
}
.controls.slider.progress {        
    width: 0;
    height: 100%;
}
.controls.slider.progress.pin {
    right: -8px;
    top: -6px;
}
.volume {
    position: relative;
}
.volume-btn {
    cursor: pointer;
}
.volume.open path {
    fill: #44BFA3;
}
.volume-controls {
    width: 30px;
    height: 135px;
    background-color: rgba(0, 0, 0, 0.62);
    border-radius: 7px;
    position: absolute;
    left: -3px;
    bottom: 52px;
    flex-direction: column;
    align-items: center;
    display: flex;
}
.volume-controls.hidden {
    display: none;
}
.volume.slider {
    margin-top: 12px;
    margin-bottom: 12px;
    width: 6px;
    border-radius: 3px;
}
.volumn.slider.progress {
    bottom: 0;
    height: 100%;
    width: 6px;
}
.volume.slider.progress.pin {
    left: -5px;
    top: -8px;
}
@keyframes spin {
  from {transform: rotateZ(0);}
  to {transform: rotateZ(1turn);}
}
svg, img {
  display: inline-block;
}
</style>