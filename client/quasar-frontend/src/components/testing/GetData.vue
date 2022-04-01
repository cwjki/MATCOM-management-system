<template>
  <button @onClick="loadData">Click Here</button>

  <p>Data</p>
  <p>{{ data }}</p>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { ref } from 'vue';
import { api } from 'boot/axios';
import { Notify } from 'quasar';

export default defineComponent({
  name: 'GetData',
  props: {
    data: {
      type: Object,
      default: null,
    },
  },
  emits: ['onClick'],
  setup(props, { emit }) {
    const data = ref(null);

    function loadData() {
      api
        .get('/api/backend')
        .then((response) => {
          data.value = response.data;
        })
        .catch(() => {
          Notify.create({
            color: 'negative',
            position: 'top',
            message: 'Loading failed',
            icon: 'report_problem',
          });
        });
    }

    return { data, loadData };
  },
});
</script>
