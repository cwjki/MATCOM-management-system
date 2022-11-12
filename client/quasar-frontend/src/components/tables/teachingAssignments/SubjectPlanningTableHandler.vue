<template>
    <p
        class="text-h6 text-primary full-width text-center"
        v-if="departament.id"
    >
        Departamento: {{ departament.name }}
    </p>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { useDepartamentSesion } from 'src/hooks/departamentSesion';
import {
    classTypeService,
    scholarYearService,
    subjectDescriptionService,
    subjectService,
    teachingGroupService,
    timePeriodService,
} from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'subjectPlanningHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const { departament } = useDepartamentSesion();
        const config = ref<GenericCrudTableConfig>({
            name: 'Planificación de las Asignaturas',
            singularLabel: 'Planificación',
            searchLabel: 'Asignatura',
            service: subjectDescriptionService,
            query: {
                ...(departament.value.id
                    ? { subject__department: departament.value.id }
                    : {}),
            },
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
                        query: {
                            ...(departament.value.id
                                ? { department: departament.value.id }
                                : {}),
                        },
                        refactorValue: (value) =>
                            value
                                ? `${
                                      value.name +
                                      ' --- ' +
                                      value.career.name +
                                      ' --- ' +
                                      ' plan ' +
                                      value.study_plan.name
                                  }`
                                : '',
                    },
                    rules: ['required'],
                },
                {
                    name: 'teaching_group',
                    label: 'Año',
                    column: {
                        transform(row) {
                            return `${row.teaching_group.name}`;
                        },
                    },
                    filter: true,
                    type: 'select',
                    selectOptions: {
                        list: teachingGroupService.list,
                        value: 'id',
                        label: 'name',
                    },
                    rules: ['required'],
                },
                {
                    name: 'class_type',
                    label: 'Actividad de Clase',
                    column: {
                        transform(row) {
                            return `${row.class_type.name}`;
                        },
                    },
                    filter: true,
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
                    label: 'Total de grupos',
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
                    name: 'scholar_year',
                    label: 'Curso Escolar',
                    column: {
                        transform(row) {
                            return `${row.scholar_year.name}`;
                        },
                    },
                    filter: true,
                    type: 'select',
                    selectOptions: {
                        list: scholarYearService.list,
                        value: 'id',
                        label: 'name',
                    },
                    rules: ['required'],
                },
                {
                    name: 'time_period',
                    label: 'Período de Tiempo',
                    column: {
                        transform(row) {
                            return `${row.time_period.name}`;
                        },
                    },
                    filter: true,
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

        return { config, departament };
    },
});
</script>
