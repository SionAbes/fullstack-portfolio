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
 * @interface BaseVolvoCaretrackAdapter
 */
export interface BaseVolvoCaretrackAdapter {
    /**
     * 
     * @type {string}
     * @memberof BaseVolvoCaretrackAdapter
     */
    username: string;
    /**
     * 
     * @type {string}
     * @memberof BaseVolvoCaretrackAdapter
     */
    password: string;
}

export function BaseVolvoCaretrackAdapterFromJSON(json: any): BaseVolvoCaretrackAdapter {
    return BaseVolvoCaretrackAdapterFromJSONTyped(json, false);
}

export function BaseVolvoCaretrackAdapterFromJSONTyped(json: any, ignoreDiscriminator: boolean): BaseVolvoCaretrackAdapter {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'username': json['username'],
        'password': json['password'],
    };
}

export function BaseVolvoCaretrackAdapterToJSON(value?: BaseVolvoCaretrackAdapter | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'username': value.username,
        'password': value.password,
    };
}
