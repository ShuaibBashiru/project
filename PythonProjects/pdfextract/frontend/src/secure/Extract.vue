<template>
<div>
<div class="col-md-10 col-md-offset-2 maindiv">
<div class="container">
    <div class="row">
        <div v-bind:class="classname">{{alert}}</div>
    <div class="border p-2">

<div class="row form-inline mb-3">
<div class="col-md-6 border-end">
<form @submit.prevent="checkForm">
<div class="row">
    <div class="col-md-8 mt-2">
    <div class="input-group">
    <button class="btn btn-secondary">Page</button>
    <input type="number" v-model="from_num" name="from_num" class="form-control" placeholder="From?" required>
    <input type="number" v-model="to_num" name="to_num" class="form-control" placeholder="To?" required>
    <button class="btn btn-secondary">To</button>
</div>
</div>
<div class="col-md-4 mt-2">
<div class="input-group d-flex justify-content-end">
 <button class="btn btn-primary mb-0">Extract</button>
</div>
</div>
</div>
</form>
</div>

<div class="col-md-6">

<form @submit.prevent="edit">
<div class="row">
    <div class="col-md-10 mt-2">
    <div class="input-group">
    <textarea v-model="searchfor" name="search" class="form-control" placeholder="Search for ?" required></textarea>
    <textarea v-model="replacewith" name="search" class="form-control" placeholder="Replace with ?" required></textarea>
</div>
</div>
<div class="col-md-2 mt-2">
<div class="input-group d-flex justify-content-end">
 <button class="btn btn-primary  mb-0 pt-4 pb-4">Proceed</button>
</div>
</div>
</div>
</form>

</div>


</div>

    </div>


</div>
<div class="row mt-2">
<div class="col-md-12 p-0">
    <div class="row">
        <div class="col-md-6">
         <p class="lead p-0 m-0 text-center bg-secondary text-white">Original</p>
        </div>
               <div class="col-md-6">
         <p class="lead p-0 m-0 text-center bg-secondary text-white">Extract(s)</p>
        </div>
    </div>
    </div>
</div>
<div class="row mt-2">
<div class="col-md-12 p-0 border-bottom border-top border-start border-end">
    <div class="row">
        <div class="col-md-6">
            <object :data="require('file-loader!@/assets/uploaded/'+id+'.pdf')" type="application/pdf" width="100%" height="700px"></object>
        </div>
        <div class="col-md-6">
            <object :data="require('file-loader!@/assets/extracted/'+fileprocessed)" type="application/pdf" width="100%" height="700px"></object>
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
            notetitle:this.$route.query.title,
            id:this.$route.query.filename,
            filename:this.$route.query.filename,
            from_num:null,
            to_num:null,
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
            searchfor:null,
            replacewith:null,
            fileprocessed:'blank.pdf'
        }
    },

    methods:{
        checkForm: function(){
            this.extracts()
        },

        extracts(){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait....'
            const fd = new FormData();
            fd.append('from_num', this.from_num)
            fd.append('to_num', this.to_num)
            fd.append('filename', this.filename)
            axios.post('/api/file_extract/', fd)
            .then(response => {
                if(response.data.status==response.data.confirmed){
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.fileprocessed = response.data.fileprocessed
                }else{
                this.alert=response.data.msg
                this.classname=response.data.classname
                }
                
            }).catch((error)=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert=error
            })
        },

           edit(){
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

    },
    //end of methods

}
</script>