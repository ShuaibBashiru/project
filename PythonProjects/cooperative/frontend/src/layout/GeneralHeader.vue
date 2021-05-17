<template>
<div :style="opacity">
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
    </ul>
    <ul class="navbar-nav m-0 p-0 ms-auto">
    <li class="nav-item p-1 pt-0 pb-0"> <a v-bind:class="'nav-link ' + appinfo.f_color" href="/site/help"><i class="bi-question-circle" role="img" aria-label="Help" style="font-size: 1.4rem; color: black;"></i></a> </li>
    <li class="nav-item p-1 pt-0 pb-0"> <a v-bind:class="'nav-link ' + appinfo.f_color" href="#"><i class="bi-list" role="img" aria-label="Apps" style="font-size: 1.4rem; color: black;"></i></a> </li>
  
    </ul>
</div>
</nav>
</div>
</div>
</div>
<br clear="all"/>
<div class="container">
<div class="row">
<div class="col-md-12">
    <slot></slot>
</div>
</div>
</div>



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
        },
    methods:{
    },

}
</script>