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
 * @interface CreatedMetricBase
 */
export interface CreatedMetricBase {
    /**
     * 
     * @type {number}
     * @memberof CreatedMetricBase
     */
    machineId: number;
    /**
     * 
     * @type {number}
     * @memberof CreatedMetricBase
     */
    userId: number;
    /**
     * 
     * @type {string}
     * @memberof CreatedMetricBase
     */
    createdAt: string;
}

export function CreatedMetricBaseFromJSON(json: any): CreatedMetricBase {
    return CreatedMetricBaseFromJSONTyped(json, false);
}

export function CreatedMetricBaseFromJSONTyped(json: any, ignoreDiscriminator: boolean): CreatedMetricBase {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'machineId': json['machine_id'],
        'userId': json['user_id'],
        'createdAt': json['created_at'],
    };
}

export function CreatedMetricBaseToJSON(value?: CreatedMetricBase | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'machine_id': value.machineId,
        'user_id': value.userId,
        'created_at': value.createdAt,
    };
}
