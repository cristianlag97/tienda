<template>
  <div>
    <v-toolbar dense dark>
      <v-toolbar-items>
        <v-btn to="/">Inicio</v-btn>

        <v-btn>Product</v-btn>
      </v-toolbar-items>

      <v-spacer></v-spacer>

      <v-toolbar-items>
        <v-menu 
          offset-y
          :close-on-content-click="false"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-on="on" v-bind="attrs">0 Cart</v-btn>
          </template>
          <MiniCart @click="$event.stopPropagation()"/>
        </v-menu>
      </v-toolbar-items>
    </v-toolbar>
  </div>
</template>
<script lang="ts">
import MiniCart from './MniCart.vue'
import { Component, Vue } from 'vue-property-decorator';
@Component({
  components:{
    MiniCart
  }
})
export default class HelloWorld extends Vue {
  
}
</script>