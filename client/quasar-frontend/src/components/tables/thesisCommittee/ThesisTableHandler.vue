<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { thesisService, professorService, keywordService } from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'thesisHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Tesis',
            singularLabel: 'Tesis',
            searchLabel: 'Título',
            service: thesisService,
            fields: [
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
                                    tutor.name + ' ' + tutor.last_name + ', ';
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
                                result += keyword.name + ', ';
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
        return { config };
    },
});
</script>
