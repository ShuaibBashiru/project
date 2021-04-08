<template>
<div>
    <AdminHeader/>
<div class="col-md-10 col-md-offset-2 maindiv">
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
<div class="btn-group m-2" role="group" aria-label="First group"><a href="#" class="btn btn-outline-secondary text-center" onClick="window.location.reload()">  <i class="bi-arrow-clockwise"></i> Refresh </a></div>

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
            <div class="col-md-6">
                <div class="m-1">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info"><i class="bi-bricks"></i></button>
                    <input type="text" v-model="widget" :disabled="isDisabled" id="widget" minlength="3" maxlength="100" class="form-control" required placeholder="New widget">
                    <button type="reset" class="btn btn-outline-info">X</button>
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger">{{err_widget}}</small>
                
                </div>
            </div>
            <div class="col-md-6 d-flex justify-content-end">
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

</div>
</div>
</template>
<script>
import axios from 'axios'
export default {
    data (){
        return{
        alert:null,
        alertmodal:null,
        token: null,
        widget: null,
        err_widget: null,
        selectDefault:"Select",
        classname:null,
        submit:'Submit',
        isDisabled:false,
        error_btn: null,
    }
    },
    created(){
    this.tokenize()
    },
    methods:{
    formCheck: function(e){
        if (this.widget==null || this.widget.lenght < 1) {
        this.err_email="Valid email required.";
        this.error_btn="Go back and check error message";
        }else{
            this.err_widget=""
            this.error_btn="";
        this.submit="Please wait.."
        this.addwidget()
        }
    e.preventDefault();
    },
    addwidget: function(){
    const form = new FormData();
        form.append('widget', this.widget)
        form.append('csrfmiddlewaretoken', this.token)
    axios.post('/posts/widget/', form)
        .then(response => {
        if(response.data.status==response.data.confirmed){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit="Submit"
        }else{
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit="Submit"
        }
        
    }).catch(()=>{
        this.classname='alert alert-danger p-1 text-center'
        this.alert='Error connecting, please try again.'
        this.submit="Submit"
    })  
    },

    // tokenize: function(){
    // const form = new FormData();
    // form.append('token', Math.random(9,99999))
    // axios.get('/auth/tokenize/',form, {
    // }).then(response => {
    //     if(response.data.status==response.data.confirmed){
    //     this.token=response.data.key
    //     axios.defaults.headers.common['X-CSRF-TOKEN'] = response.data.key;
    //     }else{
    //     this.alert='Kindly refresh or try again later.'
    //     }
        
    // }).catch(()=>{
    //     this.classname='alert alert-danger p-1 text-center'
    //    this.alert='Error connecting, please try again.'

    // })
    // },


    },


    }
</script>