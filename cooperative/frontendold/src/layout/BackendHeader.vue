<template>
<div>
<div class="container-fluid">
<div class="row border border-top-0 border-right-0 border-left-0 header">
<div class="col-md">
<nav :class="'navbar navbar-expand-lg p-1 ' + appinfo.bg_color">
<a :class="'navbar-brand '+appinfo.f_color" href="/oath/dashboard"><img :src="require('@/assets/logo.png')" :width="appinfo.logoWidth" :height="appinfo.logoHeight"  alt="" class=""> &nbsp; {{appinfo.appname}}</a>
<div class="navbar-toggler p-0" aria-expanded="false" aria-label="Toggle navigation">
<div class="d-flex">
<span  class="m-1"><div class="dp"></div></span>
<span class="m-2 mr-0" data-bs-target="#navbarSupportedContent" data-bs-toggle="collapse">
<i :class="'bi-list '+appinfo.f_color"></i>
</span>
</div>
</div>
<div class="collapse navbar-collapse" id="navbarSupportedContent">
<div style="border-top:1.5px solid #eee"></div>
<ul class="navbar-nav">
    <li class="nav-item dropdown"> <a href="#" v-bind:class="'nav-link dropdown-toggle ' + appinfo.f_color" id="dropdownlink1" role="button" data-bs-toggle="dropdown" aria-expanded="false">Quick Links</a>
        <ul class="dropdown-menu" aria-labelledby="dropdownlink1">
        <li><a class="dropdown-item" href="#">Links</a></li>
        <div class="dropdown-divider"></div>
        <li class="nav-item p-2">Empty</li>
        </ul>
    </li>
</ul>
<ul class="navbar-nav ms-auto m-3 mt-0 mb-0">
    <li class="nav-item p-1 pt-0 pb-0"> <a v-bind:class="'nav-link ' + appinfo.f_color" href="/site/logout">Sign Out</a> </li>
    <li class="nav-item p-1 pt-0 pb-0"><div class="dp"></div></li>
</ul>
</div>
</nav>
</div>
</div>

</div>
    <div class="col-md-2 sidebar p-1 border border-top-0 border-bottom-0 border-right-0">
       <div class="input-group sticky-top">
           <input type="search" class="form-control" id="search-input" placeholder="Search menu" aria-label="Search for..." autocomplete="off">
       </div>
      <ul class="list-group mt-4 pl-0 m-0 list-group-flush">
    <li class="list-group-item active"><router-link to="/oath/dashboard" class="text-white">Menu</router-link></li>
  <li class="list-group-item"><router-link class="" to="/oath/searchaccount"><i class="bi-search"></i> Search Account</router-link></li>
  <li class="list-group-item"><router-link class="" to="/oath/admin"><i class="bi-person-plus-fill"></i> Admin Account</router-link></li>
  <li class="list-group-item"><router-link class="" to="/oath/user"><i class="bi-person-plus"></i> User's Account</router-link></li>
  <li class="list-group-item"><router-link class="" to="/oath/uploadlist"><i class="bi-upload"></i> Upload payment</router-link></li>
  <li class="list-group-item"><router-link class="" to="/oath/transactions"><i class="bi-wallet2"></i> Transactions</router-link></li>
  <li class="list-group-item"><router-link class="" to="/oath/patientaccount"><i class="bi-file-earmark-excel"></i> Create Report</router-link></li>
  <li class="list-group-item"><router-link class="" to="/oath/market"><i class="bi-mailbox"></i> Loan </router-link></li>
  <li class="list-group-item"><router-link class="" to="/oath/market"><i class="bi-mailbox"></i> Commodities </router-link></li>
  <li class="list-group-item"><router-link class="" to="/oath/market"><i class="bi-mailbox"></i> Send Mail</router-link></li>
</ul>
       <!-- layer one -->
    </div>
</div>

</template>
<style scoped>
.dp{
    border-radius:50%;
    width: 32px;
    height: 32px;
    border:1px solid #eee;
    background-image: url('../assets/passport/avatar.png');
    background-size: 32px 32px;
}
.dp img{
    border-radius:50%;
    width: 32px;
    height: 32px;
}
</style>
<script>
import appsettings from '../json/myapp.json'
export default {
    data(){
        return {
            "media":appsettings.media,
            "appinfo":appsettings.appinfo,
            alert:null,
            progress:null,
            userid:null,
            pwd:'',
            classname:'',
        }
    },
    methods:{
    
       
    },
    // end of methods

}
</script>