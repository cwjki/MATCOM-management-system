<template>
    <q-table> </q-table>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { GenericCrudTableConfig } from '../models/table.model'

export default defineComponent({
    props:{
        config: {
            type: Object as PropType<GenericCrudTableConfig>,
            required: true
        },
    },
    setup(props) {
        const {} = 

        return {}
    },
})
</script>
