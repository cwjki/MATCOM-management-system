<template>
    <q-table
        title="Planificación de las Asignaturas"
        :loading="loading"
        :rows="rows"
        :columns="columns"
        table-header-class="bg-secondary text-white"
        row-key="name"
    />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { subjectPlanningTable } from './subjectPlanningTableHooks';
export default defineComponent({
    name: 'subjectPlanningHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const { columns, rows, loading } = subjectPlanningTable();
        return { columns, rows, loading };
    },
});
</script>
