<template>
    <q-card style="width: 70vw !important">
        <q-card-section
            class="bg-primary text-white q-pa-sm text-center full-width"
        >
            <div class="text-h6">
                {{ edit ? 'Editando ' : 'Creando ' }} {{ title }}
            </div>
        </q-card-section>

        <q-card-section class="q-pt-none">
            {{ fields }}
        </q-card-section>

        <q-card-section class="q-pt-none">
            {{ editeItem }}
        </q-card-section>

        <q-card-actions align="between" class="bg-white text-teal">
            <q-btn
                flat
                label="Cancel"
                no-caps
                @click="$emit('cancel')"
                color="secondary"
            />

            <q-btn
                :label="edit ? 'Editar' : 'Crear'"
                @click="onCrud"
                no-caps
                color="primary"
            />
        </q-card-actions>
    </q-card>
</template>

<script lang="ts">
import { FieldModel } from '../models/field.model';
import { defineComponent, PropType } from 'vue';

export default defineComponent({
    props: {
        fields: {
            type: Array as PropType<FieldModel[]>,
            required: true,
        },
        title: String,
        editeItem: {
            type: Object,
        },
        edit: {
            type: Boolean,
        },
    },
    emits: ['cancel', 'crudAction'],
    setup(props, { emit }) {
        return {
            onCrud() {
                /*
                    1: Validar el formulario
                    2: Reducir el editItem into a Payload
                    3: Emit crudAction con el Payload
                */
                alert('on Crud clicking');
                emit('crudAction');
            },
        };
    },
});
</script>
