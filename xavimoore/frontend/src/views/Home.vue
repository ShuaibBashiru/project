<template>
<div>
    <GeneralHeader> </GeneralHeader>
<div class="container-fluid pb-4" style="background:#0b0b12;">
<div class="container">
<br clear="all">
<div class="row mt-5">
<div class="col-md-3 mt-1 d-flex justify-content-center"><img src="@/assets/images/sideimg1.png" class="img-responsive mt-5" style="width:100%;" height="320" alt=""></div>
<div class="col-md-6 mt-1 p-3 pt-0">
    <h1 class="text-center text-white header-4">Custom Menswear <br> Built for The Modern Day</h1>
    <p class="text-center text-white mt-4"><typical
        :steps="['Xavimoore! The Largest fashion store!', 2000]"
        :loop="1"
        :wrapper="'p'"
        ></typical></p>
    <div class="text-center mt-5">
        <button class="btn btn-primary p-2">Xavimoore Catalogs</button>
    </div>
</div>
<div class="col-md-3 mt-1 d-flex justify-content-center"><img src="@/assets/images/sideimg2.png" class="img-responsive mt-5" style="width:100%;" height="320" alt=""></div>
</div>

</div>
<!--  -->

<div class="container mt-4">
    <div class="row text-white">
        <div class="col-md mb-1"><p class="lead">Mobile body scan</p></div>
        <div class="col-md mb-1"><p class="lead">Tech enabled</p></div>
        <div class="col-md mb-1"><p class="lead">Quality made</p></div>
        <div class="col-md mb-1"><p class="lead">100% Fit Guarantee</p></div>
    </div>
</div>
<!--  -->

</div>
<!-- end container-colored -->

<!--  -->
<div class="container-fluid mt-4 p-5 pt-0 pb-0">
<div class="rounded" style="background:#0b0b12;">
           <div class="row p-2 m-0 mt-1">
            <div class="col-md-8 mt-1">
            <h6 class="text-white">Newsletter</h6>
            <p class="text-muted">Subscribe to our newsletter to get updates on our latest offers!</p>
                          </div>
        <div class="col-md-4 mt-2 d-flex justify-content-end"> 
            <button type="button" class="btn btn-primary m-3" data-bs-toggle="modal" data-bs-target="#exampleModal">Subscribe</button></div>
       </div> 
</div>
</div>

<!-- Modal -->
<div class="modal fade" id="exampleModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
        <form @submit.prevent="formCheck" class="needs-validation">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Newsletter</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
                <div class="row">
                    <div class="col-md-8 mt-1"> 
                        <input type="text" class="form-control" 
                        placeholder="Enter E-mail address" required>
                    </div>
                    <div class="col-md-4 mt-1">
                    <select name="" id="" required class="form-select">
                        <option value="">Gender</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                    </select>
                    </div>
                    </div>
                     <small class="text-danger">{{err_email}}</small>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="submit" class="btn btn-primary">Subscribe</button>
      </div>
            </form>
    </div>
  </div>
</div>

<!--  -->
<!--  -->
<div class="container-fluid mt-4 p-5 pt-0 pb-0">
        <div class="border pb-2">
            <div class="row border-bottom p-0 m-0 bg-primary text-white" style="">
                    <div class="col-md-10 p-0 m-0"><p class="text-left m-1">Featured Categories</p></div>
                    <div class="col-md-2 p-0 m-0 d-flex justify-content-end"><a href="" class="p-2 pb-1 mt-1 text-white">See All <i class="bi-arrow-right"></i></a></div>
                </div>
                    <div class="row">
                    <div class="col-md-3 mb-1 text-center box">
                        <img src="@/assets/collections/img1.jpeg" 
                        class="img-responsive" width="196"
                        height="300" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Essential Blazers</p>
                        </div>
                    </div>
                       <div class="col-md-3 mb-1 text-center box">
                        <img src="@/assets/collections/img2.jpeg" 
                        class="img-responsive" width="196"
                        height="300" alt=""><br clear="all">
                           <div class="text-center description">
                            <p class="p-1">Essential Blazers</p>
                        </div>
                    </div>

                       <div class="col-md-3 mb-1 text-center box">
                        <img src="@/assets/collections/img3.jpeg" 
                        class="img-responsive" width="196"
                        height="300" alt=""><br clear="all">
                           <div class="text-center description">
                            <p class="p-1">Essential Blazers</p>
                        </div>
                    </div>

                       <div class="col-md-3 mb-1 text-center box">
                        <img src="@/assets/collections/img3.jpeg" 
                        class="img-responsive" width="196"
                        height="300" alt=""><br clear="all">
                           <div class="text-center description">
                            <p class="p-1">Essential Blazers</p>
                        </div>
                    </div>

            </div>
            </div>
</div>
<!--  -->

<!--  -->
<div class="container-fluid mt-4 p-5 pt-0 pb-0">
        <div class="border pb-2 pt-2">
    <div class="row m-0">
    <div class="col-md-6 mb-1 text-center">
         <img src="@/assets/collections/banner1.png" 
                        class="img-responsive w-100" width=""
                        height="" alt=" ">
    </div>

    <div class="col-md-6 mb-1 text-center">
        <img src="@/assets/collections/banner2.png" 
              class="img-responsive w-100" width=""
                        height="" alt=" ">
    </div>
            </div>
            </div>
