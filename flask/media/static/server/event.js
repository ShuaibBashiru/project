function showloader(){
$('.loaderbox').show();
}
function hideloader(){
$('.loaderbox').hide();
}
$(document).on('click', '.trashlevel', function() {
var data=$(this).data('id');
var tdname='trashlevel';
var $clicked_btn=$(this);
$.ajax({
    url:"/trash",
    type:"post",
    data:{id:data, tdname:tdname},
    beforeSend:function(){
        showloader();
    },
    success:function(response){
        hideloader();
    if(response=='deleted') {
        $clicked_btn.closest('tr').remove();
        document.getElementById('response').innerHTML="<span class='redalert'>Deleted successfully</span>";
    }else{
        document.getElementById('response').innerHTML="<span class='redalert'>Error in connection, please refresh this page or try again later.</span>";

    }
    },
    error:function(){
        hideloader();
        document.getElementById('response').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

    }
})

})

$(document).on('click', '.trashcourse', function() {
var data=$(this).data('id');
var tdname='trashcourse';
var $clicked_btn=$(this);
$.ajax({
    url:"/trash",
    type:"post",
    data:{id:data, tdname:tdname},
    beforeSend:function(){
        showloader();
    },
    success:function(response){
        hideloader();
    if(response=='deleted') {
        $clicked_btn.closest('tr').remove();
        document.getElementById('response').innerHTML="<span class='redalert'>Deleted successfully</span>";
    }else{
        document.getElementById('response').innerHTML="<span class='redalert'>Error in connection, please refresh this page or try again later.</span>";

    }
    },
    error:function(){
        hideloader();
        document.getElementById('response').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

    }
})
})

// $(document).on('click', '.viewcourse', function() {
// var data=$(this).data('id');
// $.ajax({
//     url:"/listdata",
//     data: {tablename:'viewdata', id:data},
//     type:"POST",
//     beforeSend:function(){
//         showloader();
//     },
//     success:function(response){
//         hideloader();
//         var newdata=JSON.parse(response);
//         let count=1;
//     if(newdata.msg=='norecord') {
//         document.getElementById('message').innerHTML="<span class='redalert'>No records found</span>";
//     }else{
//     //append to table
//     $('#recordlist2 tr').remove();
//     let html;
//     html+='<tr>';
//     html+='<th>S/N</th>';
//     html+='<th>Matric Number</th>';
//     html+='<th>Level</th>';
//     html+='<th>Semester</th>';
//     html+='<th>Course Code</th>';
//     html+='<th>Unit</th>';
//     html+='<th>Grades</th>';
//     html+='<th>Status</th>';
//     html+='</tr>';
//     $("#response2").html("Course registration Summary");
//     $("#recordlist2").append(html);
//     var totalUnit=0.0;
//     var totalScore=0.0;
//     for (let i = 0; i<newdata.length; i++) {
//         totalUnit += parseFloat(Math.round(newdata[i].CourseUnit));
//         totalScore += parseFloat(Math.round(newdata[i].CourseUnit*newdata[i].Score));
//         if (newdata[i].LevelID==1) {
//                 var level='ND 1';
//         }else if (newdata[i].LevelID==2) {
//             var level='ND 2';
//         }else if (newdata[i].LevelID==3) {
//             var level='ND 3';
//         }else if (newdata[i].LevelID==4) {
//             var level='HND 1';
//         }else if (newdata[i].LevelID==5) {
//             var level='HND 2';
//         }

//         if (newdata[i].SemesterID==1) {
//                 var semester='FIRST SEMESTER';
//         }else if (newdata[i].SemesterID==2) {
//             var semester='SECOND SEMESTER';
//         }
//     $('#recordlist2').append('<tr><td>'+ count++ +'</td><td>'+newdata[i].MatricNo+'</td><td>'+level+'</td><td>'+semester+'</td><td>'+newdata[i].CourseCode+'</td><td>'+newdata[i].CourseUnit+'</td><td>'+newdata[i].Grade+'</td><td><button type="button" class="edit" data-id="'+newdata[i].id+'"><i class="fa fa-check"></i></button></td></tr>');
//     }
//     alert(totalScore/totalUnit);
//     }
//     },
//     error:function(){
//         hideloader();
//         document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

//     }
// })



// })