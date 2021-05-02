<template>
<div :style="opacity">
<section v-if="accountActive==true">
<div class="container-fluid header">
<div class="row">
<div class="col-md p-0 border-bottom" :style="appinfo.css.headerbg">
<nav class="navbar navbar-expand-lg p-1 m-1 mt-0 mb-0">
<a class="navbar-brand" href="/secure/dashboard" :style="appinfo.css.headercolor"><img src="@/assets/logo.png" :width="appinfo.logoWidth" :height="appinfo.logoHeight"  alt=""> &nbsp; {{appinfo.appname}}</a>
<span class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
<i class="bi-list"></i>
</span>
<div class="collapse navbar-collapse" id="navbarSupportedContent">
<div style="border-top:1.5px solid #eee"></div>
    <ul class="navbar-nav m-0 p-0 ms-auto">
<div class="btn-group">
  <li class="dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
  Links
  </li>
  <ul class="dropdown-menu">
      <ul class="list-group list-group-flush" v-for="(d, index) in menus" :key="index">
    <li class="list-group-item"><a class="dropdown-item" :href="'/secure/'+d['menuName']">{{d['menu_description']}}</a></li>
      </ul>
<li class="dropdown-divider"></li>
<li class="dropdown-item"> <a href="/site/logout"> Logout </a></li>
  </ul>
</div>
    </ul>
    <ul class="navbar-nav m-0 p-0 ms-auto">
    <li class="nav-item p-1 pt-0 pb-0"> <a v-bind:class="'nav-link ' + appinfo.f_color" href="/site/help"><i class="bi-question-circle" role="img" aria-label="Help" style="font-size: 1.4rem; color: black;"></i></a> </li>
    <li class="nav-item p-1 pt-0 pb-0"> <a v-bind:class="'nav-link ' + appinfo.f_color" href="#"><i class="bi-list" role="img" aria-label="Apps" style="font-size: 1.4rem; color: black;"></i></a> </li>
    <li class="nav-item p-1 pt-0 pb-0 dropdown">
        <a href="/site/logout"><div class="dp mt-2"></div></a>
    </li>
  
    </ul>
</div>
</nav>
</div>
</div>
</div>
<br clear="all"/>
<div class="container">

<div class="row">
    <div class="col-md-2 sidebar p-2 border-end" :style="appinfo.css.sidebarbg">
        <div class="row mt-1">
        <div class="col">
        <small><i class="bi-person" style="font-size: 0.9rem; color: black;"></i> Welcome, {{userdata['surname']}}</small>
        </div>
        </div>

       <div class="input-group sticky-top mt-3">
           <input type="search" class="form-control" id="search-input" placeholder="Search menu" aria-label="Search for..." autocomplete="off">
       </div>
      <ul class="list-group mt-2 list-group-flush">
        <li class="list-group-item active border"><router-link to="/secure/dashboard" class="text-white"><i class="bi-list" style="font-size: 1.1rem; color: #fff;"></i> Dashboard </router-link></li>
      </ul>
      <ul class="list-group mt-2 list-group-flush" v-for="(d, index) in menus" :key="index">
    <li class="list-group-item"><router-link :to="'/secure/'+d['menuName']" class="userlink"><i :class="d['menu_icon']" style="font-size: 0.9rem; color: black;"></i> {{d['menu_description']}} </router-link></li>
   </ul>
</div>
<div class="col-md-10 offset-md-2 maindiv">
<section v-if="ifUserHasAccess==true">
    <slot></slot>
</section>
<section v-else>
   <div class="container-fluid">
       <div class="row mt-5 text-center ">
           <div class="col-8 mt-5 mx-auto d-flex justify-content-center">
   <p class="lead mt-2 text-danger" style="line-height:1.5">{{norecord}}</p>
           </div>
 <div class="col-8 mt-5 mx-auto d-flex justify-content-center">
<p class="m-2" @click="$router.go(-1)" :style="'display:'+backbtn"><a href="#" class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> Back </a></p>
           </div>
       </div>
   </div>
</section>
</div>
</div>
</div>
</section>
<section v-else>
   <div class="container-fluid mt-5">
       <div class="row mt-5 text-center ">
           <div class="col-8 mt-5 mx-auto d-flex justify-content-center">
   <p class="lead mt-2 text-danger" style="line-height:1.5">{{norecord}}</p>
           </div>
 <div class="col-8 mt-5 mx-auto d-flex justify-content-center">
<p class="m-2" @click="$router.go(-1)" :style="'display:'+backbtn"><a href="#" class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> Back </a></p>
           </div>
       </div>
   </div>
</section>


</div>
</template>


<style scoped>
.list-group-item{
    /* background: none; */
    padding-left:4px;
}

.list-group-item i{
    margin-right: 5px;
}
.userlink{
    text-decoration: none;
    color: rgb(59, 56, 56);
}
.active{
border-top-left-radius: 5px;
border-top-right-radius: 5px;
}
</style>
<script>
import appsettings from '../json/myapp.json'
import axios from 'axios'
export default {
    data(){
        return {
            info:[],
            userdata:[],
            menus:[],
            "media":appsettings.media,
            "appinfo":appsettings.appinfo,
            progress:null,
            accountActive:false,
            ifUserHasAccess:false,
            userid:null,
            page: '',
            pwd:'',
            classname:'',
            isDisabled: false,
            error_btn: null,
            errormodal: null,
            record:false,
            norecord:'',
            loader:false,
            loaderstatus:'',
            backbtn:'none',
            counter:'0',
            pagename: this.$route.name,
            opacity_enable:'opacity:0.5; pointer-events:None;',
            opacity_disable:'opacity:1; pointer-events:All;',
            opacity:'',
            }
    },
        created(){
        this.auth_check()
        },
    methods:{
     listmenu: function(){
            this.$Progress.start()
            this.isDisabled = true
            this.opacity = this.opacity_enable
        axios.get('/api/admin_menus/',{
            params:{

                'pagename':this.pagename
            }
        })
        .then(response => {
            if(response.data.status == response.data.confirmed){
            this.norecord=response.data.msg
            this.alert=''
            this.classname=''
            this.menus = response.data.result
            this.ifUserHasAccess=response.data.ifUserHasAccess
            this.accountActive = true
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }else{
            this.alert=''
            this.norecord=response.data.msg
            this.classname=''
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        
        }).catch(()=>{
            this.backbtn='block'
            this.alert=''
            this.classname=''
            this.norecord='Check network connection or reload this page'
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
        })
    },

    auth_check: function(){
    this.$Progress.start()
    this.isDisabled = true
    this.opacity = this.opacity_enable
    axios.get('/auth/auth_check/')
        .then(response => {
            if(response.data.status==response.data.confirmed){
                this.userdata = response.data.userdata
                this.accountActive = true
                this.$Progress.finish()
                this.isDisabled = false
                this.opacity = this.opacity_disable
                this.listmenu()
                localStorage.setItem("userdata", response.data.userdata);

                }else{
                this.$Progress.finish()
                this.isDisabled = false
                this.opacity = this.opacity_disable
                this.accountActive = false
                localStorage.removeItem('userdata');
                window.location.href='/site/logout'
            }
        }).catch(()=>{
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            this.accountActive = false
            this.alert = 'Check network connection or reload this page'
            localStorage.removeItem("userdata");
            window.location.href='/site/logout'
        })
    },



    },

}
</script>