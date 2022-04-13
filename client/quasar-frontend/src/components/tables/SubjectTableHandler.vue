<template>
    <q-table
        title="Asignaturas"
        :loading="loading"
        :rows="rows"
        :columns="columns"
        table-header-class="bg-secondary text-white"
        row-key="name"
    />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { subjectTable } from './subjectTableHooks';
export default defineComponent({
    name: 'subjectHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const { columns, rows, loading } = subjectTable();
        return { columns, rows, loading };
    },
});
</script>
