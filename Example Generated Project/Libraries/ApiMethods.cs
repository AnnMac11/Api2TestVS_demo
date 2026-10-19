using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace Api2Test.Generated.Libraries
{
    /// <summary>
    /// The API Method Library, generated into your project as one static class. The shipped
    /// library has 26 methods covering HTTP verbs, status validation, response extraction, base
    /// paths and authentication; this example keeps only the six the test below calls.
    /// </summary>
    public static class ApiMethods
    {
        // Shared client for the helpers that do not open their own.
        private static readonly HttpClient _httpClient = new HttpClient();

        // ---------- Base Path ----------

        /// <summary>Base URL for the PetStore API.</summary>
        public static string PetStoreBaseUrl() => "https://petstore3.swagger.io/api/v3";

        // ---------- Authentication ----------

        /// <summary>The PetStore demo key. A real project reads this from configuration.</summary>
        public static Task<string> PetStoreApiKey() => Task.FromResult("special-key");

        // ---------- HTTP Requests ----------

        /// <summary>POSTs a JSON body to a URL with a bearer token.</summary>
        public static async Task<HttpResponseMessage> PostJsonAsync(string token, string url, string jsonBody)
        {
            using (var request = new HttpRequestMessage(HttpMethod.Post, url))
            {
                request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token);
                request.Headers.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
                request.Content = new StringContent(jsonBody, Encoding.UTF8, "application/json");
                return await _httpClient.SendAsync(request);
            }
        }

        /// <summary>GETs a URL with a bearer token.</summary>
        public static async Task<HttpResponseMessage> GetAsync(string token, string url)
        {
            using (var request = new HttpRequestMessage(HttpMethod.Get, url))
            {
                request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token);
                request.Headers.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
                return await _httpClient.SendAsync(request);
            }
        }

        // ---------- Response ----------

        /// <summary>True when the response status is 200 or 201.</summary>
        public static Task<bool> ValidateSuccess_200_201Async(HttpResponseMessage response)
        {
            var code = (int)response.StatusCode;
            return Task.FromResult(code == 200 || code == 201);
        }

        /// <summary>
        /// Reads one field out of a JSON response body in its native type, so a captured id can
        /// drop straight into a typed request field. The test names the type argument.
        /// </summary>
        public static async Task<T> ExtractFieldAsync<T>(HttpResponseMessage response, string fieldPath)
        {
            var body = await response.Content.ReadAsStringAsync();
            using (var document = JsonDocument.Parse(body))
            {
                var element = document.RootElement;
                foreach (var segment in fieldPath.Split(new[] { "." }, StringSplitOptions.None))
                {
                    element = element.GetProperty(segment);
                }

                return JsonSerializer.Deserialize<T>(element.GetRawText())!;
            }
        }
    }
}
