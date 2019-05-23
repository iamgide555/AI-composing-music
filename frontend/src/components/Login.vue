<template>
    <div>
        Login page
        <section class="column is-half is-offset-one-quarter">
            {{userData}}
            <b-field label="Username" v-bind:type="invalidUsername ? '' : 'is-danger'" v-bind:message="invalidUsername? '' : 'Invalid username'">
                <b-input v-model="username" placeholder="Username" maxlength="30"></b-input>
            </b-field>
            <b-field
                for="password"
                label="Password"
                v-bind:type="wrongPassword ? '' : 'is-warning'"
                v-bind:message="wrongPassword ? '' : 'Wrong password'"
                >
                <b-input
                    placeholder="Password"
                    type="password"
                    vname="password"
                    v-model="password"
                    password-reveal
                >
                </b-input>
            </b-field>
            <br>
            <button
            class="button is-primary is-outlined is-focused"
            v-on:click="login"
            >
                Login
            </button>
            <br>
                <br> Don't have an account?
            <br>
            <router-link to="signup">
                <br>
                <button class="button is-black is-outlined is-focused is-small">
                    Create Account
                </button>
            </router-link>
        </section>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';
export default {
    name: 'Login',
    data() {
        return {
            userData: [],
            username: '',
            password: '',
            member: '',
            invalidUsername: true,
            wrongPassword: true
        }
    },
    methods:{
        getUser() {
            const path = 'http://localhost:5000/getUser'
            axios.get(path)
            .then((res) =>{
                this.userData = res.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
        login() {
            this.invalidUsername = true;
            this.wrongPassword = true;
            var i;
            var checkU = 0;
            var checkP = 0;
            for(i=0;i<this.userData.length;i++) {
                if(this.username == this.userData[i]["username"]) {
                    if(this.password == this.userData[i]["password"]){
                        this.$store.commit('login', this.userData[i])
                        this.$router.push('/')
                    }
                    else{
                        this.invalidUsername = true;
                        this.wrongPassword = false;
                        break;
                    }
                }
                else{
                    checkU = 1
                }
            }
            if(checkU == 1){
                this.invalidUsername = false;
            }
        }
    },
    created() {
        this.getUser()
    }
}
</script>

