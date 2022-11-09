<template>
    <q-card style="width: 70vw !important" class="row justify-center">
        <q-card-section
            class="bg-primary text-white q-pa-sm text-center full-width"
        >
            <div class="text-h6">
                {{ edit ? 'Editando ' : 'Creando ' }} {{ title }}
            </div>
        </q-card-section>
        <q-linear-progress
            dark
            rounded
            indeterminate
            color="secondary"
            v-if="loading"
        />

        <q-form class="full-width row justify-center" autofocus ref="myform">
            <q-card-section
                v-for="(field, i) in fields.filter((x) => !!x.type)"
                :class="`q-pa-sm q-pb-none ${getResponsive(field)}`"
                :key="i"
            >
                <generic-field-handler
                    :field="field"
                    :editeItem="editeItem"
                    @onChangekey="$emit('onChangekey', field.name, $event)"
                />
            </q-card-section>
        </q-form>

        <q-separator class="full-width" inset />
        <!-- {{ editeItem }} -->
        <q-card-actions align="between" class="bg-white text-teal full-width">
            <q-btn
                outline
                label="Cancelar"
                no-caps
                @click="$emit('cancel')"
                class="col-md-4 col-lg-3 col-5"
                color="secondary"
            />

            <q-btn
                :label="edit ? 'Editar' : 'Crear'"
                @click="onCrud"
                class="col-md-4 col-lg-3 col-5"
                no-caps
                color="primary"
            />
        </q-card-actions>
    </q-card>
</template>

<script lang="ts">
import { FieldModel } from '../models/field.model';
import { defineComponent, PropType, ref } from 'vue';
import { Dictionary } from 'src/models/base';
import GenericFieldHandler from './GenericFieldHandler.vue';

export default defineComponent({
    components: { GenericFieldHandler },
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
        loading: Boolean,
    },
    emits: ['cancel', 'crudAction', 'onChangekey'],
    setup(props, { emit }) {
        const myform = ref(null as any);
        return {
            myform,
            onCrud() {
                /*
                    * 1: Validar el formulario
                    2: Reducir el editItem into a Payload
                    *3: Emit crudAction con el Payload
                */
                myform.value.validate().then((success: boolean) => {
                    if (success) {
                        const payload = { ...props.editeItem };
                        emit('crudAction', payload);
                    } else {
                    }
                });
            },

            getResponsive(field: FieldModel) {
                if (field.form && field.form.responsiveOptions) {
                    let s = '';
                    const obj =
                        field.form &&
                        (field.form.responsiveOptions as Dictionary);
                    Object.keys(obj).map((key) => {
                        s += `col-${key}-${obj[key]} `;
                    });
                    s += 'col-12';
                    return s;
                }
                return 'col-md-6 col-12';
            },
        };
    },
});
</script>
