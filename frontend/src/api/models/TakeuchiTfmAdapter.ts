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
    BaseAdapter,
    BaseAdapterFromJSON,
    BaseAdapterFromJSONTyped,
    BaseAdapterToJSON,
    BaseTakeuchiTfmAdapter,
    BaseTakeuchiTfmAdapterFromJSON,
    BaseTakeuchiTfmAdapterFromJSONTyped,
    BaseTakeuchiTfmAdapterToJSON,
} from './';

/**
 * 
 * @export
 * @interface TakeuchiTfmAdapter
 */
export interface TakeuchiTfmAdapter {
    /**
     * 
     * @type {number}
     * @memberof TakeuchiTfmAdapter
     */
    id: number;
    /**
     * 
     * @type {number}
     * @memberof TakeuchiTfmAdapter
     */
    userId: number;
    /**
     * 
     * @type {string}
     * @memberof TakeuchiTfmAdapter
     */
    createdAt: string;
    /**
     * 
     * @type {string}
     * @memberof TakeuchiTfmAdapter
     */
    updatedAt: string;
    /**
     * 
     * @type {string}
     * @memberof TakeuchiTfmAdapter
     */
    adapterName: string;
    /**
     * 
     * @type {string}
     * @memberof TakeuchiTfmAdapter
     */
    cronExpression: string;
    /**
     * 
     * @type {string}
     * @memberof TakeuchiTfmAdapter
     */
    dataUrl: string;
    /**
     * 
     * @type {string}
     * @memberof TakeuchiTfmAdapter
     */
    clientSecret: string;
    /**
     * 
     * @type {string}
     * @memberof TakeuchiTfmAdapter
     */
    clientId: string;
    /**
     * 
     * @type {string}
     * @memberof TakeuchiTfmAdapter
     */
    tokenUrl: string;
}

export function TakeuchiTfmAdapterFromJSON(json: any): TakeuchiTfmAdapter {
    return TakeuchiTfmAdapterFromJSONTyped(json, false);
}

export function TakeuchiTfmAdapterFromJSONTyped(json: any, ignoreDiscriminator: boolean): TakeuchiTfmAdapter {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
        'userId': json['user_id'],
        'createdAt': json['created_at'],
        'updatedAt': json['updated_at'],
        'adapterName': json['adapter_name'],
        'cronExpression': json['cron_expression'],
        'dataUrl': json['data_url'],
        'clientSecret': json['client_secret'],
        'clientId': json['client_id'],
        'tokenUrl': json['token_url'],
    };
}

export function TakeuchiTfmAdapterToJSON(value?: TakeuchiTfmAdapter | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'user_id': value.userId,
        'created_at': value.createdAt,
        'updated_at': value.updatedAt,
        'adapter_name': value.adapterName,
        'cron_expression': value.cronExpression,
        'data_url': value.dataUrl,
        'client_secret': value.clientSecret,
        'client_id': value.clientId,
        'token_url': value.tokenUrl,
    };
}
