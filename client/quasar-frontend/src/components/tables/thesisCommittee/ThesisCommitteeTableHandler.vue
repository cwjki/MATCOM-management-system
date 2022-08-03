<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import {
    thesisCommitteeService,
    thesisService,
    professorService,
    studentService,
} from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'thesisCommitteeHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Tribunales de Tesis',
            singularLabel: 'Tribunal',
            service: thesisCommitteeService,
            fields: [
                {
                    name: 'thesis',
                    label: 'Título',
                    column: {
                        transform(row) {
                            return `${row.thesis.title}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: thesisService.list,
                        value: 'id',
                        label: 'title',
                    },
                    rules: ['required'],
                },
                {
                    name: 'opponent',
                    label: 'Oponente',
                    column: {
                        transform(row) {
                            return `${
                                row.opponent.name + ' ' + row.opponent.last_name
                            }`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: professorService.list,
                        value: 'id',
                        label: 'name',
                    },
                    rules: ['required'],
                },
                {
                    name: 'secretary',
                    label: 'Secretario',
                    column: {
                        transform(row) {
                            return `${
                                row.secretary.name +
                                ' ' +
                                row.secretary.last_name
                            }`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: professorService.list,
                        value: 'id',
                        label: 'name',
                    },
                    rules: ['required'],
                },
                {
                    name: 'date',
                    label: 'Fecha',
                    type: 'date',
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
