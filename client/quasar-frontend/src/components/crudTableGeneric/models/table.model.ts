import { CRUDService } from 'src/services';
import { FieldModel } from './field.model';

export interface CrudTableConfig {
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
