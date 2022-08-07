<template>
    <q-page padding>
        <faculty-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import FacultyTableHandler from 'src/components/tables/teachingAssignments/FacultyTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        FacultyTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
