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
 * @interface UpdateUser
 */
export interface UpdateUser {
    /**
     * 
     * @type {boolean}
     * @memberof UpdateUser
     */
    isSuperuser?: boolean;
    /**
     * 
     * @type {string}
     * @memberof UpdateUser
     */
    firstName?: string;
    /**
     * 
     * @type {string}
     * @memberof UpdateUser
     */
    lastName?: string;
    /**
     * 
     * @type {string}
     * @memberof UpdateUser
     */
    email?: string;
    /**
     * 
     * @type {string}
     * @memberof UpdateUser
     */
    password?: string;
}

export function UpdateUserFromJSON(json: any): UpdateUser {
    return UpdateUserFromJSONTyped(json, false);
}

export function UpdateUserFromJSONTyped(json: any, ignoreDiscriminator: boolean): UpdateUser {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'isSuperuser': !exists(json, 'is_superuser') ? undefined : json['is_superuser'],
        'firstName': !exists(json, 'first_name') ? undefined : json['first_name'],
        'lastName': !exists(json, 'last_name') ? undefined : json['last_name'],
        'email': !exists(json, 'email') ? undefined : json['email'],
        'password': !exists(json, 'password') ? undefined : json['password'],
    };
}

export function UpdateUserToJSON(value?: UpdateUser | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'is_superuser': value.isSuperuser,
        'first_name': value.firstName,
        'last_name': value.lastName,
        'email': value.email,
        'password': value.password,
    };
}
