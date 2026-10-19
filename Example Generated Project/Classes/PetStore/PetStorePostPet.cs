using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Text.Json.Serialization;
using Api2Test.Generated.Libraries;

namespace Api2Test.Generated.Classes.PetStore
{
    /// <summary>
    /// Request body for POST /pet. The class name is Application + Verb + path segments, so
    /// every endpoint gets its own class and no two collide.
    /// Each property keeps the spec field name as its JSON key, and its default value is the
    /// Data Method the Data Dictionary assigned to that field.
    /// </summary>
    public class PetStorePostPet
    {
        [JsonPropertyName("id")] public int Id { get; set; } = new DataGenerator().RandomId(1, 100000);
        [JsonPropertyName("name")] public string Name { get; set; } = new DataGenerator().ProductName();
        [JsonPropertyName("category")] public Category Category { get; set; } = new Category();
        [JsonPropertyName("photoUrls")] public List<string> PhotoUrls { get; set; } = new List<string> { "https://example.com/photo.jpg" };
        [JsonPropertyName("tags")] public List<Tag> Tags { get; set; } = new List<Tag> { new Tag() };
        [JsonPropertyName("status")] public string Status { get; set; } = new DataGenerator().RandomStr(8);

        /// <summary>Serialises this instance to a JSON string for use as a request body.</summary>
        public string ToJson() => JsonSerializer.Serialize(this);
    }

    public class Category
    {
        [JsonPropertyName("id")] public int Id { get; set; } = new DataGenerator().RandomId(1, 100000);
        [JsonPropertyName("name")] public string Name { get; set; } = new DataGenerator().ProductName();
    }

    public class Tag
    {
        [JsonPropertyName("id")] public int Id { get; set; } = new DataGenerator().RandomId(1, 100000);
        [JsonPropertyName("name")] public string Name { get; set; } = new DataGenerator().RandomStr(8);
    }
}
