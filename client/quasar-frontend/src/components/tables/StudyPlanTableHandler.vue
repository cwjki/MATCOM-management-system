<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { studyPlanService } from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'studyPlanHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Planes de estudio',
            singularLabel: 'Plan de estudio',
            service: studyPlanService,
            fields: [
                {
                    name: 'name',
                    label: 'Nombre',
                },
                {
                    name: 'since',
                    label: 'Desde',
                },
                {
                    name: 'until',
                    label: 'Hasta',
                },
                {
                    name: 'number_of_semesters',
                    label: 'Cantidad de semestres',
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
