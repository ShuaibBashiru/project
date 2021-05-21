
<template>
<div :style="opacity">
<AdminHeader>
    <div class="container mt-2">
        <div class="row">
            <div class="col">
            <div v-bind:class="'alert '+ classname + ' p-2 text-center'">{{alert}}</div>
            </div>
        </div>
    </div>
<div class="container">
<div class="row">
<div class="col-md-4">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-primary"> Menus </h5>
</div>
</div>
<div class="col-md-8 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" title="Go back" role="group" aria-label="First group" @click="$router.go(-1)"><a href="#" class="btn btn-outline-primary text-center">  <i class="bi-arrow-left"></i>  </a></div>
<div class="btn-group m-2" title="Records" role="group" aria-label="First group"><a href="/secure/adminmenus" class="btn btn-outline-secondary text-center">  <i class="bi-list"></i> </a></div>
<div class="btn-group m-2" title="Refresh" role="group" aria-label="First group"><a href="#" onclick="location.reload()" class="btn btn-outline-primary text-center">  <i class="bi-arrow-clockwise"></i>  </a></div>

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
                    <span class="input-group-text">Category</span>
                    <select v-model="category" class="form-control" id="menu" required>
                       <option disabled value="" selected>Select</option>
                        <option value="sidebar">Sidebar</option>

                   </select>
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>


            <div class="col-md-6">
                <div class="m-1">
                        <input type="hidden" class="d-none" v-model="token" required readonly>
                <div class="input-group">
                    <span class="input-group-text">Icon</span>
                    <select v-model="menuicon" class="form-control" required>
                       <option disabled value="">Select</option>
                        <option value="bi-bricks">bi-bricks</option>
                       <option value="bi-list">bi-list</option>
                       <option value="bi-list-check">bi-list-check</option>
                       <option value="bi-card-checklist">bi-card-checklist</option>
                       <option value=">">None</option>
                   </select>
                    <span class="input-group-text"><i :class="menuicon"></i></span>
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>
         <div class="col-md-6">
                <div class="m-1">
                <div class="input-group">
                     <span class="input-group-text">Menu</span>
                    <input type="text" name="menu" v-model="menuname" class="form-control" required placeholder="Type here">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
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
</AdminHeader>

<!-- modal -->
</div>
</template>

<script>
import axios from 'axios'
export default {
    data (){
        return{
        auth_check: false,
        token: '',
        alert: null,
        alertmodal: null,
        error: '',
        info: [],
        checked: true,
        category: '',
        menuicon: '',
        menuname: null,
        loader: false,
        loadermodal: false,
        selectDefault:"Select",
        classname: null,
        classnamemodal: null,
        submit: 'Submit',
        submittxt:'Submit',
        isDisabled: false,
        opacity_enable:'opacity:0.5; pointer-events:None;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
        error_btn: null,
        errormodal: null,
        record:false,
        norecord:'',
    }
    },

    created(){
    this.tokenize()
    }, 

    methods:{
      formCheck: function(e){
        this.addNew()
    e.preventDefault();
    },
    addNew: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        this.submit='Please wait..'
        const form = new FormData();
        form.append('category', this.category)
        form.append('menuname', this.menuname)
        form.append('menuicon', this.menuicon)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/adminmenu/new/', form)
        .then(response => {
        if(response.data.status==response.data.statusmsg){
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        }else{
        this.classname=response.data.classname
        this.alert=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.opacity = this.opacity_disable
        }
    }).catch(()=>{
        this.classname='alert-danger'
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
      if(response.data.status==response.data.statusmsg){
      this.token=response.data.key
      axios.defaults.headers.common['X-CSRF-TOKEN'] = response.data.key;
      this.$Progress.finish()
      this.isDisabled = false
      }else{
      this.$Progress.finish()
      this.isDisabled = false
     this.classname='text-danger'
      this.alert=localStorage.getItem('error')
      }
    
  }).catch(()=>{
      this.$Progress.fail()
      this.isDisabled = false
      this.classname='text-danger'
      this.alert=localStorage.getItem('error')
  })
  },


    },


    }
</script>