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
 * @interface Token
 */
export interface Token {
    /**
     * 
     * @type {string}
     * @memberof Token
     */
    refreshToken: string;
    /**
     * 
     * @type {string}
     * @memberof Token
     */
    accessToken: string;
}

export function TokenFromJSON(json: any): Token {
    return TokenFromJSONTyped(json, false);
}

export function TokenFromJSONTyped(json: any, ignoreDiscriminator: boolean): Token {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'refreshToken': json['refresh_token'],
        'accessToken': json['access_token'],
    };
}

export function TokenToJSON(value?: Token | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'refresh_token': value.refreshToken,
        'access_token': value.accessToken,
    };
}