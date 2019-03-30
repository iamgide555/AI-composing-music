
<template>
    <div>
        Signup Page
        <section>
            {{userData}}
            <b-field label="Username">
                <b-input v-model="username" placeholder="Username"></b-input>
            </b-field>
            <font color="red" v-if="checkAccount">Same username!</font>
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
/* eslint-disable */
import axios from 'axios';
export default {
    data() {
        return {
            userData: [],
            username: '',
            password: '',
            email: '',
            checkAccount: false,
            status: ''
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
                this.userData = res.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
        addUser() {
            const path = 'http://localhost:5000/addUser'
            var i;
            for(i=0;i<this.userData.length;i++) {
                if(this.username == this.userData[i]["username"]) {
                    this.checkAccount = true;
                }
            }
            if(this.checkAccount == false) {
                const payload = {
                username: this.username,
                password: this.password,
                email:this.email
                }
                axios.post(path,payload)
                .catch((error) => {
                    console.log(error)
                })
                this.$router.push('/login')
            }
            
        }
    },
    created() {
        this.getUser()
    }
}
</script>
