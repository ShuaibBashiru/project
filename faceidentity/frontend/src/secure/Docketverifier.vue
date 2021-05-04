<template>
    <div>
<div class="col-md-10 col-md-offset-2 mt-1 maindiv">
   <div v-bind:class="classname">{{alert}}</div>

        <div class="container">
            <div class="row">
                <div class="col-md-6">
        <h1 class="">Docket verification</h1>
                </div>
                <!-- {{filename}} -->
                <div class="col-md-6 d-flex justify-content-center">
            <img :src="require('@/assets/passport/'+ filename )" width="150" height="150" alt="img" class="float-right rounded">
                </div>
            </div>

<div class="row">
    <div class="col-md-6 mt-1">
        <!-- <form > -->
        <div class="border p-2">
        <div class="form-group">
            <div class="row">
            <div class="col-md"> 
            <label for="id" class="mb-1">Enter your ID</label>
            <input type="text" v-model="myInput" style="text-transform:uppercase;" required name="myInput" maxlength="20" class="form-control" placeholder="Your ID">
            </div>
            </div>
        </div>

          <div class="form-group mt-3">
            <label for="id" class="text-muted"> <strong>Note:</strong>   Only the registered ID is allowed</label>
        </div>
           <div class="btn-group mt-3 d-flex">
            <button class="btn btn-primary m-1" @click="identifyUsingDocket"> <i class="bi-person"></i> Proceed</button>
        </div>


        </div>
 <!-- </form> -->

       
    </div>

    <div class="col-md-6 mt-1">
        <div class="border p-2">
                <div class="table-responsive">
<table id="user-table" class="table table-bordered nowrap" cellspacing="0" width="100%">
    <!-- {{sms}} -->
    <thead>
        <tr>
            <th>Name</th>
            <th>Code</th>
            <th>Title</th>
            <th>Unit</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="(d, index) in record" :key="index">
            <td>{{d[1]}}</td>
            <td>{{d[6]}}</td>
            <td>{{d[7]}}</td>
            <td>{{d[8]}}</td>
        </tr>
    </tbody>

</table>


    </div>
        </div>
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
            alert:null,
            progress:null,
            biodata:null,
            record:[],
            myInput:'',
            loader: '',
            classname:'',
            filename:'avatar.png',
            selectedFile: null
        }
    },

    methods:{

        identifyUsingDocket(){
          const fd = new FormData()
          fd.append('userid', this.myInput)
            axios.post('http://127.0.0.1:8000/faceRecognition/docket_id/23/', fd, {
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            })

            .then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.record=response.data.row
                this.filename=response.data.filename
                console.log(response)
            }).catch((error)=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Error connecting to server. Try again'     
                console.log(error)

            })
        },


    }
    // end of method

}
</script>
<style scoped>
input{
    text-transform: uppercase;
}
</style>