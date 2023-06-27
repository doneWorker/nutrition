<script setup lang="ts">
defineProps<{
  breadcrumbs: {
    title: string;
    url: string;
  }[];
}>();

const viewMode = reactive({ view: "grid" });
</script>

<template>
  <div class="filters">
    <div class="filters__inner d-flex justify-space-between align-center">
      <div class="breadcrumbs">
        <span class="breadcrumbs__item" v-for="item in $props.breadcrumbs">
          <a :href="item.url">{{ item.title }}</a>
        </span>
      </div>
      <div class="options">
        <VBtnToggle v-model="viewMode.view" class="view" density="compact">
          <VBtn
            icon="mdi-view-grid"
            value="grid"
            class="view__button"
            size="33"
          />
          <VBtn
            icon="mdi-format-list-bulleted"
            class="view__button"
            value="list"
            size="33"
          />
        </VBtnToggle>
        <VSelect
          class="sort"
          append-icon="mdi-chevron-down"
          density="compact"
          :items="[
            'California',
            'Colorado',
            'Florida',
            'Georgia',
            'Texas',
            'Wyoming',
          ]"
        />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "../styles/variables.scss";

.breadcrumbs {
  &__item {
    &:not(:last-child):after {
      content: " / ";
    }

    a {
      font-size: 14px;
      font-weight: 500;
      color: $green-dark-active;
    }
  }
}

.options {
  display: flex;

  .view {
    &__button {
      background-color: $green-normal-active;
      color: rgba($white, 0.5);
      font-size: 14px;

      &.v-btn--active {
        background-color: $green-dark-active;
        color: $white;
      }
    }
  }

  .sort {
    height: 33px;
    background-color: red;
  }
}
</style>
