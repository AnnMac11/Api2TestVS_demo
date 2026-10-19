# Example Generated Project — PetStore API Tests

This is a worked example of what **API2Test** writes into your project when you deploy a test
case. It targets the public [Swagger PetStore](https://petstore3.swagger.io) API, and the matching
input spec is in [`../Example Swagger Files`](../Example%20Swagger%20Files).

## Layout

Folders mirror namespaces, so a generated test compiles wherever you deploy it:

```
Example Generated Project/
├─ PetStore.Tests.csproj                   # net9.0 MSTest project (see csproj packages below)
├─ Libraries/                              -> Api2Test.Generated.Libraries
│  ├─ ApiMethods.cs                        #   from the API Method Library
│  └─ DataGenerator.cs                     #   from the Data Library
├─ Classes/PetStore/                       -> Api2Test.Generated.Classes.PetStore
│  ├─ PetStorePostPet.cs                   #   request body for POST /pet
│  └─ PetStoreGetPetByPetId.cs             #   parameters for GET /pet/{petId}
└─ Tests/PetStore/                         -> Api2Test.Generated.Tests.PetStore
   └─ CreateThenGetPetTests.cs             #   one generated test class per test case
```

`Libraries/` is shared by every application. `Classes/` and `Tests/` are split per application, so
importing a second API never collides with the first. A deploy of a complete unit writes all three.

## How the pieces fit together

- **The Data Dictionary** assigns a Data Method to each field, which becomes that property's
  default value — `public string Name { get; set; } = new DataGenerator().ProductName();`
- **The request class name** is Application + verb + path segments, with `{petId}` rendered as
  `ByPetId`: `POST /pet` → `PetStorePostPet`, `GET /pet/{petId}` → `PetStoreGetPetByPetId`.
- **The test case header** picks the base path and the token method, which is why each test opens
  with `var baseUrl = PetStoreBaseUrl();` and `var token = await PetStoreApiKey();`
- **Each step of the chain** is one API Method call, in order, with a `// Step n:` comment above
  it. A `Validate…` step becomes an assertion; an `Extract…` step captures a value (here `petId`)
  that a later step uses.
- **`ApiMethods` is imported with `using static`**, so the methods are called by their bare names.

## csproj packages

```xml
<PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.*" />
<PackageReference Include="MSTest.TestAdapter" Version="3.*" />
<PackageReference Include="MSTest.TestFramework" Version="3.*" />
<PackageReference Include="Bogus" Version="35.*" />
```

For NUnit use `NUnit` + `NUnit3TestAdapter`; for xUnit use `xunit` +
`xunit.runner.visualstudio`. The extension generates the attributes for whichever framework the
test case was set to.

## Run it

```bash
dotnet build
dotnet test
```

> This sample is illustrative and trimmed for readability — the shipped API Method Library has 26
> methods and the Data Library around 100, where this keeps only the ones the example calls. The
> structure, namespaces and generated shapes are the real ones. Pressing **Execute** on a test case
> in the extension builds and runs exactly this kind of project in a sandbox for you; a real
> generation run also records the classes and tests in `~/.vscode/API2Test/data/`
> (`generated-classes.json`, `api-tests.json`).
