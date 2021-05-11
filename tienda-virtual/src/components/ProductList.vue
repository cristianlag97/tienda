<template>
  <div class="d-flex align-self-stretch flex-wrap">
    <product-card v-for="product in Products" :key="product.id" :product="product"/>
  </div>
</template>

<script lang="ts">

import ProductCard from '@/components/ProductCard.vue'
import { Component, Vue } from 'vue-property-decorator';
@Component({
  components:{
    ProductCard
  }
})
export default class ProductList extends Vue {

  get Products(){
    return this.$store.state.products
  }

  mounted() {
    this.$store.dispatch('getProducts')
  }
}
</script>