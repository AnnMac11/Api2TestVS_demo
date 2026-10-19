using System;
using System.Text.Json.Serialization;
using Api2Test.Generated.Libraries;

namespace Api2Test.Generated.Classes.PetStore
{
    /// <summary>
    /// Parameters for GET /pet/{petId}. A path segment of {petId} becomes ByPetId in the class
    /// name. There is no request body here, so this class carries no ToJson().
    /// </summary>
    public class PetStoreGetPetByPetId
    {
        [JsonPropertyName("petId")] public int PetId { get; set; } = new DataGenerator().RandomId(1, 100000);
    }
}
