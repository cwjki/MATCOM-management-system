<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { subjectDescriptionService } from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'subjectPlanningHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Planificación de las Asignaturas',
            singularLabel: 'Planificación',
            service: subjectDescriptionService,
            fields: [
                {
                    name: 'subject',
                    label: 'Asignatura',
                },
                {
                    name: 'classType',
                    label: 'Actividad de Clase',
                },
                {
                    name: 'numberOfGroups',
                    label: 'Grupos',
                },
                {
                    name: 'numberOfHours',
                    label: 'Horas',
                },
                {
                    name: 'timePeriod',
                    label: 'Período de Tiempo',
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
