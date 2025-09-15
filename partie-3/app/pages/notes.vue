<script setup lang="ts">
import {NoteArraySchema} from "~/schemas/note";
</script>

<template>
  <DataTable endpoint="/notes" :schema="NoteArraySchema"/>
</template>