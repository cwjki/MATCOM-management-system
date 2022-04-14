<template>
    <!-- <q-table
        title="Profesores"
        :loading="loading"
        :rows="rows"
        :columns="columns"
        table-header-class="bg-secondary text-white"
        row-key="name"
    /> -->
    <g-crud-data-table :config="config" />
</template>

<script lang="ts">
import { professorService } from 'src/services';
import { defineComponent, PropType, computed, ref, toRef, Ref } from 'vue';
import { CrudTableConfig } from '../crudTableGeneric/models/table.model';
import GCrudDataTable from '../crudTableGeneric/view/GCrudDataTable.vue';
export default defineComponent({
    components: { GCrudDataTable },
    name: 'professorHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<CrudTableConfig>({
            name: 'Profesores',
            singularLabel: 'Profesor',
            service: professorService,
            fields: [
                {
                    name: 'id',
                },
                {
                    name: 'name',
                },
                {
                    name: 'lastName',
                },
                {
                    name: 'scientificDegree',
                },
                {
                    name: 'teachingCategory',
                },
            ],
            actions: {
                create: true,
                update: true,
                delete: true,
            },
        });
        return { config };
    },
});
</script>
