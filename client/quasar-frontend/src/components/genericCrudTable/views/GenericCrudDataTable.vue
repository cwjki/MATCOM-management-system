<template>
    <q-table
        :title="config.name"
        :loading="loading"
        :rows="rows"
        :columns="columns"
    >
    </q-table>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import { GenericCrudTableConfig } from '../models/table.model';
import { useGenericDataTable } from '../hooks/table.hooks';

export default defineComponent({
    props: {
        config: {
            type: Object as PropType<GenericCrudTableConfig>,
            required: true,
        },
    },
    setup(props) {
        const {
            loading,
            rows,
            columns,
            actions,
            isActionOnTable,
            load,
            onCreate,
            onEdit,
            onDelete,
        } = useGenericDataTable(props.config);

        load({});

        return {
            loading,
            rows,
            columns,
            actions,
            isActionOnTable,
            load,
            onCreate,
            onEdit,
            onDelete,
        };
    },
});
</script>
