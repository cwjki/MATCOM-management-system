import { quasarColumn } from 'src/models/base';
import { FieldColumn, FieldModel } from '../models/field.model';

export const transformQuasarColumn = (
    fields: FieldModel[],
    action: boolean
): quasarColumn[] => {
    return [
        ...fields.map((field) => {
            const column = field.column as FieldColumn;
            return {
                field: (column && column.transform) || field.name,
                name: field.name,
                label: field.label || field.name,
                align: (column && column.align) || 'center',
                sortable: (column && column.ordering) || false,
                // TODO: finish map fieldModel to quasarColumn
            } as quasarColumn;
        }),
        ...(action
            ? [
                  {
                      name: 'csactions',
                      label: 'Acciones',
                      field: 'csactions',
                      align: 'center',
                  } as quasarColumn,
              ]
            : []),
    ];
};
