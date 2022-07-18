<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../genericCrudTable/views/GenericCrudDataTable.vue';
import { scientificDegreeService } from 'src/services';

export default defineComponent({
    name: 'scientificDegreeHandler',
    components: { GenericCrudDataTable },
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Grados Científicos',
            singularLabel: 'Grado Científico',
            service: scientificDegreeService,
            fields: [
                {
                    name: 'name',
                    label: 'Grado Científico ',
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
