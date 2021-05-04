<template>
<div>
<div class="col-md-10 col-md-offset-2 maindiv">
<div class="container">
    <div class="row">
<div class="col-md-6">

</div>

    </div>
    <div class="row">

        <div class="col-md-12">
  <div  class="border p-2">
<form @submit.prevent="uploadfile">
    <div class="row form-inline mb-3">
<div class="col-md-6">
<div class="m-1">
    <div class="input-group">
    <input type="file" class="form-control" @change="onFileSelected" required>
    <button class="btn btn-outline-primary" @click="onUpload">Upload</button>
</div>
</div>
</div>
<div class="col-md-6 d-flex justify-content-end">
    <div class="m-1">
    <button class="btn btn-primary" @click="preview">Preview</button>
    </div>
</div>
</div>
</form>

<div class="row border p-2 m-0">
<div class="col-12">
</div>
</div>
</div>
<!-- End of wrapper -->
    </div>
</div>

</div>
</div>
</div>
</template>


<script>

</script>
<style>

</style>

<script>
import axios from 'axios';
export default{
    data(){
        return {
            info:[],
            selectedFile: null
        }
    },
    methods:{
        onFileSelected(event){
            this.selectedFile = event.target.files[0]
        },
        onUpload(){
            const fd = new FormData();
            fd.append('image', this.selectedFile, this.selectedFile.name)
            axios.post('/api/upload_pay/', fd,{
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                this.alert='Please wait...'
                this.classname='alert-primary text-center p-1'
               }
            }).then(response => {
                if(response.data.status==response.data.confirmed){
                this.token=response.data.key
                axios.defaults.headers.common['X-CSRF-TOKEN'] = response.data.key;
                }else{
                this.alert=response.data.msg
                }
              
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Error connecting.., try again.'

            })
        },

        preview(){
            const fd = new FormData();
            fd.append('null', 'null')
            axios.get('/api/upload_pay/', fd,{
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                this.alert='Please wait...'
                this.classname='alert-primary text-center p-1'
               }
            }).then(response => {
                if(response.data.status==response.data.confirmed){
                this.token=response.data.key
                axios.defaults.headers.common['X-CSRF-TOKEN'] = response.data.key;
                }else{
                this.alert=response.data.msg
                }
              
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Error connecting.., try again.'

            })
        },

    }
}
</script>