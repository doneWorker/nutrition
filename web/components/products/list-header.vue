<script lang="ts" setup>
defineProps<{
  categoryTitle: string;
}>();
</script>

<template>
  <div class="d-flex justify-space-between align-center products-header">
    <h2 class="category">{{ $props.categoryTitle }}</h2>
    <VBtn class="filter-btn" icon="mdi-filter" elevation="0" size="30" />
  </div>
</template>

<style scoped lang="scss">
@import "../styles/variables.scss";

.products-header {
  margin: 10px;

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
