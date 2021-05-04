<template>
<div>
<div class="container-fluid">
<div class="row border border-top-0 border-right-0 border-left-0">
    <div class="col-md fixed-top">
            <nav class="navbar navbar-expand-lg">
            <a class="navbar-brand" href="/oath/dashboard"><img src="../assets/logo.png" alt="Dash" class="site_logo"> &nbsp; YCT</a>
            <span class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <i class="bi-list"></i>
            </span>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <div style="border-top:1.5px solid #eee"></div>
                <ul class="navbar-nav m-0 p-0">
                    <li class="nav-item dropdown"> <a href="#" class="nav-link dropdown-toggle" id="dropdownlink1" role="button" data-bs-toggle="dropdown" aria-expanded="false">Browse services</a>
                        <!-- <ul class="dropdown-menu" aria-labelledby="dropdownlink1">
                        <li><a class="dropdown-item" href="#">Services</a></li>
                        <div class="dropdown-divider"></div>
                        <li class="nav-item"><a class="dropdown-item" href="#">Enroll</a></li>
                        <li class="nav-item"><a class="dropdown-item" href="#">Capture</a></li>
                        <li><a class="dropdown-item" href="#"></a></li>
                        </ul> -->
                    </li>

                    <li class="nav-item"> <router-link class="nav-link" target="_blank" to="/page/about">About</router-link> </li>
                </ul>
                
                <ul class="navbar-nav m-0 p-0 ms-auto">
                    <li class="nav-item"> <router-link class="nav-link" to="/oath/signout">Sign Out</router-link> </li>
                    <li class="nav-item"> <router-link class="nav-link" target="_blank" to="/page/contactus">Help(Chat)</router-link> </li>
                </ul>
            </div>
            </nav>
    </div>
</div>
</div>

<div class="container-fluid p-0">
<div class="row">
<!-- side bar -->
 <!-- border border-top-0 border-bottom-0 border-right-0 -->
    <div class="col-sm-3 col-md-2 p-1 border border-top-0 border-bottom-0 border-right-0 sidebar">
       <div class="input-group">
           <input type="search" class="form-control" id="search-input" placeholder="Search menu" aria-label="Search for..." autocomplete="off">
           <div class="input-group-append">
           <span class="input-group-text"><i class="bi-search"></i></span>
           </div>
       </div>
      <ul class="list-group list-group-flush">
  <li class="list-group-item"><router-link class="" to="/page/s">Cras justo odio</router-link></li>
  <li class="list-group-item"><router-link class="" to="/page/s">Dapibus ac facilisis in</router-link></li>
  <li class="list-group-item"><router-link class="" to="/page/s">Morbi leo risus</router-link></li>
  <li class="list-group-item"><router-link class="" to="/page/s">Porta ac consectetur ac</router-link></li>
  <li class="list-group-item"><router-link class="" to="/page/s">Vestibulum at eros</router-link></li>
    <li class="list-group-item"><router-link class="" to="/page/s">Cras justo odio</router-link></li>
  <li class="list-group-item"><router-link class="" to="/page/s">Dapibus ac facilisis in</router-link></li>
  <li class="list-group-item"><router-link class="" to="/page/s">Morbi leo risus</router-link></li>
  <li class="list-group-item"><router-link class="" to="/page/s">Porta ac consectetur ac</router-link></li>
<li class="list-group-item"><router-link class="" to="/page/s">Last one</router-link></li>
</ul>
    </div>

    <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 maindiv">
       <slot/>
    </div>
    <!-- content panel end -->
</div>
</div>
 
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

        // method(){
        //     function search(){
        //         $("#search-input").on("keyup", function() {
        //         var value = $(this).val().toLowerCase();
        //         $(".menusort li"  ).filter(function() {
        //         $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        //         })
        //         })
        //     }
        // }
    }
}
</script>
