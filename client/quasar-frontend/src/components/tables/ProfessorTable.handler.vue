<template>
    <q-table
        title="Profesores"
        :loading="loading"
        :rows="rows"
        :columns="columns"
        table-header-class="bg-secondary text-white"
        row-key="name"
    />
</template>

<script lang="ts">
import { defineComponent, PropType, computed, ref, toRef, Ref } from 'vue';
import { professorTable } from './professorTable.hooks';
export default defineComponent({
    name: 'professorHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const { columns, rows, loading } = professorTable();
        return { columns, rows, loading };
    },
});
</script>
