import { Dictionary } from 'src/models/base';
import { CRUDService } from 'src/services';
import { FieldModel } from './field.model';

export interface GenericCrudTableConfig {
    name: string;

    singularLabel: string;

    searchLabel?: string;

    actions?: {
        create?: boolean;
        update?: boolean;
        delete?: boolean;
        external?: {
            color: string;
            icon: string;
            func: () => void;
        }[];
    };

    service: CRUDService;

    query?: Dictionary;

    fields: FieldModel[];

    defaultValues?: Dictionary;
}

export interface RequestModel {
    filter: string;
    pagination: {
        sortBy: string;
        descending: boolean;
        page: number;
        rowsPerPage: number;
        rowsNumber: number;
    };
}
