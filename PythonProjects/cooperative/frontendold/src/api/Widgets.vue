
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
<div class="col-md-4">
<div class="p-1 pb-0 ml-0 pl-0">
    <h5 class="mt-2 text-primary"> Widgets </h5>
</div>
</div>
<div class="col-md-8 p-0 d-flex justify-content-end">
<div class="btn-toolbar m-1" role="toolbar" aria-label="Toolbar with button groups">
<div class="btn-group m-2" title="New" role="group" aria-label="First group"><a href="#" class="text-center btn btn-default">  {{counter}} </a></div>
<div class="btn-group m-2" title="" role="group" aria-label="First group"><a href="/secure/newwidget" class="btn btn-outline-primary text-center">  <i class="bi-plus" style="font-size: 1rem;"></i> New </a></div>
<div class="btn-group m-2" title="Menu" role="group" aria-label="First group"><a href="#" class="btn btn-outline-secondary text-center dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false"> Menu </a>
  <ul class="dropdown-menu">
    <li class="p-2 pb-0 pt-0"><strong>Records</strong> </li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="listcounter">Update status</a></li>
    <li><hr class="dropdown-divider"></li>
    <li class="p-2 pb-0 pt-0"><strong>Download</strong> </li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#" @click="downloadfile" data-bs-toggle="modal" data-bs-target="#downloadbox">Excel</a></li>
  </ul></div>
<div class="btn-group m-2" title="Refresh" role="group" aria-label="First group"><a href="#" class="btn btn-outline-primary text-center" @click="preview">  <i class="bi-arrow-clockwise" style="font-size: 1rem;"></i> </a></div>

</div>

</div>
</div>
</div>

<div class="container">
<div class="border">
<div class="row">
<div class="col-md-12">
    <div class="p-2">
            <form @submit.prevent="searchby" class="needs-validation">
            <fieldset class="border p-2 pt-0">
                <legend class="w-auto" style="float: none; padding: inherit;"></legend>
            <div class="row">
            <div class="col-md-5">
                <div class="m-1">
                <div class="input-group">
                    <span class="input-group-text">Filter</span>
                   <select @change="filter()" v-model="filterlist" class="form-control" id="fitler">
                       <option disabled value="" selected>Select</option>
                       <option value="1">Active</option>
                       <option value="0">Inactive</option>
                   </select>
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger"></small>
                
                </div>
            </div>
         <div class="col-md-5">
                <div class="m-1">
                <div class="input-group">
                    <span class="input-group-text">Search</span>
                    <input type="text" name="search" v-model="search" maxlength="100" class="form-control" required placeholder="Type here">
                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger">{{error}}</small>
                
                </div>
            </div>

            <div class="col-md-2 d-flex justify-content-end">
                <div class="m-1">
                <div class="input-group">
                    <button type="submit" :disabled="isDisabled" class="btn btn-primary">{{searchbtn}}</button>
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

<div class="container">
    <div class="row">
        <div class="col-md-12">
            <section v-if="record==true">
            <div class="table-responsive">
     
                <table class="table border" id="myTable">
                    <thead>
                        <tr>
                            <!-- <th><div class="form-check"><input type="checkbox" @click="selectToggle(this)" v-model="selectToggleValue" class="form-check-input"></div></th> -->
                            <th><i class="bi-check-square btn p-0 text-primary"></i></th>
                            <th>Name</th>
                            <th>Title</th>
                            <th>Last Modified</th>
                            <th class="text-center">Status</th>
                            <th class="text-center">Edit</th>
                            <th class="text-center">Delete</th>
                        </tr>
                        <tr v-for="(d, index) in info" :key="index">
                            <td> <div class="form-check"><input type="checkbox" name="checkbox" :id="d['id']" :value="d['id']" v-model="list_id" class="form-check-input"></div> </td>
                            <td>{{d['widgetName']}}</td>
                            <td>{{d['widgetTitle']}}</td>
                            <td>{{d['date_modified']}} {{d['time_modified']}}</td>
                            <td class="text-center" v-if="d['status_id']==1"> <i class="bi-check-square btn p-0 text-primary"></i></td>
                            <td class="text-center" v-else> <i class="bi-x-square btn p-0 text-danger"></i></td>
                            <td class="text-center"> <a :href="'/secure/updatewidget/'+d['widgetTitle']+'/'+d['uniqueCode']+'?category='+d['widgetName']"><i class="bi-pencil-square btn p-0 text-primary"></i> </a></td>
                            <td class="text-center"> <a :href="'/secure/deletewidget/'+d['widgetTitle']+'/'+d['uniqueCode']+'?category='+d['widgetName']"><i class="bi-trash btn p-0 text-danger"></i> </a></td>
                        </tr>
                    </thead>
                </table>
            </div>
