import { quasarColumn } from 'src/models/base';
import { ref } from 'vue';
import { DepartmentModel } from 'src/models/department.model';
import { departmentService } from 'src/services';

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
    const rows = ref<DepartmentModel[]>([]);
    const loading = ref(true);

    departmentService.list().then((response) => {
        rows.value = response.data.results;
    });

    return {
        columns,
        loading,
        rows,
    };
};
