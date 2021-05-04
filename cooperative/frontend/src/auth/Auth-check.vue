<template>
    <div>
    <GeneralHeader/>
<section v-if="loader==false"></section>
<section v-else>
   <div class="container-fluid">
       <br clear="all/">
       <br clear="all/">
       <br clear="all/">
       <br clear="all/">
       <br clear="all/">
       <div class="row mt-5">
           <div class="col-12 mt-5 d-flex justify-content-center">
<div class="lds-roller"><div></div><div></div><div></div></div>
           </div>
           <div class="col-12 mt-5 d-flex justify-content-center"><small></small></div>
       </div>

       <div class="row mt-5">
           <div class="col text-center">
               <p class="text-muted">{{message}}</p>

               <section v-if="error_found==true">
                   <a href="/site/signin/" class="btn btn-primary">Sign In again</a>
               </section>

           </div>
       </div>
   </div>
</section>

    </div>
</template>
<script>
import axios from 'axios'
export default {
data(){
    return{
        message: 'Please wait a moment',
        statusMsg: null,
        error_found: false,
        loader:true,
    }
},
created(){
   this.auth_check(); 
},
    methods:{
            auth_check: function(){
                this.$Progress.start()
            axios.get('/auth/auth_check/')
        .then(response => {
            if(response.data.status==response.data.confirmed){
                this.$Progress.finish()
                this.message = response.data.msg
                this.error_found = false
                localStorage.setItem("userdata", response.data.userdata);  
                setTimeout(function(){
                window.location.href=response.data.redirect
                },2000)
            }else{
                this.$Progress.finish()
                this.message = response.data.msg
                this.error_found = true
                 setTimeout(function(){
                window.location.href='/site/logout'
                },3000)
            }
        }).catch(()=>{
            this.$Progress.finish()
            this.message = 'Check network connection or reload this page'
            this.error_found = true
               setTimeout(function(){
                window.location.href='/site/logout'
                },3000)
            

        })
    },

}
}
</script>