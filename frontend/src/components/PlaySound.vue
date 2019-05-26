<template>
    <div>
        {{getComment}}
        <div class="container">
            <button class="button-1" v-on:click=playSong>Play</button>
            <button class="button-1" v-on:click=stopSong>Stop</button> 
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
            <section>
                <b-message v-for=" x in comment" v-bind:title="x['username']">
                    {{x['comment']}}
                </b-message>
            </section>
        </div>
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
.container {
    position: relative;
    margin : 20px;
    width: 1200px;
}
.button-1 {
  background-color: rgb(91, 43, 119);
  color: white;
  padding: 10px 20px;
  margin: 15px 5px;
  text-align: center;
  display: inline-block;
  font-size: 16px;
}
.button-1:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}
</style>
