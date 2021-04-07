<template>
<div>
<div class="col-md-10 col-md-offset-2 maindiv">
<div class="container">
    <div class="row">
        <div v-bind:class="classname">{{alert}}</div>
    <div class="border p-2">
<div class="row form-inline mb-3  d-flex justify-content-end">
<div class="col-md-7 mt-2 ">
    <div class="input-group">
    <button class="btn btn-secondary">Title</button>
    <input type="text" v-model="notetitle" maxlength="100" class="form-control" placeholder="Untitled note">
    <input type="email" v-model="username" maxlength="100" class="form-control" placeholder="Email">
    <button class="btn btn-secondary">Email</button>

</div>
</div>


<div class="col-md-5 mt-2">
<div class="input-group justify-content-end">
 <button class="btn btn-secondary m-1 mb-0" @click="checkForm">Extract</button>
 <button class="btn btn-primary m-1 mb-0" @click="checkSummary">Save</button>
</div>
</div>

</div>
    </div>


</div>
<div class="row mt-2">
<div class="col-md-12 p-0">
    <div class="row">
        <div class="col-md-8">
    <form @submit.prevent="uploadCheck">
    <div class="input-group">
    <input type="file" @change="onFileSelected" class="form-control" required>
    <button type="submit" class="btn btn-primary"><i class="bi-plus"></i> Upload file</button>
    </div>
        </form>
        </div>

        <div class="col-md-4 border-start">
         <p class="lead p-0 m-0 text-center bg-secondary text-white">Output{{summaryLenght}}</p>
        </div>
    </div>
    </div>
</div>

<div class="row mt-2">
<div class="col-md-12 p-0 border-bottom border-top border-start border-end">
    <div class="row">
        <div class="col-md-8">
            <textarea v-model="notes" class="w-100 m-1 p-2" style="min-height:300px;">
                </textarea>
        </div>

        <div class="col-md-4 border-start">
            <textarea v-model="summary" class="w-100 p-2" style="min-height:300px;">
                </textarea>
        </div>
    </div>
    </div>
</div>





</div>
</div>
</div>
</template>
<style scoped>
.col-4 h3{
    font-size: 16px;
}
</style>
<script>
import axios from 'axios';
export default{
    data(){
        return {
            info:[],
            username:null,
            notetitle:null,
            notes:null,
            summary:null,
            alert:null,
            progress:null,
            summaryLenght:null,
            originalLenght:null,
            passport:null,
            selectedFile: null,
            fileurl:null,
            imgError:null,
            classname:' ',

        }
    },
    methods:{
        checkForm: function(){
      if(this.notes == null){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='You can not summarize empty Note'
        }else{
            this.summarize()
        }

        },

        uploadCheck: function(){
        if(this.notetitle == null){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Please enter your Note Title'
        }else if(this.username == null){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Your email is required'
        }else{
            this.onUpload()
        }

        },


    checkSummary: function(){
        if(this.notetitle == null){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Please enter your Note Title'
        }else if(this.notes == null){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='You can not summarize empty Note'
        }else if(this.summary == null){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='You do not have any text summarized'
        }else if(this.username == null){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Your email is required'
        }else{
            this.savesummary()
        }

        },

        onFileSelected(event){
            this.selectedFile = event.target.files[0]
        },
        onUpload(){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait....'
            const fd = new FormData();
            fd.append('image', this.selectedFile, this.selectedFile.name)
            axios.post('/api/upload/', fd, {

                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            })

            .then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
            }).catch((error)=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert="Error: " + error

            })
        },

           summarize(){
               this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while processing....'
            axios.get('/api/summarize/',{
            params: {
                    notes: this.notes,
                    notetitle: this.notetitle,
                    username: this.username,
                },
                }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.summary = response.data.result
                this.summaryLenght = '(Length: '+ response.data.summaryLenght +')'
                this.originalLenght = '(Length '+ response.data.originalLenght +')'
                console.log(response)
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Request failed, Please note that the number of particles must not be less than the function variable' 

            })
        },
       
         savesummary(){
               this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while processing....'
            axios.get('/api/savesummary/',{
            params: {
                    notes: this.notes,
                    notetitle: this.notetitle,
                    username: this.username,
                    summary: this.summary,
                },
                }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.summarynote = response.data.result
                console.log(response)
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Request failed, Please note that the number of particles must not be less than the function variable' 

            })
        },
       

    },
    //end of methods

}
</script>