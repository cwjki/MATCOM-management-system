<template>
    <q-page padding>
        <carmen-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import CarmenTableHandler from 'src/components/tables/CarmenTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        CarmenTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
