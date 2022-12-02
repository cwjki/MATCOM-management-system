<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { facultyService, departmentService } from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'departmentHandler',
    props: {},
    emits: [],
    setup() {
        const config = ref<GenericCrudTableConfig>({
            name: 'Departamentos',
            singularLabel: 'Departamento',
            searchLabel: 'Departamento o Facultad',
            service: departmentService,
            fields: [
                {
                    name: 'name',
                    label: 'Departamento',
                    type: 'text',
                },
                {
                    name: 'faculty',
                    label: 'Facultad',
                    column: {
                        transform(row) {
                            return `${row.faculty.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: facultyService.list,
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
