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
 * @interface Machine
 */
export interface Machine {
    /**
     * 
     * @type {number}
     * @memberof Machine
     */
    id?: number;
    /**
     * 
     * @type {string}
     * @memberof Machine
     */
    createdAt?: string;
    /**
     * 
     * @type {string}
     * @memberof Machine
     */
    updatedAt?: string;
    /**
     * 
     * @type {string}
     * @memberof Machine
     */
    unitInstalledAt?: string;
    /**
     * 
     * @type {string}
     * @memberof Machine
     */
    oemName?: string;
    /**
     * 
     * @type {string}
     * @memberof Machine
     */
    model?: string;
    /**
     * 
     * @type {string}
     * @memberof Machine
     */
    make?: string;
    /**
     * 
     * @type {string}
     * @memberof Machine
     */
    equipmentId?: string;
    /**
     * 
     * @type {string}
     * @memberof Machine
     */
    serialNumber?: string;
    /**
     * 
     * @type {string}
     * @memberof Machine
     */
    pin?: string;
}

export function MachineFromJSON(json: any): Machine {
    return MachineFromJSONTyped(json, false);
}

export function MachineFromJSONTyped(json: any, ignoreDiscriminator: boolean): Machine {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': !exists(json, 'id') ? undefined : json['id'],
        'createdAt': !exists(json, 'created_at') ? undefined : json['created_at'],
        'updatedAt': !exists(json, 'updated_at') ? undefined : json['updated_at'],
        'unitInstalledAt': !exists(json, 'unit_installed_at') ? undefined : json['unit_installed_at'],
        'oemName': !exists(json, 'oem_name') ? undefined : json['oem_name'],
        'model': !exists(json, 'model') ? undefined : json['model'],
        'make': !exists(json, 'make') ? undefined : json['make'],
        'equipmentId': !exists(json, 'equipment_id') ? undefined : json['equipment_id'],
        'serialNumber': !exists(json, 'serial_number') ? undefined : json['serial_number'],
        'pin': !exists(json, 'pin') ? undefined : json['pin'],
    };
}

export function MachineToJSON(value?: Machine | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'created_at': value.createdAt,
        'updated_at': value.updatedAt,
        'unit_installed_at': value.unitInstalledAt,
        'oem_name': value.oemName,
        'model': value.model,
        'make': value.make,
        'equipment_id': value.equipmentId,
        'serial_number': value.serialNumber,
        'pin': value.pin,
    };
}
