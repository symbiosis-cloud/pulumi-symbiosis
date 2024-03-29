# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'NodePoolAutoscalingArgs',
    'NodePoolTaintArgs',
]

@pulumi.input_type
class NodePoolAutoscalingArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 max_size: pulumi.Input[int],
                 min_size: pulumi.Input[int]):
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "max_size", max_size)
        pulumi.set(__self__, "min_size", min_size)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Input[int]:
        return pulumi.get(self, "max_size")

    @max_size.setter
    def max_size(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_size", value)

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> pulumi.Input[int]:
        return pulumi.get(self, "min_size")

    @min_size.setter
    def min_size(self, value: pulumi.Input[int]):
        pulumi.set(self, "min_size", value)


@pulumi.input_type
class NodePoolTaintArgs:
    def __init__(__self__, *,
                 effect: pulumi.Input[str],
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] effect: Taint effect. Can be either NoSchedule, PreferNoSchedule or NoExecute. See: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
        """
        pulumi.set(__self__, "effect", effect)
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def effect(self) -> pulumi.Input[str]:
        """
        Taint effect. Can be either NoSchedule, PreferNoSchedule or NoExecute. See: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
        """
        return pulumi.get(self, "effect")

    @effect.setter
    def effect(self, value: pulumi.Input[str]):
        pulumi.set(self, "effect", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


