<template>
    <div>
        <button v-on:click=playSong>Play</button>
        <button v-on:click=stopSong>Stop</button>
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
