<template>
<div :style="opacity">
<AdminHeader>
    <div class="container">
        <div class="row">
            <div class="col m-2 mt-0 mb-1">
            <div v-bind:class="classname">{{alert}}</div>
            </div>
        </div>
    </div>
<div class="container">
<div class="row">
<div class="col-md-8">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2">Cassava | 2021 <i class="bi-caret-down"></i>  | May <i class="bi-caret-down"></i></h5>
</div>
</div>
<div class="col-md-4 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" title="Go back" role="group" aria-label="First group" @click="livestream"><a href="#" class="btn btn-primary text-center">  <i class="bi-camera"></i> Live stream </a></div>
<div class="btn-group m-2" title="Go back" role="group" aria-label="First group"><a href="#" class="btn btn-primary text-center">  <i class="bi-gear"></i> Set up </a></div>
</div>
</div>

</div>
</div>

<div class="container mb-4">
<div class="row">
<div class="col-md-4 pt-3 pb-3 shadow border-end">
    <div class="d-flex m-2 mt-0 mb-0">
    <i class="bi-cloud" style="font-size: 2.5rem; color: cornflowerblue;"></i>
    <div>
        <big class="m-3 mb-0 text-muted">Crop name</big>
        <p class="m-3 mt-0 lead"> Cassava </p>
    </div>
</div>
</div>

<div class="col-md-4 pt-3 pb-3 shadow border-end">
    <div class="d-flex m-2 mt-0 mb-0">
    <i class="bi-rulers" style="font-size: 2.5rem; color: cornflowerblue;"></i>
    <div>
        <big class="m-3 mb-0 text-muted">Area</big>
        <p class="m-3 mt-0 lead"> 53 Acre </p>
    </div>
</div>
</div>

<div class="col-md-4 pt-3 pb-3 mt-2 shadow">
    <div class="d-flex m-2 mt-0 mb-0">
    <i class="bi-tree" style="font-size: 2.5rem; color: cornflowerblue;"></i>
    <div>
        <big class="m-3 mb-0 text-muted">Last production</big>
        <p class="m-3 mt-0 lead"> 1200 kg </p>
    </div>
</div>
</div>

</div>
</div>

<div class="container mb-4">
<div class="row justify-content-between">
<div class="col-md-3 pt-3 pb-3 shadow">
<div class="row">
   <div class="col-md-12 pt-3 pb-3  border-bottom">
        <div class="d-flex m-2 mt-0 mb-0">
        <div class="">
        <div class="row">
            <div class="col-12"><big class="text-muted">Air temperature</big></div>
            <div class="col"><big class="mt-4 mt-0 mt-1"> 38 <sup>o</sup> C  </big></div>
            <div class="col"><big class="p-1 pt-0 pb-0 btn btn-outline-danger">High</big></div>
        </div>
        </div>
        </div>   
    </div>

   <div class="col-md-12 pt-3 pb-3  border-bottom">
        <div class="d-flex m-2 mt-0 mb-0">
        <div class="">
        <div class="row">
            <div class="col-12"><big class="text-muted">Water content</big></div>
            <div class="col"><big class="mt-4 mt-0 mt-1"> 32%  </big></div>
            <div class="col"><big class="p-1 pt-0 pb-0 btn btn-outline-success">Good</big></div>
        </div>
        </div>
        </div>   
    </div> 

   <div class="col-md-12 pt-3 pb-3  border-bottom">
        <div class="d-flex m-2 mt-0 mb-0">
        <div class="">
        <div class="row">
            <div class="col-12"><big class="text-muted">pH value</big></div>
            <div class="col"><big class="mt-4 mt-0 mt-1"> 8  </big></div>
            <div class="col"><big class="p-1 pt-0 pb-0 btn btn-outline-warning">Base</big></div>
        </div>
        </div>
        </div>   
    </div> 
</div>
</div>

<div class="col-md-3 pt-3 pb-3 shadow">
<div class="row">
   <div class="col-md-12 pt-3 pb-3  border-bottom">
        <div class="d-flex m-2 mt-0 mb-0">
        <div class="">
        <div class="row">
            <div class="col-12"><big class="text-muted">Soil temperature</big></div>
            <div class="col"><big class="mt-4 mt-0 mt-1"> 65 to 75 F  </big></div>
            <div class="col"><big class="p-1 pt-0 pb-0 btn btn-outline-danger">High</big></div>
        </div>
        </div>
        </div>   
    </div>

   <div class="col-md-12 pt-3 pb-3  border-bottom">
        <div class="d-flex m-2 mt-0 mb-0">
        <div class="">
        <div class="row">
            <div class="col-12"><big class="text-muted">Maisture Level</big></div>
            <div class="col"><big class="mt-4 mt-0 mt-1"> 35%  </big></div>
            <div class="col"><big class="p-1 pt-0 pb-0 btn btn-outline-success">Good</big></div>
        </div>
        </div>
        </div>   
    </div> 

   <div class="col-md-12 pt-3 pb-3  border-bottom">
        <div class="d-flex m-2 mt-0 mb-0">
        <div class="">
        <div class="row">
            <div class="col-12"><big class="text-muted">Pressure value</big></div>
            <div class="col"><big class="mt-4 mt-0 mt-1"> 90/60mmHg  </big></div>
            <div class="col"><big class="p-1 pt-0 pb-0 btn btn-outline-warning">Good</big></div>
        </div>
        </div>
        </div>   
    </div> 
</div>
</div>

<div class="col-md-6 pt-3 pb-3 shadow">
<div class="row">
    <div class="col">
    <p class="m-3 mb-0 lead">Financial statistics</p>
    <small class="m-3 mt-0 text-muted">Compare with last time</small>
    </div>
    <div class="col">
    <div class="d-grid d-md-flex justify-content-md-end m-3 mb-0">
        <button class="btn btn-outline-secondary">All data <i class="bi-arrow-down-short"></i>   </button>
    </div>
    </div>
