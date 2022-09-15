<template>
    <q-page padding>
        <keyword-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import KeywordTableHandler from 'src/components/tables/thesisCommittee/KeywordTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        KeywordTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
