import axios from 'axios'
 export default {
   data() {
       return{
        msg: 'Hello World',
        statusMsg: null
       }
   },
   methods: {
    auth_check: function(){
    axios.get('/auth/auth_check/')
        .then(response => {
            if(response.data.status==response.data.confirmed){
                this.statusMsg = 'success'
            }else{
                this.statusMsg = 'failed'
            }
        }).catch(()=>{
            this.statusMsg = 'failed'

        })
    },
   },


}