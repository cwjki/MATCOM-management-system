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
        prepareEdit(obj: any) {
            editeItem.value = obj;
            crudDialog.value = true;
        },
        prepareCreate() {
            editeItem.value = {};
            config.fields.map((f) => {
                if (f.form && f.form.defaultValue) {
                    editeItem.value[f.name] = f.form.defaultValue;
                }
            });

            crudDialog.value = true;
        },
    };
};
