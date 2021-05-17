<template>
    <div>
<div class="col-md-10 col-md-offset-2 mt-1 maindiv">
<div v-bind:class="classname">{{alert}}</div>
        <div class="container">
            <div class="row mt-5 d-flex justify-content-center">

                <div class="col-10">
        <h2 class="text-center">Hello! Welcome to,</h2>
        <p class="lead text-center text-muted mt-4">Computational Platform that optimizes a problem by iteratively trying to improve a candidate solution with regard to a given measure of quality.
          <br><br> <strong> Click on <big>Functions</big> menu to begin </strong>
        </p>
                </div>
            </div>

        </div>
</div>
</div>
</template>


<script>

export default{
    data(){
        return{
            alert:null,
            classname:null,
        }
    }
}

</script>
<style>

</style>
