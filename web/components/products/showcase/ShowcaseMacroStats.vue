<script lang="ts" setup>
import { useBasket } from "~/composables/useBasket";

const { totalMacroNutrients } = useBasket();

// const macroNutriments = ref({
//   energy: 0,
//   protein: 0,
//   carbs: 0,
//   fats: 0,
// });

const plannedMacroNutriments = {
  energy: 3500,
  protein: 150,
  carbs: 300,
  fats: 200,
};
</script>

<template>
  <div class="stats">
    <div class="stats--inner">
      <div class="stats__item stats__item--energy">
        <div
          class="stats__item--fill"
          :style="{
            width: `${
              (totalMacroNutrients.energy * 100) / plannedMacroNutriments.energy
            }%`,
          }"
        ></div>
        <VIcon icon="mdi-lightning-bolt" size="sm" /><span>
          {{ totalMacroNutrients.energy }} kcal</span
        >
      </div>
      <div class="stats__item stats__item--protein">
        <div
          class="stats__item--fill"
          :style="{
            width: `${
              (totalMacroNutrients.protein * 100) /
              plannedMacroNutriments.protein
            }%`,
          }"
        ></div>
        <VIcon icon="mdi-dumbbell" size="sm" /><span>
          {{ totalMacroNutrients.protein }}g protein</span
        >
      </div>
      <div class="stats__item stats__item--fat">
        <div
          class="stats__item--fill"
          :style="{
            width: `${
              (totalMacroNutrients.fat * 100) / plannedMacroNutriments.fats
            }%`,
          }"
        ></div>
        <VIcon icon="mdi-cheese" size="sm" />
        <span>{{ totalMacroNutrients.fat }}g fat</span>
      </div>
      <div class="stats__item stats__item--carbs">
        <div
          class="stats__item--fill"
          :style="{
            width: `${
              (totalMacroNutrients.carbs * 100) / plannedMacroNutriments.carbs
            }%`,
          }"
        ></div>
        <VIcon icon="mdi-spoon-sugar" size="sm" />
        <span>{{ totalMacroNutrients.carbs }}g carbs</span>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "styles/variables.scss";

.stats {
  position: absolute;
  top: 16px;
  right: 10px;
  height: 20px;

  &--inner {
    display: flex;
  }

  &__item {
    position: relative;
    line-height: 25px;
    padding: 0 40px 0 15px;
    overflow: hidden;

    font-size: 16px;
    border: 1.5px solid $white;
    border-radius: 25px;
    color: $white;

    span {
      margin-left: 3px;
    }

    &--fill {
      position: absolute;
      left: 0;
      height: 100%;
      z-index: -1;

      background-color: rgba(0, 0, 0, 0.2);
    }

    &--energy {
      background-color: $red-normal-hover;
      transform: translateX(90px);
    }
    &--protein {
      background-color: $green-normal-hover;
      transform: translateX(60px);
    }
    &--fat {
      background-color: $yellow-normal-hover;
      transform: translateX(30px);
    }
    &--carbs {
      background-color: $blue-normal-hover;
      padding-right: 25px;
      z-index: 2;
    }
  }
}
</style>
