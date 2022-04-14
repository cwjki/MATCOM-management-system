import { quasarColumn } from 'src/models/base';
import { api } from 'boot/axios';
import { ref } from 'vue';
import { professorService } from 'src/services';
import { ProfessorModel } from 'src/models/professor.model';
export const professorTable = () => {
    const columns = ref<quasarColumn[]>([
        {
            name: 'name',
            required: true,
            label: 'Nombre',
            align: 'center',
            field: (row: any) => row.name,
            sortable: true,
        },
        {
            name: 'lastName',
            label: 'Apellidos',
            field: 'lastName',
            sortable: true,
        },
        {
            name: 'department',
            label: 'Departamento',
            field: 'department',
            sortable: true,
        },
        {
            name: 'scientificDegree',
            label: 'Grado Científico',
            field: 'scientificDegree',
        },
        {
            name: 'teachingCategory',
            label: 'Categoría Docente',
            field: 'teachingCategory',
        },
    ]);
    const rows = ref<ProfessorModel[]>([]);
    const loading = ref(true);
    professorService.list().then((response) => {
        rows.value = response.data.results;
    });
    // api.get('http://127.0.0.1:8000/professors/').then((response) => {
    //     for (let professor of response.data.results) {
    //         rows.value.push({
    //             name: professor.name,
    //             lastName: professor.lastName,
    //             department: professor.department,
    //             scientificDegree: professor.scientificDegree,
    //             teachingCategory: professor.teachingCategory,
    //         });
    //     }
    // });

    return {
        columns,
        loading,
        rows,
    };
};
