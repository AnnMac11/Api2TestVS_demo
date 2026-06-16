using System;

namespace DataLibrary
{
    /// <summary>
    /// Reusable test-data methods. These map to entries in the API2Test
    /// Data Library and are referenced from the Data Dictionary.
    /// </summary>
    public static class DataGenerator
    {
        private static readonly Random Rng = new();

        public static long GenerateRandomId() => Rng.Next(1, 1_000_000);

        public static int RandomInt(int min, int max) => Rng.Next(min, max + 1);

        public static string RandomName()
        {
            string[] names = { "Rex", "Bella", "Milo", "Luna", "Charlie" };
            return names[Rng.Next(names.Length)];
        }

        public static string PickFrom(params string[] values) =>
            values[Rng.Next(values.Length)];
    }
}
