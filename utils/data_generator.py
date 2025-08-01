from faker import Faker
from datetime import datetime, timedelta
import random
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DateType, TimestampType

spark = SparkSession.builder.getOrCreate()
fake = Faker()

def generate_synthetic_data(spark, catalog, schema, table_name, columns, row_count=1000, mode="overwrite"):
    fields = []
    for col in columns:
        if col["type"] == "string":
            fields.append(StructField(col["name"], StringType(), True))
        elif col["type"] == "integer":
            fields.append(StructField(col["name"], IntegerType(), True))
        elif col["type"] == "float":
            fields.append(StructField(col["name"], DoubleType(), True))
        elif col["type"] == "date":
            fields.append(StructField(col["name"], DateType(), True))
        elif col["type"] == "timestamp":
            fields.append(StructField(col["name"], TimestampType(), True))
        else:
            raise ValueError(f"Unsupported data type: {col['type']}")

    schema_def = StructType(fields)

    def row_gen(_):
        row = []
        for col in columns:
            if col["type"] == "string":
                row.append(fake.word())
            elif col["type"] == "integer":
                row.append(random.randint(0, 10000))
            elif col["type"] == "float":
                row.append(round(random.uniform(0, 10000), 2))
            elif col["type"] == "date":
                row.append(fake.date_between(start_date="-1y", end_date="today"))
            elif col["type"] == "timestamp":
                row.append(datetime.now() - timedelta(days=random.randint(0, 365)))
        return tuple(row)

    rdd = spark.sparkContext.parallelize([row_gen(i) for i in range(row_count)])
    df = spark.createDataFrame(rdd, schema_def)
    full_name = f"{catalog}.{schema}.{table_name}"
    df.write.format("delta").mode(mode).saveAsTable(full_name)
    return full_name
