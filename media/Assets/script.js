const tl = gsap.timeline();

tl.from(".nav-bar" , {duration:2 , y :"-110%" , delay:1  , stagger:"0.5" ,ease:"slow" })
tl.from(".landingpage-collage" , { duration:1  , scale:0 ,  opacity:0  , x:"100%" , ease:"ease-in-out"} , 1)
tl.from(".student-text" , {duration:2 , opacity:0 , x:"-20%" , ease:"ease-in-out"} , 1)
tl.to('.student-round-text' , {duration:20 , rotation:360 ,repeat:Infinity , ease:'power'} , 0)
tl.to('.teacher-round-text' , {duration:20 , rotation:360 ,repeat:Infinity , ease:'power'} , 0)
tl.to(".community-hands" , {duration:20 , rotation:360 , repeat:Infinity ,ease:"ease-in-out"} , 0)
gsap.from(".teacher-img" , {
    scrollTrigger:{
        trigger:".teacher-img" ,
        scrub:true ,
        start : "top bottom"
    } ,
    duration:0.5 ,
    y:"30%" ,
    ease:"ease-in " ,
    opacity:0 ,
     
});

gsap.from(".about" , {
    scrollTrigger : {
    trigger : ".about-section" ,
    scrub : true ,
    start : "top 70%"
} ,
x:"30%" ,
opacity:0.4 ,
duration:1 ,
stagger : 0.25 ,
ease : "ease-in" ,

})