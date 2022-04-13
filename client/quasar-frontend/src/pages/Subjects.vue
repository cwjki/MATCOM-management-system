<template>
    <q-page padding>
        <subject-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import SubjectTableHandler from 'src/components/tables/SubjectTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        SubjectTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
