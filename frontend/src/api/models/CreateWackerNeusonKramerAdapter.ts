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
    BaseWackerNeusonKramerAdapter,
    BaseWackerNeusonKramerAdapterFromJSON,
    BaseWackerNeusonKramerAdapterFromJSONTyped,
    BaseWackerNeusonKramerAdapterToJSON,
} from './';

/**
 * 
 * @export
 * @interface CreateWackerNeusonKramerAdapter
 */
export interface CreateWackerNeusonKramerAdapter {
    /**
     * 
     * @type {string}
     * @memberof CreateWackerNeusonKramerAdapter
     */
    adapterName: string;
    /**
     * 
     * @type {string}
     * @memberof CreateWackerNeusonKramerAdapter
     */
    dataUrl: string;
    /**
     * 
     * @type {string}
     * @memberof CreateWackerNeusonKramerAdapter
     */
    cronExpression: string;
    /**
     * 
     * @type {string}
     * @memberof CreateWackerNeusonKramerAdapter
     */
    tokenUrl: string;
    /**
     * 
     * @type {string}
     * @memberof CreateWackerNeusonKramerAdapter
     */
    username: string;
    /**
     * 
     * @type {string}
     * @memberof CreateWackerNeusonKramerAdapter
     */
    password: string;
    /**
     * 
     * @type {string}
     * @memberof CreateWackerNeusonKramerAdapter
     */
    clientId: string;
    /**
     * 
     * @type {string}
     * @memberof CreateWackerNeusonKramerAdapter
     */
    clientSecret: string;
}

export function CreateWackerNeusonKramerAdapterFromJSON(json: any): CreateWackerNeusonKramerAdapter {
    return CreateWackerNeusonKramerAdapterFromJSONTyped(json, false);
}

export function CreateWackerNeusonKramerAdapterFromJSONTyped(json: any, ignoreDiscriminator: boolean): CreateWackerNeusonKramerAdapter {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'adapterName': json['adapter_name'],
        'dataUrl': json['data_url'],
        'cronExpression': json['cron_expression'],
        'tokenUrl': json['token_url'],
        'username': json['username'],
        'password': json['password'],
        'clientId': json['client_id'],
        'clientSecret': json['client_secret'],
    };
}

export function CreateWackerNeusonKramerAdapterToJSON(value?: CreateWackerNeusonKramerAdapter | null): any {
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
        'token_url': value.tokenUrl,
        'username': value.username,
        'password': value.password,
        'client_id': value.clientId,
        'client_secret': value.clientSecret,
    };
}