<template>
    <generic-crud-data-table :config="config">
        <!-- <template v-slot:column-student="props">
            <q-badge> {{ props.value.thesis.student }} </q-badge>
        </template> -->
        <!-- <template v-slot:table-column-student="props">
            <q-btn> {{ props.value.thesis.student }} </q-btn>
        </template> -->
    </generic-crud-data-table>
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
import { axios } from 'src/boot/axios';

type ProfessorCharge = {
    name: string;
    opponent_amount: number;
    president_amount: number;
    opponent_thesis: {
        name: string;
        keywords: string[];
    };
    president_thesis: {
        name: string;
        keywords: string[];
    };
};

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
                    name: 'student',
                    label: 'Estudiante',
                    column: {
                        transform(row) {
                            return `${row.thesis.student}`;
                        },
                    },
                },
                {
                    name: 'thesis',
                    label: 'Título',
                    column: {
                        transform(row) {
                            return `${row.thesis.title}`;
                        },
                        maxLength: 20,
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
                    name: 'tutor',
                    label: 'Tutor(es)',
                    column: {
                        transform(row) {
                            var result =
                                row.thesis.tutor.name +
                                ' ' +
                                row.thesis.tutor.last_name;

                            if (row.thesis.cotutors.length > 0) {
                                result += '<br>';
                                row.thesis.cotutors.forEach((tutor: any) => {
                                    result +=
                                        tutor.name +
                                        ' ' +
                                        tutor.last_name +
                                        ', ';
                                });
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
                            row.opponent
                                ? `${
                                      row.opponent.name +
                                      ' ' +
                                      row.opponent.last_name
                                  }`
                                : '',
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
                    name: 'president',
                    label: 'Presidente',
                    column: {
                        transform: (row) =>
                            row.president
                                ? `${
                                      row.president.name +
                                      ' ' +
                                      row.president.last_name
                                  }`
                                : '',
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
                // {
                //     name: 'secretary',
                //     label: 'Secretario',
                //     column: {
                //         transform: (row) =>
                //             row.secretary
                //                 ? `${
                //                       row.secretary.name +
                //                       ' ' +
                //                       row.secretary.last_name
                //                   }`
                //                 : '',
                //     },
                //     filter: true,
                //     type: 'select',
                //     selectOptions: {
                //         list: professorService.list,
                //         value: 'id',
                //         label: 'name',
                //         refactorValue: (value) =>
                //             value
                //                 ? `${value.name + ' ' + value.last_name}`
                //                 : '',
                //     },
                //     rules: ['required'],
                // },

                {
                    name: 'keywords',
                    label: 'Palabras clave',
                    column: {
                        transform(row) {
                            var result = '';
                            row.thesis.keywords.forEach((keyword: any) => {
                                result += keyword.name + '<br>';
                            });
                            return `${result.slice(0, -2)}`;
                        },
                    },
                },
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
                                url: 'http://127.0.0.1:8000/thesis-assignment/thesis-committee-csv-download/',
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
                                    'Tribunales de tesis' + '.csv'
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
