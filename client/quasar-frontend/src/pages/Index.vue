<template>
    <q-page padding>
        <p class="text-h5 text-secondary">Welcome</p>
        <div class="bg-primary full-width" style="height: 100px"></div>
    </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CSVDownload from '../components/csvDownload/CSVDownload.vue';

export default defineComponent({
    components: { CSVDownload },

    setup(props, { emit }) {
        return {};
    },
});
</script>
