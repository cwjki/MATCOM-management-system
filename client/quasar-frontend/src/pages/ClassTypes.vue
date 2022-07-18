<template>
    <q-page padding>
        <class-types-table-handler />
    </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import ClassTypesTableHandler from 'src/components/tables/ClassTypesTableHandler.vue';
export default defineComponent({
    components: {
        ClassTypesTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
