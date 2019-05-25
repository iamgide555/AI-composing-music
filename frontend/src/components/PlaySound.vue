<template>
    <div>
        <button v-on:click=playSong>Play</button>
        <button v-on:click=stopSong>Stop</button> <br>
        <progress class="progress is-small" v-bind:value="duration" max="100">15%</progress>
        <b-field label="Comment">
            <b-input maxlength="200" type="textarea" size="is-small"></b-input>
        </b-field>
        <br>
        <b-button type="is-success">Submit</b-button>     <b-button type="is-danger">Reset</b-button>
        <br>
        Comment: {{comment}}

    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
export default {
    data() {
        return {
            user: this.$store.state.user,
            path: this.$store.state.path,
            duration: this.$store.state.duration,
            comment:[],
        }
    },
    methods: {
        getComment() {
            const path = 'http://localhost:5000/getComment'
            axios.get(path)
                .then((res) =>{
                    this.comment = res.data
                })
                .catch((error) => {
                    console.log(error)
                })
        },
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
