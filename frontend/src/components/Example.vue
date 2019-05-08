<template>
    <div>
        Happy Song Example : <button @click="playSong('../frontend/static/testOutput/test_output_happy_final_2.mid')">play</button>
        <button v-on:click=stopSong>Stop</button> <br>
        Sad Song Example : <button @click="playSong('../frontend/static/testOutput/test_output_sad_final_2.mid')">play</button>
        <button v-on:click=stopSong>Stop</button> <br>
        Relax Song Example : <button @click="playSong('../frontend/static/testOutput/test_output_relax_final_2.mid')">play</button>
        <button v-on:click=stopSong>Stop</button>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
export default {
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
        playSong(data) {
            const path = 'http://localhost:5000/playSong'
            const payload = {
                fileName: data
            }
            axios.post(path,payload)
                .then((res) =>{
                    console.log(res.data)
                })
                .catch((error) => {
                    console.log(error)
                })
        },
    },
}
</script>