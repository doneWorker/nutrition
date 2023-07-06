<script lang="ts" setup>
import { signOut } from "~/api/auth";

definePageMeta({
  middleware: ["only-users"],
});

const onSignOut = async () => {
  await signOut();
};
</script>
<template>
  <VBtn :onclick="onSignOut">Sign Out</VBtn>
</template>
