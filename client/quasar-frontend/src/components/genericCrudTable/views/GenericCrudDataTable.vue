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
            :rows-per-page-options="[10, 15, 25, 50, 100]"
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
                <q-btn
                    v-for="(item, i) in external"
                    :key="`btn-${i}`"
                    :color="item.color"
                    :icon="item.icon"
                    round
                    class="q-mr-sm"
                    no-caps
                    @click="item.func()"
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

                <q-select
                    v-model="filterObj[f.name]"
                    @update:model-value="onChangeFilter"
                    v-for="(f, i) in fieldToFilter"
                    :label="f.label"
                    dense
                    :options="filterOptions[f.name] || []"
                    :option-value="f.field.selectOptions.value"
                    :option-label="
                        f.field.selectOptions.refactorValue ||
                        f.field.selectOptions.label
                    "
                    emit-value
                    :readonly="!filterOptions[f.name]"
                    :key="`f-${i}`"
                    :class="`q-ml-md ${$q.screen.xs && 'q-mt-sm'}`"
                    map-options
                    use-chips
                    debounce="300"
                    outlined
                    borderless
                    style="width: 170px !important"
                >
                    <template v-slot:append>
                        <q-icon name="search" />
                    </template>
                </q-select>

                <q-input
                    v-model="filter"
                    :placeholder="config.searchLabel"
                    dense
                    :class="`q-ml-md ${$q.screen.xs && 'q-mt-sm'}`"
                    debounce="300"
                    style="width: 170px !important"
                    outlined
                    borderless
                >
                    <template v-slot:append>
                        <q-icon name="search" />
                    </template>
                </q-input>
            </template>

            <!-- redefine how show the columns -->
            <template v-slot:body-cell="props">
                <q-td :props="props">
                    <slot :name="'column-' + props.col.name" :value="props.row">
                        <q-toggle
                            dense
                            checked-icon="check"
                            disable
                            v-if="
                                mappedFieldDef[props.col.name] &&
                                mappedFieldDef[props.col.name].type == 'bool'
                            "
                            :label="''"
                            v-model="props.value"
                        />
                        <p
                            class="q-mb-none"
                            v-else-if="
                                mappedField[props.col.name] &&
                                mappedField[props.col.name].maxLength
                            "
                        >
                            {{
                                `${props.value.substr(
                                    0,
                                    mappedField[props.col.name].maxLength
                                )}${
                                    (mappedField[props.col.name].maxLength ||
                                        0) < props.value.length
                                        ? '...'
                                        : ''
                                }`
                            }}
                            <q-tooltip> {{ props.value }} </q-tooltip>
                        </p>
                        <p class="q-mb-none" v-else v-html="props.value"></p>
                    </slot>
                </q-td>
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

            <template v-slot:item="props">
                <div
                    class="q-pa-xs col-xs-12 col-sm-6 col-md-4 col-lg-3 grid-style-transition"
                    :style="props.selected ? 'transform: scale(0.95);' : ''"
                >
                    <q-card :class="props.selected ? 'bg-grey-2' : ''">
                        <q-card-section
                            class="row q-pa-none"
                            :key="'csactions'"
                            v-if="isActionOnTable"
                        >
                            <!-- <p class="q-mb-none">Acciones</p> -->
                            <q-space />
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
                        </q-card-section>
                        <q-separator />
                        <q-list dense class="q-py-sm">
                            <q-item
                                v-for="col in props.cols.filter(
                                    (col) => col.name !== 'csactions'
                                )"
                                :key="col.name"
                            >
                                <slot
                                    :name="'table-column-' + col.name"
                                    :value="props.row"
                                >
                                    <q-item-section>
                                        <q-item-label>{{
                                            col.label
                                        }}</q-item-label>
                                    </q-item-section>
                                    <q-item-section>
                                        <q-toggle
                                            dense
                                            checked-icon="check"
                                            disable
                                            v-if="
                                                mappedFieldDef[col.name] &&
                                                mappedFieldDef[col.name].type ==
                                                    'bool'
                                            "
                                            :label="''"
                                            v-model="col.value"
                                        />
                                        <q-item-label
                                            class="q-mb-none"
                                            v-else-if="
                                                mappedField[col.name] &&
                                                mappedField[col.name].maxLength
                                            "
                                        >
                                            {{
                                                `${col.value.substr(
                                                    0,
                                                    mappedField[col.name]
                                                        .maxLength
                                                )}${
                                                    (mappedField[col.name]
                                                        .maxLength || 0) <
                                                    col.value.length
                                                        ? '...'
                                                        : ''
                                                }`
                                            }}
                                            <q-tooltip>
                                                {{ col.value }}
                                            </q-tooltip>
                                        </q-item-label>
                                        <q-item-label
                                            class="q-mb-none"
                                            v-else
                                            v-html="col.value"
                                        ></q-item-label>
                                    </q-item-section>
                                </slot>
                            </q-item>
                        </q-list>
                    </q-card>
                </div>
            </template>
        </q-table>
        <q-dialog
            v-model="crudDialog"
            persistent
            full-width
            transition-show="scale"
            transition-hide="scale"
        >
            <generic-form-handler
                :title="config.singularLabel"
                :loading="crudLoading"
                :editeItem="editeItem"
                :fields="config.fields"
                :edit="!!editeItem.id"
                @cancel="crudDialog = false"
                @onChangekey="changeKey"
                @crudAction="
                    !editeItem.id ? onCreate(editeItem) : onEdit(editeItem)
                "
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
import GenericFormHandler from './GenericFormHandler.vue';
import { useSerializer } from '../hooks/serializer.hooks';
import { Dictionary } from 'src/models/base';
import { Notify } from 'quasar';
export default defineComponent({
    components: { GenericFormHandler },
    emits: ['onRequest'],
    props: {
        config: {
            type: Object as PropType<GenericCrudTableConfig>,
            required: true,
        },
    },
    setup(props, { emit }) {
        const {
            loading,
            rows,
            columns,
            actions,
            isActionOnTable,
            pagination,
            external,

            filter,
            fieldToFilter,
            filterObj,
            filterOptions,
            onChangeFilter,

            load,
            onRequest,
            mappedField,
            mappedFieldDef,
        } = useGenericDataTable(props.config, emit);

        // emit('onRequest');

        const {
            crudLoading,
            crudDialog,
            editeItem,
            prepareEdit,
            prepareCreate,
            changeKey,
        } = useCrud(props.config);

        load();

        const uploadData = (row: Dictionary, edit: boolean) => {
            crudLoading.value = true;
            const payload = useSerializer(
                row,
                props.config.defaultValues || {},
                props.config.fields
            ).getPayload();
            const serviceMethods = edit
                ? props.config.service.update(row.id, payload)
                : props.config.service.create(payload);
            serviceMethods
                .then((r) => {
                    load();
                    setTimeout(() => {
                        const success_action = edit ? 'editó' : 'creó';
                        Notify.create({
                            type: 'positive',
                            message: `Se ${success_action} una instancia de '${props.config.singularLabel}' correctamente`,
                        });
                        crudLoading.value = false;
                        crudDialog.value = false;
                    }, 200);
                })
                .catch((e) => {
                    const fail_action = edit ? 'editar' : 'crear';
                    Notify.create({
                        type: 'negative',
                        message: `Error al ${fail_action} una instancia de  '${props.config.singularLabel}''`,
                    });
                    crudDialog.value = false;
                    crudLoading.value = false;
                });
        };

        const onCreate = (row: Dictionary) => {
            // alert('creating');
            uploadData(row, false);
        };

        const onEdit = (row: Dictionary) => {
            uploadData(row, true);
        };

        const onDelete = (row: Dictionary) => {
            // alert('deleting: ' + row.id);
            props.config.service
                .delete(row.id)
                .then((response) => {
                    // todo put this event on event hooks
                    setTimeout(() => {
                        Notify.create({
                            type: 'positive',
                            message: `Se eliminó una instancia de '${props.config.singularLabel}' correctamente`,
                        });
                        crudLoading.value = false;
                        crudDialog.value = false;
                    }, 200);
                    load();
                })
                .catch((error) => {
                    error.value = 'Error en delete';
                });
        };
        return {
            loading,
            rows,
            columns,
            actions,
            isActionOnTable,
            pagination,
            external,

            filter,
            fieldToFilter,
            filterObj,
            filterOptions,
            onChangeFilter,

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
            changeKey,
            mappedField,
            mappedFieldDef,
        };
    },
});
</script>
