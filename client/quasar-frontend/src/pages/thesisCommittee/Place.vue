<template>
    <q-page padding>
        <place-table-handler />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import PlaceTableHandler from 'src/components/tables/thesisCommittee/PlaceTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        PlaceTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
