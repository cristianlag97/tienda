<template>
  <v-row class="mt-5" v-if="product">
    <v-col cols="4">
      <v-img 
        :src="product.image"
        height="250"
        width="300"
        ></v-img>
    </v-col>
    <v-col cols="8">
      <h1>{{ product.title }}</h1>
      <h3>$ {{ product.price }}</h3>

      <v-text-field
        label="Outlined"
        outlined
        class="p-1"
      ></v-text-field>
      <v-btn color="blue" dark @click="addToCart()">Añadir al carrito</v-btn>

      <p class="mt-4">{{ product.description }}</p>
    </v-col>
  </v-row>
</template>
<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
@Component
export default class Product extends Vue {
  @Prop() private id!:number

  get product(){
    return this.$store.state.product
  }
  
  mounted() {
    this.$store.dispatch('getProduct', this.id)
  }

  addToCart(){
    this.$store.dispatch('addProductToCart', {
      product: this.product,
      quantity: 1
    })
  }
}
</script>
