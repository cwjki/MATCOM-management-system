<template>
    <q-page padding>
        <teaching-category-table-handler />
    </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TeachingCategoryTableHandler from 'src/components/tables/teachingAssignments/TeachingCategoryTableHandler.vue';
export default defineComponent({
    components: {
        TeachingCategoryTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
