package main

import (
	"github.com/kuraudo-io/pulumi-symbiosis/sdk/go/symbiosis"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := symbiosis.NewCluster(ctx, "example", &symbiosis.ClusterArgs{
			Region: pulumi.String("germany-1"),
		})
		if err != nil {
			return err
		}
		return nil
	})
}
