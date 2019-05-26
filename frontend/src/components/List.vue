<template>
    <div>
    {{getSong}}
        List Page <br>
        <div class="container">
            <!-- b-tabs -->
            <b-tabs>
                <b-tab-item label="List">
                    <b-table
                        :data="data"
                        :columns="columns"
                        selectable
                        focusable
                        @select="song">
                    </b-table>
                </b-tab-item>
                <b-tab-item label="My List">
                    <b-table
                        :data="yourData"
                        :columns="columns"
                        selectable
                        focusable
                        @select="song">
                    </b-table>
                </b-tab-item>
            </b-tabs>
        <!-- / b-tabs END -->
        </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
export default {
    data() {
        return {
            data:[],
            yourData:[],
            columns: [
                    {
                        field: 'ID_song',
                        label: 'ID',
                        width: '40',
                        numeric: true
                    },
                    {
                        field: 'nameSong',
                        label: 'Song Name',
                    },
                    {
                        field: 'mood',
                        label: 'Mood',
                    },
                    {
                        field: 'username',
                        label: 'BY',
                        width: '100',
                    },
                ]
        }
    },
    methods: {
        song(data) {
            var file = [data['path'],data['ID_song'],data['nameSong'],data['duration']]
            this.$store.commit('getFilename',file)
            this.$router.push('/PlaySound')
        },
    },
    computed: {
        getSong() {
            const path = 'http://localhost:5000/getSong'
            axios.get(path)
                .then((res)=>{
                    this.data = res.data
                    for(var x in this.data){
                        if(this.data[x]['username'] == this.$store.state.user.username){
                            this.yourData.push(this.data[x])
                        }
                    }
                })
                .catch((err)=>{
                    console.log(err)
                })
        }
    },
}
</script>
<style>
html,body {
  background: -webkit-linear-gradient(#24234D 0%,#241428 100%); 
  font-family: "Open Sans", sans-serif;
}
.container {
    position: relative;
    margin : 20px;
    padding-left: 20%;
    width: 1200px;
    cursor: pointer;
}

</style>    