<template>
<div>
<div class="container-fluid">
<div class="row border border-top-0 border-right-0 border-left-0 header">
<div class="col-md">
<nav class="navbar navbar-expand-lg">
<a class="navbar-brand" href="/"><img src="../assets/logo.png" alt="HashiCorp" class="site_logo"> &nbsp; {{appinfo.appname}}</a>
<span class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
<i class="bi-list"></i>
</span>
<div class="collapse navbar-collapse pl-3" id="navbarSupportedContent">
<div style="border-top:1.5px solid #eee"></div>
<ul class="navbar-nav">
    <li class="nav-item dropdown"> <a href="#" class="nav-link dropdown-toggle" id="dropdownlink1" role="button" data-bs-toggle="dropdown" aria-expanded="false">Browse services</a>
        <ul class="dropdown-menu" aria-labelledby="dropdownlink1">
        <li><a class="dropdown-item" href="#">Services</a></li>
        <div class="dropdown-divider"></div>
        <!-- <li><router-link class="dropdown-item" to="/oath/analyze">Analyze</router-link></li>
        <li><router-link class="dropdown-item" to="/oath/import">Import</router-link></li>
        <li><router-link class="dropdown-item" to="/oath/explore">Live update</router-link></li> -->
        </ul>
    </li>

    <!-- <li class="nav-item"> <a class="nav-link" href="/site/about">About</a> </li> -->
    <li class="nav-item"> <a class="nav-link" href="/site/contact">Contacts</a> </li>
</ul>

<ul class="navbar-nav m-0 p-0 ms-auto">
    <li class="nav-item"> <a class="nav-link" href="#">Follow us on</a> </li>
    <li class="nav-item"> <a class="nav-link" target="_blank" v-bind:href="media.facebook"><i class="bi-facebook"></i></a> </li>
    <li class="nav-item"> <a class="nav-link" target="_blank" v-bind:href="media.twitter"><i class="bi-twitter"></i></a> </li>
    <li class="nav-item"> <a class="nav-link" target="_blank" v-bind:href="media.instagram"><i class="bi-instagram"></i></a> </li>
    <li class="nav-item"> <router-link class="nav-link" to="/site/contact">Help(Chat)</router-link> </li>
</ul>
</div>
</nav>
</div>
</div>
</div>
<br clear="all">
<br clear="all">
<br clear="all">
<!-- Vetur can't find `tsconfig.json` or `jsconfig.json` in /home/helloworld/Develops/Web_apps/django/application. -->
</div>
</template>
<script>
import appsettings from '../json/myapp.json'
export default {
data(){
return {
"media":appsettings.media,
"appinfo":appsettings.appinfo
}
}
}
</script>
