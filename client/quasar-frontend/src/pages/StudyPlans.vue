<template>
    <q-page padding>
        <study-plan-table-handler />
    </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import StudyPlanTableHandler from 'src/components/tables/StudyPlanTableHandler.vue';
export default defineComponent({
    components: {
        StudyPlanTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
