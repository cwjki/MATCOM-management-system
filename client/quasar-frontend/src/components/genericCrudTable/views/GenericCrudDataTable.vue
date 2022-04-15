<template>
    <q-table
        :title="config.name"
        :loading="loading"
        :rows="rows"
        :columns="columns"
        :grid="$q.screen.lt.md"
        table-header-class="bg-secondary text-white"
        row-key="id"
        v-model:pagination="pagination"
        @request="onRequest1"
        :filter="filter"
    >
        <!-- add new row btn  and search bar-->
        <template v-slot:top-right v-if="actions && actions.create">
            <q-btn
                color="primary"
                icon-right="add"
                :label="'Crear ' + config.singularLabel"
                no-caps
                @click="onCreate"
            />
            <q-input
                v-model="filter"
                placeholder="Search"
                dense
                class="q-ml-md"
                debounce="300"
                outlined
                borderless
            >
                <template v-slot:append>
                    <q-icon name="search" />
                </template>
            </q-input>
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
                    @click="onDelete(props.row)"
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
            pagination,
            filter,

            load,
            onRequest,
            onCreate,
            onEdit,
            onDelete,

            load1,
            onRequest1,
        } = useGenericDataTable(props.config);

        load1();

        return {
            loading,
            rows,
            columns,
            actions,
            isActionOnTable,
            pagination,
            filter,

            load,
            onRequest,
            onCreate,
            onEdit,
            onDelete,

            load1,
            onRequest1,
        };
    },
});
</script>
