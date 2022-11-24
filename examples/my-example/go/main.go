package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
  "github.com/kuraudo-io/pulumi-symbiosis/sdk/go/symbiosis"
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
