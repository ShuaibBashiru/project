import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)
export default new Router({
mode: 'history',
base: '/',
routes:[
{
    path: '*',
    name:'404',
    meta:{layout: 'GeneralHeader', title:'404-page',},
    component: ()=> import('./views/PageNotFound.vue'),
},
{
    path: '/',
    name:'Home',
    meta:{layout:'GeneralHeader', title:'Home'},
    component: ()=> import('./views/Home.vue'),
},
{
    path: '/site/about',
    name:'About',
    meta:{layout:'GeneralHeader', title:'About us',},
    component: ()=> import('./views/About.vue')
},
{
    path: '/site/contact',
    name:'Contact',
    meta:{layout:'GeneralHeader', title:'Contact us'},
    component: ()=> import('./views/Contactus.vue')
},
{
    path: '/oath/signin',
    name:'Signin',
    meta:{layout:'GeneralHeader', title: 'Sign In'},
    component: ()=> import('./secure/Signin.vue')
},
{
    path: '/oath/dashboard',
    name: 'dashboard',
    meta: {layout:'SidebarNoOath', title: 'Dashboard'},
    component: ()=> import('./secure/Dashboard.vue')
},

{
    path: '/oath/uploadresult',
    name: 'uploadresult',
    meta: {layout:'SidebarNoOath', title: 'upload result'},
    component: ()=> import('./secure/Uploadresult.vue')
},

{
    path: '/oath/sendsms',
    name: 'sendsms',
    meta: {layout:'SidebarNoOath', title: 'Send result'},
    component: ()=> import('./secure/Sendsms.vue')
},

]


})