<script lang="ts" setup>
let loading = ref(false);

const onSearch = () => {};
</script>

<template>
  <header class="header">
    <VRow no-gutters justify="center">
      <VCol class="d-flex align-center py-2">
        <VBtn
          class="mr-6"
          density="comfortable"
          variant="plain"
          icon="mdi-menu"
        />
        <VTextField
          class="search-input mr-10"
          density="compact"
          variant="solo"
          label="Search..."
          append-inner-icon="mdi-magnify"
          color="green"
          clearable
          single-line
          hide-details
          :loading="loading"
          :disabled="loading"
          @click:append-inner="onSearch"
        />
      </VCol>
      <VDivider
        class="border-opacity-75 mt-1"
        vertical
        thickness="2"
        length="45"
        color="white"
      />
      <VCol class="d-flex justify-end align-center">
        <VBtn
          class="text-capitalize"
          variant="outlined"
          prepend-icon="mdi-square-edit-outline"
          height="33"
          >Change requirements</VBtn
        >
        <VBtn icon class="ml-6" size="small">
          <VAvatar icon="mdi-account" color="teal-accent-4" />
        </VBtn>
      </VCol>
    </VRow>
  </header>
</template>

<style lang="scss" scoped>
@import "styles/variables.scss";

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 66px;
  padding: 10.5px 30px;

  background-color: $green-dark-hover;
  color: $white;

  .search-input {
    border-radius: 50px;
    overflow: hidden;
  }
}
</style>
