<script setup>
import clsx from "clsx";

const nutriments = [
  {
    id: "energy",
    name: "Calories",
    value: 55,
  },
  {
    id: "protein",
    name: "Protein",
    value: 10,
  },
  {
    id: "fat",
    name: "Fat",
    value: 80,
  },
  {
    id: "carbs",
    name: "Carbs",
    value: 30,
  },
];
</script>

<template>
  <div class="nutriment-requirements">
    <div class="stats">
      <VProgressLinear
        :class="clsx('stats-item', stat.id)"
        v-for="stat in nutriments"
        :model-value="stat.value"
        height="8"
      />
    </div>
    <VBtn class="settings-button" variant="text" icon="mdi-cog-outline" />
  </div>
</template>

<style scoped lang="scss">
@import "styles/variables.scss";

.nutriment-requirements {
  display: flex;
  height: 40px;

  box-shadow: 0px 2px 5px 0px rgba(0, 0, 0, 0.25);
  background-color: $white;

  .stats {
    width: calc(100% - 40px);
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    align-items: center;
    gap: 2px;
    padding: 0 15px;

    &-item {
      &.energy {
        color: $red-normal;
      }
      &.protein {
        color: $green-normal;
      }
      &.fat {
        color: $yellow-normal;
      }
      &.carbs {
        color: $blue-normal;
      }
    }
  }

  .settings-button {
    width: 40px;
    height: 40px;

    border-left: 1px solid $grey-light;
    border-radius: 0;
    color: $grey-normal;
  }
}
</style>
