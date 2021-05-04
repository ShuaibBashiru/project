<template>
<div>
<div class="container-fluid">
    <div class="row">
        
<div class="col-md-12">
<div class="col m-2 mt-0 mb-1"><div v-bind:class="classname">{{alert}}</div></div>
<div class="container-fluid">
<div class="row">
<div class="col-md-4">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-primary"><i class="bi-person-plus" style="font-size: 1.5rem;"></i> Patient test </h5>
</div>
</div>
<div class="col-md-8 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" role="group" aria-label="First group"><a href="#" class="btn btn-outline-secondary text-center" onClick="window.location.reload()">  <i class="bi-arrow-clockwise"></i> Refresh </a></div>

</div>

</div>
</div>
</div>
<div class="container-fluid">
<div class="border">
<div class="row">
<div class="col-md-12">
    <div class="p-2">
            <form @submit.prevent="formCheck" class="needs-validation">
            <fieldset class="border p-2 pt-0">
                <legend class="w-auto" style="float: none; padding: inherit;">Enter your test results</legend>
            <div class="row">
         <div class="col-md-3">
                <div class="m-1">
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info">Glucose</button>
                    <input type="number" v-model="Glucose" maxlength="100" class="form-control" required placeholder="Glucose">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>

                     <div class="col-md-3">
                <div class="m-1">
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info">BloodPressure</button>
                    <input type="number" v-model="BloodPressure" maxlength="100" class="form-control" required placeholder="BloodPressure">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>

                     <div class="col-md-4">
                <div class="m-1">
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info">SkinThickness</button>
                    <input type="number" v-model="SkinThickness" maxlength="100" class="form-control" required placeholder="SkinThickness">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>

                     <div class="col-md-2">
                <div class="m-1">
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info">Insulin</button>
                    <input type="number" v-model="Insulin" maxlength="100" class="form-control" required placeholder="Insulin">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>


                     <div class="col-md-2">
                <div class="m-1">
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info">BMI</button>
                    <input type="number" v-model="BMI" maxlength="100" class="form-control" required placeholder="BMI">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>

                     <div class="col-md-3">
                <div class="m-1">
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info">Pedigree</button>
                    <input type="number" v-model="Pedigree" maxlength="100" class="form-control" required placeholder="Pedigree">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>

                     <div class="col-md-2">
                <div class="m-1">
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info">Age</button>
                    <input type="number" v-model="Age" maxlength="100" class="form-control" required placeholder="Age">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>

            <div class="col-md d-flex justify-content-end">
                <div class="m-1">
                <div class="input-group">
                    <button type="reset" class="btn btn-primary m-1">Reset</button>
                    <button type="submit" :disabled="isDisabled" class="btn btn-primary m-1">{{submit}}</button>
                </div>
                </div>
                    <small class="pb-2 text-danger text-center">{{error_btn}}</small>
            </div>


            
                </div>
                </fieldset>
            </form>
        
    </div>
</div>
</div>
<div class="row">
<div class="col-md-12">
    <div class="border p-5"> 
        <p class="lead text-justify">{{result}}</p>
    </div>
</div>


</div>
</div>
</div>

</div>


    </div>
</div>
</div>
</template>
<script>
import axios from 'axios'
export default {
    data (){
        return{
        alert: null,
        Glucose: null,
        BloodPressure: null,
        SkinThickness: null,
        Insulin: null,
        BMI: null,
        Pedigree: null,
        Age: null,
        result: null,
        selectDefault:"Select",
        classname: null,
        submit:'Check result',
        isDisabled: false,
        error_btn: null,
    }
    },

    methods:{
    formCheck: function(e){
     this.checktestresult()
    e.preventDefault();
    },
    checktestresult: function(){
    const form = new FormData();
        form.append('glucose', this.Glucose)
        form.append('bloodPressure', this.BloodPressure)
        form.append('skinThickness', this.SkinThickness)
        form.append('insulin', this.Insulin)
        form.append('bmi', this.BMI)
        form.append('pedigree', this.Pedigree)
        form.append('age', this.Age)
    axios.post('/api/classify/', form)
        .then(response => {
        if(response.data.status==response.data.confirmed){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.result=response.data.result
        this.submit="Check result"
        }else{
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit="Check result"
        }
        
    }).catch(()=>{
        this.classname='alert alert-danger p-1 text-center'
        this.alert='Error connecting, please try again.'
        this.submit="Submit"
    })  
    },



    },


    }
</script>