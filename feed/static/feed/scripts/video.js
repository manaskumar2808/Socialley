var video=document.getElementById('video');
var videoContainer=document.querySelector('.video-container');
var videoElements=document.querySelectorAll('.video-element');
var pp=document.querySelector('.play-pause');

var mainControls=document.querySelector('.main-controls');
var controls=document.querySelector('.controls');



const forward=document.querySelector('.forward');
const backward=document.querySelector('.backward');

pp.onclick=function(){
    if(video.paused){
        console.log('video is playing');
        video.play();
        pp.innerHTML='<i class="fas fa-pause fa-2x pause float-right"></i>';
    }
    else{
        console.log('video is paused');
        video.pause();
        pp.innerHTML='<i class="fas fa-play fa-2x play float-right"></i>';
    }
};

const bar=document.querySelector('.bar');
const juice=document.querySelector('.bar-juice');
var playedTime=document.querySelector('.played-time');
var leftTime=document.querySelector('.left-time');

video.addEventListener('timeupdate',()=>{
    juice.style.width=(video.currentTime/video.duration)*100+"%";

    var p_s=parseInt(video.currentTime%60);
    var p_m=parseInt((video.currentTime/60)%60);
    var p_h=parseInt((video.currentTime/(60*60))%60);
    
    if(p_h==0){
        if(p_m<10)
        {
            if(p_s<10)
                playedTime.innerHTML="0"+p_m+":0"+p_s;
            else
                playedTime.innerHTML="0"+p_m+":"+p_s;
        }
        else
        {
            if(p_s<10)
                playedTime.innerHTML=p_m+":0"+p_s;
            else
                playedTime.innerHTML=p_m+":"+p_s;
        }

    }

    else
        playedTime.innerHTML=p_h+":"+p_m+":"+p_s;
    
    var l_s=parseInt((video.duration-video.currentTime)%60);
    var l_m=parseInt(((video.duration-video.currentTime)/60)%60);
    var l_h=parseInt(((video.duration-video.currentTime)/(60*60))%60);

    if(l_h==0){
        if(l_m<10)
        {
            if(l_s<10)
                leftTime.innerHTML="0"+l_m+":0"+l_s;
            else
                leftTime.innerHTML="0"+l_m+":"+l_s;
        }
        else
        {
            if(l_s<10)
                leftTime.innerHTML=l_m+":0"+l_s;
            else
                leftTime.innerHTML=l_m+":"+l_s;
        }

    }

    if(video.ended){
        pp.innerHTML='<i class="fas fa-play play"></i>';
    }
});


forward.onclick=function(){
    video.currentTime+=10;
    forward.style.transform='rotate(360deg)';
}

backward.onclick=function(){
    video.currentTime-=10;
    backward.style.transform='rotate(-360deg)';
}



var volume=document.querySelector('.volume');
var caption=document.querySelector('.caption');
var size=document.querySelector('.size');

var captionContainer=document.querySelector('.caption-container');
var sizeContainer=document.querySelector('.size-container');


caption.onclick=function(){
    if(!caption.classList.toggle("fas"))
        caption.classList.add("far");
    else
        caption.classList.remove("far");
}

size.onclick=function(){
    if(!size.classList.toggle("fa-compress"))
        size.classList.add('fa-expand');
    else
        size.classList.remove('fa-expand');
}

volume.onclick=function(){
    if(video.volume==1)
    {
        console.log('volume decreasing');
        video.volume-=0.1;
    }


    else 
    {
        console.log('volume increasing');
        video.volume+=0.1;
    }
}


videoContainer.onmouseenter=function(){
    controls.style.visibility="visible";
    mainControls.style.visibility="visible";
}

videoContainer.onmouseleave=function(){
    controls.style.visibility="hidden";
    mainControls.style.visibility="hidden";
}

