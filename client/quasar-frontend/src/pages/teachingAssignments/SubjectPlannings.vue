<template>
    <q-page padding>
        <subject-planning-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import SubjectPlanningTableHandler from 'src/components/tables/teachingAssignments/SubjectPlanningTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        SubjectPlanningTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
