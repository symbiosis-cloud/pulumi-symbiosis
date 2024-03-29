// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Symbiosis.Pulumi.Symbiosis.Inputs
{

    public sealed class NodePoolTaintArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Taint effect. Can be either NoSchedule, PreferNoSchedule or NoExecute. See: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
        /// </summary>
        [Input("effect", required: true)]
        public Input<string> Effect { get; set; } = null!;

        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public NodePoolTaintArgs()
        {
        }
        public static new NodePoolTaintArgs Empty => new NodePoolTaintArgs();
    }
}
