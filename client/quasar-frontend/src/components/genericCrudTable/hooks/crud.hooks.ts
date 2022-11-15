import { ref } from 'vue';
import { GenericCrudTableConfig } from '../models/table.model';

export const useCrud = (config: GenericCrudTableConfig) => {
    const crudLoading = ref(false);
    const crudDialog = ref(false);
    const editeItem = ref({} as any);
    return {
        crudLoading,
        crudDialog,
        editeItem,
        changeKey(key: string, value: any) {
            editeItem.value[key] = value;
            // alert('someone change me');
        },
        prepareEdit(obj: any) {
            console.log({ ...(config.defaultValues || {}), ...obj });
            editeItem.value = { ...(config.defaultValues || {}), ...obj };
            crudDialog.value = true;
        },
        prepareCreate() {
            editeItem.value = { ...(config.defaultValues || {}) };
            config.fields.map((f) => {
                if (f.form && f.form.defaultValue) {
                    editeItem.value[f.name] = f.form.defaultValue;
                }
            });
            crudDialog.value = true;
        },
    };
};
