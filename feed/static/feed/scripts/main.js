$(document).ready(function(){


//guest carousel
$('#guest-carousel').carousel({
    interval:3000
})

//popover start

$('[data-toggle="popover"]').popover();
$('.popover-dismiss').popover({
    trigger: 'focus'
})


//navigation management

var nav_home=$('#nav-home')
var nav_message=$('#nav-message')
var nav_post=$('#nav-post')
var nav_explore=$('#nav-explore')
var nav_heart=$('#nav-heart')
var nav_profile_img=$('#nav-profile-img')


var profile_post=$('#profile-post-section')
var profile_igtv=$('#profile-igtv-section')
var profile_bookmark=$('#profile-bookmark-section')
var profile_tagged=$('#profile-tagged-section')

var profile_post_content=$('#profile-post-content')
var profile_igtv_content=$('#profile-igtv-content')
var profile_bookmark_content=$('#profile-bookmark-content')
var profile_tagged_content=$('#profile-tagged-content')

var profile_post_container=$('#profile-post-container')
var profile_igtv_container=$('#profile-igtv-container')
var profile_bookmark_container=$('#profile-bookmark-container')
var profile_tagged_container=$('#profile-tagged-container')

profile_post.click(function(){
    console.log('profile post')

    profile_igtv.removeClass('text-dark').addClass('text-muted')
    profile_post.addClass('text-dark').removeClass('text-muted')
    profile_bookmark.removeClass('text-dark').addClass('text-muted')
    profile_tagged.removeClass('text-dark').addClass('text-muted')

    profile_post_container.addClass('top-border')
    profile_igtv_container.removeClass('top-border')
    profile_bookmark_container.removeClass('top-border')
    profile_tagged_container.removeClass('top-border')

    profile_post_content.css('display','block')
    profile_igtv_content.css('display','none')
    profile_bookmark_content.css('display','none')
    profile_tagged_content.css('display','none')

})

profile_igtv.click(function(){
    console.log('profile igtv')

    profile_post.removeClass('text-dark').addClass('text-muted')
    profile_igtv.addClass('text-dark').removeClass('text-muted')
    profile_bookmark.removeClass('text-dark').addClass('text-muted')
    profile_tagged.removeClass('text-dark').addClass('text-muted')

    profile_post_container.removeClass('top-border')
    profile_igtv_container.addClass('top-border')
    profile_bookmark_container.removeClass('top-border')
    profile_tagged_container.removeClass('top-border')

    profile_post_content.css('display','none')
    profile_igtv_content.css('display','block')
    profile_bookmark_content.css('display','none')
    profile_tagged_content.css('display','none')
})

profile_bookmark.click(function(){
    console.log('profile bookmark')

    profile_post.removeClass('text-dark').addClass('text-muted')
    profile_igtv.removeClass('text-dark').addClass('text-muted')
    profile_bookmark.addClass('text-dark').removeClass('text-muted')
    profile_tagged.removeClass('text-dark').addClass('text-muted')

    profile_post_container.removeClass('top-border')
    profile_igtv_container.removeClass('top-border')
    profile_bookmark_container.addClass('top-border')
    profile_tagged_container.removeClass('top-border')


    profile_post_content.css('display','none')
    profile_igtv_content.css('display','none')
    profile_bookmark_content.css('display','block')
    profile_tagged_content.css('display','none')
})

profile_tagged.click(function(){
    console.log('profile tagged')

    profile_post.removeClass('text-dark').addClass('text-muted')
    profile_igtv.removeClass('text-dark').addClass('text-muted')
    profile_bookmark.removeClass('text-dark').addClass('text-muted')
    profile_tagged.addClass('text-dark').removeClass('text-muted')

    profile_post_container.removeClass('top-border')
    profile_igtv_container.removeClass('top-border')
    profile_tagged_container.addClass('top-border')
    profile_bookmark_container.removeClass('top-border')

    profile_post_content.css('display','none')
    profile_igtv_content.css('display','none')
    profile_tagged_content.css('display','block')
    profile_bookmark_content.css('display','none')
})

//  for sm profile-navbar


var profile_post_sm=$('#profile-post-section-sm')
var profile_igtv_sm=$('#profile-igtv-section-sm')
var profile_bookmark_sm=$('#profile-bookmark-section-sm')
var profile_tagged_sm=$('#profile-tagged-section-sm')

var profile_post_container_sm=$('#profile-post-container-sm')
var profile_igtv_container_sm=$('#profile-igtv-container-sm')
var profile_bookmark_container_sm=$('#profile-bookmark-container-sm')
var profile_tagged_container_sm=$('#profile-tagged-container-sm')

profile_post_sm.click(function(){
    console.log('profile post')
    profile_post_sm.addClass('text-primary').removeClass('text-muted')
    profile_igtv_sm.removeClass('text-primary').addClass('text-muted')
    profile_bookmark_sm.removeClass('text-primary').addClass('text-muted')
    profile_tagged_sm.removeClass('text-primary').addClass('text-muted')


    profile_post_content.css('display','block')
    profile_igtv_content.css('display','none')
    profile_bookmark_content.css('display','none')
    profile_tagged_content.css('display','none')

})

profile_igtv_sm.click(function(){
    console.log('profile igtv')
    profile_post_sm.removeClass('text-primary').addClass('text-muted')
    profile_igtv_sm.addClass('text-primary').removeClass('text-muted')
    profile_bookmark_sm.removeClass('text-primary').addClass('text-muted')
    profile_tagged_sm.removeClass('text-primary').addClass('text-muted')

    profile_post_content.css('display','none')
    profile_igtv_content.css('display','block')
    profile_bookmark_content.css('display','none')
    profile_tagged_content.css('display','none')
})

profile_bookmark_sm.click(function(){
    console.log('profile bookmark')
    profile_post_sm.removeClass('text-primary').addClass('text-muted')
    profile_igtv_sm.removeClass('text-primary').addClass('text-muted')
    profile_bookmark_sm.addClass('text-primary').removeClass('text-muted')
    profile_tagged_sm.removeClass('text-primary').addClass('text-muted')

    profile_post_content.css('display','none')
    profile_igtv_content.css('display','none')
    profile_bookmark_content.css('display','block')
    profile_tagged_content.css('display','none')
})

profile_tagged_sm.click(function(){
    console.log('profile tagged')
    profile_post_sm.removeClass('text-primary').addClass('text-muted')
    profile_igtv_sm.removeClass('text-primary').addClass('text-muted')
    profile_bookmark_sm.removeClass('text-primary').addClass('text-muted')
    profile_tagged_sm.addClass('text-primary').removeClass('text-muted')

    profile_post_content.css('display','none')
    profile_igtv_content.css('display','none')
    profile_tagged_content.css('display','block')
    profile_bookmark_content.css('display','none')
})



})

