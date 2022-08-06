<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';
import { careerService, facultyService } from 'src/services';

export default defineComponent({
    name: 'careerHandler',
    components: { GenericCrudDataTable },
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Carreras',
            singularLabel: 'Carrera',
            service: careerService,
            fields: [
                {
                    name: 'name',
                    label: 'Nombre',
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
