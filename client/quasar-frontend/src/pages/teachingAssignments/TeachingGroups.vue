<template>
    <q-page padding>
        <teaching-group-table-handler />
    </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TeachingGroupTableHandler from 'src/components/tables/teachingAssignments/TeachingGroupTableHandler.vue';
export default defineComponent({
    components: {
        TeachingGroupTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
