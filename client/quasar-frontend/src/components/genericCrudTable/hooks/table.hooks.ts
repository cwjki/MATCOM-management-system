import { Dictionary } from 'src/models/base';
import { ref } from 'vue';
import { GenericCrudTableConfig } from '../models/table.model';
import { transformQuasarColumn } from './utils.hooks';

export const useGenericDataTable = (config: GenericCrudTableConfig) => {
    const loading = ref(false);
    const rows = ref<any[]>([]);
    const actions = ref(config.actions || {});
    const isActionOnTable = !!(actions.value.delete || actions.value.update);
    const columns = ref(transformQuasarColumn(config.fields, isActionOnTable));
    const error = ref('');

    const load = (query: Dictionary) => {
        loading.value = true;
        config.service
            .list(query)
            .then((response) => {
                loading.value = false;
                rows.value = response.data.results;
            })
            .catch((error) => {
                loading.value = false;
                error.value = 'Error en loading';
            });
    };

    const onCreate = () => {
        alert('creating');
    };

    const onEdit = (row: Dictionary) => {
        alert('editing' + row.id);
    };

    const onDelete = (row: Dictionary) => {
        alert('deleting: ' + row.id);
        config.service
            .delete(row.id)
            .then((response) => {
                // todo put this event on event hooks
                load({});
            })
            .catch((error) => {
                error.value = 'Error en delete';
            });
    };

    return {
        loading,
        rows,
        columns,
        error,
        actions,
        isActionOnTable,
        load,
        onCreate,
        onEdit,
        onDelete,
    };
};
