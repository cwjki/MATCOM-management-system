<template>
    <q-page padding>
        <time-period-table-handler />
    </q-page>
</template>

<script lang="ts">
import TimePeriodTableHandler from 'src/components/tables/teachingAssignments/TimePeriodsTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        TimePeriodTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
