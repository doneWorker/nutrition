<script setup lang="ts">
defineProps<{
  category?: {
    title: string;
    id: string;
  };
  variant?: "grid" | "list";
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
  <div :class="`products-list products-list--${$props.variant} py-2 pb-10`">
    <ProductsItem
      v-for="product in $props.list"
      :variant="$props.variant"
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

<style scoped lang="scss">
@import "../styles/mixins.scss";

.products-list {
  width: 100%;
  display: grid;
  grid-gap: 25px 10px;
  padding-bottom: 100px;
  grid-template-columns: repeat(2, 1fr);

  @include from-breakpoint("sm") {
    margin-top: 20px;
    grid-template-columns: repeat(3, 1fr);

    &--list {
      grid-template-columns: 1fr !important;
      grid-gap: 5px 0;
    }
  }

  @include from-breakpoint("md") {
    grid-template-columns: repeat(4, 1fr);
  }
}
</style>
