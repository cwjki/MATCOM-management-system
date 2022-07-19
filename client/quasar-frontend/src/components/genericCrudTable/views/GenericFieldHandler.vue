<template>
    <div class="full-width">
        <g-select-field
            :editeItem="editeItem"
            :field="field"
            v-if="field.type === 'select'"
            :rules="getRulesFromField(field)"
            @onChangekey="$emit('onChangekey', $event)"
        />
        <g-text-field
            :editeItem="editeItem"
            :field="field"
            v-else-if="field.type === 'text' || field.type === 'date'"
            :rules="getRulesFromField(field)"
            @onChangekey="$emit('onChangekey', $event)"
        />
    </div>
</template>

<script lang="ts">
import { FieldModel } from '../models/field.model';
import { defineComponent, PropType } from 'vue';
import { Dictionary } from 'src/models/base';
import GTextField from './fields/GTextField.vue';
import GSelectField from './fields/GSelectField.vue';

export default defineComponent({
    components: { GTextField, GSelectField },
    emits: ['onChangekey'],
    props: {
        field: {
            type: Object as PropType<FieldModel>,
            required: true,
        },
        editeItem: {
            type: Object,
        },
    },
    setup(props) {
        return {
            getRulesFromField(field: FieldModel) {
                const rules: Dictionary = {
                    required: (x: any) => !!x || 'Este campo es requerido',
                };
                if (field.rules) {
                    return field.rules.map((key) => rules[key]);
                }
                return [];
            },
        };
    },
});
</script>
