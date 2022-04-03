export interface Dictionary<T = any> {
    [key: string]: T;
}

export interface quasarColumn {
    // unique id
    // identifies column
    // (used by pagination.sortBy, "body-cell-[name]" slot, ...)
    name: string;

    // label for header
    label: string;

    // row Object property to determine value for this column
    field: string | ((row: any) => string);
    // OR field: row => row.some.nested.prop,

    // (optional) if we use visible-columns, this col will always be visible
    required?: boolean;

    // (optional) alignment
    align?: 'left' | ' right' | 'center';

    // (optional) tell QTable you want this column sortable
    sortable?: boolean;

    // (optional) compare function if you have
    // some custom data or want a specific way to compare two rows
    sort?: (a: any, b: any, rowA: any, rowB: any) => boolean;
    // function return value:
    //   * is less than 0 then sort a to an index lower than b, i.e. a comes first
    //   * is 0 then leave a and b unchanged with respect to each other, but sorted with respect to all different elements
    //   * is greater than 0 then sort b to an index lower than a, i.e. b comes first

    // (optional) override 'column-sort-order' prop;
    // sets column sort order: 'ad' (ascending-descending) or 'da' (descending-ascending)
    sortOrder?: 'ad' | 'da'; // or 'da'

    // (optional) you can format the data with a function
    format?: (val: any, row: any) => string;
    // one more format example:
    // format: val => val
    //   ? /* Unicode checkmark checked */ "\u2611"
    //   : /* Unicode checkmark unchecked */ "\u2610",

    // body td:
    style?: string;
    // or as Function --> style: row => ... (return String/Array/Object)
    classes?: string;
    // or as Function --> classes: row => ... (return String)

    // header th:
    headerStyle?: string;
    headerClasses?: string;
}
