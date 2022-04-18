import { Notify } from 'quasar';
import { Dictionary } from 'src/models/base';
import { ref } from 'vue';
import { GenericCrudTableConfig, RequestModel } from '../models/table.model';
import { useSerializer } from './serializer.hooks';
import { transformQuasarColumn } from './utils.hooks';

export const useGenericDataTable = (config: GenericCrudTableConfig) => {
    const loading = ref(false);
    const rows = ref<any[]>([]);
    const actions = ref(config.actions || {});
    const isActionOnTable = !!(actions.value.delete || actions.value.update);
    const columns = ref(transformQuasarColumn(config.fields, isActionOnTable));
    const error = ref('');
    const filter = ref('');
    const pagination = ref({
        sortBy: '',
        descending: false,
        page: 1,
        rowsPerPage: 10,
        rowsNumber: 10,
    });

    const load = () => {
        onRequest({
            filter: filter.value,
            pagination: pagination.value,
        });
    };

    const onRequest = (request: RequestModel) => {
        loading.value = true;
        pagination.value = request.pagination;

        const query = {
            size: request.pagination.rowsPerPage,
            page: request.pagination.page,
            search: request.filter,
        };

        config.service
            .list(query)
            .then((response) => {
                loading.value = false;
                rows.value = response.data.results;
                pagination.value.rowsNumber = response.data.count;
                console.log(pagination);
            })
            .catch((error) => {
                loading.value = false;
                error.value = 'Error en loading';
            });
    };

    return {
        loading,
        rows,
        columns,
        error,
        actions,
        isActionOnTable,
        pagination,
        filter,

        load,
        onRequest,
    };
};
