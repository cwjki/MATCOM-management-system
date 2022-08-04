<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { teachingGroupService, studyPlanService } from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'teachingGroupHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Grupos',
            singularLabel: 'Grupo',
            service: teachingGroupService,
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
