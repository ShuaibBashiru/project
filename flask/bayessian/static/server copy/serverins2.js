$(document).ready(function(){
    function showloader(){
        $('.loaderbox').show();
      }
      function hideloader(){
        $('.loaderbox').hide();
      }

      $(".refresh").on('click', function(e){
          list();
          document.getElementById('statdiv').innerHTML="";

      })
        $(".generatereport").on('click', function(e){
    $.ajax({
        url:"http://127.0.0.1:2000/analysis",
        method:"POST",
        contentType:false,
        cache:false,
        processData:false,
        data:{'fetch':1},
        beforeSend:function(){
            showloader()
        },success:function(response){
            hideloader();
            list();
            document.getElementById('statdiv').innerHTML="";

        },error:function(){
            hideloader();
            document.getElementById('statdiv').innerHTML="<span class='redalert'>Something went wrong! Or no analysis created yet.</span>";
        }
    })
})

      list();
function list(){
    $.ajax({
        url:"http://127.0.0.1:2000/classfetch",
        method:"POST",
        contentType:false,
        cache:false,
        processData:false,
        data:{'fetch':1},
        beforeSend:function(){
            showloader()
        },success:function(response){
            hideloader();
            var newdata=response;
        for (let i = 0; i<newdata.length; i++) {
$('.statdiv').append("<img src='http://127.0.0.1:2000/static/plots/"+newdata[i]+"'>");
         }
        },error:function(){
            hideloader();
            document.getElementById('statdiv').innerHTML="<span class='redalert'>Something went wrong! Or no analysis created yet.</span>";
        }
    })
}

    $("#jj").on('submit', function(e){
        e.preventDefault();
        var matricno=$('.matricno').val();
        if (matricno=="") {
            document.getElementById('message').innerHTML="<span class='greenalert'>Please select a passport </span>";
                return false;
        }else{
        var form_data= new FormData(this);
        $.ajax({
            url:"http://127.0.0.1:3000/checkperformance",
            method:"POST",
            contentType:false,
            cache:false,
            processData:false,
            data:form_data,
            beforeSend:function(){
                showloader()
            },
            success:function(response){
                hideloader();
                var newdata=response;
                let count=1;
            // if(response.msg=='norecord') {
            //     document.getElementById('message').innerHTML="<span class='redalert'>Account already exist with the email provided</span>";
            // }else{
            //append to table
            $('#recordlist tr').remove();
            let html;
            html+='<tr>';
            html+='<th>S/N</th>';
            html+='<th>Matric No</th>';
            html+='<th>Department</th>';
            html+='<th>Level</th>';
            html+='<th>Session</th>';
            html+='<th>Course Code</th>';
            html+='<th>Semester</th>';
            html+='<th>Test</th>';
            html+='<th>Exam</th>';
            html+='</tr>';
            $("#recordlist").append(html);
            for (i in myObj.cars) {
                x += "<h1>" + myObj.cars[i].name + "</h1>";
                for (j in myObj.cars[i].models) {
                  x += myObj.cars[i].models[j];
                }
              }
            for (let i = 0; i<newdata[0].length; i++) {
            //   console.log(newdata[i])
              console.log(newdata[i])
            // $('#recordlist').append('<tr><td>'+ count++ +'</td><td>'+newdata[i].matricno+'</td><td>'+newdata[i].department+'</td><td>'+newdata[i].level+'</td><td>'+newdata[i].session+'</td><td>'+ newdata[i].coursecode +'</td><td>'+ newdata[i].semester +'</td><td>'+newdata[i].text +'</td><td>'+newdata[i].exam +'</td></tr>');
             }
            // }
            },
            error:function(){
                hideloader();
                document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";
            }
        })
    }
    })
function account(usersaccount){
    $.ajax({
        url:"http://localhost:8080/code/index.php/comsel/u_records",
        method:"POST",
        data:{account:1},
        beforeSend:function(){
           showloader();
        },
        success:function(response){
            hideloader();
            var newdata=JSON.parse(response);
            let count=1;
        if(response.msg=='norecord') {
            document.getElementById('message').innerHTML="<span class='redalert'>Account already exist with the email provided</span>";
        }else{
        //append to table
        $('#recordlist tr').remove();
        let html;
        html+='<tr>';
        html+='<th>S/N</th>';
        html+='<th><input class="check" type="checkbox"/></th>';
        html+='<th>First Name</th>';
        html+='<th>Last Name</th>';
        html+='<th>Address</th>';
        html+='<th>Email</th>';
        html+='<th>Contact</th>';
        html+='<th>View</th>';
        html+='<th>Edit</th>';
        html+='<th>Delete</th>';
        html+='</tr>';
        $("#recordlist").append(html);
        for (let i = 0; i<newdata.length; i++) {
        $('#recordlist').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].id +' type="checkbox"/></td><td>'+newdata[i].__surname+'</td><td>'+newdata[i].__oname+'</td><td>'+newdata[i].address+'</td><td>'+newdata[i].__email+'</td><td>'+newdata[i].__phone+'</td><td><button class="view" value='+ newdata[i].__id +'><i class="fa fa-eye"></i></button></td><td><button class="edit" value='+ newdata[i].__id +'><i class="fa fa-edit"></i></button></td><td><button class="trash" value='+ newdata[i].__id +'><i class="fa fa-trash"></i></button></td></tr>');
         }
        }
        },
        error:function(){
            hideloader();
            document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

        }
    })
}
//admin account
$("#aform").on('submit', function(e){
    e.preventDefault();
    var file=$('.file').val();
    if (file=="") {
        document.getElementById('message').innerHTML="<span class='greenalert'>Please select a passport </span>";
            return false;
    }else{
    var form_data= new FormData(this);
    $.ajax({
        url:"http://localhost:8080/code/index.php/comins/a_insert",
        method:"POST",
        contentType:false,
        cache:false,
        processData:false,
        data:form_data,
        beforeSend:function(){
            showloader()
        },
        success:function(response){
            $("#file").trigger('reset');
            hideloader();
            var newdata=JSON.parse(response);
           if (newdata.msg=='created') {
            document.getElementById('message').innerHTML="<span class='greenalert'>Account created successfully</span>";
            fetchaccount();
           } else if(newdata.msg=='exist') {
            document.getElementById('message').innerHTML="<span class='redalert'>Account already exist with the email provided</span>";

        }else{
            document.getElementById('message').innerHTML="<span class='redalert'>Somewthing went wrong, please try again or refresh this page.</span>";
        }
        },
        error:function(){
            hideloader();
            document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

        }
    })
}
})
function admin(adminaccount){
$.ajax({
    url:"http://localhost:8080/code/index.php/comsel/a_records",
    method:"POST",
    data:{account:1},
    beforeSend:function(){
       showloader();
    },
    success:function(response){
        hideloader();
        var newdata=JSON.parse(response);
        let count=1;
    if(response.msg=='norecord') {
        document.getElementById('message').innerHTML="<span class='redalert'>Account already exist with the email provided</span>";
    }else{
    //append to table
    $('#recordlist tr').remove();
    let html;
    html+='<tr>';
    html+='<th>S/N</th>';
    html+='<th><input class="check" type="checkbox"/></th>';
    html+='<th>First Name</th>';
    html+='<th>Last Name</th>';
    html+='<th>Email</th>';
    html+='<th>Contact</th>';
    html+='<th>View</th>';
    html+='<th>Edit</th>';
    html+='<th>Delete</th>';
    html+='</tr>';
    $("#recordlist").append(html);
    for (let i = 0; i<newdata.length; i++) {
    $('#recordlist').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].__id +' type="checkbox"/></td><td>'+newdata[i].__surname+'</td><td>'+newdata[i].__oname+'</td><td>'+newdata[i].__email+'</td><td>'+newdata[i].__phone+'</td><td><button class="view" value='+ newdata[i].__id +'><i class="fa fa-eye"></i></button></td><td><button class="edit" value='+ newdata[i].__id +'><i class="fa fa-edit"></i></button></td><td><button class="trash" value='+ newdata[i].__id +'><i class="fa fa-trash"></i></button></td></tr>');
     }
    }
    },
    error:function(){
        hideloader();
        document.getElementById('message').innerHTML=response+"<span class='redalert'>Something went wrong, error in netework connection.</span>";

    }
})
}



})