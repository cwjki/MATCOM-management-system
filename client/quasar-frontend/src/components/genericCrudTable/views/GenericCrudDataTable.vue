<template>
    <q-table
        :title="config.name"
        :loading="loading"
        :rows="rows"
        :columns="columns"
        :grid="$q.screen.lt.md"
        table-header-class="bg-secondary text-white"
        row-key="id"
    >
        <!-- add new row btn -->
        <template v-slot:top-right v-if="actions && actions.create">
            <q-btn
                color="primary"
                icon-right="add"
                :label="'Crear ' + config.singularLabel"
                no-caps
                @click="onCreate"
            />
        </template>

        <!-- edit and delete btns -->
        <template v-slot:body-cell-csactions="props" v-if="isActionOnTable">
            <q-td :props="props">
                <q-btn
                    icon="edit"
                    color="warning"
                    round
                    flat
                    @click="onEdit(props.row)"
                    v-if="actions && actions.update"
                />
                <q-btn
                    icon="delete"
                    color="red"
                    round
                    flat
                    @click="onEdit(props.row)"
                    v-if="actions && actions.delete"
                />
            </q-td>
        </template>
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
