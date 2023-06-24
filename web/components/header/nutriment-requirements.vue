<script lang="ts" setup>
import clsx from "clsx";
import { onMounted } from "vue";

type NutrimentItem = { id: string; name: string; value?: number };
let nutriments = ref<NutrimentItem[]>([
  {
    id: "energy",
    name: "Energy",
  },
  {
    id: "protein",
    name: "Protein",
  },
  {
    id: "fat",
    name: "Fat",
  },
  {
    id: "carbs",
    name: "Carbs",
  },
]);

const rand = (from: number, to: number): number => {
  const range = to - from + 1;
  return Math.floor(Math.random() * range) + from;
};

onMounted(() => {
  const setValues = () => {
    nutriments.value = nutriments.value.map((nutriment) => {
      return { ...nutriment, value: rand(30, 100) };
    });
  };

  setTimeout(setValues, 2_000);
});
</script>

<template>
  <div class="nutriment-requirements">
    <div class="stats">
      <div :class="clsx('stats-item', stat.id)" v-for="stat in nutriments">
        <VProgressLinear :model-value="stat?.value || 0" height="8" />
        {{ stat.name }}
      </div>
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
    margin-top: 11px;

    &-item {
      font-size: 10px;
      font-family: Inter;
      font-weight: 500;
      --v-border-opacity: 1;

      .v-progress-linear {
        transition-duration: 0.75s;
      }

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

    font-size: 12px;
    border-left: 1px solid $grey-light;
    border-radius: 0;
    color: $grey-normal;
  }
}
</style>
