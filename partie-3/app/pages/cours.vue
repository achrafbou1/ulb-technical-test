<script setup lang="ts">
import {CoursArraySchema} from "~/schemas/cours";
</script>

<template>
  <DataTable endpoint="/cours" :schema="CoursArraySchema"/>
</template>