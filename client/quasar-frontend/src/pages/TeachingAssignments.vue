<template>
    <q-page padding>
        <teaching-assignment-table-handler />
    </q-page>
</template>

<script lang="ts">
import TeachingAssignmentTableHandler from 'src/components/tables/TeachingAssignmentTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        TeachingAssignmentTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
