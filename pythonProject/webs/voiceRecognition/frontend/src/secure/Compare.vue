<template>
    <div>
<div class="col-md-10 col-md-offset-2 mt-1 maindiv">
        <div class="container">
            <div class="row">
                <div class="col">
        <h1 class="">Hello! Voice maching</h1>
<p class="lead text-muted">Please follow the steps below to complete your enrollment.</p>
                </div>
            </div>

<div class="row">
    <div class="col-md-6 mt-1">
        <div class="border p-2">

        <div class="form-group">
            <div class="row">
            <div class="col-md"> 
            <label for="id" class="mb-1">Enter your Username</label>
            <input type="text" readonly v-model="username" name="username" maxlength="20" class="form-control" placeholder="Your username">
            </div>
            </div>

        </div>

          <div class="form-group mt-3">
            <label for="id" class="text-muted">You are to repeat the same speech registered. Click compare to begin!</label>
        </div>
           <div class="btn-group mt-3 d-flex">
            <button class="btn btn-primary" @click="compareVoice">Compare voice</button>
            <!-- <button class="btn btn-outline-danger" @click="compareVoice">Start Afresh</button> -->
        </div>

        </div>
    </div>

    <div class="col-md-6 mt-1">
        <div class="border p-2">
            <ul class="list-group">
                <li class="list-group-item">{{loader}}</li>
                <li class="list-group-item">Username: {{username_txt}}</li>
                <li class="list-group-item">{{feedback}}</li>
                <!-- <li class="list-group-item">Text: {{text}}</li> -->
            </ul>
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
            recordVoiceFeedback:null,
            username:null,
            username_txt:null,
            selectedFile: null,
            loader: null,
            feedback: null,
            text: null,
        }
    },
    methods:{
         compareVoice(){
             const fd = new FormData();
            fd.append('username', '2')
            axios.post('http://127.0.0.1:8000/api/compare_voice/', fd, {
                onUploadProgress: uploadEvent => {
                    this.loader='Processing : '+ Math.round(uploadEvent.loaded / uploadEvent.total * 100) + "%"
                }
            }).then((response) => {
                this.feedback=response.data.msg
                this.username_txt=response.data.row[1]
                console.log(response)
            }).catch((error) =>{
                this.feedback=error
            })
        },
    }
}
</script>
