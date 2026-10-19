using System;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using static Api2Test.Generated.Libraries.ApiMethods;
using Api2Test.Generated.Classes.PetStore;

namespace Api2Test.Generated.Tests.PetStore
{
    /// <summary>
    /// One generated test per test case. This one is a 3-step E2E chain built in the extension:
    /// create a pet, capture the id it comes back with, then fetch that pet by id.
    /// The header of the test case chose the base path and the token method, which is why the
    /// method opens with those two lines.
    /// </summary>
    [TestClass]
    public class CreateThenGetPetTests
    {
        [TestMethod]
        public async Task CreateThenGetPet()
        {
            var baseUrl = PetStoreBaseUrl();
            var token = await PetStoreApiKey();

            // Step 1: PostJsonAsync
            var result1 = await PostJsonAsync(token, baseUrl + "/pet", new PetStorePostPet().ToJson());

            // Step 2: ValidateSuccess_200_201Async
            Assert.IsTrue(await ValidateSuccess_200_201Async(result1));

            // Step 3: ExtractFieldAsync
            var petId = await ExtractFieldAsync<int>(result1, "id");

            // Step 4: GetAsync
            var result4 = await GetAsync(token, baseUrl + "/pet/" + petId);

            // Step 5: ValidateSuccess_200_201Async
            Assert.IsTrue(await ValidateSuccess_200_201Async(result4));
        }
    }
}
