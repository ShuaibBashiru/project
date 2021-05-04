<template>
<div>
<div class="col-md-10 col-md-offset-2 maindiv">
<div class="container">
           <div class="row form-inline mb-3  d-flex justify-content-end">
<div class="col-md-3 mt-2 ">
    <div class="input-group">
    <button class="btn btn-primary">Run time</button>
    <input type="number" v-model="runtime" min="1" maxlength="4" class="form-control" placeholder="Number" value="1">
</div>
</div>

<div class="col-md-3 mt-2 ">
    <div class="input-group">
    <button class="btn btn-primary">Iterations</button>
    <input type="number" v-model="iteration" min="1" maxlength="4" class="form-control" placeholder="Number" value="1">
</div>
</div>

<div class="col-md-3 mt-2">
    <div class="input-group">
    <input type="number" v-model="particle" min="1" maxlength="4" class="form-control" placeholder="Number" value="1">
    <button class="btn btn-primary">Particles</button>
</div>
</div>

        </div>
    <div class="row">
        <div class="col-12">
            <div v-bind:class="classname">{{alert}}</div>
<div class="row border m-0">
    <div class="col-md-12">
        <p class="lead m-1"><strong>Functions: </strong>(Set number of particle and iteration then click any function to optimize)</p>
<hr class="m-1">
<div class="row">

<div class="col-4" @click="function_1">
<div class="border rounded p-1 m-1 text-center"><h3>F1: x^2 + (3 * x) + 2 = 0</h3></div>
</div>

     
<div class="col-4" @click="function_2">
<div class="border rounded p-1 m-1 text-center"><h3>F2: x^2 + (7 * x) + 4 = 0</h3></div>
</div>

        
<div class="col-4" @click="function_3">
<div class="border rounded p-1 m-1 text-center"><h3>F3: -x^2 + (5 * x) + 20 = 0 </h3></div>
</div>

        
<div class="col-4" @click="function_4">
<div class="border rounded p-1 m-1 text-center"><h3>F4: x*3 + (4 * x*2) + (3 * x) +6 = 0</h3></div>
</div>
       
<div class="col-4" @click="function_5">
<div class="border rounded p-1 m-1 text-center"><h3>F5: (x+1) * (x-1) + 0.152 = 0 </h3></div>
</div>
    
<div class="col-4" @click="function_6">
<div class="border rounded p-1 m-1 text-center"><h3>F6: x*3 + x*2 = 0 </h3></div>
</div>
    
    <div class="col-4" @click="function_7">
<div class="border rounded p-1 m-1 text-center"><h3>F7: x*3 – (0.165 * x*2) + (0.0003993 * x) = 0 </h3></div>
</div>
    
    <div class="col-4" @click="function_8">
<div class="border rounded p-1 m-1 text-center"><h3>F8: (x^2 * sin(20x)+cos(x−π))^3+1 </h3></div>
</div>
    
    
</div>


    </div>
</div>

<div class="row border p-2 m-0">
<div class="col-3">
    <div class="border p-2 text-center">
<img src="../assets/images/demo.gif" alt="" class="img-responsive" width="250" height="230">
</div>
</div>

<div class="col-9">
    <div class="border p-2">
        <!-- <p class="lead">{{message}}</p> -->
<div class="table-responsive">
    <table class="table table-striped">
        <thead>
            <tr>
                <th>Function</th>
                <th>GeneralPso</th>
                <th>Cognitive</th>
                <th>Particle</th>
                <th>Iteration</th>

            </tr>
        </thead>
        <tbody>
                    <tr>
                <td>{{f1.function}}</td>
                <td>{{f1.gpos}}</td>
                <td>{{f1.cpos}}</td>
                <td>{{f1.particle}}</td>
                <td>{{f1.iteration}}</td>
            </tr>

                <tr>
                <td>{{f2.function}}</td>
                <td>{{f2.gpos}}</td>
                <td>{{f2.cpos}}</td>
                <td>{{f2.particle}}</td>
                <td>{{f2.iteration}}</td>
            </tr>

                <tr>
                <td>{{f3.function}}</td>
                <td>{{f3.gpos}}</td>
                <td>{{f3.cpos}}</td>
                <td>{{f3.particle}}</td>
                <td>{{f3.iteration}}</td>
            </tr>
 

                <tr>
                <td>{{f4.function}}</td>
                <td>{{f4.gpos}}</td>
                <td>{{f4.cpos}}</td>
                <td>{{f4.particle}}</td>
                <td>{{f4.iteration}}</td>
            </tr>
 

                <tr>
                <td>{{f5.function}}</td>
                <td>{{f5.gpos}}</td>
                <td>{{f5.cpos}}</td>
                <td>{{f5.particle}}</td>
                <td>{{f5.iteration}}</td>
            </tr>
 
 
                <tr>
                <td>{{f6.function}}</td>
                <td>{{f6.gpos}}</td>
                <td>{{f6.cpos}}</td>
                <td>{{f6.particle}}</td>
                <td>{{f6.iteration}}</td>
            </tr>
 
                <tr>
                <td>{{f7.function}}</td>
                <td>{{f7.gpos}}</td>
                <td>{{f7.cpos}}</td>
                <td>{{f7.particle}}</td>
                <td>{{f7.iteration}}</td>
            </tr>
 
                <tr>
                <td>{{f8.function}}</td>
                <td>{{f8.gpos}}</td>
                <td>{{f8.cpos}}</td>
                <td>{{f8.particle}}</td>
                <td>{{f8.iteration}}</td>
            </tr>
 
        </tbody>
    </table>
