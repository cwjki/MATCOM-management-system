import { Dictionary } from 'src/models/base';
import { FieldModel, FieldSelect } from '../models/field.model';

export const useSerializer = (obj: Dictionary, fields: FieldModel[]) => {
    return {
        getPayload: () => {
            let payload: Dictionary = {};
            console.log(obj, fields);
            fields.map((f) => {
                console.log('reducing', f.name, obj[f.name], payload);
                if (f.type === 'select') {
                    const opt = f as FieldSelect;

                    if (!opt) {
                        alert(' i put a select field without a selectOpt');
                    } else if (obj[f.name]) {
                        payload[f.name + '_id'] =
                            obj[f.name][opt.selectOptions.value];
                    }
                } else payload[f.name] = obj[f.name];
            });

            return payload;
        },
    };
};
