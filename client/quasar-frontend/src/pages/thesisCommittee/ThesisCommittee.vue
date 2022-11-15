<template>
    <q-page padding>
        <thesis-committee-table-handler :idC="idC" :Cname="Cname" />
        <!-- <div class="bg-secondary full-width" style="height: 100px"></div> -->
    </q-page>
</template>

<script lang="ts">
import ThesisCommitteeTableHandler from 'src/components/tables/thesisCommittee/ThesisCommitteeTableHandler.vue';
import { defineComponent } from 'vue';

export default defineComponent({
    props: ['idC', 'Cname'],

    components: {
        ThesisCommitteeTableHandler,
    },
    setup(props, { emit }) {
        return {};
    },
});
</script>
