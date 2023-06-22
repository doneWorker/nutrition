<template>
  <div class="products-list">
    <ProductsItem v-for="n in 10" />
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
