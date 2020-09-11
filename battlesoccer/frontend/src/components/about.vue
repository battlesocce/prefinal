<template>
<div clas="ody">
  <div class="abt">

<center>
 <div class="card">
      <div class="card-image">
        <div class="background-image" :style="{'background-image': `url(${require('@/assets/img/card.jpg')})`}"></div>
        <div class="publication-details">
            Battle Begins
          <span class="date"><i class="fas fa-calendar-alt"></i> April 01, 2020</span>
        </div>
      </div>

      <div class="card-content">
        <h2 class="title">Battle of Takedown</h2>
        <h3 class="subtitle">Join the Real battle now</h3>
        <router-link 
        :to="{ name: 'contest'}" >
        <div class="cta1">
          <a href="">Read more &rarr;</a>
        </div></router-link>
      </div> 
 </div>

</center><br>
<div class="right2"><div data-aos="zoom-in">
      <h2>About</h2><br>

    <h3 >Create your team today</h3>
    <h4>Stop looking at the Highlights</h4>
    Come on let us battle on the real field and Create One!!<br>
    <h4 class="quotes">"Play to learn, learn to burn"</h4>
  </div></div>

   <div class="right2"><div data-aos="zoom-in">
    Battle soccer is a real time online game challenge!!<br>Now come let's<br>Play in the real world
        <br><br><h4>If you think LOVE is the best feeling ever!!<br><br><span class="quotes"> "Try playing FootBall"</span></h4><br><br>
      </div>  
  </div>
</div></div>
</template>
<script>
export default {
    name:"about"
}
</script>
<style scoped>
 @import '../assets/css/about.css';


.right2 {
  color:black;
  float:left;
  width:100%;
  padding:18px;
  margin-top:10px;
  text-align:center;
}

.background-image {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background-size: cover;
  z-index: 0;
  transition: transform 5s;
  overflow: hidden;

}
h1{
            font-size:55px;

        }

h2{
            font-size:45px;

        }
h3{
          font-size:35px;
}
h4{
            font-size:25px;
        }

h5{
            font-size:20px;
        }
@media only screen and (max-width:700px) {
h1{
            font-size:40px;

        }
h2{
            font-size:30px;

        }
h3{
            font-size:25px;
}
h4{
            font-size:25px;
        }
h5{
            font-size:20px;

        }
}
</style>