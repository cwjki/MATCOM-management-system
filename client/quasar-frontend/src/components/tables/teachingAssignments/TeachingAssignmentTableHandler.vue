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
import { ListResult } from '../../../services/api.service';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'teachingAssignmentHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const list: ListResult<number> = {
            results: [1, 2, 3],
            count: 3,
        };
        const config = ref<GenericCrudTableConfig>({
            name: 'Asignaciones de docencia',
            singularLabel: 'Asignación de docencia',
            filterLabel: 'Filtrar por Departamento',
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
                        refactorValue: (value) =>
                            value
                                ? `${
                                      value.subject.name +
                                      ' --- ' +
                                      value.class_type.name +
                                      ' --- ' +
                                      value.scholar_year.teaching_group +
                                      ' --- ' +
                                      ' plan ' +
                                      value.scholar_year.study_plan
                                  }`
                                : '',
                    },
                },
                {
                    name: 'scholar_year',
                    label: 'Año',
                    column: {
                        transform(row) {
                            return `${row.subject_description.scholar_year}`;
                        },
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
                // {
                //     name: 'time_period',
                //     label: 'Período de tiempo',
                //     column: {
                //         transform(row) {
                //             return `${row.subject_description.time_period}`;
                //         },
                //     },
                // },
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
                    name: 'group',
                    label: 'Grupo',
                    column: {
                        transform(row) {
                            return `${row.group}`;
                        },
                    },
                },
                {
                    name: 'professor',
                    label: 'Profesor',
                    column: {
                        transform(row) {
                            return `${
                                row.professor.name +
                                ' ' +
                                row.professor.last_name
                            }`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: professorService.list,
                        value: 'id',
                        label: 'name',
                        refactorValue: (value) =>
                            value
                                ? `${value.name + ' ' + value.last_name}`
                                : '',
                    },
                },
                {
                    name: 'percent',
                    label: 'Porciento',
                    column: {
                        transform(row) {
                            return `${row.percent}%`;
                        },
                    },
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
