<template>
  <v-app>
    <Navbar/>
    <v-main>
      <v-container>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Navbar from './components/Navbar.vue';
import { Component, Vue } from 'vue-property-decorator';

@Component({
  components:{
    Navbar
  }
})
export default class App extends Vue {
  
}
</script>