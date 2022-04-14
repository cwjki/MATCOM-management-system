import { quasarColumn } from 'src/models/base';
import { api } from 'boot/axios';
import { ref } from 'vue';
import { subjectService } from 'src/services';
import { SubjectModel } from 'src/models/subject.model';

export const subjectTable = () => {
    const columns = ref<quasarColumn[]>([
        {
            name: 'name',
            label: 'Nombre',
            field: 'name',
            required: true,
            align: 'center',
            sortable: true,
        },
        {
            name: 'department',
            label: 'Departamento',
            field: 'department',
            sortable: true,
        },
        {
            name: 'career',
            label: 'Carrera',
            field: 'career',
            sortable: true,
        },
        {
            name: 'studyPlan',
            label: 'Plan de Estudio',
            field: 'studyPlan',
            sortable: true,
        },
        {
            name: 'semester',
            label: 'Semestre',
            field: 'semester',
            sortable: true,
        },
        {
            name: 'numberOfHours',
            label: 'Horas',
            field: 'numberOfHours',
            sortable: true,
        },
    ]);
    const rows = ref<SubjectModel[]>([]);
    const loading = ref(true);

    subjectService.list().then((response) => {
        rows.value = response.data.results;
    });

    return {
        columns,
        loading,
        rows,
    };
};
