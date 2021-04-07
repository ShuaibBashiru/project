$(document).ready(function(){
function showloader(){
$('.loaderbox').show();
}
function hideloader(){
$('.loaderbox').hide();
}

var getpagename=$(location).attr("href").split('/').pop();
var str=$(location).attr("href");
if (getpagename=='account') {
usersaccount();
}else if (getpagename=='uploadimages') {
fetchcategory();
// resultdata();
}else if (getpagename=='uploadcourse') {
fetchcategory();
cousedata();
}else if (getpagename=='createclass') {
leveldata();
}else if (str.includes('statistics')) {
counter();
}else if (str.includes('performance')) {
    listimages();
}else{

}


function listimages(){
    id=1;
    $.ajax({
    url:"/listdata",
    data: {tablename:'listimages', id:id},
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
    $(".formdiv").append(newdata);
    var orgWidth, orgHeight, size, filetype, types, sizes;
    for (let i = 0; i<newdata.length; i++) {
        var tmpImg = new Image();
        tmpImg.src='static/document/uploadedfiles/'+newdata[i].filename+''; //or  document.images[i].src;
        orgWidth = tmpImg.width;
        orgHeight = tmpImg.height;
        size=parseInt(newdata[i].others)/1024;
        sizes=Math.round(size);
        filetype=newdata[i].filename;
        filetype=filetype.split('.');
        types=filetype[1];

    $('.formdiv').append('<div class="imgbox"><div class="img"><img id="imgname" src="static/document/uploadedfiles/'+newdata[i].filename+'"></div><div class="imgcontents"><li>Source: '+newdata[i].cname+'</li><li>Height: '+orgHeight+'</li><li>Height: '+orgWidth+'</li><li>File type: '+types+'</li><li>File Size: '+sizes+'Kb</li></div></div>');


}

    }
    },
    error:function(){
    hideloader();
    document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

    }
    })
    }




//category account
$('#formlevel').submit(function(e){
e.preventDefault();
$.ajax({
url:"/insertclass",
data: $('form').serialize(),
type:"POST",
beforeSend:function(){
showloader();
},
success:function(response){
hideloader();
if (response=='created') {
document.getElementById('message').innerHTML="<span class='greenalert'>Item created successfully</span>";
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
// return false;

})


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
document.getElementById('message').innerHTML="<span class='redalert'>Account already exist with the email provided</span>";
}else{
$(".cid").html("");
$(".cid").append("<option value=''>Select category</option>");
for (let i = 0; i<newdata.length; i++) {
$('.cid').append('<option value="'+newdata[i].id+'">'+newdata[i].cname+'</option>');
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
// var file=document.getElementById("file").files[0];
// form_data.append('size', file.size);
var form_data= new FormData(this);
$.ajax({
url:"/bulkimages",
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
// resultdata();
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
html+='<th>Level name</th>';
html+='<th>Session</th>';
html+='<th>Semester</th>';
html+='<th>Date Created</th>';
html+='<th>View</th>';
html+='<th>Delete</th>';
html+='</tr>';
$("#recordlist").append(html);
for (let i = 0; i<newdata.length; i++) {
$('#recordlist').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].id +' type="checkbox"/></td><td>'+newdata[i].cname+'</td><td>'+newdata[i].session+'</td><td>'+newdata[i].semester+'</td><td>'+newdata[i].dateCreated+'</td><td><button type="button" class="viewcourse view" data-id="'+newdata[i].id+'"><i class="fa fa-eye"></i></button></td><td><button type="button" class="trashcourse" data-id="'+newdata[i].id+'"><i class="fa fa-trash"></i></button></td></tr>');
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
id=1;
$.ajax({
url:"/listdata",
data: {tablename:'leveldata', id:id},
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
html+='<th>Level name</th>';
html+='<th>Status</th>';
html+='<th>Date Created</th>';
html+='<th>Delete</th>';
html+='</tr>';
$("#recordlist").append(html);
for (let i = 0; i<newdata.length; i++) {
$('#recordlist').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].id +' type="checkbox"/></td><td>'+newdata[i].cname+'</td><td>'+newdata[i].status+'</td><td>'+newdata[i].date_Created+'</td><td><button type="button" class="trashlevel" data-id="'+newdata[i].id+'"><i class="fa fa-trash"></i></button></td></tr>');
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
id=1;
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
html+='<th>Level name</th>';
html+='<th>Session</th>';
html+='<th>Semester</th>';
html+='<th>Date Created</th>';
html+='<th>View</th>';
html+='<th>Delete</th>';
html+='</tr>';
$("#recordlist").append(html);
for (let i = 0; i<newdata.length; i++) {
$('#recordlist').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].id +' type="checkbox"/></td><td>'+newdata[i].cname+'</td><td>'+newdata[i].session+'</td><td>'+newdata[i].semester+'</td><td>'+newdata[i].dateCreated+'</td><td><button type="button" class="viewcourse view" data-id="'+newdata[i].id+'"><i class="fa fa-eye"></i></button></td><td><button type="button" class="trashcourse" data-id="'+newdata[i].id+'"><i class="fa fa-trash"></i></button></td></tr>');
}

}
},
error:function(){
hideloader();
document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

}
})
}

