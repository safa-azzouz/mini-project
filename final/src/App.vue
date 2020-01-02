<!--<template>
  <div id="app">
    <img src="./assets/play.jpg">-->
    <!--<h1>{{ msg }}</h1>
    <input type="button" value="log in" onclick="window.location.href='http://127.0.0.1:8000/admin/'" />7
    <input type="button" value="Play" onclick=""/>
    <input type="button" value="register" onclick="window.location.href='http://127.0.0.1:8000/admin/auth/user/add/'" />-->
    <!--<h2>Essential Links</h2>
    <ul>
      <li><a href="https://vuejs.org" target="_blank">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank">Forum</a></li>
      <li><a href="https://chat.vuejs.org" target="_blank">Community Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank">Twitter</a></li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li><a href="http://router.vuejs.org/" target="_blank">vue-router</a></li>
      <li><a href="http://vuex.vuejs.org/" target="_blank">vuex</a></li>
      <li><a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
    </ul>
  </div>
</template>
-->
<!--<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Are you ready to guess ?!'
    }
  }
}
</script>-->
<template>
<div id="app">
 <div class="body"></div>
		<div class="grad"></div>
		<div class="header"><div>proj<span>Batvoice</span></div>
		</div>
       <form @submit="onSubmit" action="http://127.0.0.1:8000/api/submissions/submissions/" method="post" novalidate="true">
          <b>Please correct the following error(s):</b>
            <ul>
              <li v-for="error in errors">{{ error }}</li>
            </ul>
		<br>
		<div class="login">
      <button  class="button" @click.prevent="playSound()" >listen</button>
      <br><br>
				<input type ="text" id="msg" name="message" v-model="model.text" placeholder ="speech uttered"><br>
      <button class="button" >Submit</button>
		</div>

        </form>
    <br><br>

  </div>
</template>

<script>
import *as  axios from "axios";

var x=Math.random()*6;
var set = ["(", ")", "'", "a", "A", "-", "à", "À", "?", "â", "Â", ",", "b", "B", ".", "c", "C", ";", "ç", "Ç", ":", "d", "D", "!", "e", "E", "é", "É", "è", "È", "ê", "Ê", "ë", "f", "F", "g", "G", "h", "H", "i", "I", "î", "Î", "ï", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "ô", "Ô", "p", "P", "q", "Q", "r", "R", "s", "S","t", "T", "u", "U", "ù", "û", "v", "V", "w", "W", "x", "X", "y", "Y", "z"];
const BASE_URL = 'http://127.0.0.1:8000/';
export default({
       el: '#app',

  mounted () {
    axios
      .get(`${BASE_URL}api/voice/voices/?format=json`)
      .then(response => (this.info = response))
  },
  methods : {
    playSound() {
      var x=Math.random()*6;
      var audio = new Audio(`http://127.0.0.1:8000/api/voice/voices/musics/${x}.mp3`);
      audio.play();
    },

    verify: function () {
      console.log(this.model);
      this.errors = [];

      if (this.model.text == null) {
        this.errors.push('text required.');
      }
      if (!this.valid(this.model.text)){
        this.errors.push('valid text required.');
      }

      if (!this.errors.length) {
        return true;
      }

    }
  },
  spaceNB: function(text){
    var list= text.split(" ");
    var i;
    for (i;list.length-1;i++){
        if (i===""){
            return false}}
    return true
},
  letter :function (text,set){
         var m =text.split(" ");
         var i,j;
    for (i;i<m.length;i++) {
        for (j;j<m[i].length;j++) {
            if (!(l in set)){
              return false
          }}}
    return true
},
   valid: function (msg) {
     const list = msg.split(" ");
     if( list[0]===""){
        return false}
    if (this.letter(text,set)){
        return false}
    if (!(this.spaceNB(text))){
        return false}
    for (i; i<list.length;i++){
        if (list[i].length>=2){
            if ((list[i][0].toUpperCase()===list[i][0]) && (list[i][1].toUpperCase()===list[i][1])) {
                for (j;len(list[i]);j++){
                    if (list[i][j].toLowerCase() ===list[i][j]){
                        return false}}}}
        if (list[i] in ['?','.','!']){
            if (i!==len(list)-1){
                if (!(list[i+1][0].toUpperCase()===list[i+1][0])){
                    return false}}}
        for (j; j<len(list[i])-1;j++) {
            if( (list[i][j]==='.') || (list[i][j]===j) || (list[i][j]===j)){
                return false }}
    }
      return true

   },
      data: function() {

            return{
              info: null,
              errors :[],
    model :{
      num : 5,
      text: null,
      message : new Audio(`http://127.0.0.1:8000/api/voice/voices/musics/${x}.mp3`),

    }}
        },
        // Form handler
        onSubmit: function(e) {

          console.log(this.model);
          if (this.verify()){
            this.$http.post('http://127.0.0.1:8000/api/submissions/submissions/',this.model,function(data){
              });}

        }
    })
