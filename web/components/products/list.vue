<script setup lang="ts"></script>

<template>
  <div class="products-list">
    <ProductsItem />
    <ProductsItem />
  </div>
</template>

<style lang="scss">
.products-list {
  padding: 10px;
  width: 100%;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 10px;
}
</style>
