<template>
  <q-table
    title="Treats"
    :loading="loading"
    :rows="rows"
    :columns="columns"
    table-header-class="bg-secondary text-white"
    row-key="name"
  />
</template>

<script lang="ts">
import { defineComponent, PropType, computed, ref, toRef, Ref } from 'vue';
import { studentTable } from './studentTable.hooks';
export default defineComponent({
  name: 'studentHandler',
  props: {},
  emits: [],
  setup(props, { emit }) {
    const { options, rows, loading } = studentTable();
    return { options, rows, loading };
  },
});
</script>
