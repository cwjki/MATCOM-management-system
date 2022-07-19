<template>
    <q-page padding>
        <professor-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import ProfessorTableHandler from 'src/components/tables/teachingAssignments/ProfessorTable.handler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        ProfessorTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
