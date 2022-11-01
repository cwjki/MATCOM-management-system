<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import {
    thesisDefenseService,
    thesisCommitteeService,
    placeService,
} from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'thesisDefenseHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Defensas de Tesis',
            singularLabel: 'Defensa de Tesis',
            searchLabel: 'Fecha o Título de la tesis',
            service: thesisDefenseService,
            fields: [
                {
                    name: 'date',
                    label: 'Fecha',
                    type: 'date',
                    rules: ['required'],
                },
                {
                    name: 'time',
                    label: 'Hora',
                    type: 'time',
                    rules: ['required'],
                },
                {
                    name: 'place',
                    label: 'Lugar',
                    column: {
                        transform(row) {
                            return `${row.place.name}`;
                        },
                    },
                    filter: true,
                    type: 'select',
                    selectOptions: {
                        list: placeService.list,
                        value: 'id',
                        label: 'name',
                    },
                    rules: ['required'],
                },
                {
                    name: 'thesis_committee',
                    label: 'Título de la tesis',
                    column: {
                        transform(row) {
                            return `${row.thesis_committee.thesis.title}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: thesisCommitteeService.list,
                        value: 'id',
                        label: 'thesis_committee',
                        refactorValue: (value) =>
                            value.thesis ? `${value.thesis.title}` : '',
                    },
                    rules: ['required'],
                },
                {
                    name: 'student',
                    label: 'Estudiante',
                    column: {
                        transform(row) {
                            return `${row.thesis_committee.thesis.student}`;
                        },
                    },
                },
                {
                    name: 'tutor',
                    label: 'Tutor(es)',
                    column: {
                        transform(row) {
                            var result =
                                row.thesis_committee.thesis.tutor.name +
                                ' ' +
                                row.thesis_committee.thesis.tutor.last_name;

                            if (
                                row.thesis_committee.thesis.cotutors.length > 0
                            ) {
                                result += ', ';
                                row.thesis_committee.thesis.cotutors.forEach(
                                    (tutor: any) => {
                                        result +=
                                            tutor.name +
                                            ' ' +
                                            tutor.last_name +
                                            ', ';
                                    }
                                );
                                result = result.slice(0, -2);
                            }

                            return `${result}`;
                        },
                    },
                },
                // {
                //     name: 'president',
                //     label: 'Presidente',
                //     column: {
                //         transform(row) {
                //             return `${row.thesis_committee.president}`;
                //         },
                //     },
                // },
                // {
                //     name: 'secretary',
                //     label: 'Secretario',
                //     column: {
                //         transform(row) {
                //             return `${row.thesis_committee.secretary}`;
                //         },
                //     },
                // },
                // {
                //     name: 'opponent',
                //     label: 'Oponente',
                //     column: {
                //         transform(row) {
                //             return `${row.thesis_committee.opponent}`;
                //         },
                //     },
                // },
                // {
                //     name: 'keywords',
                //     label: 'Palabras Claves',
                //     column: {
                //         transform(row) {
                //             return `${row.thesis_committee.keywords}`;
                //         },
                //     },
                // },
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
