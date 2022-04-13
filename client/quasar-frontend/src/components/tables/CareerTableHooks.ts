import { quasarColumn } from 'src/models/base';
import { api } from 'boot/axios';
import { ref } from 'vue';

export const careerTable = () => {
    const columns = ref<quasarColumn[]>([
        {
            name: 'name',
            required: true,
            label: 'Nombre',
            align: 'center',
            field: (row: any) => row.name,
            sortable: true,
        },
    ]);
    const rows = ref<any[]>([]);
    const loading = ref(true);

    api.get('http://127.0.0.1:8000/careers/').then((response) => {
        for (let career of response.data.results) {
            rows.value.push({
                name: career.name
            });
        }
    });

    return {
        columns,
        loading,
        rows,
    };
};
