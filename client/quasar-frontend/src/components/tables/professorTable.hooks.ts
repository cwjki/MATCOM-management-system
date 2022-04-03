import { quasarColumn } from 'src/models/base';
import { api } from 'boot/axios';
import { ref } from 'vue';

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

    const rows = ref<any[]>([]);
    const loading = ref(true);
    api.get('http://127.0.0.1:8000/professors/').then((response) => {
        console.log(response.data);
    });
    setTimeout(() => {
        loading.value = false;
        rows.value = [{}];
    }, 5000);

    return {
        columns,
        loading,
        rows,
    };
};
