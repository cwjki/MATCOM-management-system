<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { thesisService, professorService, studentService } from 'src/services';
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
                    column: {
                        transform(row) {
                            return `${
                                row.student.name + ' ' + row.student.last_name
                            }`;
                        },
                    },
                    type: 'select',
                    selectOptions: {
                        list: studentService.list,
                        value: 'id',
                        label: 'name',
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
                    name: 'cotutor',
                    label: 'Cotutor',
                    column: {
                        transform(row) {
                            return `${
                                row.cotutor.name + ' ' + row.cotutor.last_name
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
