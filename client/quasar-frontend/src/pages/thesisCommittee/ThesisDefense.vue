<template>
    <q-page padding>
        <thesis-defense-table-handler :idC="idC" :Cname="Cname" />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import ThesisDefenseTableHandler from 'src/components/tables/thesisCommittee/ThesisDefenseTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    props: ['idC', 'Cname'],
    components: {
        ThesisDefenseTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
