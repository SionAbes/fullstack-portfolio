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
import {
    BaseCreateAdapter,
    BaseCreateAdapterFromJSON,
    BaseCreateAdapterFromJSONTyped,
    BaseCreateAdapterToJSON,
    BaseLiebherrLidatAdapter,
    BaseLiebherrLidatAdapterFromJSON,
    BaseLiebherrLidatAdapterFromJSONTyped,
    BaseLiebherrLidatAdapterToJSON,
} from './';

/**
 * 
 * @export
 * @interface CreateLiebherrLidatAdapter
 */
export interface CreateLiebherrLidatAdapter {
    /**
     * 
     * @type {string}
     * @memberof CreateLiebherrLidatAdapter
     */
    adapterName: string;
    /**
     * 
     * @type {string}
     * @memberof CreateLiebherrLidatAdapter
     */
    dataUrl: string;
    /**
     * 
     * @type {string}
     * @memberof CreateLiebherrLidatAdapter
     */
    cronExpression: string;
    /**
     * 
     * @type {string}
     * @memberof CreateLiebherrLidatAdapter
     */
    username: string;
    /**
     * 
     * @type {string}
     * @memberof CreateLiebherrLidatAdapter
     */
    password: string;
}

export function CreateLiebherrLidatAdapterFromJSON(json: any): CreateLiebherrLidatAdapter {
    return CreateLiebherrLidatAdapterFromJSONTyped(json, false);
}

export function CreateLiebherrLidatAdapterFromJSONTyped(json: any, ignoreDiscriminator: boolean): CreateLiebherrLidatAdapter {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'adapterName': json['adapter_name'],
        'dataUrl': json['data_url'],
        'cronExpression': json['cron_expression'],
        'username': json['username'],
        'password': json['password'],
    };
}

export function CreateLiebherrLidatAdapterToJSON(value?: CreateLiebherrLidatAdapter | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'adapter_name': value.adapterName,
        'data_url': value.dataUrl,
        'cron_expression': value.cronExpression,
        'username': value.username,
        'password': value.password,
    };
}
