/* tslint:disable */
/* eslint-disable */
/**
 * Fullstack Portfolio API
 * FastAPI of Fullstack Portfolio
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface GenericError
 */
export interface GenericError {
    /**
     * 
     * @type {string}
     * @memberof GenericError
     */
    details?: string;
}

export function GenericErrorFromJSON(json: any): GenericError {
    return GenericErrorFromJSONTyped(json, false);
}

export function GenericErrorFromJSONTyped(json: any, ignoreDiscriminator: boolean): GenericError {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'details': !exists(json, 'details') ? undefined : json['details'],
    };
}

export function GenericErrorToJSON(value?: GenericError | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'details': value.details,
    };
}
