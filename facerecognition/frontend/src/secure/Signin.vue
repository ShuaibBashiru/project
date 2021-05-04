<template>
<div>
<div class="container-fluid">
<div class="row d-flex justify-content-center">
    <div class="col-md-4 mt-2">
  <form action="" role="form">
  <div class="form-row">
<div class="form-group col text-center">
    <h2>Sign in</h2>
<p>to continue to your account</p>
</div>
    <div class="form-group mt-4 col">
        <label for="userid" class="text-muted">UserID</label>
      <input type="email" class="form-control" name="email" placeholder="Enter your email" id="userid" required maxlength="100" minlength="10">
    </div>

    <div class="form-group mt-3 col">
        <label for="pwd" class="text-muted">Password</label>
      <input type="password" class="form-control" name="pwd" placeholder="Password" id="pwd" required maxlength="50" minlength="8">
    </div>

    <div class="form-group mt-2">
    <div class="form-check">
        <input class="form-check-input" type="checkbox" id="remember">
        <label class="form-check-label" for="remember">
        Remember me
        </label>
    </div>
    </div>

      <div class="form-group mt-3 col">
     <button type="submit" name="signin" class="btn btn-primary form-control">Sign in</button>
    </div>

  </div>
</form>



    </div>

</div>

</div>
</div>
</template>

<script>
export default{
}
</script>


<style>
header a{
    text-decoration: none;
}

li{
    list-style: none;
}
.body_image{
    width:445px;
    height: 120px;
}
</style>