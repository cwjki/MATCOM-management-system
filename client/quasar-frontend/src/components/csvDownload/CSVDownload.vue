<template>
    <div class="dropdown-menu mr-auto" aria-labelledby="navbarDropdown">
        <button class="dropdown-item" v-on:click="csvDownload()">
            Descargar csv de {{ fileName }}
        </button>
    </div>
</template>

<script>
import { defineComponent } from '@vue/runtime-core';
import { axios } from 'src/boot/axios';

export default defineComponent({
    props: ['url', 'fileName'],

    setup(props) {
        const fileName = props.fileName;

        const csvDownload = () => {
            return axios({
                url: props.url,
                method: 'GET',
                responseType: 'blob',
            }).then((response) => {
                const File = window.URL.createObjectURL(
                    new Blob([response.data])
                );
                const docUrl = document.createElement('a');
                docUrl.href = File;
                docUrl.setAttribute('download', fileName + '.csv');
                document.body.appendChild(docUrl);
                docUrl.click();
            });
        };

        return {
            fileName,

            csvDownload,
        };
    },
});
</script>
