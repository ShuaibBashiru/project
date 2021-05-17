<template>
    <div>
        <br>
        <br>
        <br>
    <div class="container-fluid footer mt-5">
        <div class="">
        <div class="row">

            <div class="col-md-4 mt-2">
                <p class="text-muted">Copyright &copy; {{appinfo.year}} {{appinfo.displaynamelower}} All rights reserved</p>
            </div>
            <div class="col-md-4 mt-2  d-flex justify-content-center">
            <ul class="nav">
                    <li class="nav-item"><a class="nav-link p-2 pt-0 pb-0" href="#">Contact</a></li>
                    <li class="nav-link text-primary p-0">|</li>
                    <li class="nav-item"><a class="nav-link p-2 pt-0 pb-0" href="#">Terms & conditions</a></li>
                    <li class="nav-link text-primary p-0">|</li>
                    <li class="nav-item"><a class="nav-link p-2 pt-0 pb-0" href="#">Privacy</a></li>
                  </ul>
            </div>
            <div class="col-md-4 mt-2  d-flex justify-content-end">
                <h4>Chat <i class="bi-question-circle" role="img" aria-label="Help" style="font-size: 1.4rem; color: black;"></i></h4>
            </div>
        </div>
    </div>


    </div>
    </div>
</template>
<style scoped>

.footer{
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    z-index:1000;
    background-color: #f5f5f5;
    border-top: 1px solid #ccc;
   }

</style>
<script>
import appsettings from '../json/myapp.json'
// import csc from 'country-state-city'
export default {
    data(){
        return {
            "media":appsettings.media,
            "appinfo":appsettings.appinfo,
            // getLocation: csc,
            gettingLocation: null,
            errorStr: null,
            location: null

        }
    },
    methods:{
    //     getLocationFunction: function(){
    // navigator.geolocation.getCurrentPosition(pos => {
    //   this.gettingLocation = false;
    //   this.location = pos;
    //         }, err => {
    //   this.gettingLocation = false;
    //   this.errorStr = err.message;

    // })

    //     }
    },

    created(){
        this.getLocationFunction()
    }

}
</script>