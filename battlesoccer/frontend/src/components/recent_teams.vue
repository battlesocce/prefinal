<template>
  <div class="container-sm"><hr>
    <div class="container" style="margin-bottom:40px;" >
<h1><br>Recently added Teams</h1></div>
<div class="row">
<div class="col-6 col-lg-3"  v-for="teamd in teamdata" :key="teamd.id"><div data-aos="zoom-in-down">
        <router-link
        :to="{ name: 'Teamveiw', params: { id: teamd.id } }"
        >
  <div class="our-team">
    <div class="picture">
      <img :src="teamd.logo + '?'+ new Date().getTime()">
         </div>

    <div class="team-content">
      <h4 class="name">{{teamd.teamname| capitalize}}</h4>
    </div>

  </div>
        </router-link></div>
</div>
</div>
  </div>

</template>

<script>


export default{
name: "recentteam",
props: {
    teamdata: {
      type: Array,
      required: true
    },
    }
}

</script>

<style scoped>
@import '../assets/css/userprofile.css';
hr {
  border: 0;
  clear:both;
  display:block;
  width: 96%;               
  background-color:white;
  height: 1px;
}
.ody a{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


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
