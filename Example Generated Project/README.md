# Example Generated Project — PetStore API Tests

This is a worked example of what **API2Test** produces after you import an API and
generate test cases. It targets the public
[Swagger PetStore](https://petstore3.swagger.io) API.

The matching input spec is in [`../Example Swagger Files`](../Example%20Swagger%20Files).

## Layout

```
Example Generated Project/
├─ PetStore.Tests.csproj      # .NET 8 MSTest project
├─ GeneratedClasses/
│  └─ Pet.cs                  # request/response model generated from the schema
├─ DataLibrary/
│  └─ DataGenerator.cs        # reusable test-data methods (Data Library)
└─ Tests/
   └─ PetApiTests.cs          # generated API test cases
```

This mirrors the API2Test output: model classes land in the `GeneratedClasses`
namespace, reusable data methods in `DataLibrary`, and one test method per endpoint.

## Run it

```bash
dotnet test
```

> This sample is illustrative and trimmed for readability. A real generation run also
> records the classes and tests in `~/.vscode/API2Test/data/` (`generated-classes.json`,
> `api-tests.json`).