</section>
<section v-else>
    <p class="text-danger mt-2">{{norecord}}</p>
</section>

        </div>
    </div>
    </div>

</AdminHeader>

<!-- Modal container -->
<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
<form @submit.prevent="formCheckStatus" class="needs-validation">

      <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">Update status</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
                   <div class="row">
            <div class="col-md-12">
                <div class="col m-2 mt-0 mb-1"><div v-bind:class="classnamemodal">{{alertmodal}}</div></div>
                <div class="m-1">
                    <input type="hidden" class="form-control d-none" v-model="token" required readonly>
                    <input type="hidden" class="form-control d-none" v-model="get_list_array">
                    <p class="">You are updating <strong>{{selectedlist}}</strong> record(s)</p>
                <div class="input-group">
                    <span class="input-group-text">Status</span>
                   <select v-model="listStatus" class="form-control" id="fitler" required>
                       <option disabled value="" selected>Select</option>
                       <option value="1">Active</option>
                       <option value="0">Inactive</option>
                   </select>

                </div>
                <small class="form-text text-muted"></small>
                <small class="text-danger">{{errormodal}}</small>
                
                </div>
            </div>
                </div>
        
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="submit" :disabled="isDisabled" class="btn btn-primary">{{submit}}</button>
      </div>

</form>
    </div>
  </div>
</div>

<!-- modal -->
<div class="modal fade" id="downloadbox" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">

      <div class="modal-header">
        <h5 class="modal-title" id="staticBackdropLabel">Download File</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>

      <div class="modal-body">
                   <div class="row">
            <div class="col-md-12">
                <div class="m-1">
                    <p class="text-primary">{{downloadmsg}}</p>
                </div>
            </div>
                </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
       <section v-if="isdownload==true">
            <a :href="baseData" :download="baseDataname"><button type="submit" class="btn btn-primary">Download now</button></a>
       </section>
      </div>

    </div>
  </div>
</div>

</div>
</template>

