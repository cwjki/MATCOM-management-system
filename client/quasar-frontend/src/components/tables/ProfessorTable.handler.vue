<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { professorService } from 'src/services';
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
                },
                {
                    name: 'lastName',
                    label: 'Apellidos',
                },
                {
                    name: 'department',
                    label: 'Departamento',
                },
                {
                    name: 'scientificDegree',
                    label: 'Grado Científico',
                },
                {
                    name: 'teachingCategory',
                    label: 'Categoría Docente',
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
