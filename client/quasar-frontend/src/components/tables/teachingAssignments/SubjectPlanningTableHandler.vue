<template>
    <div class="full-width justify-between row items-center q-pb-sm">
        <q-btn
            class=""
            no-caps
            color="secondary"
            outline
            label="Asignaturas"
            @click="$router.push({ name: 'subjects' })"
        >
        </q-btn>
        <p class="text-h6 text-primary q-mb-none" v-if="department.id">
            Departamento: {{ department.name }}
            <q-btn
                color="red"
                icon="clear"
                class="q-ml-sm"
                dense
                rounded
                outline
                @click="clear"
                fabmini
            ></q-btn>
        </p>
        <q-btn
            class=""
            no-caps
            color="secondary"
            outline
            label="Asignar docencia"
            @click="$router.push({ name: 'teaching-assignments' })"
        >
        </q-btn>
    </div>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { useDepartmentSession } from 'src/hooks/departmentSession';
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
        const { department, clear } = useDepartmentSession();
        const config = ref<GenericCrudTableConfig>({
            name: 'Planificación de las Asignaturas',
            singularLabel: 'Planificación',
            searchLabel: 'Asignatura',
            service: subjectDescriptionService,
            query: {
                ...(department.value.id
                    ? { subject__department: department.value.id }
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
                            ...(department.value.id
                                ? { department: department.value.id }
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

        return { config, department, clear };
    },
});
</script>
