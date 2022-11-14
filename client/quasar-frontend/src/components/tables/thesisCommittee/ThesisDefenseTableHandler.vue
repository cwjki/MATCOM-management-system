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
import { axios } from 'src/boot/axios';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'thesisDefenseHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Defensas de Tesis',
            singularLabel: 'Defensa de Tesis',
            searchLabel: 'Fecha o Tesis',
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
                        transform: (row) =>
                            row.place ? `${row.place.name}` : '',
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
                    label: 'Tesis',
                    column: {
                        transform(row) {
                            return `${row.thesis_committee.thesis.title}`;
                        },
                        maxLength: 20,
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
                                result += '<br>';
                                row.thesis_committee.thesis.cotutors.forEach(
                                    (tutor: any) => {
                                        result +=
                                            tutor.name +
                                            ' ' +
                                            tutor.last_name +
                                            '<br>';
                                    }
                                );
                                result = result.slice(0, -2);
                            }

                            return `${result}`;
                        },
                    },
                },
                {
                    name: 'opponent',
                    label: 'Oponente',
                    column: {
                        transform: (row) =>
                            row.thesis_committee.opponent
                                ? `${
                                      row.thesis_committee.opponent.name +
                                      ' ' +
                                      row.thesis_committee.opponent.last_name
                                  }`
                                : ' ',
                    },
                },
                {
                    name: 'president',
                    label: 'Presidente',
                    column: {
                        transform: (row) =>
                            row.thesis_committee.president
                                ? `${
                                      row.thesis_committee.president.name +
                                      ' ' +
                                      row.thesis_committee.president.last_name
                                  }`
                                : ' ',
                    },
                },
                // {
                //     name: 'secretary',
                //     label: 'Secretario',
                //     column: {
                //         transform: (row) =>
                //             row.thesis_committee.secretary
                //                 ? `${
                //                       row.thesis_committee.secretary.name +
                //                       ' ' +
                //                       row.thesis_committee.secretary.last_name
                //                   }`
                //                 : ' ',
                //     },
                // },
                {
                    name: 'keywords',
                    label: 'Palabras clave',
                    column: {
                        transform(row) {
                            var result = '';
                            row.thesis_committee.thesis.keywords.forEach(
                                (keyword: any) => {
                                    result += keyword.name + '<br>';
                                }
                            );
                            return `${result.slice(0, -2)}`;
                        },
                    },
                },

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
                external: [
                    {
                        icon: 'download',
                        color: 'green',
                        func: () => {
                            return axios({
                                url: 'http://127.0.0.1:8000/thesis-assignment/thesis-defense-csv-download/',
                                method: 'GET',
                                responseType: 'blob',
                            }).then((response) => {
                                const File = window.URL.createObjectURL(
                                    new Blob([response.data])
                                );
                                const docUrl = document.createElement('a');
                                docUrl.href = File;
                                docUrl.setAttribute(
                                    'download',
                                    'Defensas de tesis' + '.csv'
                                );
                                document.body.appendChild(docUrl);
                                docUrl.click();
                            });
                        },
                    },
                ],
            },
        });
        return { config };
    },
});
</script>
