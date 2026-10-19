using System;
using System.Collections.Generic;
using System.Linq;
using Bogus;

namespace Api2Test.Generated.Libraries
{
    /// <summary>Generates field values for test data (the Data Library). Request classes call
    /// it as <c>new DataGenerator().Method()</c>.</summary>
    public class DataGenerator
    {
        private readonly Faker _faker = new Faker();

        /// <summary>A random id within a range.</summary>
        public int RandomId(int min = 1, int max = 100000) => _faker.Random.Int(min, max);

        /// <summary>A random integer within a range.</summary>
        public int RandomInt(int min = 0, int max = 100) => _faker.Random.Int(min, max);

        /// <summary>A product-style name.</summary>
        public string ProductName() => $"{_faker.Commerce.ProductAdjective()} {_faker.Commerce.Product()}";

        /// <summary>A random alphanumeric string.</summary>
        public string RandomStr(int length = 8) => _faker.Random.AlphaNumeric(length);

        /// <summary>Todays date, offset by a number of days, as a string.</summary>
        public string DateStr(int daysOffset = 0, string format = "yyyy-MM-dd") =>
            DateTime.Now.AddDays(daysOffset).ToString(format);
    }
}
