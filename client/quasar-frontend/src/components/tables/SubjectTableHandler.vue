<template>
    <generic-crud-data-table :config="config" />
</template>

<script lang="ts">
import { subjectService } from 'src/services';
import { defineComponent, ref } from 'vue';
import { GenericCrudTableConfig } from '../genericCrudTable/models/table.model';
import GenericCrudDataTable from '../genericCrudTable/views/GenericCrudDataTable.vue';

export default defineComponent({
    components: { GenericCrudDataTable },
    name: 'subjectHandler',
    props: {},
    emits: [],
    setup(props, { emit }) {
        const config = ref<GenericCrudTableConfig>({
            name: 'Asignaturas',
            singularLabel: 'Asignatura',
            service: subjectService,
            fields: [
                {
                    name: 'name',
                    label: 'Nombre',
                },
                {
                    name: 'studyPlan',
                    label: 'Plan de Estudio',
                },
                {
                    name: 'career',
                    label: 'Carrera',
                },
                {
                    name: 'department',
                    label: 'Departamento',
                },
                {
                    name: 'semester',
                    label: 'Semestre',
                },
                {
                    name: 'numberOfHours',
                    label: 'Horas',
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
