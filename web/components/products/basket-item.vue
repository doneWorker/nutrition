<script lang="ts" setup>
import { ProductInBasket } from "~/types/products";

defineProps<ProductInBasket>();
</script>

<template>
  <div class="basket-item">
    <div><img :src="image_url" :alt="name" /></div>
    <div>{{ name }}</div>
    <div>{{ price }}</div>
  </div>
</template>

<style scoped lang="scss">
@import "../styles/variables.scss";

.basket-item {
  background-color: $white;

  img {
    max-width: 100%;
  }
}
</style>
