<template>
<div>
<div class="col-md-10 col-md-offset-2 maindiv">
<div class="row p-1 m-0">
    <div class="col">
    <h4 class="">Result Upload</h4>
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
            <th>Name</th>
            <th>Matric</th>
            <th>Level</th>
            <th>Semester</th>
            <th>Phone</th>
            <th>Courses</th>
            <th>GPA</th>
            <th>CGPA</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="(d, index) in info" :key="index">
            <td>{{d[1]}} {{d[2]}}</td>
            <td>{{d[4]}}</td>
            <td>{{d[5]}}</td>
            <td>{{d[6]}}</td>
            <td>{{d[7]}}</td>
            <td>{{d[8]}}</td>
            <td>{{d[9]}}</td>
            <td>{{d[10]}}</td>


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
            token:'',
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
            fd.append('file', this.selectedFile, this.selectedFile.name)
            // fd.append('csrfmiddlewaretoken', this.token)
            axios.post('/api/upload_sms_list/', fd, {

                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            })

            .then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
            }).catch((error)=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert=error

            })
        },
        preview: function(){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait....'
            axios.get('/api/get_sms_list/')
            .then(response => {
               if(response.data.status == response.data.confirmed){
                this.alert=''
                this.classname=''
                this.info = response.data.result
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