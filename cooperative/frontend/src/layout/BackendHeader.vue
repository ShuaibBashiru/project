<template>
<div>

<div class="container-fluid header">
<div class="row">
<div class="col-md p-0" :style="appinfo.css.headerbg">
<nav class="navbar navbar-expand-lg p-1 m-1 mt-0 mb-0">
<a class="navbar-brand" href="/" :style="appinfo.css.headercolor"><img src="@/assets/logo.png" :width="appinfo.logoWidth" :height="appinfo.logoHeight"  alt=""> &nbsp; {{appinfo.appname}}</a>
<span class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
<i class="bi-list text-white"></i>
</span>
<div class="collapse navbar-collapse" id="navbarSupportedContent">
<div style="border-top:1.5px solid #eee"></div>
    <ul class="navbar-nav m-0 p-0 ms-auto">
<div class="btn-group">
  <li class="text-white dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    Quick Links
  </li>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
</div>
    </ul>
    <ul class="navbar-nav m-0 p-0 ms-auto">
    <!-- <li class="nav-item"> <a class="nav-link" href="/site/contact">CHAT US</a> </li> -->
    <li class="nav-item p-1 pt-0 pb-0"> <a v-bind:class="'nav-link ' + appinfo.f_color" href="/site/logout">Sign Out</a> </li>
    <li class="nav-item p-1 pt-0 pb-0"><div class="dp"></div></li>
    </ul>
</div>
</nav>
</div>
</div>
</div>

    <div class="col-md-2 sidebar p-2" :style="appinfo.css.sidebarbg">
       <div class="input-group sticky-top mt-2">
           <input type="search" class="form-control" id="search-input" placeholder="Search menu" aria-label="Search for..." autocomplete="off">
       </div>
      <ul class="list-group mt-4 list-group-flush">
    <li class="list-group-item active border"><router-link to="/secure/dashboard" class="text-white"><i class="bi-list"></i> Menu</router-link></li>
  <li class="list-group-item"><router-link class="" to="/secure/adminaccount"><i class="bi-person-plus-fill"></i> Admin Account</router-link></li>
  <li class="list-group-item"><router-link class="" to="/secure/widget"><i class="bi-bricks"></i> Widgets</router-link></li>
  <li class="list-group-item"><router-link class="" to="/secure/post"><i class="bi-file-post"></i> Posts</router-link></li>
  <li class="list-group-item"><router-link class="" to="/secure/newsletter"><i class="bi-newspaper"></i> Newsletters </router-link></li>
  <li class="list-group-item"><router-link class="" to="/secure/mailer"><i class="bi-mailbox"></i> Send Mail</router-link></li>
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
.navbar-nav .nav-item a{
color:#ffffff;
font-size: 14px;
font-family: 'Geomanist book webfont',Arial,sans-serif;
}
.list-group-item{
    background: none;
    padding-left:4px;
}
.list-group-item a{
    color: #ffffff;
}

.list-group-item i{
    margin-right: 5px;
}
.active{
border-top-left-radius: 5px;
border-top-right-radius: 5px;
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
    // end of methods

}
</script>