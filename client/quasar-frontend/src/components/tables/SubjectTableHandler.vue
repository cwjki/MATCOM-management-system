<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import {
    careerService,
    departmentService,
    semesterService,
    studyPlanService,
    subjectService,
} from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'subjectHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Asignaturas',
            singularLabel: 'Asignatura',
            service: subjectService,
            fields: [
                {
                    name: 'name',
                    label: 'Nombre',
                    type: 'text',
                },
                {
                    name: 'study_plan',
                    label: 'Plan de Estudio',
                    column: {
                        transform(row) {
                            return `${row.study_plan.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: studyPlanService.list,
                        value: 'id',
                        label: 'name',
                    },
                },
                {
                    name: 'career',
                    label: 'Carrera',
                    column: {
                        transform(row) {
                            return `${row.career.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: careerService.list,
                        value: 'id',
                        label: 'name',
                    },
                },
                {
                    name: 'department',
                    label: 'Departamento',
                    column: {
                        transform(row) {
                            return `${row.department.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: departmentService.list,
                        value: 'id',
                        label: 'name',
                    },
                },
                {
                    name: 'semester',
                    label: 'Semestre',
                    column: {
                        transform(row) {
                            return `${row.semester.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: semesterService.list,
                        value: 'id',
                        label: 'name',
                    },
                },
                {
                    name: 'number_of_hours',
                    label: 'Horas',
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
