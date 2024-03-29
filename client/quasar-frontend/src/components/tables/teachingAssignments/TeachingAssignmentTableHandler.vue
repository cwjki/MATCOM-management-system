<template>
    <q-card
        class="full-width q-mb-md"
        :style="
            $q.screen.xs ||
            'position: sticky !important;top: 60px !important;z-index: 1000 !important;'
        "
    >
        <div
            class="full-width justify-between row items-center q-pb-md q-pt-md q-px-md"
            v-if="department.id"
        >
            <q-btn
                class=""
                no-caps
                color="secondary"
                icon="navigate_before"
                outline
                label="Planificación"
                @click="$router.push({ name: 'subject-plannings' })"
            >
            </q-btn>

            <p class="text-h6 text-primary q-mb-none">
                Departamento: {{ department.name }}
                <q-btn
                    color="red"
                    icon="clear"
                    class="q-ml-sm"
                    dense
                    rounded
                    outline
                    @click="clear"
                    fabmini
                ></q-btn>
            </p>

            <q-btn
                class=""
                no-caps
                color="secondary"
                icon-right="home"
                outline
                label="Página principal"
                @click="$router.push({ name: 'home' })"
            >
            </q-btn>
        </div>

        <q-separator />

        <q-card-section
            class="full-width row justify-center items-center q-pa-none q-pt-md"
        >
            <div
                class="q-px-sm q-mb-md"
                v-for="(obj, key) in userCharges"
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
                        {{ `${obj.hours.toFixed(0)}h` }}
                    </q-badge>
                    <q-tooltip>
                        {{ refactorName(obj.subjects) }}
                    </q-tooltip>
                </q-btn>
            </div>
        </q-card-section>
    </q-card>
    <generic-crud-data-table @onRequest="onReload" :config="config" />
</template>

<script lang="ts">
import {
    professorService,
    subjectDescriptionService,
    teachingAssignmentService,
} from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';
import { Dictionary } from 'src/models/base';
import { axios } from 'src/boot/axios';
import { useDepartmentSession } from 'src/hooks/departmentSession';

type UserCharge = {
    name: string;
    hours: number;
    subjects: {
        hour: number;
        name: string;
        class_type: string;
    }[];
};

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'teachingAssignmentHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const { department, clear } = useDepartmentSession();

        const config = ref<GenericCrudTableConfig>({
            name: 'Asignaciones de docencia',
            singularLabel: 'Asignación de docencia',
            searchLabel: 'Asignatura o Actividad',
            service: teachingAssignmentService,
            query: {
                ...(department.value.id
                    ? {
                          subject_description__subject__department:
                              department.value.id,
                      }
                    : {}),
            },
            fields: [
                {
                    name: 'subject_description',
                    label: 'Asignatura',
                    column: {
                        transform(row) {
                            return `${row.subject_description.subject.name}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        query: {
                            ...(department.value.id
                                ? { subject__department: department.value.id }
                                : {}),
                        },
                        list: subjectDescriptionService.list,
                        value: 'id',
                        label: 'subject_description',
                        refactorValue: (value) =>
                            value.subject
                                ? `${
                                      value.subject.name +
                                      ' --- ' +
                                      value.class_type.name +
                                      ' --- ' +
                                      value.teaching_group.name
                                      //   ' --- ' +
                                      //   ' plan ' +
                                      //   value.subject.study_plan
                                  }`
                                : '',

                        // REVISAR ESTO ME DA BATEO EDITAR SI MUESTRO LOS CAMPOS CORRECTAMENTE
                    },
                    rules: ['required'],
                },
                {
                    name: 'scholar_year',
                    label: 'Año',
                    column: {
                        transform(row) {
                            return `${row.subject_description.teaching_group.name}`;
                        },
                    },
                },
                {
                    name: 'class_type',
                    label: 'Actividad de clase',
                    column: {
                        transform(row) {
                            return `${row.subject_description.class_type.name}`;
                        },
                    },
                },
                // {
                //     name: 'time_period',
                //     label: 'Período de tiempo',
                //     column: {
                //         transform(row) {
                //             return `${row.subject_description.time_period}`;
                //         },
                //     },
                // },
                {
                    name: 'number_of_hours',
                    label: 'Cantidad de horas',
                    column: {
                        transform(row) {
                            return `${row.subject_description.number_of_hours}`;
                        },
                    },
                },
                {
                    name: 'number_of_groups',
                    label: 'Total de grupos',
                    column: {
                        transform(row) {
                            return `${row.subject_description.number_of_groups}`;
                        },
                    },
                },
                {
                    name: 'group',
                    label: 'Grupo',
                    column: {
                        transform: (row) => (row.group ? `${row.group}` : ''),
                    },
                    type: 'text',
                    rules: ['required'],
                },
                {
                    name: 'professor',
                    label: 'Profesor',
                    column: {
                        ordering: true,
                        transform: (row) =>
                            row.professor
                                ? `${
                                      row.professor.name +
                                      ' ' +
                                      row.professor.last_name
                                  }`
                                : '',
                    },
                    filter: true,
                    type: 'select',
                    selectOptions: {
                        list: professorService.list,
                        value: 'id',
                        label: 'name',
                        query: {
                            ...(department.value.id
                                ? { department: department.value.id }
                                : {}),
                        },
                        refactorValue: (value) =>
                            value
                                ? `${value.name + ' ' + value.last_name}`
                                : '',
                    },
                    rules: ['required'],
                },
                {
                    name: 'percent',
                    label: 'Porciento',
                    column: {
                        ordering: true,
                        transform: (row) =>
                            row.percent ? `${row.percent}%` : '',
                    },
                    type: 'text',
                    rules: ['required'],
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
                                url: 'http://127.0.0.1:8000/teaching-assignment/csv-download/',
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
                                    'Asignación de docencia' + '.csv'
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

        const userCharges = ref<Dictionary<UserCharge>>({});

        return {
            config,
            userCharges,
            onReload() {
                console.log('onreloaded');
                loading.value = true;
                Object.keys(userCharges.value).map((key) => {
                    userCharges.value[key].hours = 0;
                    userCharges.value[key].subjects = [];
                });
                teachingAssignmentService
                    .list({
                        size: 100000,
                        ...(department.value.id
                            ? {
                                  subject_description__subject__department:
                                      department.value.id,
                              }
                            : {}),
                    })
                    .then((response: any) => {
                        response.data.results.map((x: any) => {
                            if (!x.professor) return;
                            const idp = x.professor.id;
                            if (!userCharges.value[idp]) {
                                userCharges.value[idp] = {
                                    hours: 0,
                                    name:
                                        x.professor.name +
                                        ' ' +
                                        x.professor.last_name,
                                    subjects: [],
                                };
                            }

                            userCharges.value[idp].hours +=
                                (x.subject_description.number_of_hours *
                                    x.percent) /
                                100.0;
                            userCharges.value[idp].subjects.push({
                                hour: x.subject_description.number_of_hours,
                                name: x.subject_description.subject.name,
                                class_type:
                                    x.subject_description.class_type.name,
                            });
                        });
                    })
                    .finally(() => {
                        loading.value = false;
                    });
            },
            loading,
            clear,
            department,
            refactorName(
                data: {
                    hour: number;
                    name: string;
                    class_type: string;
                }[]
            ) {
                return data.reduce((prev, current, index) => {
                    return (
                        prev +
                        `${current.name}-${
                            current.class_type
                        } (${current.hour.toFixed(0)}h) | `
                    );
                }, '| ');
            },
        };
    },
});
</script>
