<script setup lang="ts">
import {InscriptionArraySchema} from "~/schemas/inscription";
</script>

<template>
  <DataTable endpoint="/inscriptions" :schema="InscriptionArraySchema"/>
</template>