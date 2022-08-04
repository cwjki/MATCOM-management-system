<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import {
    professorService,
    subjectDescriptionService,
    teachingAssignmentService,
} from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'teachingAssignmentHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Asignaciones de docencia',
            singularLabel: 'Asignación de docencia',
            service: teachingAssignmentService,
            fields: [
                {
                    name: 'subject_description',
                    label: 'Asignatura',
                    column: {
                        transform(row) {
                            return `${row.subject_description.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: subjectDescriptionService.list,
                        value: 'id',
                        label: 'id',
                    },
                },
                {
                    name: 'subject_description',
                    label: 'Asignatura',
                    column: {
                        transform(row) {
                            return `${row.subject_description.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: subjectDescriptionService.list,
                        value: 'id',
                        label: 'id',
                    },
                },
                {
                    name: 'class_type',
                    label: 'Actividad de clase',
                    column: {
                        transform(row) {
                            return `${row.subject_description.class_type}`;
                        },
                    },
                },
                {
                    name: 'time_period',
                    label: 'Período de tiempo',
                    column: {
                        transform(row) {
                            return `${row.subject_description.time_period}`;
                        },
                    },
                },
                {
                    name: 'number_of_hours',
                    label: 'Cantidad de horas',
                    column: {
                        transform(row) {
                            return `${row.subject_description.number_of_hours}`;
                        },
                    },
                },
                {
                    name: 'number_of_groups',
                    label: 'Cantidad de grupos',
                    column: {
                        transform(row) {
                            return `${row.subject_description.number_of_groups}`;
                        },
                    },
                },
                {
                    name: 'professor',
                    label: 'Profesor',
                    column: {
                        transform(row) {
                            return `${row.professor.name + ' ' + row.professor.last_name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: professorService.list,
                        value: 'id',
                        label: 'name',
                    },
                },
                {
                    name: 'percent',
                    label: 'Porciento',
                    type: 'text',
                },
                {
                    name: 'group',
                    label: 'Grupo',
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
