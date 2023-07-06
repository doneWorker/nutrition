<script lang="ts" setup>
import { ProductItemModel } from "~/types/products";

defineProps<{
  category?: {
    title: string;
    id: string;
  };
  variant: "grid" | "list";
  list: ProductItemModel[];
}>();
</script>

<template>
  <ProductsListHeader
    class="d-flex d-sm-none"
    categoryTitle="Fruits and vegetables"
  />
  <div :class="`products-list products-list--${variant} py-2 pb-10`">
    <ProductsItem
      v-for="product in list"
      :key="product.id"
      :variant="variant"
      v-bind="product"
    />
  </div>
</template>

<style lang="scss" scoped>
@import "styles/mixins.scss";

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
