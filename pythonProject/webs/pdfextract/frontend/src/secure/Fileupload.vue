<template>
<div>
<div class="col-md-10 col-md-offset-2 maindiv">
<div class="container">
    <div class="row">
        <div v-bind:class="classname">{{alert}}</div>
    <div class="border p-2">
        <form @submit.prevent="onUpload">
<div class="row form-inline mb-3  d-flex justify-content-end">
<div class="col-md-7 mt-2 ">
    <div class="input-group">
    <input type="file" @change="onFileSelected" class="form-control" required>
    <input type="text" v-model="notetitle" class="form-control" placeholder="Untitled note" required>
    <button type="button" class="btn btn-secondary">Title</button>
</div>
</div>

<div class="col-md-5 mt-2">
<div class="input-group justify-content-end">
 <button class="btn btn-primary m-1 mb-0">Save</button>
 <button type="button" class="btn btn-warning m-1 mb-0" @click="preview">Preview</button>
</div>
</div>

</div>
    </form>
    </div>


</div>


<div class="row border p-2 m-0">
<div class="col-12">
    <h2>Your Files</h2>
    <div class="table-responsive">
<table id="user-table" class="table table-bordered nowrap" cellspacing="0" width="100%">
    <!-- {{sms}} -->
    <thead>
        <tr>
            <th>ID</th>
            <th>File Title</th>
            <th>Date uploaded</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="(d, index) in info" :key="index">
            <td>{{d[3]}}</td>
            <td>{{d[2]}}</td>
            <td>{{d[5]}}</td>
            <td><a :href="'/oath/extract?filename='+d[3]+'&title='+d[2]" class="btn btn-primary">Extract</a></td>
        </tr>
    </tbody>

</table>


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
            alert:'',
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

        onFileSelected(event){
            this.selectedFile = event.target.files[0]
        },
        onUpload(){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait....'
            const fd = new FormData();
            fd.append('image', this.selectedFile, this.selectedFile.name)
            fd.append('notetitle', this.notetitle)
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

         preview(){
               this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while processing....'
            axios.get('/api/file_uploads/',{
                }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.info = response.data.result
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Request failed, please try again' 

            })
        },
       

    },
    //end of methods
    created(){
        this.preview()
    }

}
</script>