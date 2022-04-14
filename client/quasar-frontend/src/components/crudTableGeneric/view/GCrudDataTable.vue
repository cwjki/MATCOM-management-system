<template>
    <q-table
        :title="config.name"
        :loading="loading"
        :rows="rows"
        :columns="columns"
        :grid="$q.screen.lt.md"
        v-model:pagination="pagination"
        :filter="filter"
        @request="onRequest"
        table-header-class="bg-secondary text-white"
        :loading-label="'Cargando ...'"
        :rows-per-page-label="'row'"
        :no-data-label="'No hay datos'"
        :no-results-label="'No hay resultados'"
        :pagination-label="(a, b, c) => `${a}-${b} ${'de'} ${c}`"
        :rows-per-page-options="[]"
        row-key="id"
    >
        <template v-slot:top-right v-if="actions && actions.create">
            <q-btn
                color="primary"
                icon-right="add"
                :label="'Crear ' + config.singularLabel"
                no-caps
                @click="onCreate"
            />
            <q-input
                borderless
                dense
                debounce="300"
                class="q-ml-md"
                outlined
                v-model="filter"
                placeholder="Search"
            >
                <template v-slot:append>
                    <q-icon name="search" />
                </template>
            </q-input>
        </template>
        <template v-slot:body-cell-csaction="props" v-if="isActionOnTable">
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
                    @click="onDelete(props.row)"
                    v-if="actions && actions.delete"
                />
            </q-td>
        </template>
    </q-table>
    <!-- <p></p> -->
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import { CrudTableConfig } from '../models/table.model';
import { useDataTable } from '../hooks/table.hooks';
export default defineComponent({
    props: {
        config: {
            type: Object as PropType<CrudTableConfig>,
            required: true,
        },
    },
    setup(props) {
        const {
            columns,
            loading,
            rows,
            actions,
            isActionOnTable,
            filter,
            pagination,
            onDelete,
            onCreate,
            onEdit,
            onRequest,
            load,
        } = useDataTable(props.config);

        load();

        return {
            columns,
            filter,
            pagination,
            loading,
            rows,
            isActionOnTable,
            actions,
            load,
            onDelete,
            onCreate,
            onEdit,
            onRequest,
        };
    },
});
</script>
