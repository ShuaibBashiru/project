<template>
<div>
<div class="col-md-10 col-md-offset-2 maindiv">
<div class="container">
    <div class="row">
        <div v-bind:class="classname">{{alert}}</div>
    <div class="border p-2">
    <p class="lead">Summaries</p>

<div class="row form-inline mb-3  d-flex justify-content-end">
<div class="col-md-7 mt-2">
    <div class="input-group">
    <button class="btn btn-secondary">Email</button>
    <input type="email" v-model="username" maxlength="100" class="form-control" placeholder="Email">
</div>
</div>


<div class="col-md-5 mt-2">
<div class="input-group justify-content-end">
 <button class="btn btn-primary m-1 mb-0" @click="checkForm">Preview</button>
</div>
</div>
</div>
</div>


</div>

<div class="row mt-2">
<div class="col-md-12 p-0 border-bottom border-top border-start border-end">
    <div class="row">
        <div class="col-md-12">

 <div class="table-responsive">
    <table class="table table-striped">
        <thead>

            <tr>
                <th>S/N</th>
                <th>Title</th>
                <th>Notes</th>
                <th>Summary</th>
                <th>Date Created</th>

            </tr>
        </thead>
        <tbody>
            
        <tr v-for="(d, index) in info" :key="index">
            <td>{{index + 1}}</td>
            <td>{{d[1]}}</td>
            <td>{{d[2]}}</td>
            <td>{{d[3]}}</td>
            <td>{{d[4]}}</td>
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
            info:"",
            username:null,
            alert:null,
            progress:null,
            classname:' ',
        }
    },
    methods:{
        checkForm: function(){
      if(this.username == null){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Your email is required'
        }else{
            this.preview()
        }

        },
         preview(){
               this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while processing....'
            axios.get('/api/listsummary/',{
            params: {
                username: this.username
                },
                }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.info = response.data.row
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