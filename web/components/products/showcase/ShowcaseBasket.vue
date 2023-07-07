<script lang="ts" setup>
import { useBasket } from "~/composables/useBasket";

import BasketIcon from "~/assets/icons/basket.svg";
import ShowcaseMacroStats from "./ShowcaseMacroStats.vue";
import ShowcaseProduct from "./ShowcaseProduct.vue";

const { products } = useBasket();
</script>

<template>
  <div class="basket">
    <div class="basket--inner">
      <ShowcaseMacroStats />
      <div
        class="basket__products"
        :style="{
          gridTemplateColumns: `repeat(${Math.sqrt(
            products.length
          ).toFixed()}, 1fr)`,
          gridTemplateRows: `repeat(${Math.sqrt(
            products.length
          ).toFixed()}, 1fr)`,
        }"
      >
        <ShowcaseProduct
          v-for="product in products"
          :key="product.id"
          v-bind="product"
        />
      </div>

      <div class="basket__empty" v-if="products.length === 0">
        <BasketIcon width="212.5" />
        <span class="basket__empty--text"
          >Currently your basket is empty,<br />please drop items here</span
        >
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "styles/variables.scss";

.basket {
  width: 100%;
  height: 100%;

  border-radius: 8px;
  box-shadow: 0px 3px 7px rgba(0, 0, 0, 0.25);
  background-color: $green-light-active;
  border: 4px dashed $green-normal-active;

  &--inner {
    position: relative;
    height: 100%;
    padding-top: 70px;
  }

  &__products {
    display: grid;
    padding: 0 25px;
    grid-gap: 10px;

    &.grid-1 {
      grid-template-columns: repeat(1, 1fr);
    }

    &.grid-2 {
      grid-template-columns: repeat(2, 1fr);
    }

    &.grid-3 {
      grid-template-columns: repeat(3, 1fr);
    }

    &.grid-3-plus {
      grid-template-columns: repeat(4, 1fr);
    }
  }

  &__empty {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    svg {
      color: $green-dark;
    }

    &--text {
      text-align: center;
      text-shadow: 0px 0px 100px 0px #fff;
      font-size: 18px;
      font-weight: 700;
      color: $green-dark;
    }
  }
}
</style>
