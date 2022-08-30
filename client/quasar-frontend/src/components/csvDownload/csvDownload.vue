<template>
    <div class="dropdown-menu mr-auto" aria-labelledby="navbarDropdown">
        <button class="dropdown-item" v-on:click="downloadCsv()">
            Asignación de Docencia CSV
        </button>
    </div>
</template>

<script>
import { defineComponent } from '@vue/runtime-core';
import { axios } from 'src/boot/axios';

export default defineComponent({
    setup(props) {
        const downloadCsv = ({ state }) => {
            return axios({
                url: '',
                method: 'GET',
                responseType: 'blob',
                headers: getHeaders(state.accessToken),
            }).then((response) => {
                console.log(response);
                saveAs(new Blob([response.data]), 'newfile.csv');
            });
        };

        return {
            downloadCsv,
        };
    },
});
</script>
