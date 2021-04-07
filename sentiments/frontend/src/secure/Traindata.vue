<template>
<div>
<div class="col-md-10 col-md-offset-2 maindiv">
<div class="container">
    <div class="row">
        <div v-bind:class="classname">{{alert}}</div>
    <div class="border p-2">
<div class="row form-inline mb-3  d-flex justify-content-end">
<div class="col-md-4 mt-2 ">
    <div class="input-group">
    <button class="btn btn-secondary">Iteration</button>
    <input type="number" v-model="runtime" min="1" maxlength="4" class="form-control" placeholder="Number" value="1">
    <!-- <button class="btn btn-primary" @click="trainData">Create Model</button> -->

</div>
</div>

<div class="col-md-2 mt-2 ">
    <!-- <div class="input-group">
    <button class="btn btn-primary">Iterations</button>
    <input type="number" v-model="iteration" min="1" maxlength="4" class="form-control" placeholder="Number" value="1">
</div> -->
</div>

<div class="col-md-3 mt-2">
    <!-- <div class="input-group">
    <input type="number" v-model="particle" min="1" maxlength="4" class="form-control" placeholder="Number" value="1">
    <button class="btn btn-primary">Agents</button>
</div> -->
</div>

<div class="col-md-3 mt-2">
<div class="input-group d-flex justify-content-end">
 <button class="btn btn-primary" @click="trainData">Visualize Analysis</button>
</div>
</div>
        </div>
    </div>


</div>




<div class="row mt-2">
<div class="col-md-12 p-0 border-bottom border-top border-start">
    <div class="border m-1 pt-3 p-1 justify-content-center">
    <div class="row">
        <div class="col-md-12"><h5 class="text-center">SOS On Performance Classification model</h5></div>
        <div class="col-md-12">
            <div class="table-responsive">
    <table class="table table-striped">
        <thead>

            <tr>
                <th>Algorithm</th>
                <th>Precision</th>
                <th>Recall</th>
                <th>F-measures</th>
                <th>Accuracy</th>

            </tr>
        </thead>
        <tbody>
        <tr>
                <td>{{lgr.algorithm}}</td>
                <td>{{lgr.precision}}</td>
                <td>{{lgr.recall}}</td>
                <td>{{lgr.f1_score}}</td>
                <td>{{lgr.accuracy}}</td>
            </tr>

             <tr>
                <td>{{xgb.algorithm}}</td>
                <td>{{xgb.precision}}</td>
                <td>{{xgb.recall}}</td>
                <td>{{xgb.f1_score}}</td>
                <td>{{xgb.accuracy}}</td>
            </tr>
     

            <tr>
                <td>{{svm.algorithm}}</td>
                <td>{{svm.precision}}</td>
                <td>{{svm.recall}}</td>
                <td>{{svm.f1_score}}</td>
                <td>{{svm.accuracy}}</td>
            </tr>

        </tbody>
    </table>
            </div>

        </div>
    </div>

    </div>
    </div>

</div>

<div class="row mt-2">
<div class="col-md-12 p-0 border-bottom border-top border-start">
    <div class="border m-1 pt-3 p-1 justify-content-center">
    <div class="row">
        <div class="col-md-4 p-3 justify-content-center">
            <h4 class="lead mt-5  text-center">Crop Planning Optimization using Symbiotic Organism Search algorthm</h4> 
            <p class="lead mt-5 text-center"><strong>Result showing from 1961 to 2014 </strong></p> 
        </div>
             <div class="col-md-8 text-center">
<img :src="require('@/assets/plots/'+ countplot)"  alt=" " class="img-responsive mx-auto d-block rounded" style="width:600px; height:400px;">
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
            info:[],
            xgb:[],
            lgr:[],
            svm:[],
            iteration:10,
            particle:20,
            runtime:10,
            alert:null,
            progress:null,
            accuracy:null,
            classname:'',
            feat_importances: 'avatar.png',
            countplot: 'avatar.png'
        }
    },
    methods:{
           trainData(){
               this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while processing....'
            axios.get('/api/train_data/',{
            params: {
                    particle: this.particle,
                    iteration: this.iteration,
                    runtime: this.runtime
                },
                }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.xgb=response.data.xgb_report
                this.svm=response.data.svm_report
                this.lgr=response.data.lgr_report
                this.feat_importances='feat_importances.png'
                this.countplot='countplot.png'
                console.log(response)
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Request failed, Please note that the number of particles must not be less than the function variable' 

            })
        },
       
           visualize(){
               this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while processing....'
            axios.get('/api/modelanalysis/',{
            params: {
                    particle: this.particle,
                    iteration: this.iteration,
                    runtime: this.runtime
                },
                }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                // this.xgb=response.data.xgb_report
                // this.svm=response.data.svm_report
                // this.lgr=response.data.lgr_report
                this.feat_importances='feat_importances.png'
                this.countplot='countplot.png'
                console.log(response)
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Error: Request failed, Please note that the number of particles must not be less than the function variable' 

            })
        },

    },
    //end of methods

}
</script>