<script lang="ts" setup>
import clsx from "clsx";

const active = ref("profile");

const links = [
  {
    id: "shop",
    icon: "mdi-cart",
    text: "Shop",
  },
  {
    id: "list",
    icon: "mdi-format-list-bulleted",
    text: "Shopping List",
  },
  {
    id: "saved",
    icon: "mdi-heart",
    text: "Saved",
  },
  {
    id: "profile",
    icon: "mdi-account",
    text: "Profile",
  },
];

const onClick = (e) => {
  active.value = e.currentTarget.id;
};
</script>

<template>
  <footer class="mobile-nav d-grid" :elevation="10" grow>
    <VBtn
      v-for="link in links"
      :id="link.id"
      :class="clsx('text-capitalize', active === link.id && 'active')"
      :prepend-icon="link.icon"
      size="x-small"
      variant="text"
      stacked
      @click="onClick"
    >
      {{ link.text }}
    </VBtn>
  </footer>
</template>

<style lang="scss">
@import "../styles/variables.scss";

.mobile-nav {
  width: 100vw;
  position: fixed;
  bottom: 0;
  height: 75px;
  padding: 0 10px;
  display: grid;
  align-items: center;
  grid-template-columns: repeat(4, 1fr);

  font-size: 10px;
  background-color: $white;
  box-shadow: 0px -4px 30px 0px rgba(0, 0, 0, 0.15);
  border-radius: 25px 25px 0px 0px;

  button {
    font-family: Roboto;
    border-radius: 10px;
    color: $grey-dark;
    opacity: 0.5;

    i {
      transition: all 0.3s;
    }

    &.active {
      opacity: 1;

      i {
        transform: translateY(-25%) scale(1.5);
      }
    }

    .v-btn__content {
      white-space: nowrap;
    }
  }
}
</style>
