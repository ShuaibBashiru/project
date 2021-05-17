
<template>
<div :style="opacity">
<AdminHeader>
<section v-if="record==true">
    <div class="container">
        <div class="row">
            <div class="col m-2 mt-0 mb-1">
            <div v-bind:class="classname">{{alert}}</div>
            </div>
        </div>
    </div>
<div class="container">
<div class="row">
<div class="col-md-4">
<div class="p-1 pb-0 ml-0 pl-0">

    <h5 class="mt-2 text-danger"> Trash </h5>
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
 <p class="text-danger p-3 pb-0 pt-0">Are you sure of what you are doing! Please confirm before you take this unrecoverable action.</p>
<form @submit.prevent="formCheck" class="needs-validation">
            <fieldset class="border p-2 pt-0">
                <legend class="w-auto" style="float: none; padding: inherit;">Record</legend>
            <div class="row">
            <div class="col-md-5">
                <div class="m-1">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                        <input type="hidden" class="d-none" v-model="keyid" required readonly>
                <div class="input-group">
                    <span class="input-group-text">Widget</span>
                    <input type="text" name="title" v-model="widget" class="form-control" disabled readonly>
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger">{{err_widget}}</small>
                
                </div>
            </div>
         <div class="col-md-5">
                <div class="m-1">
                <div class="input-group">
                    <span class="input-group-text">Title</span>
                    <input type="text" name="title" v-model="title" class="form-control" required readonly placeholder="Name this widget for quick reference">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger">{{err_title}}</small>
                
                </div>
            </div>

            <div class="col-md-2 d-flex justify-content-end">
                <div class="m-1">
                <div class="input-group">
                    <button type="submit" :disabled="isDisabled" class="btn btn-danger">{{submit}}</button>
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
<div class="container">
    <div class="row">
    <div class="col-12 mt-5 d-flex justify-content-center">
    <p class="lead text-danger mt-2">{{norecord}}</p> <br clear="all/">
    </div>
    <div class="col-12 mt-3 d-flex justify-content-center">
    <p class="m-2" @click="$router.go(-1)" :style="'display:'+backbtn"><a href="#" class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i> Back </a></p>
    </div>
    </div>
</div>
</section>
</AdminHeader>

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
        record:null,
        norecord:null,
        opacity_enable:'opacity:0.5; pointer-events:None;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
    }
    },

    created(){
    this.preview()
    this.tokenize()
    }, 

    methods:{
          formCheck: function(e){
        this.delete()
    e.preventDefault();
    },

       preview: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/api/validate_id/', {
            params:{
                'keyid': this.keyid_validate
            },
        })
        .then(response => {
            if(response.data.status == response.data.confirmed){
            this.alert=''
            this.classname=''
            this.norecord=''
            this.info = response.data.result
            this.widget = this.info['widgetName']
            this.title = this.info['widgetTitle']
            this.keyid = this.info['keyid']
            this.record = true
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable 
            }else{
            this.record = false
            this.classname=''
            this.alert=''
            this.norecord=response.data.msg
            this.classname=response.data.classname
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        }).catch(()=>{
            this.record = false
            this.classname=''
            this.alert=''
            this.norecord=localStorage.getItem('error')
            this.$Progress.fail()
            this.isDisabled = false
            this.opacity = this.opacity_disable
        })
    },

    delete: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        const form = new FormData();
        form.append('widget', this.widget)
        form.append('title', this.title)
        form.append('keyid', this.keyid)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/delete_widget/', form,{
        }).then(response => {
        if(response.data.status==response.data.confirmed){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        setInterval(function(){
        window.history.back()
        },3000)
        }else{
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        }
    }).catch(()=>{
        this.classname='alert alert-danger p-1 text-center'
        this.alert=localStorage.getItem('error')
        this.submit=this.submittxt
        this.$Progress.fail()
        this.isDisabled = false
        this.opacity = this.opacity_disable
    })  
    },

    tokenize: function(){
        this.$Progress.start()
      this.isDisabled = true
    axios.get('/auth/tokenize/',{
    params:{
      'token': Math.random(9, 9999)
    }
  }).then(response => {
      if(response.data.status==response.data.confirmed){
      this.token=response.data.key
      axios.defaults.headers.common['X-CSRF-TOKEN'] = response.data.key;
      this.$Progress.finish()
      this.isDisabled = false
      }else{
      this.$Progress.finish()
      this.isDisabled = false
      this.classname='alert alert-danger p-1 text-center'
      this.alert=localStorage.getItem('error')
      }
    
  }).catch(()=>{
        this.$Progress.fail()
      this.isDisabled = false
      this.classname='alert alert-danger p-1 text-center'
      this.alert=localStorage.getItem('error')
  })
  },

    },


    }
</script>