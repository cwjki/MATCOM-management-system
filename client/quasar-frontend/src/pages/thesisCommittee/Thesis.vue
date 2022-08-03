<template>
    <q-page padding>
        <thesis-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import ThesisTableHandler from 'src/components/tables/thesisCommittee/ThesisTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        ThesisTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
