<template>
    <q-page padding>
        <student-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import StudentTableHandler from 'src/components/tables/thesisCommittee/StudentTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        StudentTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
