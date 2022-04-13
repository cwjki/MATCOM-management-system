import { quasarColumn } from 'src/models/base';
import { api } from 'boot/axios';
import { ref } from 'vue';

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
    const rows = ref<any[]>([]);
    const loading = ref(true);

    api.get('http://127.0.0.1:8000/subjects/').then((response) => {
        for (let subject of response.data.results) {
            rows.value.push({
                name: subject.name,
                department: subject.department,
                career: subject.career,
                studyPlan: subject.studyPlan,
                semester: subject.semester,
                numberOfHours: subject.numberOfHours,
            });
        }
    });

    return {
        columns,
        loading,
        rows,
    };
};
