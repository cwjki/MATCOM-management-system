<template>
    <div class="full-width justify-between row items-end q-pb-sm">
        <p class="text-h6 text-primary q-mb-none" v-if="idC">
            Curso escolar: {{ Cname }}
            <q-btn
                color="red"
                icon="clear"
                class="q-ml-sm"
                dense
                rounded
                outline
                @click="$router.push({ name: 'thesis' })"
                fabmini
            ></q-btn>
        </p>
        <q-btn
            class=""
            no-caps
            color="secondary"
            outline
            label="Tribunales"
            @click="handleRoute('thesis-committees', idC, Cname)"
        >
        </q-btn>
    </div>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { FieldModel } from 'src/components/genericCrudTable/models/field.model';
import {
    thesisService,
    professorService,
    keywordService,
    scholarYearService,
} from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';
import { useRouteHandler } from 'src/hooks/routeHandler';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'thesisHandler',
    props: ['idC', 'Cname'],
    emits: [],
    setup(props, { emit }) {
        const { handleRoute } = useRouteHandler();
        const config = ref<GenericCrudTableConfig>({
            name: 'Tesis',
            singularLabel: 'Tesis',
            searchLabel: 'Título',
            service: thesisService,
            defaultValues: {
                ...(props.idC ? { scholar_year_id: props.idC } : {}),
            },
            query: {
                ...(props.idC ? { scholar_year: props.idC } : {}),
            },
            fields: [
                ...(props.idC
                    ? []
                    : ([
                          {
                              name: 'scholar_year',
                              label: 'Curso Escolar',
                              column: {
                                  transform(row) {
                                      return `${row.scholar_year.name}`;
                                  },
                              },
                              filter: true,
                              type: 'select',
                              selectOptions: {
                                  list: scholarYearService.list,
                                  value: 'id',
                                  label: 'name',
                              },
                              rules: ['required'],
                          },
                      ] as FieldModel[])),
                {
                    name: 'student',
                    label: 'Estudiante',
                    type: 'text',
                    form: {
                        responsiveOptions: {
                            md: 12,
                        },
                    },
                    rules: ['required'],
                },
                {
                    name: 'title',
                    label: 'Título',
                    column: {
                        transform(row) {
                            return `${row.title}`;
                        },
                        maxLength: 20,
                    },
                    type: 'text',
                    form: {
                        responsiveOptions: {
                            md: 12,
                        },
                    },
                    rules: ['required'],
                },
                {
                    name: 'tutor',
                    label: 'Tutor',
                    column: {
                        transform(row) {
                            return `${
                                row.tutor.name + ' ' + row.tutor.last_name
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
                    name: 'cotutors',
                    label: 'Cotutor(es)',
                    column: {
                        transform(row) {
                            var result = '';
                            row.cotutors.forEach((tutor: any) => {
                                result +=
                                    tutor.name + ' ' + tutor.last_name + '<br>';
                            });
                            return `${result.slice(0, -2)}`;
                        },
                    },
                    filter: true,
                    type: 'select',
                    selectOptions: {
                        list: professorService.list,
                        value: 'id',
                        label: 'name',
                        multiple: true,
                        refactorValue: (value) =>
                            value
                                ? `${value.name + ' ' + value.last_name}`
                                : '',
                    },
                },
                {
                    name: 'keywords',
                    label: 'Palabras Claves',
                    column: {
                        transform(row) {
                            var result = '';
                            row.keywords.forEach((keyword: any) => {
                                result += keyword.name + '<br>';
                            });
                            return `${result.slice(0, -2)}`;
                        },
                    },
                    filter: true,
                    type: 'select',
                    selectOptions: {
                        list: keywordService.list,
                        value: 'id',
                        label: 'name',
                        multiple: true,
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
        return {
            config,
            handleRoute,
        };
    },
});
</script>
