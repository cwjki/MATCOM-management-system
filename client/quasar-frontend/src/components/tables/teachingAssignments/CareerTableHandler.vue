<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';
import { careerService } from 'src/services';

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
