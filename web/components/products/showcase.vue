<script setup lang="ts">
import BasketIcon from "~/assets/icons/basket.svg";

defineProps<{
  totalItems: number;
  totalBudget: number;
  totalSpent: number;
}>();
</script>

<template>
  <div class="showcase">
    <div class="total">
      <div class="total__money">
        <div class="total__money--inner">
          <span class="total__money--spent">Current: ${{ totalSpent }}</span>
          <span class="total__money-sep" />
          <span class="total__money--budget">Budget: ${{ totalBudget }}</span>
        </div>
      </div>
      <div class="total__items">
        <span>Total items: {{ totalItems }}</span>
      </div>
    </div>
    <div class="basket">
      <div class="basket--inner">
        <div class="basket__stats"></div>
        <div class="basket__empty">
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

    &--inner {
      height: 100%;
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
