<template>
    <q-page padding>
        <class-type-table-handler />
    </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import ClassTypeTableHandler from 'src/components/tables/teachingAssignments/ClassTypeTableHandler.vue';
export default defineComponent({
    components: {
        ClassTypeTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