</div>

<div class="row ">
<div class="col mt-2 d-flex justify-content-center">
<div class="progress" style="height:200px; width:200px; border-radius:50%;">
    <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" style="width:35%" aria-valuenow="35" aria-valuemin="0" aria-valuemax="100">35%</div>
</div>
</div>
<div class="col">
<div class="row border m-3 rounded">
           <div class="col-md-12 pt-3 pb-3">
        <div class="d-flex m-2 mt-0 mb-0">
        <div class="">
        <div class="row">
            <div class="col-12"><big class="text-primary">Current profit</big></div>
            <div class="col"><big class="mt-4 mt-0 mt-1"> 64, 000 Naira  </big></div>
        </div>
        </div>
        </div>   
    </div>

   <div class="col-md-12 pt-3 pb-3  border-top">
        <div class="d-flex m-2 mt-0 mb-0">
        <div class="">
        <div class="row">
            <div class="col-12"><big class="text-primary">Expected profit</big></div>
            <div class="col"><big class="mt-4 mt-0 mt-1"> 64, 000 Naira  </big></div>
        </div>
        </div>
        </div>   
    </div> 
</div>

</div>
    </div>
    <div>
        
    <!-- </div> -->
</div>
</div>


</div>
</div>



<div class="container mb-4">
<div class="row">
    <div class="col-12"><p>Production details (2019)</p></div>
    <div class="col-12">
        <div class="row">
    <div class="col mt-2 d-flex justify-content-between">
        <div class="m-2 text-center">
        <small>2603 kg</small> <br>
        <small>60 % </small>
        <div class="progress bg-dark" style="height:200px; width:50px;">
        <div class="progress-bar" role="progressbar" style="width:65%" aria-valuenow="65" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small>January</small>
        </div>

        <div class="m-2 text-center">
        <small>1500 kg</small> <br>
        <small>20 % </small>
        <div class="progress bg-dark" style="height:200px; width:50px;">
        <div class="progress-bar" role="progressbar" style="width:35%" aria-valuenow="35" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small>February</small>
        </div>

           <div class="m-2 text-center">
        <small>1500 kg</small> <br>
        <small>0 % </small>
        <div class="progress bg-dark" style="height:200px; width:50px;">
        <div class="progress-bar" role="progressbar" style="width:0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small>March</small>
        </div>

           <div class="m-2 text-center">
        <small>1500 kg</small> <br>
        <small>0 % </small>
        <div class="progress bg-dark" style="height:200px; width:50px;">
        <div class="progress-bar" role="progressbar" style="width:0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small>April</small>
        </div>


           <div class="m-2 text-center">
        <small>1500 kg</small> <br>
        <small>0 % </small>
        <div class="progress bg-dark" style="height:200px; width:50px;">
        <div class="progress-bar" role="progressbar" style="width:0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small>May</small>
        </div>


           <div class="m-2 text-center">
        <small>1500 kg</small> <br>
        <small>0 % </small>
        <div class="progress bg-dark" style="height:200px; width:50px;">
        <div class="progress-bar" role="progressbar" style="width:0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small>June</small>
        </div>

                <div class="m-2 text-center">
        <small>1500 kg</small> <br>
        <small>20 % </small>
        <div class="progress bg-dark" style="height:200px; width:50px;">
        <div class="progress-bar" role="progressbar" style="width:35%" aria-valuenow="35" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small>July</small>
        </div>

           <div class="m-2 text-center">
        <small>1500 kg</small> <br>
        <small>0 % </small>
        <div class="progress bg-dark" style="height:200px; width:50px;">
        <div class="progress-bar" role="progressbar" style="width:0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small>August</small>
        </div>

           <div class="m-2 text-center">
        <small>1500 kg</small> <br>
        <small>0 % </small>
        <div class="progress bg-dark" style="height:200px; width:50px;">
        <div class="progress-bar" role="progressbar" style="width:0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small>September</small>
        </div>


           <div class="m-2 text-center">
        <small>1500 kg</small> <br>
        <small>0 % </small>
        <div class="progress bg-dark" style="height:200px; width:50px;">
        <div class="progress-bar" role="progressbar" style="width:0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small>October</small>
        </div>


           <div class="m-2 text-center">
        <small>1500 kg</small> <br>
        <small>0 % </small>
        <div class="progress bg-dark" style="height:200px; width:50px;">
        <div class="progress-bar" role="progressbar" style="width:0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small>November</small>
        </div>

           <div class="m-2 text-center">
        <small>2603 kg</small> <br>
        <small>60 % </small>
        <div class="progress bg-dark" style="height:200px; width:50px;">
        <div class="progress-bar" role="progressbar" style="width:65%" aria-valuenow="65" aria-valuemin="0" aria-valuemax="100"></div>
        </div>
        <small>December</small>
        </div>


</div>
           
        </div>
    </div>
</div>
</div>
</AdminHeader>
</div>
</template>

<style scoped>

</style>

<script>
// import axios from 'axios'
export default {
    data (){
        return{
        auth_check: false,
        token: '',
        alert: null,
        alertmodal: null,
        error: '',
        info: [],
        loader: false,
        loadermodal: false,
        classname: null,
        classnamemodal: null,
        submit: 'Submit',
        submittxt:'Submit',
        isDisabled: false,
        opacity_enable:'opacity:0.5; pointer-events:None;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
        errormodal: null,
        record:false,
        norecord:'',
    }
    },

    created(){
    // this.tokenize()
    }, 

    methods:{
     
    },


    }
</script>