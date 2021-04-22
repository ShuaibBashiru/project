<template>
<div>
    <AdminHeader/>
    <div class="col-md-10 col-md-offset-2 col-12 maindiv">
<section v-if="loader==false">
<div class="col m-2 mt-0 mb-1"><div v-bind:class="classname">{{alert}}</div></div>

<div class="container">
<div class="row">
<div class="col-md-4">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-primary"><i class="bi-person-plus" style="font-size: 1.5rem;"></i> Widgets </h5>
</div>
</div>
<div class="col-md-8 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" role="group" aria-label="First group" @click="$router.go(-1)"><a href="#" class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> Back </a></div>
<div class="btn-group m-2" role="group" aria-label="First group"><a href="#" onclick="location.reload()" class="btn btn-outline-secondary text-center">  <i class="bi-arrow-clockwise"></i> Refresh </a></div>
<div class="btn-group m-2" role="group" aria-label="First group"><a href="/secure/widgets" class="btn btn-outline-primary text-center">  <i class="bi-list"></i> Records </a></div>
</div>

</div>
</div>
</div>
<div class="container">
<div class="border">
<div class="row">
<div class="col-md-12">
    <div class="p-2">
            <form @submit.prevent="formCheck" class="needs-validation">
            <fieldset class="border p-2 pt-0">
                <legend class="w-auto" style="float: none; padding: inherit;">New</legend>
            <div class="row">
            <div class="col-md-5">
                <div class="m-1">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info">Widget</button>
                    
                   <select v-model="widget" class="form-control" id="widget" required>
                       <option disabled value="" selected>Select</option>
                       <option value="Banner">Banner</option>
                       <option value="Slider_single_row">Slider-Single-Row</option>
                       <option value="Slider_double_row">Slider-Double-Row</option>
                       <option value="List_three_columns">List-Three-Columns</option>
                       <option value="List_Four_columns">List-Four-Columns</option>
                       <option value="Testimonie">Testimonies</option>
                       <option value="Partners">Partners</option>
                   </select>
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger">{{err_widget}}</small>
                
                </div>
            </div>
         <div class="col-md-5">
                <div class="m-1">
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info">Title</button>
                    <input type="text" name="title" v-model="title" class="form-control" required placeholder="Name this widget for quick reference">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger">{{err_title}}</small>
                
                </div>
            </div>

            <div class="col-md-2 d-flex justify-content-end">
                <div class="m-1">
                <div class="input-group">
                    <button type="submit" :disabled="isDisabled" class="btn btn-primary">{{submit}}</button>
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
</div>
</div>
    
</section>
<section v-else>
   <div class="container-fluid">
       <div class="row mt-5 ">
           <div class="col-12 mt-5 d-flex justify-content-center">
<div class="lds-roller"><div></div><div></div><div></div></div>
           </div>
           <div class="col-12 mt-5 d-flex justify-content-center"><small></small></div>
       </div>
   </div>
</section>
</div>

</div>
</template>
<script>
import axios from 'axios'
export default {
    data (){
        return{
        auth_check: false,
        alert: null,
        checked: true,
        list_id: [],
        selectToggleValue:'',
        isChecked:false,
        alertmodal: null,
        token: null,
        widget: null,
        title: null,
        loader: false,
        err_widget: null,
        err_title: null,
        selectDefault:"Select",
        classname: null,
        submit:'Submit',
        submittxt:'Submit',
        isDisabled: false,
        error_btn: null,
    }
    },

    created(){
    this.tokenize()
    }, 

    methods:{
    formCheck: function(e){
        this.addwidget()
    e.preventDefault();
    },


    addwidget: function(){
        this.loader=true
    const form = new FormData();
        form.append('widget', this.widget)
        form.append('title', this.title)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/widget/', form)
        .then(response => {
        if(response.data.status==response.data.confirmed){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        }else{
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        }
        this.loader=false
    }).catch(()=>{
        this.loader=false
        this.classname='alert alert-danger p-1 text-center'
        this.alert='Check network connection or reload this page'
        this.submit=this.submittxt
    })  
    },

    tokenize: function(){
    const form = new FormData();
    form.append('token', Math.random(9,99999))
    axios.get('/auth/tokenize/',form, {
    }).then(response => {
        if(response.data.status==response.data.confirmed){
        this.token=response.data.key
        axios.defaults.headers.common['X-CSRF-TOKEN'] = response.data.key;
        }else{
        this.alert='Check network connection or reload this page'
        }
        
    }).catch(()=>{
        this.classname='alert alert-danger p-1 text-center'
       this.alert='Check network connection or reload this page'

    })
    },

    },


    }
</script>