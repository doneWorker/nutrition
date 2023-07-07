<template>
  <div class="footer">
    <VBtn
      variant="outlined"
      class="save-basket text-none"
      prepend-icon="mdi-content-save"
      height="38"
      >Save Basket</VBtn
    >
  </div>
</template>

<style lang="scss" scoped>
@import "styles/variables.scss";

.footer {
  display: flex;
  justify-content: flex-end;

  .save-basket {
    border-radius: 8px;
    font-size: 17px;
    color: $green-normal-active;
    border: 2px solid $green-normal-active;
  }
}
</style>
