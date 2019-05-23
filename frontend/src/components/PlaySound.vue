<template>
    <div>
        <button v-on:click=playSong>Play</button>
        <button v-on:click=stopSong>Stop</button> <br>
        <progress class="progress is-small" value="80" max="100">15%</progress>
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
            path: this.$store.state.path,
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
            console.log(this.$store.state.user)
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