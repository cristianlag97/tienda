<template>
  <div>
    <ProductList/>
  </div>
</template>
<script lang="ts">
import ProductList from '@/components/ProductList.vue'
import { Component, Vue } from 'vue-property-decorator';
@Component({
  components:{
    ProductList
  }
})
export default class HelloWorld extends Vue {
  
}
</script>


