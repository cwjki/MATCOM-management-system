<template>
    <div class="dropdown-menu mr-auto" aria-labelledby="navbarDropdown">
        <button class="dropdown-item" v-on:click="csvDownload()">
            Asignación de Docencia CSV
        </button>
    </div>
</template>

<script>
import { defineComponent } from '@vue/runtime-core';
import { axios } from 'src/boot/axios';

export default defineComponent({
    setup(props) {
        const csvDownload = () => {
            return axios({
                url: 'http://127.0.0.1:8000/csv-download/',
                method: 'GET',
                responseType: 'blob',
            }).then((response) => {
                console.log(response);
                const File = window.URL.createObjectURL(
                    new Blob([response.data])
                );
                const docUrl = document.createElement('a');
                docUrl.href = File;
                docUrl.setAttribute('download', 'Docencia.csv');
                document.body.appendChild(docUrl);
                docUrl.click();
            });
        };

        return {
            csvDownload,
        };
    },
});
</script>