</div>
<!--  -->

<!--  -->
<div class="container-fluid mt-4 p-5 pt-0 pb-0">
        <div class="border pb-2">
                <div class="row border-bottom p-0 m-0 bg-primary text-white" style="">
                    <div class="col-md-10 p-0 m-0"><p class="text-left m-1">Featured Categories</p></div>
                    <div class="col-md-2 p-0 m-0 d-flex justify-content-end"><a href="" class="p-2 pb-1 mt-1 text-white">See All <i class="bi-arrow-right"></i></a></div>
                </div>

                    <div class="row">
                        <Vslick v-bind="itemscroll">
                    <div class="col-md-3 mb-1 box">
                        <img src="@/assets/collections/img1.jpeg" 
                        class="img-responsive" width="196"
                        height="300" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Essential Blazers</p>
                        </div>
                    </div>

                    <div class="col-md-3 mb-1 box">
                        <img src="@/assets/collections/img2.jpeg" 
                        class="img-responsive" width="196"
                        height="300" alt=""><br clear="all">
                           <div class="text-center description">
                            <p class="p-1">Essential Blazers</p>
                        </div>
                    </div>

                    <div class="col-md-3 mb-1 box">
                        <img src="@/assets/collections/img3.jpeg" 
                        class="img-responsive" width="196"
                        height="300" alt=""><br clear="all">
                           <div class="text-center description">
                            <p class="p-1">Essential Blazers</p>
                        </div>
                    </div>

                       <div class="col-md-3 mb-1 box">
                        <img src="@/assets/collections/img3.jpeg" 
                        class="img-responsive" width="196"
                        height="300" alt=""><br clear="all">
                           <div class="text-center description">
                            <p class="p-1">Essential Blazers</p>
                        </div>
                    </div>

                    <div class="col-md-3 mb-1 box">
                        <img src="@/assets/collections/img3.jpeg" 
                        class="img-responsive" width="196"
                        height="300" alt=""><br clear="all">
                           <div class="text-center description">
                            <p class="p-1">Essential Blazers</p>
                        </div>
                    </div>
                        </Vslick>
                </div>
            </div>
</div>
<!--  -->
<br>
<br>
<!--  -->
<div class="container-fluid mt-5 mb-5 p-5 pt-0 pb-0">
        <div class="pb-2 pt-2">
            <h5 class="text-center">Some of our favourite fabric mills we work with</h5>
<p class="text-center text-muted">Imported fabrics are currently available offline with
     your Private Clothier or in our showroom.</p>
    <div class="row m-0 mt-5">
         <Vslick v-bind="partnerslist">
    <div class="col-md-2 mb-1 text-center">
         <img src="@/assets/collections/banner2.png" 
                        class="img-responsive" width="150"
                        height="76" alt=" ">
    </div>
        <div class="col-md-2 mb-1 text-center">
         <img src="@/assets/collections/banner1.png" 
                        class="img-responsive" width="150"
                        height="76" alt=" ">
    </div>

    <div class="col-md-2 mb-1 text-center">
         <img src="@/assets/collections/banner2.png" 
                        class="img-responsive" width="150"
                        height="76" alt=" ">
    </div>

    <div class="col-md-2 mb-1 text-center">
         <img src="@/assets/collections/banner1.png" 
                        class="img-responsive" width="150"
                        height="76" alt=" ">
    </div>
    <div class="col-md-2 mb-1 text-center">
         <img src="@/assets/collections/banner2.png" 
                        class="img-responsive" width="150"
                        height="76" alt=" ">
    </div>

    <div class="col-md-2 mb-1 text-center">
         <img src="@/assets/collections/banner1.png" 
                        class="img-responsive" width="150"
                        height="76" alt=" ">
    </div>

         </Vslick>
            </div>
            </div>
</div>
<br>
<br>
<!--  -->
<GeneralFooter></GeneralFooter>
</div>
</template>
<style scoped>
h1, h2, h3, h4, h5, h6, p{
    font-family: "Geomanist book webfont',Arial,sans-serif";
line-height: 1.6;
}

.box img{
margin: 0 auto;
}

</style>
<script>
import typical from 'vue-typical'
import Vslick from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
export default{
    components:{
        typical,
        Vslick
    },
    data(){
        return{
            itemscroll:{
                arrows: true,
                dots: true,
                rows:1,
                slidesToShow:4,
                slidesToScroll:1,
                swipe:true,
                swipeToSlide:true,
                useCSS:true,
                autoplay:true,
                centerMode:true,
                centerPadding:'50',
                responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 3,
                slidesToScroll: 2
              }
            },

            {
              breakpoint: 767,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2
              }
            },
            {
              breakpoint: 639,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            },
          ]
                // slidesPerRow:4,
            },
      
        partnerslist:{
                arrows: true,
                dots: true,
                rows:1,
                slidesToShow:6,
                slidesToScroll:1,
                swipe:true,
                swipeToSlide:true,
                useCSS:true,
                autoplay:true,
                centerMode:true,
                centerPadding:'50',
                responsive: [
            {
              breakpoint: 1024,
              settings: {
                slidesToShow: 3,
                slidesToScroll: 2
              }
            },

            {
              breakpoint: 767,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2
              }
            },
            {
              breakpoint: 639,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            },
          ]
                // slidesPerRow:4,
            }
       }     // end
}
    }
</script>