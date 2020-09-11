<template>
<div class="ody">
  <div class=home>
  </div>
    logged user:{{requestUser}}
   <br><br>
  <rankboard></rankboard>
    <div data-aos="zoom-in-right" data-aos-duration="500">
   <card></card></div><br> 
  <videos></videos><br> 
<div class="container-sm">
  <recentteam :teamdata="team"/>
</div>
<about></about>
  <footeruse></footeruse>
</div>
</template>

<script>

import { apiService } from "@/common/api.service.js";
import card from "@/components/card.vue";
import rankboard from "@/components/rankboard.vue";
import videos from "@/components/videos.vue";
import about from "@/components/about.vue";
import footeruse from "@/components/footer.vue";
import recentteam from "@/components/recent_teams.vue";

export default{
  name: "Home",
  data() {
    return {
      team: [],
      player:[],
      error: null,
      requestUser:null,
      loading: false,
      
    }
  },
       components: {
    card,
    rankboard,
    videos,
    about,
    footeruse,
    recentteam,
  },
  
   methods: {
      getTeamData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/team/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.team = data.results;
            this.team = this.team.slice(-4);

          } else {
            this.team = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
    getplayerData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/player/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.player = data.results;
          } else {
            this.player = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
    async setUserInfo() {
      // add the username of the logged in user to localStorage
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      this.requestUser = data["username"];
      const id = data["id"];
      window.localStorage.setItem("username", requestUser);
      window.localStorage.setItem("id", id);
    }
    },
  created() {
    this.getTeamData()
    this.getplayerData()
    this.setUserInfo()

    }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Quicksand:400,500,700');

.home {
    width: 100%;
    height: 100vh;
    background-image:url('~@/assets/img/homec4.jpg') ;
    background-position: center top;
	  background-size:cover;
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
  .home {
    width: 100%;
    height: 100vh;
    background-image:url('https://i.pinimg.com/originals/11/ba/e8/11bae8258ab02c454ddf553fe2133a10.png') ;
    background-position: center top;
	  background-size:cover;
}
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
