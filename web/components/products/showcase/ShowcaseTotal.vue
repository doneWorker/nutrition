<script lang="ts" setup>
const { totalSpent, products } = useBasket();
const totalBudget = 1000;
</script>

<template>
  <div class="total">
    <div class="total__money">
      <div class="total__money--inner">
        <span class="total__money--spent">Current: ${{ totalSpent }}</span>
        <span class="total__money-sep"></span>
        <span class="total__money--budget">Budget: ${{ totalBudget }}</span>
      </div>
    </div>
    <div class="total__items">
      <span>Total items: {{ products.length }}</span>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "styles/variables.scss";

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
</style>
