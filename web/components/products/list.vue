<script setup lang="ts">
defineProps<{
  category?: {
    title: string;
    id: string;
  };
  list: {
    title: string;
    id: string;
    image: string;
    calories: number;
    protein: number;
    total_carbohydrates: number;
    total_fat: number;
  }[];
}>();
</script>

<template>
  <ProductsListHeader
    class="d-flex d-sm-none"
    categoryTitle="Fruits and vegetables"
  />
  <div class="products-list py-2 pb-10">
    <ProductsItem
      v-for="product in $props.list"
      :key="product.id"
      :id="product.id"
      :image="product.image"
      :title="product.title"
      :fats="product.total_fat"
      :energy="product.calories"
      :carbs="product.total_carbohydrates"
      :protein="product.protein"
    />
  </div>
</template>

<style lang="scss">
@import "../styles/mixins.scss";

.products-list {
  padding: 0 10px;
  width: 100%;
  display: grid;
  grid-gap: 25px 10px;
  padding-bottom: 100px;
  grid-template-columns: repeat(2, 1fr);

  @include from-breakpoint("sm") {
    grid-template-columns: repeat(3, 1fr);
  }

  @include from-breakpoint("md") {
    grid-template-columns: repeat(4, 1fr);
  }
}
</style>
