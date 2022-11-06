<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';
import { teachingCategoryService } from 'src/services';

export default defineComponent({
    name: 'teachingCategoryHandler',
    components: { GenericCrudDataTable },
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Categorías Docentes',
            singularLabel: 'Categoría Docente',
            searchLabel: 'Categoría Docente',
            service: teachingCategoryService,
            fields: [
                {
                    name: 'name',
                    label: 'Categoría Docente',
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
