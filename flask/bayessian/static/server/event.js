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



    $(document).on('click', '.reportBtn', function() {
        var data=$(this).data('id');
        $.ajax({
            url:"/analysis",
            type:"POST",
            data:{'data':data},
            beforeSend:function(){
                showloader()
            },success:function(response){
                hideloader();
            },error:function(){
                hideloader();
                document.getElementById('response').innerHTML="<span class='redalert'>Something went wrong! Or no analysis created yet.</span>";
            }
        })
    })


    $(document).on('click', '.view', function() {
        var data=$(this).data('id');
        $.ajax({
            url:"/listdata",
            data: {tablename:'viewdata', id:data},
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
            $('#recordlist2 tr').remove();
            let html;
            html+='<tr>';
            html+='<th>S/N</th>';
            html+='<th><input class="check" type="checkbox"/></th>';
            html+='<th>Category name</th>';
            html+='<th>Text</th>';
            html+='<th>Date Created</th>';
            html+='<th>Delete</th>';
            html+='</tr>';
            $("#recordlist2").append(html);
            for (let i = 0; i<newdata.length; i++) {
            $('#recordlist2').append('<tr><td>'+ count++ +'</td><td><input class="check" value='+ newdata[i].id +' type="checkbox"/></td><td>'+newdata[i].levelname+'</td><td>'+newdata[i].text+'</td><td>'+newdata[i].dateCreated+'</td><td><button type="button" class="trashtext" data-id="'+newdata[i].id+'"><i class="fa fa-trash"></i></button></td></tr>');
            }
            }
            },
            error:function(){
                hideloader();
                document.getElementById('message').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

            }
        })

    })
    $(document).on('click', '.trashtext', function() {
        var data=$(this).data('id');
        var tdname='trashtext';
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
                document.getElementById('response2').innerHTML="<span class='redalert'>Deleted successfully</span>";
            }else{
                document.getElementById('response2').innerHTML="<span class='redalert'>Error in connection, please refresh this page or try again later.</span>";

            }
            },
            error:function(){
                hideloader();
                document.getElementById('response').innerHTML="<span class='redalert'>Something went wrong, error in netework connection.</span>";

            }
        })
    })

