$(document).ready(function(){
    function showloader(){
        $('.loaderbox').show();
      }
      function hideloader(){
        $('.loaderbox').hide();
      }

    let getpagename= $(location).attr("href").split('/').pop();
    if (getpagename=='account') {
        usersaccount();
    }else if (getpagename=='uploadresult') {
        fetchcategory();
        resultdata();
    }else if (getpagename=='uploadcourse') {
        fetchcategory();
        cousedata();
    }else if (getpagename=='createclass') {
        leveldata();
    }else if (getpagename=='dashboard') {
        resultdata();
    }else if (getpagename=='feedback') {
        feedback();
    }else{

    }



function fetchcategory(){
    $.ajax({
        url:"/listoption",
        data:{account:1},
        type:"POST",
        beforeSend:function(){
           showloader();
        },
        success:function(response){
            hideloader();
            var newdata=JSON.parse(response);
        if(newdata.msg=='norecord') {
         document.getElementById('message').innerHTML="<span class='redalert'>No record found</span>";
        }else{
        $(".cid").html("");
        $(".cid").append("<option value=''>Select category</option>");
        for (let i = 0; i<newdata.length; i++) {
        $('.cid').append('<option value="'+newdata[i].id+'">'+newdata[i].levelname+'</option>');
         }
        }
        },
        error:function(){
            hideloader();
            document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

        }
    })
    }

$("#coursefileupload").on('submit', function(e){
    e.preventDefault();
var form_data= new FormData(this);
    if (file=="") {
        document.getElementById('message').innerHTML="<span class='greenalert'>Please select a passport </span>";
            return false;
    }else{
    $.ajax({
        url:"/uploadfile",
        data: form_data,
        type:"POST",
        processData: false,
        contentType: false,
        beforeSend:function(){
            showloader();
        },
        success:function(response){
            // $("#file").trigger('reset');
            hideloader();
           if (response=='created') {
            document.getElementById('message').innerHTML="<span class='greenalert'>FIle was successfully uploaded</span>";
            cousedata();
           } else if(response=='exist') {
            document.getElementById('message').innerHTML="<span class='redalert'>This already exist, try with another</span>";
        }else if(response=='failed') {
            document.getElementById('message').innerHTML="<span class='redalert'>Error uploading the file</span>";
        }else{
            document.getElementById('message').innerHTML= response + "<span class='redalert'>Somewthing went wrong, please try again or refresh this page.</span>";
        }
        },
        error:function(){
            hideloader();
            document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

        }
    })
}
})
$("#resultfileupload").on('submit', function(e){
    e.preventDefault();
var form_data= new FormData(this);
    if (file=="") {
        document.getElementById('message').innerHTML="<span class='greenalert'>Please select a passport </span>";
            return false;
    }else{
    $.ajax({
        url:"/uploadresfile",
        data: form_data,
        type:"POST",
        processData: false,
        contentType: false,
        beforeSend:function(){
            showloader();
        },
        success:function(response){
            // $("#file").trigger('reset');
            hideloader();
           if (response=='created') {
            document.getElementById('message').innerHTML="<span class='greenalert'>File was successfully uploaded</span>";
            resultdata();
           } else if(response=='exist') {
            document.getElementById('message').innerHTML="<span class='redalert'>This already exist, try with another</span>";
        }else if(response=='failed') {
            document.getElementById('message').innerHTML="<span class='redalert'>Error uploading the file</span>";
        }else{
            document.getElementById('message').innerHTML= response + "<span class='redalert'>Somewthing went wrong, please try again or refresh this page.</span>";
        }
        },
        error:function(){
            hideloader();
            document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

        }
    })
}
})


$("#formlevel").on('submit', function(e){
    e.preventDefault();
    var form_data= new FormData(this);
    $.ajax({
        url:"/insertclass",
        data: form_data,
        type:"POST",
        processData: false,
        contentType: false,
        beforeSend:function(){
            showloader();
        },
        success:function(response){
            hideloader();
           if (response=='created') {
            document.getElementById('message').innerHTML="<span class='greenalert'>Class created successfully</span>";
            leveldata();
        } else if(response=='exist') {
            document.getElementById('message').innerHTML="<span class='redalert'>The name provided already exist</span>";
        }else{
            document.getElementById('message').innerHTML="<span class='redalert'>Somewthing went wrong, please try again or refresh this page.</span>";
        }
        },
        error:function(){
            hideloader();
            document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";
        }
    })

})




function resultdata(){
    id=1;
    $.ajax({
        url:"/listdata",
        data: {tablename:'resultdata', id:id},
        type:"POST",
        beforeSend:function(){
           showloader();
        },
        success:function(response){
            hideloader();
            var newdata=JSON.parse(response);
            let count=1;
        if(newdata.msg=='norecord') {
            document.getElementById('message').innerHTML="<span class='redalert'>No records found</span>";
        }else{
        //append to table
        $('#recordlist tr').remove();
        let html;
        html+='<tr>';
        html+='<th>S/N</th>';
        html+='<th><input class="check" type="checkbox"/></th>';
        html+='<th>Category name</th>';
        html+='<th>Filename</th>';
        html+='<th>Date Created</th>';
        html+='<th>Report</th>';
        html+='<th>View</th>';
        html+='<th>Delete</th>';
        html+='</tr>';
        $("#recordlist").append(html);
        for (let i = 0; i<newdata.length; i++) {
        $('#recordlist').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].id +' type="checkbox"/></td><td>'+newdata[i].levelname+'</td><td>'+newdata[i].filename+'</td><td>'+newdata[i].dateCreated+'</td><td><button type="button" class="reportBtn" data-id="'+newdata[i].classid+'"><i class="fa fa-eye"></i></button></td><td><button type="button" class="viewcourse view" data-id="'+newdata[i].classid+'"><i class="fa fa-eye"></i></button></td><td><button type="button" class="trashcourse" data-id="'+newdata[i].id+'"><i class="fa fa-trash"></i></button></td></tr>');
        }

        }
        },
        error:function(){
            hideloader();
            document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

        }
    })
    }

    function feedback(){
        id=1;
        $.ajax({
            url:"/listdata",
            data: {tablename:'feedback', id:id},
            type:"POST",
            beforeSend:function(){
               showloader();
            },
            success:function(response){
                hideloader();
                var newdata=JSON.parse(response);
                let count=1;
            if(newdata.msg=='norecord') {
                document.getElementById('message').innerHTML="<span class='redalert'>No records found</span>";
            }else{
            //append to table
            $('#recordlist tr').remove();
            let html;
            html+='<tr>';
            html+='<th>S/N</th>';
            html+='<th><input class="check" type="checkbox"/></th>';
            html+='<th>Prouct name</th>';
            html+='<th>Text</th>';
            html+='<th>Date Created</th>';
            html+='<th>Report</th>';
            html+='</tr>';
            $("#recordlist").append(html);
            for (let i = 0; i<newdata.length; i++) {
            $('#recordlist').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].id +' type="checkbox"/></td><td>'+newdata[i].pid+'</td><td>'+newdata[i].text+'</td><td>'+newdata[i].dateCreated+'</td><td><button type="button" class="reportBtn" data-id="'+newdata[i].id+'"><i class="fa fa-eye"></i></button></td></tr>');
            }

            }
            },
            error:function(){
                hideloader();
                document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

            }
        })
        }


