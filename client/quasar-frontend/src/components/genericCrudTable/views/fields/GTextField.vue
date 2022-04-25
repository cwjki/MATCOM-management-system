<template>
    <div class="full-width">
        <q-input
            outlined
            :label="field.label || field.name"
            color="primary"
            hide-bottom-space
            :rules="rules"
            @update:model-value="$emit('onChangekey', $event)"
            :model-value="editeItem[field.name]"
        >
            <template v-slot:prepend>
                <q-icon size="sm" name="edit" />
            </template>
        </q-input>
    </div>
</template>

<script lang="ts">
import { FieldModel } from '../../models/field.model';
import { defineComponent, PropType } from 'vue';

export default defineComponent({
    emits: ['onChangekey'],
    props: {
        field: {
            type: Object as PropType<FieldModel>,
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
        return {};
    },
});
</script>
