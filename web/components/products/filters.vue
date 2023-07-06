<script lang="ts" setup>
type Breadcrumbs = {
  title: string;
  url: string;
}[];

defineProps<{
  breadcrumbs: Breadcrumbs;
  viewMode: { view: "grid" | "list" };
  sortOptions: {
    sortBy: "relevance" | "protein" | "carbs" | "fats";
    sortOrder: "none" | "asc" | "desc";
  };
  onSortOrder: () => void;
}>();
</script>

<template>
  <div class="filters">
    <div class="filters__inner d-flex justify-space-between align-center">
      <VBreadcrumbs :items="breadcrumbs" class="breadcrumbs" />
      <div class="options">
        <VBtnToggle
          v-model="viewMode.view"
          class="view"
          density="compact"
          mandatory
        >
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
        <VBtnToggle class="sort">
          <VSelect
            class="sort__by"
            density="compact"
            menu-icon="none"
            variant="solo"
            hide-details
            :items="['Relevance', 'Protein', 'Fat', 'Carbs', 'Energy']"
            v-model="sortOptions.sortBy"
          />
          <VBtn
            :icon="
              sortOptions.sortOrder === 'asc'
                ? 'mdi-sort-ascending'
                : sortOptions.sortOrder === 'desc'
                ? 'mdi-sort-descending'
                : 'mdi-sort-variant-off'
            "
            @click="onSortOrder"
            class="sort__order"
            width="37"
            height="33"
            value="asc"
          />
        </VBtnToggle>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@import "styles/variables.scss";

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
  gap: 10px;
  height: 33px;

  .view {
    &__button {
      background-color: $green-normal-active;
      color: rgba($white, 0.5);
      font-size: 14px;

      &:nth-child(1) {
        border-radius: 8px 0 0 8px;
      }

      &:nth-child(2) {
        border-radius: 0 8px 8px 0;
      }

      &.v-btn--active {
        background-color: $green-dark-active;
        color: $white;
      }
    }
  }

  .sort {
    &__by {
      height: 33px;

      &::v-deep .v-field {
        height: 33px;

        border-radius: 8px 0 0 8px;
        line-height: 33px;
        font-size: 14px;
        font-weight: 500;
        box-shadow: none;
        background-color: $green-dark;
        color: $white;

        .v-field__append-inner {
          display: none;
        }

        .v-field__input {
          padding-top: 0;
          padding-bottom: 0;
          padding-right: 0;
        }
      }
    }

    &__order {
      width: 37px;
      height: 33px;

      border-radius: 0 8px 8px 0;
      background-color: $green-dark-active;
      color: $white;
    }
  }
}
</style>
