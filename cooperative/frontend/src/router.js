import Vue from 'vue'
import Router from 'vue-router'
import store from './store'
Vue.use(Router)

export default new Router({
mode: 'history',
base: process.env.BASE_URL,
routes:[
{
    path: '*',
    name:'404',
    meta:{layout: 'GeneralHeader', title:'404-page...',},
    component: ()=> import('./views/PageNotFound.vue'),
},
{
    path: '/oath/:*',
    name:'404_back',
    meta:{layout: 'BackendHeader', title:'404-page...',},
    component: ()=> import('./views/Page404.vue'),
},

{
    path: '/',
    name:'Home',
    meta:{layout:'GeneralHeader', title:'Home'},
    component: ()=> import('./views/Home.vue'),
},
{
    path: '/site/signin',
    name:'Signin',
    meta:{layout:'GeneralHeader', title: 'Sign In'},
    component: ()=> import('./secure/Signin.vue')
},
{
    path: '/site/logout',
    name: 'logout',
    meta: {layout:'GeneralHeader', title: 'logout'},
    component: ()=> import('./secure/Logout.vue')
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
    path: '/oath/statement',
    name:'Statement',
    meta:{layout:'SidebarNoOath', title:'statement'},
    component: ()=> import('./views/About.vue')
},

{
    path: '/oath/dashboard',
    name: 'dashboard',
    meta: {layout:'BackendHeader', title: 'Dashboard'},
    component: ()=> import('./secure/Dashboard.vue'),
    beforeEnter (to, from, next) {
        // if (store.state.set_user.length === 0) {
            store.dispatch('auth_check')
            next()
        // }
    },
   
},
{
    path: '/oath/panel',
    name: 'panel',
    meta: {layout:'SidebarNoOath', title: 'Base'},
    component: ()=> import('./secure/Dashboard.vue')
},

{
    path: '/oath/report',
    name: 'report',
    meta: {layout:'BackendHeader', title: 'Report'},
    component: ()=> import('./secure/Report.vue')
},


{
    path: '/oath/template',
    name: 'template',
    meta: {layout:'SidebarNoOath', title: 'Template'},
    component: ()=> import('./views/template.vue')
},

{
    path: '/oath/uploadlist',
    name: 'uploadlist',
    meta: {layout:'BackendHeader', title: 'Upload payment'},
    component: ()=> import('./secure/Uploadlist.vue')
},
{
    path: '/oath/searchaccount',
    name: 'searchaccount',
    meta: {layout:'BackendHeader', title: 'Search account'},
    component: ()=> import('./secure/Searchaccount.vue')
},
{
    path: '/oath/user',
    name: 'useraccount',
    meta: {layout:'BackendHeader', title: 'User Account'},
    component: ()=> import('./secure/user_account.vue')
},
]


})