<template>
<div>
    <GeneralHeader/>
    <br clear="all">
<div class="col-md-9 mt-5 mx-auto">
<div class="col m-2 mt-0 mb-1"></div>
<div class="container">
<div class="row">
<!-- <div class="col-md-4">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-primary"><i class="bi-person-plus" style="font-size: 1.5rem;"></i> New Account</h5>
</div>
</div> -->
<!-- <div class="col-md-8 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" role="group" aria-label="First group"><a href="#" class="btn btn-outline-secondary text-center" onClick="window.location.reload()">  <i class="bi-arrow-clockwise"></i> Refresh </a></div>
<div class="btn-group m-2" role="group" aria-label="First group"><router-link to="/site/signin" class="btn btn-primary text-center">  <i class="bi-person-circle"></i> Sign in </router-link></div>

</div>

</div> -->
</div>
</div>
<div class="container">
<div class="border">
<div class="row">
            <div class="col-md-4">
    <div class="p-2">
            <fieldset class="border p-2">
                <legend class="w-auto" style="float: none; padding: inherit;">Instructions</legend>
            <div class="row">
            <div class="col-md-12">
                <div class="m-1 mt-2">

                    <div class="alert alert-primary"><p class="">
                        Kindly provide valid information only. Your user Email and Phone number will be used 
                        for subsequent communication. Hence, A default password will be sent to the Email provided for secuirty purpose, 
                        which the you can later used to login or change password to your desired password. If you are facing any difficulty creating this account, kindly contact our support.
                        </p></div>
                </div>
            </div>


            </div>
            </fieldset>

    </div>
</div>
<div class="col-md-8">
    <div class="p-2">
            <form @submit.prevent="formCheck" class="needs-validation">
            <fieldset class="border p-2">
                <legend class="w-auto" style="float: none; padding: inherit;">Create your Business Account</legend>
            <div class="row">

            <div class="col-md-6">
                <div class="m-1 mt-2">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                    <label for="sname" class="pb-1 text-dark">Business name</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-briefcase"></i></span>
                    <input type="text" v-model="businessName" :disabled="isDisabled" id="sname" minlength="3" maxlength="50" class="form-control" required placeholder="Business name">
                </div>
                <small class="form-text text-muted"></small>
                
                </div>
            </div>


            <div class="col-md-6">
                <div class="m-1 mt-2">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                    <label for="sname" class="pb-1 text-dark">Business address</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-map"></i></span>
                    <input type="text" v-model="businessAddress" :disabled="isDisabled" id="sname" minlength="3" maxlength="50" class="form-control" required placeholder="Your Business address">
                </div>
                <small class="form-text text-muted"></small>
                
                </div>
            </div>

            <div class="col-md-6">
                <div class="m-1 mt-2">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                    <label for="sname" class="pb-1 text-dark">Your Surname</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-person"></i></span>
                    <input type="text" v-model="surname" :disabled="isDisabled" id="sname" minlength="3" maxlength="50" class="form-control" required placeholder="Surname/Lastname">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger">{{err_surname}}</small>
                
                </div>
            </div>


            <div class="col-md-6">
                <div class="m-1 mt-2">
                    <label for="fname" class="pb-1 text-dark">Your Firstname</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-person"></i></span>
                    <input type="text" v-model="firstname" :disabled="isDisabled" minlength="3" maxlength="50" id="fname" class="form-control" required placeholder="Firstname">
                </div>
                <small class="form-text text-muted"></small>
                    <small class="text-danger">{{err_firstname}}</small>
                
                </div>
            </div>


            <div class="col-md-6">
                <div class="m-1 mt-2">
                    <label for="email" class="pb-1 text-dark">Email</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-mailbox"></i></span>
                    <input type="email" v-model="email" :disabled="isDisabled" minlength="10" maxlength="100" id="email" class="form-control" required placeholder="Email address">
                </div>
                    <small class="form-text text-muted"></small>
                    <small class="text-danger">{{err_email}}</small>
                </div>
            </div>


            <div class="col-md-6">
                <div class="m-1 mt-2">
                <div class="row">
                    <div class="col-5">
                    <label for="code" class="pb-1 text-dark">Code</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-telephone"></i></span>
                    <select class="form-select p-0" v-model="countryCode" :disabled="isDisabled" id="code" required>
                    <option value="" disabled selected>Select</option>
                    <option value="+234">+234</option>
                    </select>
                    </div>
                    </div>
                <div class="col-7">
                    <label for="phone" class="pb-1 text-dark">Phone</label>
                <div class="input-group">
                    <input type="text" v-model="phone" :disabled="isDisabled" minlength="7" maxlength="15" id="phone" class="form-control" required placeholder="Number only">
                    </div>
                </div>
                    </div>
                    <small class="form-text text-muted"></small>
                    <small class="text-danger">{{err_phone}}</small>
            
                </div>
            </div>

            <div class="col-md-6">
                <div class="m-1 mt-2">
                    <label for="email" class="pb-1 text-dark">Prefered Language</label>
                <div class="input-group">
                    <span class="input-group-text"><i class="bi-telephone-forward"></i></span>
                   <select class="form-select p-0" v-model="languageCode" :disabled="isDisabled" id="code" required>
                    <option selected disabled>Select language</option>
                    <option value="English">English</option>
                    <option value="Hausa">Hausa</option>
                    <option value="Igbo">Igbo</option>
                    <option value="Yoruba">Yoruba</option>
                    </select>
                </div>
                    <small class="form-text text-muted"></small>
                </div>
            </div>
        
            <div class="col-md-6 mt-2 text-center d-flex justify-content-end">
                <div class="m-1">
                    <label for=""></label>
                <div class="input-group">
                    <button type="submit" :disabled="isDisabled" class="btn btn-primary">{{submit}}</button>
                </div>
            </div>
            <small class="pb-2 text-danger text-center">{{error_btn}}</small>
            </div>

            <div class="col-md-12 mt-2">
                <div v-bind:class="classname">{{alert}}</div>
            </div>

                </div>
                </fieldset>
            </form>
                <div class="col-md-12 mt-4 d-flex justify-content-end">
          <p class=""><a href="/site/signin">Sign in instead</a></p>
            </div>
        
    </div>
