export interface FieldColumn {
    align?: 'left' | ' right' | 'center';
    // (optional) tell QTable you want this column sortable
    sortable?: boolean;
    // body td:
    style?: string;
    // or as Function --> style: row => ... (return String/Array/Object)
    classes?: string;

    // header th:
    headerStyle?: string;
    headerClasses?: string;

    transform?: (row: any) => string;
}

export interface FieldModel {
    // name id of the field,
    name: string;

    // caption of the field
    label?: string;

    // text by default
    type?: 'text' | 'number' | 'date' | ' image';

    // false if dont show in the table
    column?: FieldColumn | false;

    icon?: string;

    // rules?: string[];

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
