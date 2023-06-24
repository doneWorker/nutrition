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
  <ProductsListHeader categoryTitle="Fruits and vegetables" />
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
.products-list {
  padding: 0 10px;
  width: 100%;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 25px 10px;
  padding-bottom: 100px;
}
</style>
