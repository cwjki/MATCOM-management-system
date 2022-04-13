<template>
    <q-table
        title="Departamentos"
        :loading="loading"
        :rows="rows"
        :columns="columns"
        table-header-class="bg-secondary text-white"
        row-key="name"
    />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { departmentTable } from './departmentTableHooks';
export default defineComponent({
    name: 'departmentHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const { columns, rows, loading } = departmentTable();
        return { columns, rows, loading };
    },
});
</script>
