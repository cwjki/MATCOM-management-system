import { quasarColumn } from 'src/models/base';
import { api } from 'boot/axios';
import { ref } from 'vue';

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
    const rows = ref<any[]>([]);
    const loading = ref(true);

    api.get('http://127.0.0.1:8000/teaching-plannings/').then((response) => {
        for (let subject of response.data.results) {
            rows.value.push({
                subject: subject.subject,
                classType: subject.classType,
                numberOfGroups: subject.numberOfGroups,
                numberOfHours: subject.numberOfHours,
                timePeriod: subject.timePeriod,
            });
        }
    });

    return {
        columns,
        loading,
        rows,
    };
};