function leveldata(){
   var id=1;
    $.ajax({
        url:"/listdata",
        data: {tablename:'leveldata', id:ids},
        type:"POST",
        beforeSend:function(){
           showloader();
        },
        success:function(response){
            hideloader();
            var newdata=JSON.parse(response);
            let count=1;
        if(newdata.msg=='norecord') {
            document.getElementById('message').innerHTML="<span class='redalert'>No records found</span>";
        }else{
        //append to table
        $('#recordlist tr').remove();
        let html;
        html+='<tr>';
        html+='<th>S/N</th>';
        html+='<th><input class="check" type="checkbox"/></th>';
        html+='<th>Category name</th>';
        html+='<th>Status</th>';
        html+='<th>Date Created</th>';
        html+='<th>Delete</th>';
        html+='</tr>';
        $("#recordlist").append(html);
        for (let i = 0; i<newdata.length; i++) {
        $('#recordlist').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].id +' type="checkbox"/></td><td>'+newdata[i].levelname+'</td><td>'+newdata[i].status+'</td><td>'+newdata[i].dateCreated+'</td><td><button type="button" class="trashlevel" data-id="'+newdata[i].id+'"><i class="fa fa-trash"></i></button></td></tr>');
        }
        }
        },
        error:function(){
            hideloader();
            document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

        }
    })
    }


