<template>
    <q-page padding>
        <thesis-defense-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import ThesisDefenseTableHandler from 'src/components/tables/thesisCommittee/ThesisDefenseTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        ThesisDefenseTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
