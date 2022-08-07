<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { teachingPlanningService } from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'teachingPlanningHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Planificación de Docencia',
            singularLabel: 'Docencia',
            service: teachingPlanningService,
            fields: [
                {
                    name: 'teaching_assignments',
                    label: 'Id',
                    column: {
                        transform(row) {
                            return `${row.id}`;
                        },
                    },
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

<!-- // row.teaching_assignments[0].professor.name +
                                // ' ' +
                                // row.teaching_assignments[0].subject_description
                                //     .name +
                                // ' ' +
                                // row.teaching_assignments[0].subject_description
                                //     .class_type -->
