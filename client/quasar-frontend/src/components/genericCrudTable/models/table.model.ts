import { CRUDService } from 'src/services';
import { FieldModel } from './field.model';

export interface GenericCrudTableConfig {
    name: string;

    singularLabel: string;

    actions?: {
        create?: boolean;
        update?: boolean;
        delete?: boolean;
    };

    service: CRUDService;

    fields: FieldModel[];
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
