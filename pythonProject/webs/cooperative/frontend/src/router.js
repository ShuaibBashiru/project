import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)

export default new Router({
mode: 'history',
base: process.env.BASE_URL,
routes:[
{
    path: '*',
    name:'404',
    meta:{title:'404-page...'},
    component: ()=> import('./views/PageNotFound.vue'),
},

{
    path: '/',
    name:'Home',
    meta:{title:'Home'},
    component: ()=> import('./secure/Signin.vue'),
},


{
    path: '/site/signin',
    name:'signin',
    meta:{title:'Sign In'},
    component: ()=> import('./secure/Signin.vue'),
},



{
    path: '/secure/dashboard',
    name:'dashboard',
    meta:{title:'Dashboard'},
    component: ()=> import('./secure/Dashboard.vue'),
},

{
    path: '/site/auth-check',
    name:'Validation',
    meta:{title:'Loggin...'},
    component: ()=> import('./auth/Auth-check.vue'),
},


{
    path: '/site/logout',
    name:'logout',
    meta:{title:'Admin account'},
    component: ()=> import('./secure/Logout.vue'),
},

{
    path: '/newaccount',
    name:'newaccount',
    meta:{title:'Create account'},
    component: ()=> import('./secure/Newaccount.vue'),
},

{
    path: '/site/newpassword/:email/:id',
    name:'newpassword',
    meta:{title:'New password'},
    component: ()=> import('./secure/Newpassword.vue'),
},

{
    path: '/site/forgotpassword/',
    name:'forgotpassword',
    meta:{title:'Forgot password'},
    component: ()=> import('./secure/ForgotPassword.vue'),
},


// Widgets 
{
    path: '/secure/newwidget',
    name:'newwidget',
    meta:{title:'New Widgets'},
    component: ()=> import('./forms/newwidget.vue'),
},
{
    path: '/secure/widgets',
    name:'Widgets',
    meta:{title:'Widgets'},
    component: ()=> import('./api/Widgets.vue'),
},
{
    path: '/secure/updatewidget/:title/:id',
    name:'updatewidget',
    meta:{title:'Update widget'},
    component: ()=> import('./formsupdate/updatewidget.vue'),
},

{
    path: '/secure/deletewidget/:title/:id',
    name:'deletewidget',
    meta:{title:'delete widget'},
    component: ()=> import('./formsdelete/deletewidget.vue'),
 
},
//End

// Priviledges

{
    path: '/secure/pageaccess',
    name:'pageaccess',
    meta:{title:'Page access'},
    component: ()=> import('./forms/Pageaccess.vue'),
},


]
})