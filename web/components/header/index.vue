<script setup lang="ts">
import DesktopHeader from "./desktop-header.vue";
import MobileHeader from "./mobile-header.vue";
import { useDisplay } from "vuetify";

const { xs } = useDisplay();
</script>

<template>
  <ClientOnly>
    <DesktopHeader v-if="!xs" />
    <MobileHeader v-if="xs" />
  </ClientOnly>
</template>
