<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { studyPlanService } from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'studyPlanHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Planes de estudio',
            singularLabel: 'Plan de estudio',
            searchLabel: 'Plan de estudio',
            service: studyPlanService,
            fields: [
                {
                    name: 'name',
                    label: 'Plan de estudio',
                    type: 'text',
                },
                {
                    name: 'since',
                    label: 'Desde',
                    type: 'date',
                },
                {
                    name: 'until',
                    label: 'Hasta',
                    type: 'date',
                },
                {
                    name: 'number_of_semesters',
                    label: 'Cantidad de semestres',
                    type: 'text',
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
