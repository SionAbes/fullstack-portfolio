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
    Token,
    TokenFromJSON,
    TokenFromJSONTyped,
    TokenToJSON,
    User,
    UserFromJSON,
    UserFromJSONTyped,
    UserToJSON,
} from './';

/**
 * 
 * @export
 * @interface LoginResponse
 */
export interface LoginResponse {
    /**
     * 
     * @type {User}
     * @memberof LoginResponse
     */
    user: User;
    /**
     * 
     * @type {string}
     * @memberof LoginResponse
     */
    refreshToken: string;
    /**
     * 
     * @type {string}
     * @memberof LoginResponse
     */
    accessToken: string;
}

export function LoginResponseFromJSON(json: any): LoginResponse {
    return LoginResponseFromJSONTyped(json, false);
}

export function LoginResponseFromJSONTyped(json: any, ignoreDiscriminator: boolean): LoginResponse {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'user': UserFromJSON(json['user']),
        'refreshToken': json['refresh_token'],
        'accessToken': json['access_token'],
    };
}

export function LoginResponseToJSON(value?: LoginResponse | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'user': UserToJSON(value.user),
        'refresh_token': value.refreshToken,
        'access_token': value.accessToken,
    };
}
