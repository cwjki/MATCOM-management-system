<template>
    <q-page padding>
        <scholar-year-table-handler />
    </q-page>
</template>

<script lang="ts">
import ScholarYearTableHandler from 'src/components/tables/teachingAssignments/ScholarYearHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        ScholarYearTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
