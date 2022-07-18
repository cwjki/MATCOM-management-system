<template>
    <q-page padding>
        <time-period-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import TimePeriodTableHandler from 'src/components/tables/TimePeriodsTableHandler.vue';
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
