<script setup>
import BasketIcon from "~/assets/icons/basket.svg";
</script>

<template>
  <header className="header">
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
  </header>
</template>

<style scoped lang="scss">
@import "styles/variables.scss";

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 60px;
  padding: 10px;
}

.basket-counter {
  &::v-deep .v-badge__badge {
    bottom: -30% !important;

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
