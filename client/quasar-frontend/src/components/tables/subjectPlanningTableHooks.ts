import { quasarColumn } from 'src/models/base';
import { api } from 'boot/axios';
import { ref } from 'vue';
import { SubjectDescriptionModel } from 'src/models/subjectDescription.model';
import { subjectDescriptionService } from 'src/services';

export const subjectPlanningTable = () => {
    const columns = ref<quasarColumn[]>([
        {
            name: 'subject',
            label: 'Asignatura',
            field: 'subject',
            required: true,
            align: 'center',
            sortable: true,
        },
        {
            name: 'classType',
            label: 'Actividad de Clase',
            field: 'classType',
            sortable: true,
        },
        {
            name: 'numberOfGroups',
            label: 'Grupos',
            field: 'numberOfGroups',
            sortable: true,
        },
        {
            name: 'numberOfHours',
            label: 'Horas',
            field: 'numberOfHours',
            sortable: true,
        },
        {
            name: 'timePeriod',
            label: 'Período de Tiempo',
            field: 'timePeriod',
            sortable: true,
        },
    ]);
    const rows = ref<SubjectDescriptionModel[]>([]);
    const loading = ref(true);

    subjectDescriptionService.list().then((response) => {
        rows.value = response.data.results;
    });

    return {
        columns,
        loading,
        rows,
    };
};
