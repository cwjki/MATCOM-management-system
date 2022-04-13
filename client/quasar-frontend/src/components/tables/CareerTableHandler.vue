<template>
    <q-table
        title="Carreras"
        :loading="loading"
        :rows="rows"
        :columns="columns"
        table-header-class="bg-secondary text-white"
        row-key="name"
    />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { careerTable } from './CareerTableHooks';
export default defineComponent({
    name: 'careerHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const { columns, rows, loading } = careerTable();
        return { columns, rows, loading };
    },
});
</script>
