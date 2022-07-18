<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import {
    carmenTableService,
    timePeriodService,
    semesterService,
    teachingGroupService,
} from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'carmenHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Tabla de Carmen',
            singularLabel: 'Tabla',
            service: carmenTableService,
            fields: [
                {
                    name: 'teaching_grupo',
                    label: 'Curso',
                    column: {
                        transform(row) {
                            return `${row.teaching_group.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: teachingGroupService.list,
                        value: 'id',
                        label: 'name',
                    },
                    rules: ['required'],
                },
                {
                    name: 'semester',
                    label: 'Semestre',
                    column: {
                        transform(row) {
                            return `${row.semester.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: semesterService.list,
                        value: 'id',
                        label: 'name',
                    },
                    rules: ['required'],
                },
                {
                    name: 'time_period',
                    label: 'Período de tiempo',
                    column: {
                        transform(row) {
                            return `${row.time_period.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: timePeriodService.list,
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
