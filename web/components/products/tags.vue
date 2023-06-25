<script setup lang="ts">
defineProps<{
  category?: {
    title: string;
    id: string;
  };
  list: {
    title: string;
    id: string;
    image: string;
    calories: number;
    protein: number;
    total_carbohydrates: number;
    total_fat: number;
  }[];
}>();
</script>

<template></template>
