<template>
    <div class="full-width">
        <q-select
            outlined
            :label="field.label || field.name"
            :multiple="field.selectOptions.multiple"
            :use-chips="field.selectOptions.multiple"
            color="primary"
            hide-bottom-space
            :rules="rules"
            :loading="loading"
            :options="options"
            :option-value="field.selectOptions.value"
            :option-label="field.selectOptions.label"
            @update:model-value="$emit('onChangekey', $event)"
            :model-value="editeItem[field.name]"
        >
            <template v-slot:prepend>
                <q-icon size="sm" name="edit" />
            </template>
        </q-select>

        <!-- {{ field.selectOptions }} -->
    </div>
</template>

<script lang="ts">
import { FieldModel, FieldSelect } from '../../models/field.model';
import { defineComponent, PropType, ref } from 'vue';
import { Dictionary } from 'src/models/base';

export default defineComponent({
    emits: ['onChangekey'],
    props: {
        field: {
            type: Object as PropType<FieldSelect>,
            required: true,
        },
        editeItem: {
            type: Object,
        },
        rules: {
            type: Array,
        },
    },
    setup(props) {
        const options = ref([] as any[]);
        const loading = ref(true);

        props.field.selectOptions.list().then((r) => {
            options.value = r.data.results;
            setTimeout(() => {
                loading.value = false;
            }, 1000);
        });
        return {
            options,
            loading,
        };
    },
});
</script>