var follow_id=''

function follow_handle(follow_id){
    console.log('follow handle working')
    follow_id=follow_id.toString()
    var follow=$('#'+follow_id)
    if(follow.attr('data-log')=='follow')
    {
        console.log('following')
        $.ajax({
            url:follow.attr('data-follow-url'),
            type:'get',
            dataType:'json',
            success:function(data){
                if(data.follow_done==true)
                {
                    console.log('followed')
                    follow.html('Unfollow')
                    follow.attr('data-log','unfollow')
                    if($('#followeds-count').attr('data-owner')=='current_user'){
                        $('#followeds-count').html(data.followeds_count)
                    }
                }
            }
        })
    }

    else{
        console.log('unfollowing')
        $.ajax({
            url:follow.attr('data-unfollow-url'),
            type:'get',
            dataType:'json',
            success:function(data){
                if(data.unfollow_done==true)
                {
                    console.log('unfollowed')   
                    follow.html('Follow')
                    follow.attr('data-log','follow')
                    if($('#followeds-count').attr('data-owner')=='current_user'){
                        $('#followeds-count').html(data.followeds_count)
                    }
                }
            }
        })

    }
    
}



var image_id=''
function show_like(image_id){
    show_like_heart=$('#'+image_id+'-heart')
    show_like_heart.fadeIn("fast");
    setTimeout(function(){
        show_like_heart.fadeOut("fast")
    },500)

}




var comment_id=''
function comment_handle(comment_id){
    comment_id=comment_id.toString()
    var comment_text=$('#'+comment_id).val().trim()
    if(comment_text.length>0){
        $('#'+comment_id+'-post').removeAttr('disabled')
        console.log('enabled')
    }
    else{
        $('#'+comment_id+'-post').attr('disabled','disabled')
        console.log('disabled')
    }

}


