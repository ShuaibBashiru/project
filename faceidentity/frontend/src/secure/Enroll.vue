<template>
<div>
<div class="col-md-10 col-md-offset-2 maindiv">
<div class="container">
    <div class="row">
        <div class="col-12">
            <!-- Start of wrapper -->
            <div v-bind:class="classname">{{alert}}</div>
<div class="row border p-2 m-0">
    <div class="col-md-4 d-flex justify-content-start">
    <button class="btn btn-primary" @click="startCamera"><i class="bi-camera"></i> Start Camera </button></div>
    <div class="col-md-4 d-flex justify-content-center"><button class="btn btn-default"><i class=""></i>{{progress}} </button></div>
    <div class="col-md-4 d-flex justify-content-end" @click="preview"><button class="btn btn-primary"><i class="bi-eye"></i> Preview</button></div>
</div>

<div class="row border p-2 m-0">
<div class="col-12">
    <h2>Face Enrollment</h2>
    <div class="table-responsive">
        <input type="search" v-model="myInput" class="mt-2 mb-2" placeholder="Enter user ID">
<table id="user-table" class="table table-bordered nowrap" cellspacing="0" width="100%">
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Program</th>
            <th>Department</th>
            <th>School</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="(d, index) in biodata" :key="index">
            <td>{{d[0]}}</td>
            <td>{{d[1]}} {{d[2]}} {{d[3]}}</td>
            <td>{{d[4]}}</td>
            <td>{{d[5]}}</td>
            <td>{{d[6]}}</td>
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
            info:[],
            alert:'',
            progress:null,
            biodata:null,
            myInput:'',
            classname:'',
            selectedFile: null
        }
    },
    methods:{
        onFileSelected(event){
            this.selectedFile = event.target.files[0]
        },
        startCamera(){
          const fd = new FormData()
          fd.append('userid', this.myInput)
            axios.post('http://127.0.0.1:8000/faceRecognition/capturephoto/23/', fd, {
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            })

            .then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                console.log(response)
            }).catch((error)=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert=error

            })
        },

        preview(){
            axios.get('http://127.0.0.1:8000/faceRecognition/bio_data/23/',{
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            })

            .then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.biodata=response.data.row
                console.log(response)
            }).catch((error)=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert="Error: " + error

            })
        },


    }
}
</script>