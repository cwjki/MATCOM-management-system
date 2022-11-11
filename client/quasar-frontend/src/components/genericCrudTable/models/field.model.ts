import { AxiosPromise } from 'axios';
import { ListResult } from 'src/services';

export interface FieldColumn {
    align?: 'left' | ' right' | 'center';
    // (optional) tell QTable you want this column sortable
    sortable?: boolean;
    // body td:
    style?: string;
    // or as Function --> style: row => ... (return String/Array/Object)
    classes?: string;

    ordering?: boolean;

    maxLength?: number;

    // header th:
    headerStyle?: string;
    headerClasses?: string;

    transform?: (row: any) => string;
}

export interface FieldBasic {
    // name id of the field,
    name: string;

    // caption of the field
    label?: string;

    // text by default
    type?: 'text' | 'select' | 'date' | 'time';

    // false if dont show in the table
    column?: FieldColumn | false;

    icon?: string;

    rules?: string[];

    filter?: boolean;

    form?: {
        responsiveOptions: {
            xs?: number;
            sm?: number;
            md?: number;
            lg?: number;
            xl?: number;
        };
        defaultValue?: any;
    };
}

export interface FieldSelect extends FieldBasic {
    type: 'select';
    selectOptions: {
        list: (query?: any) => AxiosPromise<ListResult<any>>;
        label: string;
        value: string;
        refactorValue?: (value: any) => string;
        multiple?: boolean;
    };
}

export type FieldModel = FieldBasic | FieldSelect;
