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
 * @interface CreateUser
 */
export interface CreateUser {
    /**
     * 
     * @type {boolean}
     * @memberof CreateUser
     */
    isSuperuser: boolean;
    /**
     * 
     * @type {string}
     * @memberof CreateUser
     */
    firstName?: string;
    /**
     * 
     * @type {string}
     * @memberof CreateUser
     */
    lastName?: string;
    /**
     * 
     * @type {string}
     * @memberof CreateUser
     */
    email: string;
    /**
     * 
     * @type {string}
     * @memberof CreateUser
     */
    password: string;
}

export function CreateUserFromJSON(json: any): CreateUser {
    return CreateUserFromJSONTyped(json, false);
}

export function CreateUserFromJSONTyped(json: any, ignoreDiscriminator: boolean): CreateUser {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'isSuperuser': json['is_superuser'],
        'firstName': !exists(json, 'first_name') ? undefined : json['first_name'],
        'lastName': !exists(json, 'last_name') ? undefined : json['last_name'],
        'email': json['email'],
        'password': json['password'],
    };
}

export function CreateUserToJSON(value?: CreateUser | null): any {
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
