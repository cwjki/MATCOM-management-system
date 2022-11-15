<template>
    <div class="full-width">
        <!-- <q-input
            outlined
            :v-model="field.type"
            :type="field.type"
            :label="field.label || field.name"
            :stack-label="true"
            color="primary"
            hide-bottom-space
            :rules="rules"
            @update:model-value="$emit('onChangekey', $event)"
            :model-value="editeItem[field.name]"
        >
            <template v-slot:prepend>
                <q-icon size="sm" name="edit" />
            </template>
        </q-input> -->
        <q-toggle
            :label="field.label || field.name"
            @update:model-value="$emit('onChangekey', $event)"
            :model-value="editeItem[field.name]"
            :rules="rules"
        />
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