// $("#checkperformance").on('submit', function(e){
//     e.preventDefault();
//     var form_data= new FormData(this);
//     $.ajax({
//         url:"/checkperformance",
//         data: form_data,
//         type:"POST",
//         processData: false,
//         contentType: false,
//         beforeSend:function(){
//             showloader();
//         },
//         success:function(response){
//             hideloader();
//             var newdata=JSON.parse(response);
//         if(newdata.msg=='norecord') {
//             document.getElementById('message').innerHTML="<span class='redalert'>No records found</span>";
//         }else{
//         //append to table
//         $('#recordlist tr').remove();
//         let html;
//         html+='<tr>';
//         html+='<th>S/N</th>';
//         html+='<th><input class="check" type="checkbox"/></th>';
//         html+='<th>Matric No</th>';
//         html+='<th>Name</th>';
//         html+='<th>Session</th>';
//         html+='<th>Semester</th>';
//         html+='<th>Level</th>';
//         html+='<th>TU</th>';
//         html+='<th>WGP</th>';
//         html+='<th>GPA</th>';
//         html+='<th>CTU</th>';
//         html+='<th>CTUP</th>';
//         html+='<th>CGPA</th>';
//         // html+='<th>Remark</th>';<td>'+newdata[i].Remark+'</td>
//         html+='<th>Perfomance</th>';
//         html+='<th>Courses</th>';
//         html+='</tr>';
//         $("#recordlist").append(html);
//         var performance=0.00;
//         var totalpercent=0.00;
//         var count=1;
//         for (let i = 0; i<newdata.length; i++) {
//         performance=parseFloat(Math.round((newdata[i].Cgpa/4.00)*100));
//         totalpercent +=parseFloat(Math.round((newdata[i].Cgpa/4.00)*100));
//         $('#recordlist').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].id +' type="checkbox"/></td><td>'+newdata[i].MatricNo+'</td><td>'+newdata[i].Name+'</td><td>'+newdata[i].ASession+'</td><td>'+newdata[i].Semester+'</td><td>'+newdata[i].SLevel+'</td><td>'+newdata[i].TU+'</td><td>'+newdata[i].WGP+'</td><td>'+newdata[i].GPA+'</td><td>'+newdata[i].CTU+'</td><td>'+newdata[i].CTUIP+'</td><td>'+newdata[i].Cgpa+'</td><td>'+performance+'%</td><td><button type="button" class="viewcourse view" data-id="'+newdata[i].MatricNo+'"><i class="fa fa-eye"></i></button></td></tr>');
//         }
//             var totalSemester=4;
//             var total=((totalpercent/100)*100);
//             var newcount=count-1;
//             var passed=parseInt(total/(newcount));
//             document.getElementById('tp').innerHTML=passed;
//             if (passed < 91) {
//                 document.getElementById('getto').innerHTML=parseInt(passed+5)+'-'+parseInt(passed+10);
//                 document.getElementById('donot').innerHTML=parseInt(passed-5)+'-'+parseInt(passed-10);
//                 $(".chartdiv").show();
//             }else{
//             }
//             // alert(count-1);
//         }
//         },
//         error:function(){
//             hideloader();
//             document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

//         }
//     })

