<template>
    <q-page padding>
        <scientific-degree-table-handler />
    </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import ScientificDegreeTableHandler from 'src/components/tables/teachingAssignments/ScientificDegreeTableHandler.vue';
export default defineComponent({
    components: {
        ScientificDegreeTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
