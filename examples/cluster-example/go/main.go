package main

import (
	"github.com/symbiosis-cloud/pulumi-symbiosis/sdk/go/symbiosis"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cluster, err := symbiosis.NewCluster(ctx, "example", &symbiosis.ClusterArgs{
			Region: pulumi.String("germany-1"),
		})
		if err != nil {
			return err
		}

		_, err = symbiosis.NewNodePool(ctx, "pool1", &symbiosis.NodePoolArgs{
			Cluster:  cluster.Name,
			NodeType: pulumi.String("general-1"),
			Quantity: pulumi.Int(1),
		})
		if err != nil {
			return err
		}

		return nil
	})
}
