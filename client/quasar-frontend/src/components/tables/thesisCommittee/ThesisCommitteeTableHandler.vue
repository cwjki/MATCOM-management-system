<template>
    <q-card
        class="full-width q-mb-md"
        style="
            position: sticky !important;
            top: 60px !important;
            z-index: 1000 !important;
        "
    >
        <div
            class="full-width justify-between row items-center q-pb-sm q-pt-md q-px-md"
            v-if="idC"
        >
            <q-btn
                class=""
                no-caps
                color="secondary"
                outline
                label="Tesis"
                @click="handleRoute('thesis', idC, Cname)"
            >
            </q-btn>

            <p class="text-h6 text-primary q-mb-none">
                Curso escolar: {{ Cname }}
                <q-btn
                    color="red"
                    icon="clear"
                    class="q-ml-sm"
                    dense
                    rounded
                    outline
                    @click="$router.push({ name: 'thesis-committees' })"
                    fabmini
                ></q-btn>
            </p>

            <q-btn
                class=""
                no-caps
                color="secondary"
                outline
                label="Defensas"
                @click="handleRoute('thesis-defenses', idC, Cname)"
            >
            </q-btn>
        </div>

        <q-separator />

        <q-card-section
            class="full-width row justify-center items-center q-pa-none q-pt-md"
        >
            <div
                class="q-px-sm q-mb-md"
                v-for="(obj, key) in professorCharges"
                :key="key"
            >
                <q-btn
                    :loading="loading"
                    no-caps
                    color="secondary"
                    outline
                    ripple
                    class="q-px-md"
                >
                    {{ obj.name }}
                    <q-badge
                        color="primary"
                        class="q-pa-xs"
                        floating
                        align="top"
                        style="top: -10px !important"
                    >
                        {{ obj.opponent_amount }} |
                        {{ obj.president_amount }}
                    </q-badge>
                    <q-tooltip>
                        Oponente: {{ obj.opponent_amount }} | Presidente:
                        {{ obj.president_amount }}
                    </q-tooltip>
                </q-btn>
            </div>
        </q-card-section>
    </q-card>

    <generic-crud-data-table @on-request="onReload" :config="config">
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
} from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';
import { axios } from 'src/boot/axios';
import { Dictionary } from 'src/models/base';
import { useRouteHandler } from 'src/hooks/routeHandler';

type ProfessorCharge = {
    name: string;
    opponent_amount: number;
    president_amount: number;
    thesis: {
        name: string;
        keywords: string[];
        role: string;
    }[];
};

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'thesisCommitteeHandler',
    props: ['idC', 'Cname'],
    emits: [],
    setup(props, { emit }) {
        const { handleRoute } = useRouteHandler();
        const config = ref<GenericCrudTableConfig>({
            name: 'Tribunales de Tesis',
            singularLabel: 'Tribunal',
            searchLabel: 'Título o Tutores',
            service: thesisCommitteeService,
            defaultValues: {
                ...(props.idC ? { thesis__scholar_year_id: props.idC } : {}),
            },
            query: {
                ...(props.idC ? { thesis__scholar_year: props.idC } : {}),
            },
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
                        query: {
                            ...(props.idC ? { scholar_year: props.idC } : {}),
                        },
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

        const loading = ref<boolean>(false);

        const professorCharges = ref<Dictionary<ProfessorCharge>>({});

        return {
            config,
            professorCharges,
            handleRoute,
            onReload() {
                loading.value = true;
                Object.keys(professorCharges.value).map((key) => {
                    professorCharges.value[key].opponent_amount = 0;
                    professorCharges.value[key].president_amount = 0;
                    professorCharges.value[key].thesis = [];
                });
                thesisCommitteeService
                    .list({
                        size: 100000,
                        ...(props.idC
                            ? { thesis__scholar_year: props.idC }
                            : {}),
                    })
                    .then((response: any) => {
                        response.data.results.map((x: any) => {
                            if (x.opponent) {
                                const idp = x.opponent.id;
                                if (!professorCharges.value[idp]) {
                                    professorCharges.value[idp] = {
                                        name:
                                            x.opponent.name +
                                            ' ' +
                                            x.opponent.last_name,
                                        opponent_amount: 0,
                                        president_amount: 0,
                                        thesis: [],
                                    };
                                }

                                professorCharges.value[
                                    idp
                                ].opponent_amount += 1;
                                professorCharges.value[idp].thesis.push({
                                    name: x.thesis.title,
                                    keywords: x.keywords,
                                    role: 'oponente',
                                });
                            }

                            if (x.president) {
                                const idp = x.president.id;
                                if (!professorCharges.value[idp]) {
                                    professorCharges.value[idp] = {
                                        name:
                                            x.president.name +
                                            ' ' +
                                            x.president.last_name,
                                        opponent_amount: 0,
                                        president_amount: 0,
                                        thesis: [],
                                    };
                                }

                                professorCharges.value[
                                    idp
                                ].president_amount += 1;
                                professorCharges.value[idp].thesis.push({
                                    name: x.thesis.title,
                                    keywords: x.keywords,
                                    role: 'presidente',
                                });
                            }
                        });
                    })
                    .finally(() => {
                        loading.value = false;
                    });
            },
            loading,
        };
    },
});
</script>