</div>

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
            f1:'',
            f2:'',
            f3:'',
            f4:'',
            f5:'',
            f6:'',
            f7:'',
            f8:'',
            iteration:10,
            particle:20,
            runtime:10,
            alert:null,
            progress:null,
            classname:'',
        }
    },
    methods:{
           function_1(){
               this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while optimizing....'
            axios.get('/api/f1/',{
            params: {
                    particle: this.particle,
                    iteration: this.iteration,
                    runtime: this.runtime
                }, 
                },
                {
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.f1=response.data
                console.log(response)
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Error: Request failed, Please note that the number of particles must not be less than the function variable' 

            })
        },


           function_2(){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while optimizing....'
            axios.get('/api/f2/',{
            params: {
                    particle: this.particle,
                    iteration: this.iteration,
                    runtime: this.runtime

                }, 
                },
                {
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.f2=response.data
                console.log(response)
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Error: Request failed, Please note that the number of particles must not be less than the function variable' 

            })
        },



           function_3(){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while optimizing....'
            axios.get('/api/f3/',{
            params: {
                    particle: this.particle,
                    iteration: this.iteration,
                    runtime: this.runtime
                    
                }, 
                },
                {
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.f3=response.data
                console.log(response)
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Error: Request failed, Please note that the number of particles must not be less than the function variable' 

            })
        },

       

           function_4(){
            this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while optimizing....'
            axios.get('/api/f4/',{
            params: {
                    particle: this.particle,
                    iteration: this.iteration,
                    runtime: this.runtime

                }, 
                },
                {
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.f4=response.data
                console.log(response)
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Error: Request failed, Please note that the number of particles must not be less than the function variable' 

            })
        },

       

           function_5(){
                    this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while optimizing....'
            axios.get('/api/f5/',{
            params: {
                    particle: this.particle,
                    iteration: this.iteration,
                    runtime: this.runtime

                }, 
                },
                {
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.f5=response.data
                console.log(response)
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Error: Request failed, Please note that the number of particles must not be less than the function variable' 

            })
        },

       

           function_6(){
                           this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while optimizing....'
            axios.get('/api/f6/',{
            params: {
                    particle: this.particle,
                    iteration: this.iteration,
                    runtime: this.runtime

                }, 
                },
                {
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.f6=response.data
                console.log(response)
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Error: Request failed, Please note that the number of particles must not be less than the function variable' 

            })
        },

       

           function_7(){
                           this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while optimizing....'
            axios.get('/api/f7/',{
            params: {
                    particle: this.particle,
                    iteration: this.iteration,
                    runtime: this.runtime

                }, 
                },
                {
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.f7=response.data
                console.log(response)
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Error: Request failed, Please note that the number of particles must not be less than the function variable' 

            })
        },

       

           function_8(){
                           this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while optimizing....'
            axios.get('/api/f8/',{
            params: {
                    particle: this.particle,
                    iteration: this.iteration,
                    runtime: this.runtime

                }, 
                },
                {
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
                this.f8=response.data
                console.log(response)
            }).catch(()=>{
                this.classname='alert alert-danger p-1 text-center'
                this.alert='Error: Request failed, Please note that the number of particles must not be less than the function variable' 

            })
        },
      

           function_9(){
                           this.classname='alert alert-warning p-1 text-center'
            this.alert='Pleast wait while optimizing....'
            axios.get('/api/f9/',{
            params: {
                    particle: this.particle,
                    iteration: this.iteration,
                    runtime: this.runtime

                }, 
                },
                {
                onUploadProgress: uploadEvent => {
                    this.progress='Progress : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            
            }).then(response => {
                this.alert=response.data.msg
                this.classname=response.data.classname
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