<template>
    <div class="full-width">
        <slot name="header-table" />
        <q-table
            :title="config.name"
            :loading="loading"
            :rows="rows"
            :columns="columns"
            :grid="$q.screen.lt.md"
            table-header-class="bg-secondary text-white"
            row-key="id"
            v-model:pagination="pagination"
            @request="onRequest"
            :filter="filter"
            :loading-label="'Cargando ...'"
            :rows-per-page-label="'Filas'"
            :no-data-label="'No hay datos'"
            :no-results-label="'No hay resultados'"
            :pagination-label="(a, b, c) => `${a}-${b} ${'de'} ${c}`"
            :rows-per-page-options="[]"
        >
            <!-- add new row btn  and search bar-->
            <template v-slot:top>
                <q-btn
                    v-if="actions && actions.create"
                    color="primary"
                    icon="add"
                    round
                    class="q-mr-sm"
                    no-caps
                    @click="prepareCreate"
                />
                <q-separator
                    vertical
                    color="secondary"
                    size="2px"
                    class="q-mr-sm"
                />
                <slot name="g-table-name">
                    <p
                        class="text-h6 text-primary text-weight-bolder q-mb-none"
                    >
                        {{ config.name }}
                    </p>
                </slot>

                <slot name="g-table-left-actions" />

                <q-space />

                <slot name="g-table-right-actions" />

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
                        @click="prepareEdit(props.row)"
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
        <q-dialog
            v-model="crudDialog"
            persistent
            transition-show="scale"
            transition-hide="scale"
        >
            <generic-form-handler
                :title="config.singularLabel"
                :editeItem="editeItem"
                :fields="config.fields"
                :edit="!!editeItem.id"
                @cancel="crudDialog = false"
                @crudAction="!editeItem.id ? onCreate() : onEdit(editeItem)"
            >
            </generic-form-handler>
        </q-dialog>
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import { GenericCrudTableConfig } from '../models/table.model';
import { useGenericDataTable } from '../hooks/table.hooks';
import { useCrud } from '../hooks/crud.hooks';
import { config } from 'process';
import GenericFormHandler from './GenericFormHandler.vue';
export default defineComponent({
    components: { GenericFormHandler },
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
        } = useGenericDataTable(props.config);

        const {
            crudLoading,
            crudDialog,
            editeItem,
            prepareEdit,
            prepareCreate,
        } = useCrud(props.config);

        load();

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

            crudLoading,

            crudDialog,
            editeItem,
            prepareEdit,
            prepareCreate,
        };
    },
});
</script>
