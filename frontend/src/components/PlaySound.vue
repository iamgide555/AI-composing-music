<template>
    <div>
        <button v-on:click="check">Yo</button>
        User: {{user}} <br>
        File Name: {{fileName}} <br>
        Duration of the song: {{duration}}
    </div>
</template>

<script>
/* eslint-disable */
export default {
    data() {
        return {
            test: 10,
            test2: 20,
            user: '',
            fileName: '',
            duration: ''
        }
    },
    methods: {
        check() {
            this.user = this.$store.state.user
            this.fileName = this.$store.state.fileName
            this.duration = this.$store.state.duration
            console.log(this.fileName,this.duration)
        },
        countDown() {
            console.log("In countdown")
        }
    },
}
</script>
