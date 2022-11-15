<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';
import { scholarYearService } from 'src/services';

export default defineComponent({
    name: 'timePeriodHandler',
    components: { GenericCrudDataTable },
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Cursos Escolares',
            singularLabel: 'Curso Escolar',
            searchLabel: 'Curso Escolar',
            service: scholarYearService,
            fields: [
                {
                    name: 'name',
                    label: 'Curso escolar',
                    type: 'text',
                },
                {
                    name: 'current_year',
                    label: 'Actual ?',
                    type: 'bool',
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
