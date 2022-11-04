<template>
    <q-page padding>
        <p class="text-h5 text-secondary">Welcome</p>
        <div class="bg-primary full-width" style="height: 100px"></div>

        <c-s-v-download :url="tcUrl" :fileName="tcFileName" />
        <c-s-v-download :url="tdUrl" :fileName="tdFileName" />
    </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CSVDownload from '../components/csvDownload/CSVDownload.vue';

export default defineComponent({
    components: { CSVDownload },

    setup(props, { emit }) {
        const tcUrl =
            'http://127.0.0.1:8000/thesis-assignment/thesis-committee-csv-download/';
        const tdUrl =
            'http://127.0.0.1:8000/thesis-assignment/thesis-defense-csv-download/';
        const tcFileName = 'Tribunales de Tesis';
        const tdFileName = 'Defensas de Tesis';
        return {
            tcUrl,
            tdUrl,
            tcFileName,
            tdFileName,
        };
    },
});
</script>
