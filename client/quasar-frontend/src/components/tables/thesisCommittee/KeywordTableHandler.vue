<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { keywordService } from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'keywordHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Palabras Claves',
            singularLabel: 'Palabra Clave',
            service: keywordService,
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
