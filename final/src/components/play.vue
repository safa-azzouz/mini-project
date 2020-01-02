<template>
  <div class="login-bg">
    <div class="container">
      <form class="form-signup" method="POST" v-on="submit : onSubmitForm">
        <h1 class="text-center">picstats</h1>
        <h2 class="form-signin-heading">submission</h2>
         <label for="inputName" class="sr-only">texte</label>
         <input type="text" id="inputName" v-model="user.texte" class="form-control" placeholder="Name" required autofocus>
        <label for="num" class="sr-only">Email address</label>
        <input type="number" id="num" v-model="user.num" class="form-control" required autofocus>
        <label for="msg" class="sr-only">Password</label>
        <input type="text" id="msg" v-model="user.message" class="form-control" placeholder="Password" required>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Register</button>
        <br/>
        <br/>
        <p class="text-center">Already have account ? <a href="/#/"> Sign in</a></p>
      </form>
    </div>
  </div>
</template>
<script>
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
            this.$http.post('/api/submissions',this.user,function(data){
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
}
</script>
