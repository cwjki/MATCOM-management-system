<template>
    <q-page padding>
        <teaching-planning-table-handler />
    </q-page>
</template>

<script lang="ts">
import TeachingPlanningTableHandler from 'src/components/tables/teachingAssignments/TeachingPlanningHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        TeachingPlanningTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
