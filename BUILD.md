# Build

## Locally

In order to build the provider locally for testing, you can use the included dev
container setup in [`.devcontainer/`](./.devcontainer). Running it with VS Code
is the easiest method, but you can also run it from a terminal:

```shell
docker build . -f .devcontainer/Dockerfile -t dcps
...
docker run --rm -it -v $(pwd):/build -w /build dcps
build@368612b0ea8c:/build$
```

Once you're in the container, you can use the included [`Makefile`](./Makefile)
to build the SDKs included (Node.js, Python, .NET Core and Golang) by running
the `build` target.

```shell
build@368612b0ea8c:/build$ make build
...
```

Once this has completed, you will see a `dotnet`, `go`, `nodejs` and `python`
folder appear in the [`sdk`](./sdk) directory. These are the compiled/generated
SDKs for use with Pulumi.

## Release

To make a release, there is a two-step process to go through. The first step is
making tags for the releases.

```shell
$ git tag v1.0.2 # used for the nodejs, python and dotnet releases
$ git tag sdk/v1.0.2 # used for the golang release
```

Then, you just need to push your tags.

```shell
$ git push --tags
```

Once done, [GitHub Actions](./.github/workflows/release.yaml) will take over and
(assuming you have set up the required environment variables on GitHub's end)
build & release the SDKs to NPM, PyPI, and NuGet.
