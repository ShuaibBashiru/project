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
    path: '/oath/report',
    name: 'report',
    meta: {layout:'SidebarNoOath', title: 'Report'},
    component: ()=> import('./secure/Report.vue')
},
{
    path: '/oath/export',
    name: 'export',
    meta: {layout:'SidebarNoOath', title: 'Export'},
    component: ()=> import('./secure/Export.vue')
},
{
    path: '/oath/import',
    name: 'import',
    meta: {layout:'SidebarNoOath', title: 'Import'},
    component: ()=> import('./secure/Import.vue')
},

{
    path: '/oath/compare',
    name: 'Compare',
    meta: {layout:'SidebarNoOath', title: 'Compare voice'},
    component: ()=> import('./secure/Compare.vue')
},


{
    path: '/oath/matricverifier',
    name: 'matricverifier',
    meta: {layout:'SidebarNoOath', title: 'Matric verifier'},
    component: ()=> import('./secure/Matricverifier.vue')
},
{
    path: '/oath/docketverifier',
    name: 'docketverifier',
    meta: {layout:'SidebarNoOath', title: 'docket verifier'},
    component: ()=> import('./secure/Docketverifier.vue')
},

{
    path: '/oath/enroll',
    name: 'Enrollment',
    meta: {layout:'SidebarNoOath', title: 'Enrollment'},
    component: ()=> import('./secure/Enroll.vue')
},

{
    path: '/oath/uploadbiodata',
    name: 'upload_biodata',
    meta: {layout:'SidebarNoOath', title: 'Biodata Upload'},
    component: ()=> import('./secure/uploadbiodata.vue')
},

{
    path: '/oath/uploadcourses',
    name: 'Courses',
    meta: {layout:'SidebarNoOath', title: 'Coures Upload'},
    component: ()=> import('./secure/uploadcourses.vue')
},

{
    path: '/oath/template',
    name: 'template',
    meta: {layout:'SidebarNoOath', title: 'Template'},
    component: ()=> import('./views/template.vue')
},

{
    path: '/oath/uploadpassport',
    name: 'Passport',
    meta: {layout:'SidebarNoOath', title: 'Passport'},
    component: ()=> import('./secure/uploadPassport.vue')
},
]


})