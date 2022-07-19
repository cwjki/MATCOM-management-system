<template>
    <q-page padding>
        <semester-table-handler />
    </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import SemesterTableHandler from 'src/components/tables/teachingAssignments/SemesterTableHandler.vue';
export default defineComponent({
    components: {
        SemesterTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
