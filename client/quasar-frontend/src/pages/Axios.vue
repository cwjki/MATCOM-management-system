<template>
  <q-page padding>
    <p>DATA</p>
    <get-data />
  </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import GetData from 'src/components/testing/GetData.vue';

export default defineComponent({
  components: {
    GetData,
  },
  setup(props, { emit }) {
    return {};
  },
});
</script>
