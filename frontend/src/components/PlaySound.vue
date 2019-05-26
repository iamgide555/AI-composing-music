<template>
    <div>
        {{getComment}}
        <button v-on:click=playSong>Play</button>
        <button v-on:click=stopSong>Stop</button> <br>
        <progress class="progress is-small" v-bind:value="check" v-bind:max="duration"></progress>
        <b-field label="Comment">
            <b-input maxlength="200" type="textarea" size="is-small" v-model="message"></b-input>
        </b-field>
        <br>
        <section>
            <a class="button is-success" v-on:click="submit">Submit</a>
            <a class="button is-danger" v-on:click="reset">Reset</a>
        </section>
        <br>
        {{check}}
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
            check: 0,
            comment: [],
            message:'',
            polling:null,
        }
    },
    methods: {
        pollData () {
            this.check = 0
            this.polling = setInterval(() => {
                if(this.check == this.duration){
                    return "done"
                }
                this.check = this.check + 1
                console.log(this.check)
            }, 1000)
            console.log(this.polling)
        },
        reset() {
            this.message = []
        },
        submit() {
            const path = 'http://localhost:5000/addComment'
            const payload = {
                songName:this.$store.state.file_name,
                data:[{
                    username: this.$store.state.user.username,
                    comment: this.message
                }]
            }
            console.log(payload) 
            axios.post(path,payload)
                .then((res)=>{
                    console.log("Comment submitted")
                    this.getComment()
                })
                .catch((error)=>{
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
                fileName: this.path
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
            this.pollData()
        },
    },
    computed: {
        getComment() {
            console.log("YoYo")
            const path = 'http://localhost:5000/getComment'
            axios.get(path)
                .then((res) =>{
                    for(var x in res.data){
                        if(res.data[x]['songName'] == this.$store.state.file_name){
                            this.comment = res.data[x]['data']
                        }
                    }
                })
                .catch((error) => {
                    console.log(error)
                })
        }
    }
}
</script>
<style>
.button1 {
  border: 0;
  background: transparent;
  box-sizing: border-box;
  width: 0;
  height: 74px;
  border-color: transparent transparent transparent #202020;
  transition: 100ms all ease;
  cursor: pointer;
  border-style: solid;
  border-width: 37px 0 37px 60px;
}
.button.paused {
  border-style: double;
  border-width: 0px 0 0px 60px;
}
.button:hover {
  border-color: transparent transparent transparent #404040;
}

</style>
