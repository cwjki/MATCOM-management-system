import { quasarColumn } from 'src/models/base';
import { api } from 'boot/axios';
import { ref } from 'vue';

export const departmentTable = () => {
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
            name: 'career',
            label: 'Carrera',
            field: 'career',
            sortable: true,
        },
    ]);
    const rows = ref<any[]>([]);
    const loading = ref(true);

    api.get('http://127.0.0.1:8000/departments/').then((response) => {
        for (let department of response.data.results) {
            rows.value.push({
                name: department.name,
                career: department.career,
            });
        }
    });

    return {
        columns,
        loading,
        rows,
    };
};
