using System.Net;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using DataLibrary;
using GeneratedClasses;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace PetStore.Tests
{
    /// <summary>
    /// Generated API test cases for the PetStore /pet endpoints.
    /// One test method per imported endpoint.
    /// </summary>
    [TestClass]
    public class PetApiTests
    {
        private const string BaseUrl = "https://petstore3.swagger.io/api/v3";
        private static readonly HttpClient Client = new();

        private static Pet NewPet() => new()
        {
            Id = DataGenerator.GenerateRandomId(),
            Name = DataGenerator.RandomName(),
            Status = DataGenerator.PickFrom("available", "pending", "sold"),
            PhotoUrls = { "https://example.com/photo.jpg" }
        };

        [TestMethod]
        public async Task AddPet_ReturnsOk()
        {
            var pet = NewPet();
            var content = new StringContent(pet.ToJson(), Encoding.UTF8, "application/json");

            var response = await Client.PostAsync($"{BaseUrl}/pet", content);

            Assert.AreEqual(HttpStatusCode.OK, response.StatusCode);
        }

        [TestMethod]
        public async Task GetPetById_ReturnsOk()
        {
            var pet = NewPet();
            await Client.PostAsync($"{BaseUrl}/pet",
                new StringContent(pet.ToJson(), Encoding.UTF8, "application/json"));

            var response = await Client.GetAsync($"{BaseUrl}/pet/{pet.Id}");

            Assert.AreEqual(HttpStatusCode.OK, response.StatusCode);
            var body = await response.Content.ReadAsStringAsync();
            var fetched = Pet.FromJson(body);
            Assert.IsNotNull(fetched);
            Assert.AreEqual(pet.Id, fetched!.Id);
        }

        [TestMethod]
        public async Task UpdatePet_ReturnsOk()
        {
            var pet = NewPet();
            pet.Status = "sold";
            var content = new StringContent(pet.ToJson(), Encoding.UTF8, "application/json");

            var response = await Client.PutAsync($"{BaseUrl}/pet", content);

            Assert.AreEqual(HttpStatusCode.OK, response.StatusCode);
        }

        [TestMethod]
        public async Task FindByStatus_ReturnsList()
        {
            var response = await Client.GetAsync($"{BaseUrl}/pet/findByStatus?status=available");

            Assert.AreEqual(HttpStatusCode.OK, response.StatusCode);
        }
    }
}
