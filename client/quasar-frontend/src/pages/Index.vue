<template>
    <q-page padding>
        <p class="text-h5 text-secondary">Welcome</p>
        <div class="bg-primary full-width" style="height: 100px"></div>

        <c-s-v-download :url="taUrl" :fileName="taFileName" />
        <c-s-v-download :url="tcUrl" :fileName="tcFileName" />
    </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import CSVDownload from '../components/csvDownload/CSVDownload.vue';

export default defineComponent({
    components: { CSVDownload },

    setup(props, { emit }) {
        const taUrl = 'http://127.0.0.1:8000/teaching-assignment/csv-download/';
        const tcUrl = 'http://127.0.0.1:8000/thesis-assignment/csv-download/';
        const taFileName = 'Docencia';
        const tcFileName = 'Tesis';
        return {
            taUrl,
            tcUrl,
            taFileName,
            tcFileName,
        };
    },
});
</script>
