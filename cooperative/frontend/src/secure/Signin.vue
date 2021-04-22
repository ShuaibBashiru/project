<template>
<div>
    <GeneralHeader/>
     <br clear="all">
<div class="container-fluid mt-5">
<div class="row d-flex justify-content-center">
    <div class="col-md-4 border p-5 pb-3 rounded mt-2">
  <form @submit.prevent="signIn" role="form">
  <div class="form-row">
<div class="form-group col">
    <h2 class="text-primary">Sign in</h2>
</div>

<div class="form-group col">
            <div v-bind:class="classname">{{alert}}</div>
</div>

    <div class="form-group mt-4 col">
        <label for="userid" class="text-muted">UserID</label>
        <input type="hidden" v-model="token" required>
      <input type="email" class="form-control" v-model="userid" placeholder="Enter your email" id="userid" required maxlength="100" minlength="10">
    </div>

    <div class="form-group mt-3 col">
        <label for="pwd" class="text-muted">Password</label>
      <input :type="pass_type" class="form-control" v-model="pwd" placeholder="Password" id="pwd" required maxlength="50" minlength="3">
    </div>
    <small class="text-danger">{{error}}</small>

    <div class="form-group mt-3">
<div class="row">
  <div class="col-md-12">
    <div class="form-check">
        <input class="form-check-input" type="checkbox" id="showpass"
           v-model="toggle"
           true-value="yes"
          false-value="no" @change="showpassword">
        <label class="form-check-label" for="showpass">
        <small>Show password</small>
        </label>
    </div>
  </div>
</div>
    </div>
      <div class="form-group mt-5 col">
     <div class="row">
     <div class="col pt-1">
       <small>        <a href="/secure/forgot" class="text-left">
        Forgot password?
      </a></small>
     </div>
       <div class="col d-flex justify-content-end">
         <button type="submit" name="signin" class="btn btn-primary" :disabled="isDisabled">{{button}}</button></div>
     </div>
    </div>
      <div class="form-group mt-4 col">
        <p class="text-center">I do not have an Account? <a href="/#" class="text-right">
        Contact Admin
      </a></p>
      </div>
    

  </div>
</form>


    </div>
</div>

</div>
</div>
</template>
<script>
import axios from 'axios'
export default{
data(){
  return{
            info:[],
            alert:'',
            progress:null,
            userid:null,
            pwd:'',
            classname:'',
            token:'',
            btntxt: 'Sign In',
            button: 'Sign In',
            isDisabled: false,
            error:'',
            toggle:null,
            pass_type:'password'
         }

},
methods:{
tokenize: function(){
             axios.get('/auth/tokenize/',{
              params:{
                'token': Math.random(9, 9999)
              }
            }
            ).then(response => {
                if(response.data.status==response.data.confirmed){
                this.token=response.data.key
                axios.defaults.headers.common['X-CSRF-TOKEN'] = response.data.key;
                }else{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Check network connection or reload this page'
                }
              
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Check network connection or reload this page'
            })
        },

       signIn(){
              this.button='Please wait...'
              this.isDisabled=true
              const fd = new FormData();
              fd.append('userid', this.userid)
              fd.append('pwd', this.pwd)
              fd.append('csrfmiddlewaretoken', this.token)
              axios.post('/auth/sign_in/', fd)
              .then(response => {
                if(response.data.status==response.data.confirmed){
                this.classname=response.data.classname
                this.alert=response.data.msg
                this.button=this.btntxt
                this.isDisabled=true
                this.error=''
                setTimeout(function(){
                window.location.href=response.data.redirect
                },2000)
                }else{
                this.error=response.data.msg
                this.button=this.btntxt
                this.isDisabled=false
                }
              
            }).catch(()=>{
                this.error='Check network connection or reload this page'
                this.button=this.btntxt
                this.isDisabled=false
            })
        },
    showpassword: function(){
      if(this.toggle=="yes"){
      this.pass_type = 'text'
      }else{
      this.pass_type = 'password'
      }
    }


},
// End of methods
created(){
this.tokenize()

}
}

</script>
