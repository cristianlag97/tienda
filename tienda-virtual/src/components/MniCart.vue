<template>
  <v-list class="container" style="min-width:320px">
    <v-list-item class="raya" v-for="item in cart" :key="item.product.id">
      <v-row>
        <v-col>
          <strong class="ml-auto">{{ item.product.title }}</strong>
        </v-col>
      </v-row>
      <br>
      <v-row>
        <v-col>
          <v-list-item-title> {{ item.quantity }} x ${{ item.product.price }} <v-btn text>Remove</v-btn></v-list-item-title>
        </v-col>
      </v-row>
    </v-list-item>
    <div class="container text-center">
      <span>Total: ${{cartTotalPrice}}</span>
      <v-btn text>Limpiar carrito</v-btn>
    </div>
  </v-list>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator';
@Component
export default class ProductList extends Vue {
  @Prop() private product!:Object

  get cart(){
    return this.$store.state.cart
  }

  get cartTotalPrice(){
    return this.$store.getters.cartTotalPrice
  }
}
</script>
<style>
.raya{
  border-bottom: 1px solid gray;
}
</style>