function cousedata(){
    var id=1;
    $.ajax({
        url:"/listdata",
        data: {tablename:'couseupload', id:id},
        type:"POST",
        beforeSend:function(){
           showloader();
        },
        success:function(response){
            hideloader();
            var newdata=JSON.parse(response);
            let count=1;
        if(newdata.msg=='norecord') {
            document.getElementById('message').innerHTML="<span class='redalert'>No records found</span>";
        }else{
        //append to table
        $('#recordlist tr').remove();
        let html;
        html+='<tr>';
        html+='<th>S/N</th>';
        html+='<th><input class="check" type="checkbox"/></th>';
        html+='<th>Category name</th>';
        html+='<th>Session</th>';
        html+='<th>Semester</th>';
        html+='<th>Date Created</th>';
        html+='<th>View</th>';
        html+='<th>Delete</th>';
        html+='</tr>';
        $("#recordlist").append(html);
        for (let i = 0; i<newdata.length; i++) {
        $('#recordlist').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].id +' type="checkbox"/></td><td>'+newdata[i].levelname+'</td><td>'+newdata[i].session+'</td><td>'+newdata[i].semester+'</td><td>'+newdata[i].dateCreated+'</td><td><button type="button" class="viewcourse view" data-id="'+newdata[i].id+'"><i class="fa fa-eye"></i></button></td><td><button type="button" class="trashcourse" data-id="'+newdata[i].id+'"><i class="fa fa-trash"></i></button></td></tr>');
        }

        }
        },
        error:function(){
            hideloader();
            document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

        }
    })
    }


    $("#checkperformance").on('submit', function(e){
        e.preventDefault();
        var form_data= new FormData(this);
        $.ajax({
            url:"/checkperformance",
            data: form_data,
            type:"POST",
            processData: false,
            contentType: false,
            beforeSend:function(){
                showloader();
            },
            success:function(response){
                hideloader();
                var newdata=JSON.parse(response);
            if(newdata.msg=='norecord') {
                document.getElementById('message').innerHTML="<span class='redalert'>No records found</span>";
            }else{
            //append to table
            $('#recordlist tr').remove();
            let html;
            html+='<tr>';
            html+='<th>S/N</th>';
            html+='<th><input class="check" type="checkbox"/></th>';
            html+='<th>Matric No</th>';
            html+='<th>Name</th>';
            html+='<th>Session</th>';
            html+='<th>Semester</th>';
            html+='<th>Level</th>';
            html+='<th>TU</th>';
            html+='<th>WGP</th>';
            html+='<th>GPA</th>';
            html+='<th>CTU</th>';
            html+='<th>CTUP</th>';
            html+='<th>CGPA</th>';
            // html+='<th>Remark</th>';<td>'+newdata[i].Remark+'</td>
            html+='<th>Perfomance</th>';
            html+='<th>Courses</th>';
            html+='</tr>';
            $("#recordlist").append(html);
            var performance=0.00;
            var totalpercent=0.00;
            var count=1;
            for (let i = 0; i<newdata.length; i++) {
            performance=parseFloat(Math.round((newdata[i].Cgpa/4.00)*100));
            totalpercent +=parseFloat(Math.round((newdata[i].Cgpa/4.00)*100));
            $('#recordlist').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].id +' type="checkbox"/></td><td>'+newdata[i].MatricNo+'</td><td>'+newdata[i].Name+'</td><td>'+newdata[i].ASession+'</td><td>'+newdata[i].Semester+'</td><td>'+newdata[i].SLevel+'</td><td>'+newdata[i].TU+'</td><td>'+newdata[i].WGP+'</td><td>'+newdata[i].GPA+'</td><td>'+newdata[i].CTU+'</td><td>'+newdata[i].CTUIP+'</td><td>'+newdata[i].Cgpa+'</td><td>'+performance+'%</td><td><button type="button" class="viewcourse view" data-id="'+newdata[i].id+'"><i class="fa fa-eye"></i></button></td></tr>');
            }
                var totalSemester=4;
                var total=((totalpercent/100)*100);
                var newcount=count-1;
                var passed=parseInt(total/(newcount));
                document.getElementById('tp').innerHTML=passed;
                if (passed < 91) {
                    document.getElementById('getto').innerHTML=parseInt(passed+5)+'-'+parseInt(passed+10);
                    document.getElementById('donot').innerHTML=parseInt(passed-5)+'-'+parseInt(passed-10);
                    $(".chartdiv").show();
                }else{
                }
                // alert(count-1);
            }
            },
            error:function(){
                hideloader();
                document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

            }
        })
    })



})