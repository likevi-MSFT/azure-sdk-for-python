# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EntityHealth(Model):
    """Health information common to all entities in the cluster. It contains the
    aggregated health state, health events and unhealthy evaluation.
    .

    :param aggregated_health_state: Possible values include: 'Invalid', 'Ok',
     'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str or :class:`enum
     <azure.servicefabric.models.enum>`
    :param health_events: The list of health events reported on the entity.
    :type health_events: list of :class:`HealthEvent
     <azure.servicefabric.models.HealthEvent>`
    :param unhealthy_evaluations:
    :type unhealthy_evaluations: list of :class:`HealthEvaluationWrapper
     <azure.servicefabric.models.HealthEvaluationWrapper>`
    :param health_statistics:
    :type health_statistics: :class:`HealthStatistics
     <azure.servicefabric.models.HealthStatistics>`
    """

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'health_events': {'key': 'HealthEvents', 'type': '[HealthEvent]'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
        'health_statistics': {'key': 'HealthStatistics', 'type': 'HealthStatistics'},
    }

    def __init__(self, aggregated_health_state=None, health_events=None, unhealthy_evaluations=None, health_statistics=None):
        self.aggregated_health_state = aggregated_health_state
        self.health_events = health_events
        self.unhealthy_evaluations = unhealthy_evaluations
        self.health_statistics = health_statistics
