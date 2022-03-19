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
    Machine,
    MachineFromJSON,
    MachineFromJSONTyped,
    MachineToJSON,
} from './';

/**
 * 
 * @export
 * @interface CreateMetric
 */
export interface CreateMetric {
    /**
     * 
     * @type {string}
     * @memberof CreateMetric
     */
    processedAt?: string;
    /**
     * 
     * @type {string}
     * @memberof CreateMetric
     */
    eventAt?: string;
    /**
     * 
     * @type {Machine}
     * @memberof CreateMetric
     */
    machine?: Machine;
    /**
     * 
     * @type {string}
     * @memberof CreateMetric
     */
    oem?: string;
    /**
     * 
     * @type {string}
     * @memberof CreateMetric
     */
    metric?: string;
    /**
     * 
     * @type {string}
     * @memberof CreateMetric
     */
    value?: string;
    /**
     * 
     * @type {string}
     * @memberof CreateMetric
     */
    unit?: string;
}

export function CreateMetricFromJSON(json: any): CreateMetric {
    return CreateMetricFromJSONTyped(json, false);
}

export function CreateMetricFromJSONTyped(json: any, ignoreDiscriminator: boolean): CreateMetric {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'processedAt': !exists(json, 'processed_at') ? undefined : json['processed_at'],
        'eventAt': !exists(json, 'event_at') ? undefined : json['event_at'],
        'machine': !exists(json, 'machine') ? undefined : MachineFromJSON(json['machine']),
        'oem': !exists(json, 'oem') ? undefined : json['oem'],
        'metric': !exists(json, 'metric') ? undefined : json['metric'],
        'value': !exists(json, 'value') ? undefined : json['value'],
        'unit': !exists(json, 'unit') ? undefined : json['unit'],
    };
}

export function CreateMetricToJSON(value?: CreateMetric | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'processed_at': value.processedAt,
        'event_at': value.eventAt,
        'machine': MachineToJSON(value.machine),
        'oem': value.oem,
        'metric': value.metric,
        'value': value.value,
        'unit': value.unit,
    };
}
