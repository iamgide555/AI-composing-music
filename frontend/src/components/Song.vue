<template>
  <div>
    Song Page
    <br><br>
    <router-link to="/generate">
      <a>Generate</a>
    </router-link>
    <br>
    <div class="player-wrapper">
    	<audio-player file="/static/notes/a49.mp3"></audio-player>
    </div>
  </div>
  
</template>

<script>
//ref: https://codepen.io/numerical/pen/yKMaaP
import audioPlayer from './AudioPlayer.vue';

export default {
  components: {
    audioPlayer
  }
}



</script>
