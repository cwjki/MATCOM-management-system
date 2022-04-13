<template>
    <q-page padding>
        <career-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import CareerTableHandler from 'src/components/tables/CareerTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        CareerTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
