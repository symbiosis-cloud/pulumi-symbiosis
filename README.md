# Symbiosis Resource Provider

The Symbiosis Resource Provider lets you manage [Symbiosis](https://symbiosis.host) resources.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @symbiosis-cloud/symbiosis-pulumi
```

or `yarn`:

```bash
yarn add @symbiosis-cloud/symbiosis-pulumi
```

### Python

To use from Python, install using `pip`:

```bash
pip install symbiosis-pulumi
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/symbiosis-cloud/pulumi-symbiosis/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package Symbiosis.Pulumi.Symbiosis
```

## Configuration

The following configuration points are available for the `symbiosis` provider:

- `symbiosis:apiKey` (environment: `SYMBIOSIS_API_KEY`) - The ApiKey used to authenticate requests towards Symbiosis.
- `symbiosis:endpoint` (environment: `SYMBIOSIS_ENDPOINT`) - Endpoint for reaching the symbiosis API. Used for debugging or when accessed through a proxy.

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/symbiosis/api-docs/).