/*
module.exports = {
  data:function(){
    return {
      submissions : {num: '',text: '',message: ''},
      error : ''
    }
  },
  methods: {
        onSubmitForm: function(e)
        {
            e.preventDefault();
            this.$http.post('/api/submissions/',this.user,function(data){
                 router.go('/');
            })
            .error(function(data){
              if(data.errors != 'undefined')
              {
                this.$set('error',data.errors);
              }
            });
        }
    }
}*/
</script>

<style lang="scss">

@import url(https://fonts.googleapis.com/css?family=Exo:100,200,400);
@import url(https://fonts.googleapis.com/css?family=Source+Sans+Pro:700,400,300);
#app {

  body {
    margin: 0;
    padding: 0;
    background: #fff;

    color: #fff;
    font-family: Arial;
    font-size: 12px;
  }

  .body {
    position: absolute;
    top: -20px;
    left: -20px;
    right: -40px;
    bottom: -40px;
    width: auto;
    height: auto;
    background-image: url(http://ginva.com/wp-content/uploads/2012/07/city-skyline-wallpapers-008.jpg);
    background-size: cover;
    -webkit-filter: blur(5px);
    z-index: 0;
  }

  .grad {
    position: absolute;
    top: -20px;
    left: -20px;
    right: -40px;
    bottom: -40px;
    width: auto;
    height: auto;
    background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, rgba(0, 0, 0, 0)), color-stop(100%, rgba(0, 0, 0, 0.65))); /* Chrome,Safari4+ */
    z-index: 1;
    opacity: 0.7;
  }

  .header {
    position: absolute;
    top: calc(50% - 35px);
    left: calc(50% - 255px);
    z-index: 2;
  }

  .header div {
    float: left;
    color: #fff;
    font-family: 'Exo', sans-serif;
    font-size: 35px;
    font-weight: 200;
  }

  .header div span {
    color: #5379fa !important;
  }

  .login {
    position: absolute;
    top: calc(50% - 75px);
    left: calc(50% - 50px);
    height: 150px;
    width: 350px;
    padding: 10px;
    z-index: 2;
  }

  .login input[type=text] {
    width: 250px;
    height: 30px;
    background: transparent;
    border: 1px solid rgba(255, 255, 255, 0.6);
    border-radius: 2px;
    color: #fff;
    font-family: 'Exo', sans-serif;
    font-size: 16px;
    font-weight: 400;
    padding: 4px;
  }

  .login input[type=password] {
    width: 250px;
    height: 30px;
    background: transparent;
    border: 1px solid rgba(255, 255, 255, 0.6);
    border-radius: 2px;
    color: #fff;
    font-family: 'Exo', sans-serif;
    font-size: 16px;
    font-weight: 400;
    padding: 4px;
    margin-top: 10px;
  }


  button {
    width: 260px;
    height: 35px;
    background: #fff;
    border: 1px solid #fff;
    cursor: pointer;
    border-radius: 2px;
    color: #a18d6c;
    font-family: 'Exo', sans-serif;
    font-size: 16px;
    font-weight: 400;
    padding: 6px;
    margin-top: 10px;
  }
   input {
    width: 260px;
    height: 35px;
    background: #fff;
    border: 1px solid #fff;
    cursor: pointer;
    border-radius: 2px;
    color: #a18d6c;
    font-family: 'Exo', sans-serif;
    font-size: 16px;
    font-weight: 400;
    padding: 6px;
    margin-top: 10px;
  }

  .login input[type=button]:hover {
    opacity: 0.8;
  }

  .login input[type=button]:active {
    opacity: 0.6;
  }

  .login input[type=text]:focus {
    outline: none;
    border: 1px solid rgba(255, 255, 255, 0.9);
  }

  .login input[type=password]:focus {
    outline: none;
    border: 1px solid rgba(255, 255, 255, 0.9);
  }

  .login input[type=button]:focus {
    outline: none;
  }

  ::-webkit-input-placeholder {
    color: rgba(255, 255, 255, 0.6);
  }

}
</style>
