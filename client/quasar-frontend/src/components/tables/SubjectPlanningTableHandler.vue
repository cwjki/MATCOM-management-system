<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import {
    classTypeService,
    subjectDescriptionService,
    subjectService,
    timePeriodService,
} from 'src/services';
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
                    column: {
                        transform(row) {
                            return `${row.subject.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: subjectService.list,
                        value: 'id',
                        label: 'name',
                    },
                    rules: ['required'],
                },
                {
                    name: 'classType',
                    label: 'Actividad de Clase',
                    column: {
                        transform(row) {
                            return `${row.class_type.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: classTypeService.list,
                        value: 'id',
                        label: 'name',
                    },
                    rules: ['required'],
                },
                {
                    name: 'number_of_groups',
                    label: 'Grupos',
                    type: 'text',

                    rules: ['required'],
                },
                {
                    name: 'number_of_hours',
                    label: 'Horas',
                    type: 'text',
                    rules: ['required'],
                },
                {
                    name: 'timePeriod',
                    label: 'Período de Tiempo',
                    column: {
                        transform(row) {
                            return `${row.time_period.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: timePeriodService.list,
                        value: 'id',
                        label: 'name',
                    },
                    rules: ['required'],
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
