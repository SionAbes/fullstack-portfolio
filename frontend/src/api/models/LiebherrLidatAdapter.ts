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
    BaseLiebherrLidatAdapter,
    BaseLiebherrLidatAdapterFromJSON,
    BaseLiebherrLidatAdapterFromJSONTyped,
    BaseLiebherrLidatAdapterToJSON,
} from './';

/**
 * 
 * @export
 * @interface LiebherrLidatAdapter
 */
export interface LiebherrLidatAdapter {
    /**
     * 
     * @type {number}
     * @memberof LiebherrLidatAdapter
     */
    id: number;
    /**
     * 
     * @type {number}
     * @memberof LiebherrLidatAdapter
     */
    userId: number;
    /**
     * 
     * @type {string}
     * @memberof LiebherrLidatAdapter
     */
    createdAt: string;
    /**
     * 
     * @type {string}
     * @memberof LiebherrLidatAdapter
     */
    updatedAt: string;
    /**
     * 
     * @type {string}
     * @memberof LiebherrLidatAdapter
     */
    adapterName: string;
    /**
     * 
     * @type {string}
     * @memberof LiebherrLidatAdapter
     */
    cronExpression: string;
    /**
     * 
     * @type {string}
     * @memberof LiebherrLidatAdapter
     */
    dataUrl: string;
    /**
     * 
     * @type {string}
     * @memberof LiebherrLidatAdapter
     */
    username: string;
    /**
     * 
     * @type {string}
     * @memberof LiebherrLidatAdapter
     */
    password: string;
}

export function LiebherrLidatAdapterFromJSON(json: any): LiebherrLidatAdapter {
    return LiebherrLidatAdapterFromJSONTyped(json, false);
}

export function LiebherrLidatAdapterFromJSONTyped(json: any, ignoreDiscriminator: boolean): LiebherrLidatAdapter {
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
        'username': json['username'],
        'password': json['password'],
    };
}

export function LiebherrLidatAdapterToJSON(value?: LiebherrLidatAdapter | null): any {
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
        'username': value.username,
        'password': value.password,
    };
}
