<script setup lang="ts">
import BasketIcon from "~/assets/icons/basket.svg";
import { useBasket } from "~/composables/use-basket";
import BasketItem from "./basket-item.vue";
import clsx from "clsx";

const { products } = useBasket();

defineProps<{
  total: { totalItems: number; totalBudget: number; totalSpent: number };
}>();
</script>

<template>
  <div class="showcase">
    <div class="total">
      <div class="total__money">
        <div class="total__money--inner">
          <span class="total__money--spent"
            >Current: ${{ total.totalSpent }}</span
          >
          <span class="total__money-sep" />
          <span class="total__money--budget"
            >Budget: ${{ total.totalBudget }}</span
          >
        </div>
      </div>
      <div class="total__items">
        <span>Total items: {{ total.totalItems }}</span>
      </div>
    </div>
    <div class="basket">
      <div class="'basket--inner'">
        <div class="basket__stats">energy</div>
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
          <BasketItem
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
    <div class="showcase-footer">
      <VBtn
        variant="outlined"
        class="save-basket text-none"
        prepend-icon="mdi-content-save"
        height="38"
        >Save Basket</VBtn
      >
    </div>
  </div>
</template>

<style scoped lang="scss">
@import "../styles/variables.scss";

.showcase {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 15px;

  .total {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 54px;

    &__money {
      width: 300px;
      height: 30px;
      overflow: hidden;

      border-radius: 8px;
      border: 1px solid $white;
      box-shadow: 0px 0px 15px 0px rgba(245, 161, 34, 0.35);
      color: $white;

      &--inner {
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 100%;

        font-weight: 500;
      }

      &-sep {
        width: 1px;
        height: 100%;
        background-color: $white;
      }

      &--spent,
      &--budget {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        text-shadow: 0 0 1px $green-dark;
      }

      &--spent {
        background: linear-gradient(
          224deg,
          #f2ed67 0%,
          #f0ab25 50%,
          #df643d 100%
        );
      }

      &--budget {
        background: linear-gradient(
          -224deg,
          #f2ed67 0%,
          #f0ab25 50%,
          #df643d 100%
        );
      }
    }

    &__items {
      color: $green-dark-active;
      font-weight: bold;
    }
  }

  .basket {
    width: 100%;
    height: 100%;

    border-radius: 8px;
    box-shadow: 0px 3px 7px rgba(0, 0, 0, 0.25);
    background-color: $green-light-active;
    border: 4px dashed $green-normal-active;

    &__stats {
      position: absolute;
    }

    &--inner {
      height: 100%;
    }

    &__products {
      display: grid;
      padding: 25px;
      /* grid-template-columns: repeat(3, 1fr); */
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

  .showcase-footer {
    display: flex;
    justify-content: flex-end;

    .save-basket {
      border-radius: 8px;
      font-size: 17px;
      color: $green-normal-active;
      border: 2px solid $green-normal-active;
    }
  }
}
</style>
