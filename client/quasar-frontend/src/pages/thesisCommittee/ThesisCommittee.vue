<template>
    <q-page padding>
        <thesis-committee-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import ThesisCommitteeTableHandler from 'src/components/tables/thesisCommittee/ThesisCommitteeTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        ThesisCommitteeTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
