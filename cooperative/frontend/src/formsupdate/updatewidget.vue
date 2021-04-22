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
    <h5 class="mt-2 text-primary"><i class="bi-pencil-square" style="font-size: 1.5rem;"></i> Update Widgets </h5>
</div>
</div>
<div class="col-md-8 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" role="group" aria-label="First group" @click="$router.go(-1)"><a href="#" class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> Back </a></div>
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
                <legend class="w-auto" style="float: none; padding: inherit;">Update</legend>
            <div class="row">
            <div class="col-md-5">
                <div class="m-1">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                        <input type="hidden" class="d-none" v-model="keyid" required readonly>
                <div class="input-group">
                    <button type="button" class="btn btn-outline-info">Widget</button>
                    <input type="text" name="title" v-model="widget" class="form-control" disabled readonly>
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
<div class="lds-roller" :style="'display:'+loaderstatus"><div></div><div></div><div></div></div>
           </div>
           <div class="col-12 mt-5 d-flex justify-content-center">
   <p class="text-danger mt-2">{{norecord}}</p> <br clear="all/">
           </div>
 <div class="col-12 mt-5 d-flex justify-content-center">
<p class="m-2" @click="$router.go(-1)" :style="'display:'+backbtn"><a href="#" class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> Back </a></p>
           </div>
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
        info:[],
        auth_check: false,
        alert: null,
        checked: true,
        keyid_validate: this.$route.params.id,
        keyid:'',
        selectToggleValue:'',
        isChecked:false,
        alertmodal: null,
        token: null,
        widget: '',
        title: '',
        loader: false,
        err_widget: null,
        err_title: null,
        selectDefault:"Select",
        classname: null,
        submit:'Submit',
        submittxt:'Submit',
        isDisabled: false,
        error_btn: null,
        norecord:null,
        loaderstatus:'',
        backbtn:'none',
    }
    },

    created(){
    this.preview()
    this.tokenize()
    }, 

    methods:{
    formCheck: function(e){
        this.update()
    e.preventDefault();
    },

       preview: function(){
        axios.get('/api/validate_id/', {
            params:{
                'keyid': this.keyid_validate
            },
        }, this.loader=true, this.loaderstatus='block')
        .then(response => {
            if(response.data.status == response.data.confirmed){
            this.loader=false
            this.loaderstatus='none'
            this.backbtn='none'
            this.alert=''
            this.classname=''
            this.norecord=''
            this.info = response.data.result
            this.widget = this.info['widgetName']
            this.title = this.info['widgetTitle']
            this.keyid = this.info['keyid']
            this.record = false
            }else{
            this.loader=true
            this.loaderstatus='none'
            this.backbtn='block'
            this.record = true
            this.classname=''
            this.alert=''
            this.norecord=response.data.msg
            this.classname=response.data.classname
            }
        }).catch(()=>{
            this.loader=true
            this.loaderstatus='none'
            this.backbtn='block'
            this.record = true
            this.classname=''
            this.alert=''
            this.norecord='Check network connection or reload this page'
        })
    },

    update: function(){
    const form = new FormData();
        form.append('widget', this.widget)
        form.append('title', this.title)
        form.append('keyid', this.keyid)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/update_widget/', form,{
        },
         this.loader=true, this.loaderstatus='block' 
        ).then(response => {
        if(response.data.status==response.data.confirmed){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.loader=false
        this.loaderstatus='none'
        }else{
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
         this.loader=false
         this.loaderstatus='none'
        }
    }).catch(()=>{
        this.loader=false
        this.loaderstatus='none'
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