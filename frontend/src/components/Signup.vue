<template>
    <div>
        Signup Page
        <section>
            {{userData}}
            <b-field label="Username">
                <b-input v-model="username" placeholder="Username"></b-input>
            </b-field>
            <b-field label="Password">
                <b-input type="password"
                    placeholder="Password"
                    password-reveal
                    v-model="password">
                </b-input>
            </b-field>
            <b-field label="Email">
                <b-input type="email"
                    placeholder="Email"
                    maxlength="30"
                    v-model="email">
                </b-input>
            </b-field>
        </section>
        <section>
            <a class="button is-danger" v-on:click="resetData">Reset</a>
            <a class="button is-success" v-on:click="addUser">Submit</a>
            <!-- <a class="button is-success" v-on:click="submitData">Submit</a> -->
        </section>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            userData: [],
            username: '',
            password: '',
            email: ''
        }
    },
    methods: {
        resetData() {
            this.username = '';
            this.password = '';
            this.email = '';
        },
        getUser() {
            const path = 'http://localhost:5000/getUser'
            axios.get(path)
            .then((res) =>{
                console.log(res.data)
                this.userData = res.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
        addUser() {
            const path = 'http://localhost:5000/addUser'
            const payload = {
                username: this.username,
                password: this.password,
                email:this.email
            }
            axios.post(path,payload)
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getUser()
    }
}
</script>
