<template>
    <div class="full-width justify-between row items-center q-pb-sm">
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
            label="Asignaturas"
            @click="$router.push({ name: 'subjects' })"
        >
        </q-btn>
    </div>

    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import {
    departmentService,
    professorService,
    scientificDegreeService,
    teachingCategoryService,
} from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';
import { useDepartmentSession } from 'src/hooks/departmentSession';
import { FieldModel } from 'src/components/genericCrudTable/models/field.model';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'professorHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const { department, clear } = useDepartmentSession();
        const config = ref<GenericCrudTableConfig>({
            name: 'Profesores',
            singularLabel: 'Profesor',
            searchLabel: 'Buscar por texto',
            service: professorService,
            // defaultValues: {
            //     ...(departament.value.id
            //         ? { department_id: departament.value.id }
            //         : {}),
            // },
            query: {
                ...(department.value.id
                    ? { department: department.value.id }
                    : {}),
            },
            fields: [
                {
                    name: 'name',
                    label: 'Nombre',
                    type: 'text',
                    form: {
                        responsiveOptions: {
                            md: 12,
                        },
                    },
                    rules: ['required'],
                },
                {
                    name: 'last_name',
                    label: 'Apellidos',
                    type: 'text',
                    form: {
                        responsiveOptions: {
                            md: 4,
                        },
                    },
                    rules: ['required'],
                },
                // {
                //     name: 'faculty',
                //     label: 'Facultad',
                //     column: {
                //         transform(row) {
                //             return `${row.faculty.name}`;
                //         },
                //     },
                // },
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
                              filter: true,
                              type: 'select',
                              selectOptions: {
                                  list: departmentService.list,
                                  value: 'id',
                                  label: 'name',
                              },
                              rules: ['required'],
                          },
                      ] as FieldModel[])),

                {
                    name: 'scientific_degree',
                    label: 'Grado Científico',
                    column: {
                        transform(row) {
                            return `${row.scientific_degree.name}`;
                        },
                    },
                    filter: true,
                    type: 'select',
                    selectOptions: {
                        list: scientificDegreeService.list,
                        value: 'id',
                        label: 'name',
                    },
                    rules: ['required'],
                },
                {
                    name: 'teaching_category',
                    label: 'Categoría Docente',
                    column: {
                        transform(row) {
                            return `${row.teaching_category.name}`;
                        },
                    },
                    filter: true,
                    type: 'select',
                    selectOptions: {
                        list: teachingCategoryService.list,
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
