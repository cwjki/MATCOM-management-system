<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { departmentService } from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'departmentHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Departamentos',
            singularLabel: 'Departamento',
            service: departmentService,
            fields: [
                {
                    name: 'name',
                    label: 'Nombre',
                },
                {
                    name: 'career',
                    label: 'Carrera',
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
