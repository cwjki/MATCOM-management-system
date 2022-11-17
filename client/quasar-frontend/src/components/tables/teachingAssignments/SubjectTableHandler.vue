<template>
    <div class="full-width justify-between row items-center q-pb-sm">
        <q-btn
            class=""
            no-caps
            color="secondary"
            outline
            label="Profesores"
            @click="$router.push({ name: 'professors' })"
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
            label="Planificar asignaturas"
            @click="$router.push({ name: 'subject-plannings' })"
        >
        </q-btn>
    </div>
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
import { useDepartmentSession } from 'src/hooks/departmentSession';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';
import { FieldModel } from 'src/components/genericCrudTable/models/field.model';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'subjectHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const { department, clear } = useDepartmentSession();
        const config = ref<GenericCrudTableConfig>({
            name: 'Asignaturas',
            singularLabel: 'Asignatura',
            searchLabel: 'Asignatura',
            service: subjectService,
            defaultValues: {
                ...(department.value.id
                    ? { department_id: department.value.id }
                    : {}),
            },
            query: {
                ...(department.value.id
                    ? { department: department.value.id }
                    : {}),
            },
            fields: [
                {
                    name: 'name',
                    label: 'Asignatura',
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
                    filter: true,
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
                    filter: true,
                    type: 'select',
                    selectOptions: {
                        list: careerService.list,
                        value: 'id',
                        label: 'name',
                    },
                },
                ...(department.value.id
                    ? []
                    : ([
                          {
                              name: 'department',
                              label: 'Departamento',
                              column: {
                                  transform(row) {
                                      return `${row.department.name}`;
                                  },
                              },
                              type: 'select',
                              filter: true,
                              selectOptions: {
                                  list: departmentService.list,
                                  value: 'id',
                                  label: 'name',
                              },
                          },
                      ] as FieldModel[])),
                {
                    name: 'semester',
                    label: 'Semestre',
                    filter: true,
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

        return { config, department, clear };
    },
});
</script>
