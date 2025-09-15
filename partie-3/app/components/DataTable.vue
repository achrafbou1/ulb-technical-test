<script setup lang="ts">
import {useEntity} from "~/composables/useEntity";
import {getPaginationRowModel} from '@tanstack/vue-table'
import type {ZodSchema} from "zod";

interface Props<T> {
  endpoint: string
  schema: ZodSchema<T[]>
}

const props = defineProps<Props<unknown>>()

const {data, pending, error} = useEntity(props.endpoint, props.schema)

const pagination = ref({
  pageIndex: 0,
  pageSize: 5
})

const table = useTemplateRef('table')
</script>

<template>
  <div v-if="error">{{ error.message }}</div>
  <UTable
      ref="table"
      v-model:pagination="pagination"
      :data="data"
      :loading="pending"
      loading-color="primary"
      loading-animation="carousel"
      :pagination-options="{
        getPaginationRowModel: getPaginationRowModel()
      }"
      class="w-full"
  />

  <div class="flex justify-center border-t border-default pt-4">
    <UPagination
        :default-page="(table?.tableApi?.getState().pagination.pageIndex || 0) + 1"
        :items-per-page="table?.tableApi?.getState().pagination.pageSize"
        :total="table?.tableApi?.getFilteredRowModel().rows.length"
        @update:page="(p) => table?.tableApi?.setPageIndex(p - 1)"
    />
  </div>
</template>