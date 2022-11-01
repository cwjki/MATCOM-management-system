<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import {
    thesisCommitteeService,
    thesisService,
    professorService,
    placeService,
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
            searchLabel: 'Título o Tutores',
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
                    name: 'student',
                    label: 'Estudiante',
                    column: {
                        transform(row) {
                            return `${row.thesis.student}`;
                        },
                    },
                },
                {
                    name: 'tutor',
                    label: 'Tutor(es)',
                    column: {
                        transform(row) {
                            var result =
                                row.thesis.tutor.name +
                                ' ' +
                                row.thesis.tutor.last_name;

                            if (row.thesis.cotutors.length > 0) {
                                result += ', ';
                            }

                            row.thesis.cotutors.forEach((tutor: any) => {
                                result +=
                                    tutor.name + ' ' + tutor.last_name + ', ';
                            });
                            result = result.slice(0, -2);
                            return `${result}`;
                        },
                    },
                },
                {
                    name: 'president',
                    label: 'Presidente',
                    column: {
                        transform(row) {
                            return `${
                                row.president.name +
                                ' ' +
                                row.president.last_name
                            }`;
                        },
                    },
                    filter: true,
                    type: 'select',
                    selectOptions: {
                        list: professorService.list,
                        value: 'id',
                        label: 'name',
                        refactorValue: (value) =>
                            value
                                ? `${value.name + ' ' + value.last_name}`
                                : '',
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
                    filter: true,
                    type: 'select',
                    selectOptions: {
                        list: professorService.list,
                        value: 'id',
                        label: 'name',
                        refactorValue: (value) =>
                            value
                                ? `${value.name + ' ' + value.last_name}`
                                : '',
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
                    filter: true,
                    type: 'select',
                    selectOptions: {
                        list: professorService.list,
                        value: 'id',
                        label: 'name',
                        refactorValue: (value) =>
                            value
                                ? `${value.name + ' ' + value.last_name}`
                                : '',
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
