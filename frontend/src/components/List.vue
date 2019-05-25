<template>
    <div>
    {{getSong}}
        List Page <br>
        <!-- b-tabs -->
        <b-tabs>
            <b-tab-item label="List">
                <b-table
                    :data="data"
                    :columns="columns"
                     focusable>
                </b-table>
            </b-tab-item>
            <b-tab-item label="My List">
                <b-table
                    :data="yourData"
                    :columns="columns"
                     focusable>
                </b-table>
            </b-tab-item>
        </b-tabs>
        <!-- / b-tabs END -->
        {{data}}
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