<script>
import axios from 'axios'
import $ from "jquery";
export default {
    data (){
        return{
        auth_check: false,
        token: '',
        baseData: '',
        baseDataname: '',
        downloadmsg:'',
        isdownload:false,
        alert: null,
        alertmodal: null,
        error: '',
        info: [],
        filterlist:'',
        search:'',
        checked: true,
        list_id: [],
        get_list_array: '0',
        listStatus:null,
        selectToggleValue: '',
        selectedlist: null,
        isChecked:false,
        loader: false,
        loadermodal: false,
        selectDefault:"Select",
        classname: null,
        classnamemodal: null,
        submit: 'Submit',
        submittxt:'Submit',
        searchbtn:'Search',
        searchbtntxt:'Search',
        isDisabled: false,
        opacity_enable:'opacity:0.5; pointer-events:None;',
        opacity_disable:'opacity:1; pointer-events:All;',
        opacity:'',
        error_btn: null,
        errormodal: null,
        record:false,
        norecord:'',
        counter:'0'
    }
    },

    created(){
    this.preview()
    this.tokenize()
    }, 

    methods:{
    formCheckStatus: function(e){
        if (this.token.length < 1) {
        this.errormodal="Check network connection or reload this page";
        }else if(this.list_id.length < 1 || this.get_list_array.length < 1){
        this.errormodal="Please select the record(s) you wanted to update.";
        }else{
        this.updateStatus()
        }
    e.preventDefault();
    },
    updateStatus: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.submit='Please wait..'
        const form = new FormData();
        form.append('listStatus', this.listStatus)
        form.append('keyid', this.get_list_array)
        form.append('csrfmiddlewaretoken', this.token)
        axios.post('/posts/update_widget_status/', form)
        .then(response => {
        if(response.data.status==response.data.confirmed){
        this.classnamemodal=response.data.classname
        this.alertmodal=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false
        this.unselectAll();
        this.preview()
        }else{
        this.classnamemodal=response.data.classname
        this.alertmodal=response.data.msg
        this.submit=this.submittxt
        this.$Progress.finish()
        this.isDisabled = false

        }
    }).catch(()=>{
        this.classnamemodal='alert alert-danger p-1 text-center'
        this.alertmodal='Check network connection or reload this page'
        this.submit=this.submittxt
        this.$Progress.fail()
        this.isDisabled = false

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
      this.$Progress.fail()
      this.isDisabled = false
      this.classname='alert alert-danger p-1 text-center'
      this.alert='Check network connection or reload this page'
      }
    
  }).catch(()=>{
        this.$Progress.finish()
      this.isDisabled = false
      this.classname='alert alert-danger p-1 text-center'
      this.alert='Check network connection or reload this page'
  })
  },


    preview: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
        axios.get('/api/widget/',{})
        .then(response => {
            if(response.data.status == response.data.confirmed){
            this.alert=''
            this.classname=''
            this.info = response.data.result
            this.counter = 'Total: '+ this.info.length
            this.record = true
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }else{
            this.record = false
            this.counter = 'Total: 0'
            this.alert=''
            this.norecord=response.data.msg
            this.classname=''
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        
        }).catch(()=>{
            this.record = false
            this.norecord=''
            this.counter = 'Total: 0'
            this.classname='alert alert-danger p-1 text-center'
            this.alert='Check network connection or reload this page'
            this.$Progress.fail()
            this.isDisabled = true
            this.opacity = this.opacity_disable
        })
    },

       filter: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
       axios.get('/api/widgetfilter/', {
            params:{
                'status_id': this.filterlist
            }
        })
        .then(response => {
            if(response.data.status == response.data.confirmed){
            this.alert=''
            this.classname=''
            this.info = response.data.result
            this.counter = 'Total: '+ this.info.length
            this.record = true
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }else{
            this.record = false
            this.counter = 'Total: 0'
            this.alert=''
            this.norecord=response.data.msg
            this.classname=''
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        
        }).catch(()=>{
            this.record = false
            this.norecord=''
            this.counter = 'Total: 0'
            this.classname='alert alert-danger p-1 text-center'
            this.alert='Check network connection or reload this page'
            this.$Progress.fail()
            this.isDisabled = true
            this.opacity = this.opacity_disable
        })
    },
       searchby: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.opacity = this.opacity_enable
       axios.get('/api/widgetsearch/', {
            params:{
                'search': this.search
            }
        })
        .then(response => {
            if(response.data.status == response.data.confirmed){
            this.alert=''
            this.classname=''
            this.info = response.data.result
            this.counter = 'Total: '+ this.info.length
            this.record = true
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }else{
            this.record = false
            this.counter = 'Total: 0'
            this.alert=''
            this.norecord=response.data.msg
            this.classname=''
            this.$Progress.finish()
            this.isDisabled = false
            this.opacity = this.opacity_disable
            }
        
        }).catch(()=>{
            this.record = false
            this.norecord=''
            this.counter = 'Total: 0'
            this.classname='alert alert-danger p-1 text-center'
            this.alert='Check network connection or reload this page'
            this.$Progress.fail()
            this.isDisabled = true
            this.opacity = this.opacity_disable
        })
    },
        listcounter: function(){
        this.selectedlist = this.list_id.length
        this.get_list_array = this.list_id
        this.errormodal="";
        this.alertmodal="";
        this.classnamemodal="";
        },
  
  
        downloadfile: function(){
        this.$Progress.start()
        this.isDisabled = true
        this.downloadmsg='Please wait...'
        axios.get('/api/download_widget/', {
            params:{
                "filetype":"excel"
            }
        },  this.loader=true, this.loaderstatus='block')
        .then(response => {
           if(response.data.status == response.data.confirmed){
            this.alert=''
            this.classname=''
            this.record = true
            this.norecord=''
            this.downloadmsg = response.data.msg
            this.baseDataname=response.data.baseDataname
            this.baseData=response.data.baseData
            this.isdownload=true
            this.$Progress.finish()
            this.isDisabled = false
            }else{
            this.norecord=''
            this.downloadmsg=response.data.msg
            this.classname=''
            this.$Progress.finish()
            this.isDisabled = false
            }

        }).catch(()=>{
            this.norecord=''
            this.classname=''
            this.downloadmsg='Check network connection or reload this page'
            this.$Progress.finish()
            this.isDisabled = false
        })
    },

    selectToggle: function(){
    var checkboxes = document.getElementsByName('checkbox');
    if(this.selectToggleValue == false){
        var newlist=[]
        $(checkboxes).each(function() {
            this.checked = true;
            newlist.push(this.value)                        
        });
        this.list_id = newlist
    }else{
        $(checkboxes).each(function() {
            this.checked = false;
        });
        this.list_id = []

      }
        
          },
        unselectAll: function(){
        var checkboxes = document.getElementsByName('checkbox');
             $(checkboxes).each(function() {
            this.checked = false;
        });
        this.list_id = []
        },


    },


    }
</script>