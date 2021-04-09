<template>
<div>
    <GeneralHeader> </GeneralHeader>
<div class="container-fluid pb-4" style="background:#0b0b12;">
<div class="container">
<br clear="all">
<div class="row mt-5">
<div class="col-md-3 mt-1 d-flex justify-content-center"><img src="@/assets/collections/loan.png" class="img-responsive mt-5 rounded" style="width:100%;" height="250" alt=""></div>
<div class="col-md-6 mt-1 p-3 pt-0">
    <h1 class="text-center text-white header-4">Our services<br> ensure Members are satisfied and happy </h1>
    <p class="text-center text-white mt-4"><typical
        :steps="[appinfo.sloganslide, 2000]"
        :loop="1"
        :wrapper="'p'"
        ></typical></p>
    <div class="text-center mt-5">
        <a href="#"><button class="btn btn-success p-2">Commodities</button></a>
    </div>
</div>
<div class="col-md-3 mt-1 d-flex justify-content-center"><img src="@/assets/collections/commodity.png" class="img-responsive mt-5 rounded" style="width:100%;" height="250" alt=""></div>
</div>

</div>
<!--  -->

<div class="container mt-4">
    <div class="row text-white">
        <div class="col-md mb-1"><p class="lead text-center">0% Interest Loan</p></div>
        <div class="col-md mb-1"><p class="lead text-center">Savings Secure</p></div>
        <div class="col-md mb-1"><p class="lead text-center">100% Guarantee</p></div>
        <div class="col-md mb-1"><p class="lead text-center">Commodities</p></div>
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
            <h6 class="text-white">Members</h6>
            <p class="text-muted">Register or Sign In to get updates on our latest offers!</p>
                          </div>
        <div class="col-md-4 mt-2 justify-content-end"> 
              <div>
                <button type="button" class="btn btn-success mt-2 col-md-4 col-12" data-bs-toggle="modal" data-bs-target="#exampleModal">Register</button>
              <span class="btn btn-default mt-2 col-md-4 col-12 text-white p-0" data-bs-toggle="modal" data-bs-target="#exampleModal">Or</span>
              <button type="button" class="btn btn-success mt-2 col-md-4 col-12" data-bs-toggle="modal" data-bs-target="#exampleModal">Sign In</button>
              </div>
            </div>
       </div> 
</div>
</div>


<!--  -->
<div class="container-fluid mt-4 p-5 pt-0 pb-0">
        <div class="border pb-2 pt-2">
    <div class="row m-0">
    <div class="col-md-4 mb-2 mt-4 text-center">
         <img src="@/assets/collections/saving.jpeg" 
                        class="img-responsive w-75" width=""
                        height="200" alt=" ">
                        <br clear="all">
                        <div class="text-center description">
                            <h3 class="p-1">Savings</h3>
                            <p class="p-1">Registered members can save part of their salaries for the future</p>
                        <button class="btn btn-primary">Save</button>
                        </div>
    </div>
    <div class="col-md-4 mb-2 mt-4 text-center">
         <img src="@/assets/collections/loan.png" 
                        class="img-responsive w-75" width=""
                        height="200" alt=" ">
                        <br clear="all">
                        <div class="text-center description">
                            <h3 class="p-1">Loan</h3>
                            <p class="p-1">The society offers to its members 0% Interest rate</p>
                        <button class="btn btn-primary">Apply</button>
                        </div>
    </div>
    <div class="col-md-4 mb-2 mt-4 text-center">
         <img src="@/assets/collections/commodity.png" 
                        class="img-responsive w-75" width=""
                        height="200" alt=" ">
                        <br clear="all">
                        <div class="text-center description">
                            <h3 class="p-1">Commodities</h3>
                            <p class="p-1">The registered members can purchase stocks (goods) in lesser cost.</p>
                        <button class="btn btn-primary">Apply</button>
                        </div>
    </div>
            </div>
            </div>
</div>
<!--  -->


