<template>
    <q-page padding>
        <department-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import DepartmentTableHandler from 'src/components/tables/DepartmentTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        DepartmentTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
