import { api, baseURL } from 'src/boot/axios';
import { Dictionary } from 'src/models/base';

export interface ListResult<T> {
    results: T[];
    count: number;
}

const reduceListParams =
    (label: string, params: Dictionary) =>
    (acc: string, curr: string, i: number) => {
        return acc + `${i !== 0 ? '&' : ''}${label}=${curr}`;
    };

const accumulateQueryParams =
    (params: Dictionary) => (acc: string, curr: string, i: number) => {
        if (typeof params[curr] === 'object')
            return (
                acc +
                `${i !== 0 ? '&' : ''}` +
                (params[curr] as Dictionary).reduce(
                    reduceListParams(curr, params[curr]),
                    ''
                )
            );
        return acc + `${i !== 0 ? '&' : ''}${curr}=${params[curr]}`;
    };

export const buildQuery = (params: Dictionary): string => {
    // console.log(params);
    // alert(' i am building a query');
    let subParams: Dictionary = {};
    Object.keys(params).map((k) => {
        if (params[k] !== null && params[k] !== undefined)
            subParams[k] = params[k];
    });
    // console.log('here', subParams);
    return Object.keys(subParams).length > 0
        ? '?' +
              Object.keys(subParams).reduce(
                  accumulateQueryParams(subParams),
                  ''
              )
        : '';
};

export const CrudServiceFactory = <T = any>(url: string) => {
    return {
        url: url,
        fullUrl: baseURL + url,
        create(obj: T) {
            return api.post<T>(url, obj);
        },
        list(query: Dictionary = {}) {
            return api.get<ListResult<T>>(url + buildQuery(query));
        },
        update(id: string, obj: Dictionary) {
            return api.patch<T>(url + id, obj);
        },
        delete(id: string) {
            return api.delete<T>(url + id);
        },
    };
};

export type CRUDService = ReturnType<typeof CrudServiceFactory>;
