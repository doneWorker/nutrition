<script lang="ts" setup>
import clsx from "clsx";

defineProps<{
  categoryTitle: string;
}>();
</script>

<template>
  <div class="justify-space-between align-center products-header">
    <h2 class="category">{{ categoryTitle }}</h2>
    <VBtn class="filter-btn" icon="mdi-filter" elevation="0" size="30" />
  </div>
</template>

<style lang="scss" scoped>
@import "styles/variables.scss";

.products-header {
  .category {
    font-size: 18px;
  }

  .filter-btn {
    font-size: 10px;
    border-radius: 8px;
    background-color: $grey-light;
    color: $grey-dark-hover;
  }
}
</style>
