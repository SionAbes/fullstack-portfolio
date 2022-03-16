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
 * @interface Credentials
 */
export interface Credentials {
    /**
     * 
     * @type {string}
     * @memberof Credentials
     */
    username?: string;
    /**
     * 
     * @type {string}
     * @memberof Credentials
     */
    password: string;
    /**
     * 
     * @type {string}
     * @memberof Credentials
     */
    scope?: string;
    /**
     * 
     * @type {string}
     * @memberof Credentials
     */
    clientId?: string;
    /**
     * 
     * @type {string}
     * @memberof Credentials
     */
    clientSecret?: string;
}

export function CredentialsFromJSON(json: any): Credentials {
    return CredentialsFromJSONTyped(json, false);
}

export function CredentialsFromJSONTyped(json: any, ignoreDiscriminator: boolean): Credentials {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'username': !exists(json, 'username') ? undefined : json['username'],
        'password': json['password'],
        'scope': !exists(json, 'scope') ? undefined : json['scope'],
        'clientId': !exists(json, 'client_id') ? undefined : json['client_id'],
        'clientSecret': !exists(json, 'client_secret') ? undefined : json['client_secret'],
    };
}

export function CredentialsToJSON(value?: Credentials | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'username': value.username,
        'password': value.password,
        'scope': value.scope,
        'client_id': value.clientId,
        'client_secret': value.clientSecret,
    };
}