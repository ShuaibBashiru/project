<template>
    <div>   
    <div class="container-fluid mt-4 p-5 pt-3 pb-0 footer" style="background:#0b0b12;">
        <div class="">
        <div class="row">
            <div class="col-md-4 mt-4"> 
                <h6 class="">{{appinfo.displaynamecap}}</h6>
                <ul class="navbar-nav m-2 ml-4">
                    <li class="nav-item"><a class="nav-link p-1 text-muted" href="">About us</a></li>
                    <li class="nav-item"><a class="nav-link p-1 text-muted" href="">Contact us</a></li>
                    <li class="nav-item"><a class="nav-link p-1 text-muted" href="">Privacy Policy</a></li>
                    <li class="nav-item"><a class="nav-link p-1 text-muted" href="">Terms & Conditions</a></li>
                </ul>
                 </div>
            <div class="col-md-5 mt-4">
                <h6>CALL OR TEXT US</h6>
                <p><a :href="'tel:'+ media.phone">{{ media.phone }}</a></p>
                <p class="text-muted"> {{ media.address }} </p>
                <h6>EMAIL US</h6>
                    <a :href="'mailto:'+ media.email">{{ media.email }}</a>
            </div>
            <div class="col-md-3 mt-4">
                <h6 class="text-center">JOIN US ON</h6>
                <ul class="nav d-flex justify-content-end">
                    <li class="nav-item"><a class="nav-link" :href="media.facebook"><i class="bi-facebook"></i></a></li>
                    <li class="nav-item"><a class="nav-link" :href="media.twitter"><i class="bi-twitter"></i></a></li>
                    <li class="nav-item"><a class="nav-link" :href="media.youtube"><i class="bi-youtube"></i></a></li>
                    <li class="nav-item"><a class="nav-link" :href="media.instagram"><i class="bi-instagram"></i></a></li>
                </ul>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12 text-center mt-4">
            <hr class="text-muted">
                <p class="text-muted">Copyright - {{appinfo.displaynamelower}} - All rights reserved - {{appinfo.year}}</p>
            </div>
        </div>
    </div>


    </div>
    </div>
</template>
<style scoped>
.navbar-nav li a{
    color:#ffffff;
}
.footer h1, h2, h3, h4, h5, h6, p{
color: #ffffff;
}
</style>
<script>
import appsettings from '../json/myapp.json'
export default {
    data(){
        return {
            "media":appsettings.media,
            "appinfo":appsettings.appinfo,
        }
    },

}
</script>