// })

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
let count=1;
if(newdata.msg=='norecord') {
document.getElementById('message').innerHTML="<span class='redalert'>No records found</span>";
}else{
//append to table
$('#recordlist2 tr').remove();
let html;
html+='<tr>';
html+='<th>S/N</th>';
html+='<th>Matric Number</th>';
html+='<th>Level</th>';
html+='<th>Semester</th>';
html+='<th>Course Code</th>';
html+='<th>Unit</th>';
html+='<th>Grade Point</th>';
html+='<th>Grades</th>';
html+='<th>Status</th>';
html+='</tr>';
// $("#response2").html("Course registration Summary");
$("#recordlist2").append(html);
var totalUnit=0.00;
var totalScore=0.00,
tunit=0.00,
wgp=0.00,
ctu=0.00,
cgpa=0.00,
performance=0.00;
var totalpercent;
var matric="";
for (let i = 0; i<newdata.length; i++) {
    tunit += parseFloat(Math.round(newdata[i].CourseUnit));
    wgp += parseFloat(Math.round(newdata[i].Score*newdata[i].CourseUnit));
    ctu += parseFloat(Math.round(newdata[i].CourseUnit));
// totalScore += parseFloat(Math.round(newdata[i].CourseUnit*newdata[i].Score));
matric=newdata[i].MatricNo;
if (newdata[i].LevelID==1) {
var level='ND 1';
}else if (newdata[i].LevelID==2) {
var level='ND 2';
}else if (newdata[i].LevelID==3) {
var level='ND 3';
}else if (newdata[i].LevelID==4) {
var level='HND 1';
}else if (newdata[i].LevelID==5) {
var level='HND 2';
}

if (newdata[i].SemesterID==1) {
var semester='FIRST SEMESTER';
}else if (newdata[i].SemesterID==2) {
var semester='SECOND SEMESTER';
}
$('#recordlist2').append('<tr><td>'+ count++ +'</td><td>'+newdata[i].MatricNo+'</td><td>'+level+'</td><td>'+semester+'</td><td>'+newdata[i].CourseCode+'</td><td>'+newdata[i].CourseUnit+'</td><td>'+newdata[i].Score+'</td><td>'+newdata[i].Grade+'</td><td><button type="button" class="edit" data-id="'+newdata[i].id+'"><i class="fa fa-check"></i></button></td></tr>');
}
$('#recordlist tr').remove();
let html1;
html1+='<tr>';
html1+='<th>Matric No</th>';
html1+='<th>TU</th>';
html1+='<th>WGP</th>';
html1+='<th>CTU</th>';
html1+='<th>CGPA</th>';
html1+='<th>Perfomance</th>';
html1+='</tr>';
$("#recordlist").append(html1);
cgpa=parseFloat(wgp/tunit);
cgpa=Math.round(cgpa*100)/100;
performance=(cgpa/4.00)*100;
var passed=parseInt(performance);
document.getElementById('tp').innerHTML=passed;
if (passed < 91) {
document.getElementById('getto').innerHTML=parseInt(passed+5)+'-'+parseInt(passed+10);
document.getElementById('donot').innerHTML=parseInt(passed-5)+'-'+parseInt(passed-10);
$(".chartdiv").show();
}else{
}
$('#recordlist').append('<tr><td>'+matric+'</td><td>'+tunit+'</td><td>'+wgp+'</td><td>'+ctu+'</td><td>'+cgpa+'</td><td>'+performance+'%</td></tr>');
}
},
error:function(){
hideloader();
document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

}
})



})


function counter(){
id=1;
$.ajax({
url:"/counter",
data: {id:id},
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
for (let i = 0; i<newdata.length; i++) {
$('.totalstudent').html(newdata[0]);
$('.courseuploaded').html(newdata[1]);
$('.resultploaded').html(newdata[2]);
// $('#recordlist').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].id +' type="checkbox"/></td><td>'+newdata[i].cname+'</td><td>'+newdata[i].session+'</td><td>'+newdata[i].semester+'</td><td>'+newdata[i].dateCreated+'</td><td><button type="button" class="viewcourse view" data-id="'+newdata[i].id+'"><i class="fa fa-eye"></i></button></td><td><button type="button" class="trashcourse" data-id="'+newdata[i].id+'"><i class="fa fa-trash"></i></button></td></tr>');
}

}
},
error:function(){
hideloader();
document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

}
})
}


$(document).on('click', '.tc', function() {
var data=1;
$.ajax({
url:"/listdata",
data: {tablename:'totalcourse', id:data},
type:"POST",
beforeSend:function(){
showloader();
},
success:function(response){
hideloader();
var newdata=JSON.parse(response);
let count=1;
if(newdata.msg=='norecord') {
document.getElementById('response2').innerHTML="<span class='redalert'>No records found</span>";
}else{
//append to table
$('#recordlist2 tr').remove();
let html;
html+='<tr>';
html+='<th>S/N</th>';
html+='<th>Matric Number</th>';
html+='<th>Level</th>';
html+='<th>Semester</th>';
html+='<th>Course Code</th>';
html+='<th>Course Unit</th>';
html+='<th>Grade point</th>';
html+='<th>Grades</th>';
html+='<th>Exam Score</th>';
// html+='<th>Date Created</th>';
html+='<th>Status</th>';
html+='</tr>';
$("#response2").html("Course registration Summary");
$("#recordlist2").append(html);
for (let i = 0; i<newdata.length; i++) {
if (newdata[i].LevelID==1) {
var level='ND 1';
}else if (newdata[i].LevelID==2) {
var level='ND 2';
}else if (newdata[i].LevelID==3) {
var level='ND 3';
}else if (newdata[i].LevelID==4) {
var level='HND 1';
}else if (newdata[i].LevelID==5) {
var level='HND 2';
}else if (newdata[i].LevelID==6) {
var level='ND 6';
}

if (newdata[i].SemesterID==1) {
var semester='FIRST SEMESTER';
}else if (newdata[i].SemesterID==2) {
var semester='SECOND SEMESTER';
}
$('#recordlist2').append('<tr><td>'+ count++ +'</td><td>'+newdata[i].MatricNo+'</td><td>'+level+'</td><td>'+semester+'</td><td>'+newdata[i].CourseCode+'</td><td>'+newdata[i].CourseUnit+'</td><td>'+newdata[i].Score+'</td><td>'+newdata[i].Grade+'</td><td>'+newdata[i].Exam+'</td><td><button type="button" class="edit" data-id="'+newdata[i].id+'"><i class="fa fa-check"></i></button></td></tr>');
}
}
},
error:function(){
hideloader();
document.getElementById('response').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

}
})
})






})