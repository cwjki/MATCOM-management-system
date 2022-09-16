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
            service: thesisService,
            fields: [
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
                    name: 'tutor',
                    label: 'Tutor',
                    column: {
                        transform(row) {
                            return `${
                                row.tutor.name + ' ' + row.tutor.last_name
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
                    name: 'cotutors',
                    label: 'Cotutor(es)',
                    column: {
                        transform(row) {
                            var result = '';
                            row.cotutors.forEach((tutor: any) => {
                                result +=
                                    tutor.name + ' ' + tutor.last_name + ', ';
                            });
                            return `${result}`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: professorService.list,
                        value: 'id',
                        label: 'name',
                        multiple: true,
                    },
                    rules: ['required'],
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
                            return `${result}`;
                        },
                    },
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
