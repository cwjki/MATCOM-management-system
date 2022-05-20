<template>
    <generic-crud-data-table :config="config">
        <!-- <template v-slot:g-table-name>
            <p class="text-h5 text-secondary text-weight-bolder q-mb-none">
                {{ config.name }}
            </p>
        </template> -->
    </generic-crud-data-table>
</template>

<script lang="ts">
import {
    departmentService,
    professorService,
    scientificDegreeService,
    teachingCategoryService,
} from 'src/services';
import { defineComponent, PropType, computed, ref, toRef, Ref } from 'vue';
// import { CrudTableConfig } from '../crudTableGeneric/models/table.model';
// import GCrudDataTable from '../crudTableGeneric/view/GCrudDataTable.vue';

import { GenericCrudTableConfig } from '../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'professorHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Profesores',
            singularLabel: 'Profesor',
            service: professorService,
            fields: [
                {
                    name: 'name',
                    label: 'Nombre',
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
                    form: {
                        responsiveOptions: {
                            md: 4,
                        },
                    },
                    rules: ['required'],
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
                    rules: ['required'],
                },
                {
                    name: 'scientific_degree',
                    label: 'Grado Científico',
                    column: {
                        transform(row) {
                            return `${row.scientific_degree.name}`;
                        },
                    },
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
        return { config };
    },
});
</script>