<!--  -->
<div class="container-fluid mt-4 p-5 pt-0 pb-0">
        <div class="border pb-2">
                <div class="row border-bottom p-0 m-0 bg-success text-white" style="">
                    <div class="col-md-10 p-0 m-0"><p class="text-left m-1">Featured | Commodities </p></div>
                    <div class="col-md-2 p-0 m-0 d-flex justify-content-end"><a href="" class="p-2 pb-1 mt-1 text-white">See All <i class="bi-arrow-right"></i></a></div>
                </div>

                    <div class="row">
                        <Vslick v-bind="itemscroll">

                    <div class="col-md-3 mb-2 mt-2 box">
                        <img src="@/assets/items/item1.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Grains</p>
                        </div>
                    </div>
                                                
                    <div class="col-md-3 mb-2 mt-2 box">
                        <img src="@/assets/items/item2.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Cow</p>
                        </div>
                    </div>
                            
                    <div class="col-md-3 mb-2 mt-2 box">
                        <img src="@/assets/items/item3.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Fows</p>
                        </div>
                    </div>

                            
                    <div class="col-md-3 mb-2 mt-2 box">
                        <img src="@/assets/items/item4.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Meat</p>
                        </div>
                    </div>

                            
                    <div class="col-md-3 mb-2 mt-2 box">
                        <img src="@/assets/items/item5.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Fruits & Vegetables</p>
                        </div>
                    </div>

                                                
                    <div class="col-md-3 mb-2 mt-2 box">
                        <img src="@/assets/items/item6.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Fruits & Vegetables</p>
                        </div>
                    </div>

                        </Vslick>
                </div>
            </div>
</div>
<!--  -->


<!--  -->
<div class="container-fluid mt-4 p-5 pt-0 pb-0">
        <div class="border pb-2">
                <div class="row border-bottom p-0 m-0 bg-success text-white" style="">
                    <div class="col-md-10 p-0 m-0"><p class="text-left m-1">Commodities |</p></div>
                    <div class="col-md-2 p-0 m-0 d-flex justify-content-end"><a href="" class="p-2 pb-1 mt-1 text-white">See All <i class="bi-arrow-right"></i></a></div>
                </div>

                    <div class="row">
                        <div class="col-12 mt-4">
                                        <h5 class="text-center">Organic Foods</h5>
<p class="text-center text-muted">Some of our favourite commodities we have in closets</p>
                        </div>
                        <Vslick v-bind="itemscroll">
                        <div class="col-md-3 mb-2 mt-2 box">
                        <img src="@/assets/items/item8.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Fruits</p>
                        </div>
                    </div>
                                                
                    <div class="col-md-3 mb-2 mt-2 box">
                        <img src="@/assets/items/item9.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Tomatoes</p>
                        </div>
                    </div>
                                                                    
                    <div class="col-md-3 mb-2 mt-2 box">
                        <img src="@/assets/items/item13.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Vegetable Oil</p>
                        </div>
                    </div>

                                                
                    <div class="col-md-3 mb-2 mt-2 box">
                        <img src="@/assets/items/item14.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Red Palm Oil</p>
                        </div>
                    </div>
                            
                    <div class="col-md-3 mb-2 mt-2 box">
                        <img src="@/assets/items/item10.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Chilli Peppers</p>
                        </div>
                    </div>

                            
                    <div class="col-md-3 mb-1 mt-2 box">
                        <img src="@/assets/items/item11.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Bell Peppers</p>
                        </div>
                    </div>

                            
                    <div class="col-md-3 mb-2 mt-2 box">
                        <img src="@/assets/items/item12.jpeg" 
                        class="img-responsive" width="250"
                        height="200" alt=""> <br clear="all">
                        <div class="text-center description">
                            <p class="p-1">Peppers</p>
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
<!-- <div class="container-fluid mt-5 mb-5 p-5 pt-0 pb-0">
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
</div> -->
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
import appsettings from '../json/myapp.json'
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
            "media":appsettings.media,
            "appinfo":appsettings.appinfo,
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
                centerPadding:'10',
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
                centerPadding:'10',
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