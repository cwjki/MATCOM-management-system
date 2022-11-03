import { Notify } from 'quasar';
import { Dictionary } from 'src/models/base';
import { computed, ref } from 'vue';
import { FieldSelect } from '../models/field.model';
import { GenericCrudTableConfig, RequestModel } from '../models/table.model';
import { useSerializer } from './serializer.hooks';
import { transformQuasarColumn } from './utils.hooks';

export const useGenericDataTable = (
    config: GenericCrudTableConfig,
    emit: (x: any) => any
) => {
    const loading = ref(false);
    const rows = ref<any[]>([]);
    const actions = ref(config.actions || {});
    const external = computed(() => config.actions?.external || []);
    const isActionOnTable = !!(actions.value.delete || actions.value.update);
    const columns = ref(transformQuasarColumn(config.fields, isActionOnTable));
    const error = ref('');
    const filter = ref('');

    const filterOptions = ref<Dictionary>({});
    const filterObj = ref<Dictionary>({});

    const fieldToFilter = config.fields
        .filter((x) => x.filter && x.type === 'select')
        .map((y) => {
            return {
                field: y as FieldSelect,
                name: y.name,
                label: y.label,
            };
        });

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

    const onRelaodedFilter = () => {
        const query = {
            ...filterObj.value,
        };
        fieldToFilter.map((x) => {
            if (x.field) {
                x.field.selectOptions.list(query).then((r) => {
                    filterOptions.value[x.name] = r.data.results;
                });
            }
        });
    };

    const onChangeFilter = () => {
        onRequest({
            filter: filter.value,
            pagination: {
                sortBy: '',
                descending: false,
                page: 1,
                rowsPerPage: 10,
                rowsNumber: 10,
            },
        });
    };

    const onRequest = (request: RequestModel) => {
        emit('onRequest');
        loading.value = true;
        pagination.value = request.pagination;

        const query = {
            size: request.pagination.rowsPerPage,
            page: request.pagination.page,
            search: request.filter,
            ...(pagination.value.sortBy
                ? {
                      ordering: `${pagination.value.descending ? '-' : ''}${
                          pagination.value.sortBy
                      }`,
                  }
                : {}),
            ...filterObj.value,
        };

        onRelaodedFilter();

        config.service
            .list(query)
            .then((response) => {
                loading.value = false;
                rows.value = response.data.results;
                pagination.value.rowsNumber = response.data.count;
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
        external,

        fieldToFilter,
        filterObj,
        filterOptions,
        onChangeFilter,

        load,
        onRequest,
    };
};