var comment_form_id=''
function comment_form_handle(comment_form_id,e){
    e.preventDefault();
    console.log('comment form handle working!')
    comment_form_id=comment_form_id.toString()
    var form=$('#'+comment_form_id)
    $.ajax({
        url:form.attr('action'),
        data:form.serialize(),
        type:form.attr('method'),
        dataType:'json',
        success:function(data){
                $('#'+comment_form_id+'-list').prepend(`<li class="list-unstyled-item mb-3">
                                                            <div class="row">
                                                                <div class="col-md-2">
                                                                    <img src="`+data.commentor_image_url+`" class="rounded-circle feed-comment-img ml-1 mr-2" alt="">
                                                                </div>

                                                                <div class="col-md-9 pr-0">
                                                                    <small class="comment-font"><a href="#" class="commentor-font">`+data.commentor_username+`</a>&nbsp;`+data.comment_text+`</small>
                                                                </div>

                                                                <i class="far fa-heart comment-heart text-dark"></i>
                                                            </div>
                                                        </li>`)
        }
    })
    return false
}


var id=''
function clear_input(id){
    var input=$('#'+id)
    input.val('')
}






var id=''

function like_handle(id){
    id=id.toString()
    var like=$('#'+id)
    if(like.attr('data-liked')=="false"){
        console.log('comment like working')
        $.ajax({
            url:like.attr('data-like-url'),
            type:'get',
            dataType:'json',
            success:function(data){
                console.log('inside comment like success')
                var like_count=$('#'+id+'-count')
                like_count.html(data.count)
                like.attr('data-liked','true')
                like.toggleClass('fas far text-dark text-tomato')
            }
        })
    }
    else{
        console.log('comment unlike working')
        $.ajax({
            url:like.attr('data-unlike-url'),
            type:'get',
            dataType:'json',
            success:function(data){
                console.log('inside comment unlike success')
                var like_count=$('#'+id+'-count')
                like_count.html(data.count)
                like.attr('data-liked','false')
                like.toggleClass('fas far text-dark text-tomato')
            }
        })
    }

}


var id=''

function bookmark_handle(id){
    id=id.toString()
    var bookmark=$('#'+id)
    if(bookmark.attr('data-bookmarked')=="false"){
        console.log('bookmarking')
        $.ajax({
            url:bookmark.attr('data-bookmark-url'),
            type:'get',
            dataType:'json',
            success:function(data){
                if(data.bookmarked)
                {
                    bookmark.attr('data-bookmarked','true')
                    bookmark.toggleClass('fas far')
                }
            }
        })
    }
    else{
        $.ajax({
            url:bookmark.attr('data-unbookmark-url'),
            type:'get',
            dataType:'json',
            success:function(data){
                if(data.unbookmarked)
                {
                    bookmark.attr('data-bookmarked','false')
                    bookmark.toggleClass('fas far')
                }
            }
        })
    }

}




var video_id=''

function play_handle(video_id){
    var video=$('#'+video_id+'-video').get(0)
    var play=$('#'+video_id+'-video-play')

    if(video.paused){
        video.play()
        play.css('opacity',0)
    }
    else{
        video.pause()
        play.css('opacity',0.9)
    }
}


$('.feed-carousel').carousel({
    pause:true,
    interval: false
})


var tag_id=''

function tag_handle(tag_id){
    var tag=$('#'+tag_id)
    if(tag.attr('data-log')=='untagged')
    {
        $.ajax({
            url:tag.attr('data-tag-url'),
            type:'GET',
            dataType:'json',
            success:function(data){
                if(data.tag_successful)
                {
                    tag.html('tagged')
                    tag.attr('data-log','tagged')
                }
            }
        })

    }
    else if(tag.attr('data-log')=='tagged')
    {
        $.ajax({
            url:tag.attr('data-untag-url'),
            type:'GET',
            dataType:'json',
            success:function(data){
                if(data.untag_successful)
                {
                    tag.html('tag')
                    tag.attr('data-log','untagged')
                }
            }
        })

    }
}


var id=''

function more(id){
    description=$('#'+id)
    complete_description=$('#'+id+'-complete')
    description.css('display','none')
    complete_description.css('display','block')
}


// image preview

var preview_image=$('#id_image')
preview_image.onchange(function(event){
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('output');
        output.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
})



// video thumbnail




// status view countdown

var status_id=''
function countdown(status_id){
    status_id.toString()
    var status=$('#'+status_id)
    $.ajax({
        url:status.attr('data-end-url'),
        type:'GET',
        dataType:'json',
        success:function(data){
            
        }
    })
}

var status_id