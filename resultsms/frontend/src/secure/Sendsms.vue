<template>
<div>
<div class="col-md-10 col-md-offset-2 maindiv">
<div class="row p-1 m-0">
    <div class="col">
    <h4 class="">Result Notification</h4>
    </div>
</div>
<div class="container">
    <div class="row">
        <div class="col-12">
            <div v-bind:class="classname">{{alert}}</div>
<div class="row border p-2 m-0 mt-2">
    <div class="col-md-8 d-flex justify-content-start">
        <form @submit.prevent="preview">
                <div class="row">
                    <div class="col-md-3">
                <div class="input-group">
                    <button type="button" class="btn btn-secondary">Level</button>
                    <select class="form-select p-0" v-model="levelName" :disabled="isDisabled" id="gender" required>
                    <option value="HND 1">HND 1</option>
                    <option value="HND 2">HND 2</option>
                    <option value="HND 3">HND 3</option>
                    <option value="ND 1">ND 1</option>
                    <option value="ND 2">ND 2</option>
                    <option value="ND 3">ND 3</option>
                    </select>
                    </div>
                    </div>
                <div class="col-md-3">
                <div class="input-group">
                    <button type="button" class="btn btn-secondary">Semester</button>
                <select class="form-select p-0" v-model="semester" :disabled="isDisabled" required>
                    <option value="First semester">First semester</option>
                    <option value="Second semester">Second semester</option>
                </select>
                    </div>
                </div>

                    <div class="col-md-3">
                <div class="input-group">
                    <button type="button" class="btn btn-secondary">Program</button>
                <select class="form-select p-0" v-model="program_type" :disabled="isDisabled" required>
                    <option value="Part Time">Part Time</option>
                    <option value="Full Time">Full Time</option>
                </select>
                    </div>
                </div>
                    <div class="col-md-3">
                        <div class="input-group">
                        <button class="btn btn-warning"><i class="bi-eye"></i> Preview</button>
                    </div>
                    </div>
                    </div>
        </form>
    </div>
    <div class="col-md-4 d-flex justify-content-end" @click="sendsms"><button class="btn btn-primary"><i class="bi-eye"></i> Disseminate </button></div>
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
            program_type:null,
            levelName: null,
            semester:null,
            bulk:'',
            classname:'',
            token:'',
            selectedFile: null,
            fileurl:null,
            imgError:null,
            isDisabled:false,
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
        preview(){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait....'
            axios.get('/api/get_sms_list_select/',
            {
                params:{
                    levelName: this.levelName,
                    semester: this.semester,
                    program_type: this.program_type,
                }
            })
            .then(response => {
               if(response.data.status == response.data.confirmed){
                this.alert=''
                this.classname=''
                this.info = response.data.result
               }else{
                this.info = ''
                this.alert=response.data.msg
                this.classname=response.data.classname
                }
               
            }).catch((error)=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert=error

            })
        },

        sendsms(){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait....'
            axios.get('/api/send_sms/',
            {
                params:{
                    levelName: this.levelName,
                    semester: this.semester,
                    program_type: this.program_type,
                }
            })
            .then(response => {
               if(response.data.status == response.data.confirmed){
                this.alert=response.data.msg
                 this.classname=response.data.classname
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
}
</script>