import { quasarColumn } from 'src/models/base';
import { api } from 'boot/axios';
import { ref } from 'vue';
import { CareerModel } from 'src/models/career.model';
import { careerService } from 'src/services';

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
    const rows = ref<CareerModel[]>([]);
    const loading = ref(true);

    careerService.list().then((response) => {
        rows.value = response.data.results;
    });

    return {
        columns,
        loading,
        rows,
    };
};
