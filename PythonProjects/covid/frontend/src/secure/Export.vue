<template>
<div>
<div class="col-md-10 col-md-offset-2 maindiv">
<div class="row p-1 m-0">
    <div class="col">
    <h4 class="">Upload</h4>
    </div>
</div>
<div class="container">
    <div class="row">
        <div class="col-12">
            <div v-bind:class="classname">{{alert}}</div>
<div class="row border p-2 m-0 mt-2">
    <div class="col-md-5 d-flex justify-content-start">
        <form @submit.prevent="onUpload">
    <div class="input-group">
    <input type="file" @change="onFileSelected" class="form-control" required>
    <button type="submit" class="btn btn-primary"><i class="bi-plus"></i> Upload CSV</button>
    </div>
        </form>
    </div>
    <div class="col-md-7 d-flex justify-content-end" @click="preview"><button class="btn btn-primary"><i class="bi-eye"></i> Preview</button></div>
</div>

<div class="row border p-2 m-0">
<div class="col-12">
    <div class="table-responsive">
        <!-- <input type="text" id="myInput" placeholder="Search"> -->
<table id="searchTable" class="table table-bordered nowrap" cellspacing="0" width="100%">
  <thead>
        <tr>
        <th>S/N</th>
        <th>test_date</th>
        <th>cough</th>
        <th>fever</th>
        <th>sore_throat</th>
        <th>shortness_of_breath</th>
        <th>head_ache</th>
        <th>gender</th>
        <th>test_indication</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="(d, index) in info" :key="index">
            <td>{{index + 1}}</td>
            <td>{{d[2]}}</td>
            <td>{{d[3]}}</td>
            <td>{{d[4]}}</td>
            <td>{{d[5]}}</td>
            <td>{{d[6]}}</td>
            <td>{{d[7]}}</td>
            <td>{{d[8]}}</td>
            <td>{{d[9]}}</td>
        </tr>

    </tbody>

</table>


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
import axios from 'axios';
export default{
    data(){
        return {
            info:"",
            alert:null,
            progress:null,
            passport:null,
            bulk:'',
            classname:'',
            selectedFile: null,
            fileurl:null,
            imgError:null
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
        preview: function(){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait....'
            axios.get('/api/list_dataset/',{
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            })

            .then(response => {
                if(response.data.row){
                this.info=response.data.row
                 this.alert=''
                this.classname=''
                console.log(response.data.row)
                }else{
                this.alert=response.data.msg
                this.classname=response.data.classname
                }
           
            }).catch((error)=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert=error

            })
        },
        
    },
    
    // Methods end
    created() {
        this.preview()
  }
}
</script>