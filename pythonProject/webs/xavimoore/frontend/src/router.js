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
    component: ()=> import('./views/Home.vue'),
},

{
    path: '/secure/admin',
    name:'admin',
    meta:{title:'Administrator'},
    component: ()=> import('./secure/Dashboard.vue'),
},

{
    path: '/secure/widget',
    name:'widget',
    meta:{title:'Widgets'},
    component: ()=> import('./secure/Widget.vue'),
},

{
    path: '/secure/adminaccount',
    name:'adminaccount',
    meta:{title:'Admin account'},
    component: ()=> import('./secure/Adminaccount.vue'),
},





]
})