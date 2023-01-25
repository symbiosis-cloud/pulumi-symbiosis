# Installing the Provider

Because this provider is not an official Pulumi provider, you will need to
manually install the provider wherever you want to use it.

To do this, download an appropriate binary from the Releases section of this
repo (i.e. `linux-amd64` on an x86_64 Linux system, `darwin-arm64` on Apple
Silicon), extract it, and then use the `pulumi plugin install` command to
install it.

```shell
$ pulumi plugin install resource symbiosis v1.0.2 -f ./bin/pulumi-resource-symbiosis
[resource plugin symbiosis-1.0.2] installing
```

Now, you should be able to use the provider through any of its published SDKs.
