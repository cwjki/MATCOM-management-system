import { Dictionary } from 'src/models/base';
import { ref } from 'vue';
import { CrudTableConfig } from '../models/table.model';
import { transformQuasarColumn } from './utils.hooks';

export const useDataTable = (config: CrudTableConfig) => {
    const loading = ref(false);
    const rows = ref<any[]>([]);
    const actions = ref(config.actions || {});
    const isActionOnTable = !!(actions.value.delete || actions.value.update);
    const columns = ref(transformQuasarColumn(config.fields, isActionOnTable));

    const filter = ref('');
    const pagination = ref({
        descending: false,
        page: 1,
        rowsPerPage: 10,
        rowsNumber: 10,
        sortBy: '',
    });

    const load = (query: Dictionary) => {
        loading.value = true;
        config.service
            .list(query)
            .then((r) => {
                loading.value = false;
                rows.value = r.data.results;
                pagination.value.rowsNumber = r.data.count;
            })
            .catch((e) => {
                loading.value = false;
                error.value = 'Error en el servidor';
            });
    };
    const onRequest = (request: {
        filter: string;
        pagination: {
            descending: boolean;
            page: number;
            rowsNumber: number;
            rowsPerPage: number;
            sortBy: string;
        };
    }) => {
        console.log(request);
        pagination.value = request.pagination;
        load({
            size: request.pagination.rowsPerPage,
            page: request.pagination.page,
            search: request.filter,
        });
    };
    const error = ref('');
    return {
        loading,
        filter,
        pagination,
        rows,
        columns,
        error,
        actions,
        isActionOnTable,
        load: () => {
            onRequest({
                filter: filter.value,
                pagination: pagination.value,
            });
        },
        onDelete(row: Dictionary): Promise<void> {
            alert('deleting: ' + row.id);
            return config.service.delete(row.id).then((r) => {
                // todo put this event on event hooks
                onRequest({
                    filter: filter.value,
                    pagination: pagination.value,
                });
            });
        },
        onCreate() {
            alert('creating');
        },
        onEdit(row: Dictionary) {
            console.log(row);
            alert('editing: ' + row.id);
        },
        onRequest,
    };
};
