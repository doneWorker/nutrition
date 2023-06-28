<script setup lang="ts">
import clsx from "clsx";
import BasketIcon from "~/assets/icons/basket.svg";
import NutritionRequirements from "./nutriment-requirements.vue";

const shadowIsVisible = ref(false);

window.addEventListener("scroll", () => {
  if (window.pageYOffset > 10) shadowIsVisible.value = true;
  else shadowIsVisible.value = false;
});
</script>

<template>
  <header :class="clsx('header', shadowIsVisible && 'shadow')">
    <div class="main-header">
      <VContainer class="d-flex pa-0 gap">
        <VBtn icon="mdi-arrow-left" size="40" class="mr-4" variant="text" />
        <VTextField
          label=""
          variant="solo"
          density="compact"
          class="search-input mr-4"
          bg-color="grey-lighten-3"
          placeholder="Search for products"
          single-line
          hide-details
        />
        <VBtn class="text-none" size="40" stacked rounded variant="text">
          <VBadge content="2" class="basket-counter">
            <BasketIcon />
          </VBadge>
        </VBtn>
      </VContainer>
    </div>
    <NutritionRequirements />
  </header>
</template>

<style scoped lang="scss">
@import "styles/variables.scss";

.header {
  position: sticky;
  top: 0;
  z-index: 9;
  &.shadow {
    box-shadow: 0px 4px 30px 0px rgba(0, 0, 0, 0.15);
  }
}

.main-header {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 60px;
  padding: 10px;

  background-color: $white;
  transition: box-shadow 0.3s ease-in-out;
}

.basket-counter {
  &::v-deep .v-badge__badge {
    bottom: -30% !important;
    z-index: 2;

    font-size: 9px;
    background-color: $green-normal;
  }
}

.search-input {
  box-shadow: 0;

  &::v-deep .v-field {
    color: $grey-normal;
    border-radius: 10px;
    box-shadow: none !important;
  }
}
</style>
