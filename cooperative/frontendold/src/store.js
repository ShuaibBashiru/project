import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
export default new Vuex.Store({
    state: {
      count: 0,
      isLoggedIn: null,
      set_user: [],
    },
    actions:{
        auth_check({commit}){
            axios.get('/auth/auth_check/')
                .then(response => {
                    if(response.data.status==response.data.confirmed){
                       let set_user = response.data.row
                       let isLoggedIn = response.data.status
                       commit('SET_POSTS', set_user, isLoggedIn)
                    }else{
                       window.location.href='/site/logout'
                    }
                 }).catch((error)=>{
                    alert("no active session "+ error)
        
                })
            },
    },
    mutations:{
        SET_POSTS(state, set_user, isLoggedIn){
            state.set_user = set_user
            state.isLoggedIn = isLoggedIn
        }
    }
  })
  

