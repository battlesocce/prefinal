<template>
<div class="ody">
<div v-if="rank3.own">
    <br><br><br>
          <div class="container"><br>
<h1 class="display-4">Rankpage</h1></div><br>
<div class="container-sm">
<div class="row text-center">

<b-col cols="4">
<br><br><br><br><br><br>
<h3>2</h3>
<router-link
        :to="{ name: 'Teamveiw', params: { id: rank2.own.id } }"
        >
 <div data-aos="fade-down-right">
   <img :src="rank2.own.logo" class="respo"/>
 </div>
   <br><br>
<h4>{{rank2.own.teamname|capitalize}}</h4></router-link>
</b-col>

<b-col cols="4">
<h3>1</h3><br>
<router-link
        :to="{ name: 'Teamveiw', params: { id: rank1.own.id } }"
        >
 <div data-aos="flip-left">       
<img :src="rank1.own.logo" class="resp"/></div><br><br>
<h4>{{rank1.own.teamname|capitalize}}</h4></router-link>
</b-col>

<b-col cols="4">
<br><br><br><br><br><br>
<h3>3</h3>
<router-link
        :to="{ name: 'Teamveiw', params: { id: rank3.own.id } }"
        >
<div data-aos="fade-down-left">
  <img :src="rank3.own.logo" class="respo"/></div><br><br>
<h4>{{rank3.own.teamname|capitalize}}</h4></router-link>
</b-col>

<hr>
<br><br>
</div>
</div>
          <div class="container-sm"><br><br>
              <b-row align-v="center">
                  <b-col cols="4" ><h2>Team</h2></b-col>
              <b-col cols="8"> 
      <b-row align-v="center">
        <b-col cols="4" ><b><h4><center>Goals</center></h4></b></b-col>
          <b-col cols="4" ><b><h4><center>Play</center></h4></b></b-col>
          <b-col cols="4" ><b><h4><center>Won</center></h4></b></b-col>
     </b-row>
</b-col>
              </b-row>
<hr>
<div v-for="ranks in teamdata" :key="ranks.id">
                <b-row align-v="center">
                  <b-col cols="4">
                <router-link
        :to="{ name: 'Teamveiw', params: { id: ranks.own.id } }"
        >    
                 <h3>{{ranks.own.teamname|capitalize}}</h3><br>
                <div data-aos="zoom-in-up">
                  <img :src="ranks.own.logo" class="respo"/></div>
                </router-link>
                </b-col>
              <b-col cols="8">
      <b-row align-v="center" >
         <b-col cols="4"><h4 data-aos="flip-left"><center>{{ranks.teamgoals}}</center></h4></b-col>
         <b-col cols="4" ><h4 data-aos="flip-left"><center>{{ranks.matchs_played}}</center></h4></b-col>
         <b-col cols="4" ><h4 data-aos="flip-left"><center>{{ranks.match_won}}</center></h4></b-col>
</b-row>
              </b-col>
              </b-row>
              <hr>
              </div>
</div>
</div>
<br>
<div class="container text-center">
      <h2 v-show="loadingrank"><div class="lds-ripple"><div></div><div></div></div></h2>
      </div>
</div>

</template>

<script>

import { apiService } from "@/common/api.service.js";

export default{
    name: "rankpage",

    data() {
    return {
    teamdata:[],
      teamrank:[],
      rank1:{},
      rank2:{},
      rank3:{},
      next: null,
      loadingrank: false,
    }
    },
       mounted () {
this.scroll()
  },
methods: {
   scroll () {
      window.onscroll = () => {
        let bottomOfWindow = Math.max(window.pageYOffset, document.documentElement.scrollTop, document.body.scrollTop) + window.innerHeight === document.documentElement.offsetHeight

        if (bottomOfWindow) {
          if (this.next) { 
         this.getTeamRank();// replace it with your code
        }
        }
      }
    },

    getTeamRank() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/teamrank/`;
      apiService(endpoint)
      setTimeout(() => {
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingrank = true;
      apiService(endpoint)
 .then(data => {
          this.teamrank.push(...data.results);
          this.teamdata=this.teamrank
            this.teamrank=this.teamrank.slice(0,4)
            this.rank1=this.teamrank[0];
            this.rank2=this.teamrank[1];
            this.rank3=this.teamrank[2];
          this.loadingrank = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          } }, 2000)
        })   
    },
},
created()
{
  this.getTeamRank()
},

}


</script>

<style scoped>
@import '../assets/css/teamrank.css';
.ody a{

    font-family: "Quicksand", sans-serif;
    text-decoration: none;

    

}
.ody{
  overflow:hidden;

}
.lds-ripple {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-ripple div {
  position: absolute;
  border: 4px solid #fff;
  opacity: 1;
  border-radius: 50%;
  animation: lds-ripple 1s cubic-bezier(0, 0.2, 0.8, 1) infinite;
}
.lds-ripple div:nth-child(2) {
  animation-delay: -0.5s;
}
@keyframes lds-ripple {
  0% {
    top: 36px;
    left: 36px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0px;
    left: 0px;
    width: 72px;
    height: 72px;
    opacity: 0;
  }
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
            font-size:20px;
}
h4{
            font-size:25px;
        }
h5{
            font-size:20px;

        }
}


  </style>