</div>

</div>
</div>
</div>


</div>
</div>
</template>
<script>
import axios from 'axios'
export default {
//   components:{
// 'Menu': ()=> import('../layout/accountHeader.vue')
// },
    data (){
        return{
        alert:null,
        token: null,
        surname: null,
        firstname: null,
        othername: null,
        businessName: null,
        businessAddress: null,
        languageCode: null,
        email: null,
        persionalId: null,
        phone: null,
        countryCode: null,
        account_type: null,
        err_surname: null,
        err_firstname: null,
        err_othername: null,
        err_email: null,
        err_phone: null,
        err_account_type: null,
        err_persionalId: null,
        gender: null,
        selectDefault:"Select",
        classname:null,
        submit:'Next',
        submittxt:'Next',
        isDisabled:false,
        error_btn: null,
        opacity_enable:'opacity:0.5; pointer-events:None;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
    }
    },
    created(){
    this.tokenize()
    },
    methods:{
    validEmail: function (email) {
    var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
    },
    validDigit: function (digits) {
    var re = /^\d+$/;
    return re.test(digits);
    },
    formCheck: function(e){
        if (!this.validEmail(this.email)) {
        this.err_email="Valid email is required.";
        this.error_btn="Go back and check error message";
        }else if(!this.validDigit(this.phone)){
        this.err_phone="Valid phone number required.";
        this.error_btn="Please check and correct error(s)";
        }else{
            this.err_email=""
            this.err_phone=""
            this.error_btn="";
        this.submit="Please wait.."
        this.adminAccount()
        }
    e.preventDefault();
    },
    adminAccount: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
    const form = new FormData();
        form.append('surname', this.surname)
        form.append('firstname', this.firstname)
        form.append('businessName', this.businessName)
        form.append('businessAddress', this.businessAddress)
        form.append('languageCode', this.languageCode)
        form.append('email', this.email)
        form.append('phone', this.phone)
        form.append('csrfmiddlewaretoken', this.token)
    axios.post('/posts/newaccount/', form)
        .then(response => {
        if(response.data.status==response.data.statusmsg){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable 
        setTimeout(function(){
            window.location.href=response.data.redirect
            },2000)
        }else{
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable 
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        }
        
    }).catch(()=>{
                this.$Progress.fail()
            this.isDisabled = false
            this.opacity = this.opacity_disable 
        this.classname='alert alert-danger p-1 text-center'
        this.alert='Error connecting, please try again.'
        this.submit=this.submittxt
    })  
    },
     tokenize: function(){
        this.$Progress.start()
      this.isDisabled = true
    axios.get('/auth/tokenize/',{
    params:{
      'token': Math.random(9, 9999)
    }
  }).then(response => {
      if(response.data.status==response.data.statusmsg){
      this.token=response.data.key
      axios.defaults.headers.common['X-CSRF-TOKEN'] = response.data.key;
      this.$Progress.finish()
      this.isDisabled = false
      }else{
      this.$Progress.finish()
      this.isDisabled = false
     this.classname='text-danger p-1 text-center'
      this.alert='Check network connection or reload this page'
      }
    
  }).catch(()=>{
      this.$Progress.fail()
      this.isDisabled = false
      this.classname='text-danger p-1 text-center'
      this.alert='Check network connection or reload this page'
  })
  },
    }


    }
</script>