<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { careerService, departmentService } from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';

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
                    type: 'text',
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
