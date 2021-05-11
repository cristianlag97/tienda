<template>
  <div>
    <v-card
          max-width="300"
          class="my-5 mx-3"
    >
      <v-img
        height="250"
        :src="product.image"
      ></v-img>
      <v-card-title><router-link :to="{name: 'Product', params:{id:product.id}}">{{ product.title }}</router-link></v-card-title>
      <v-divider></v-divider>
      <v-card-text>
        <strong>$ {{ product.price }}</strong>
        <p>{{ product.description }}</p>  
      </v-card-text>
      <v-card-actions>
        <v-btn
          color="deep-purple lighten-2"
          text
        >
          Reserve
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script lang="ts">

import { Component, Prop, Vue } from 'vue-property-decorator';
@Component
export default class ProductList extends Vue {
  @Prop() private product!:Object
}
</script>