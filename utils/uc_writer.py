from pyspark.sql import SparkSession
from pyspark.sql import DataFrame

spark = SparkSession.builder.getOrCreate()

def ensure_catalog_and_schema(catalog: str, schema: str):
    """
    Ensure that the Unity Catalog catalog and schema exist.
    """
    spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog}")
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{schema}")

def write_to_uc(
    df: DataFrame,
    catalog: str,
    schema: str,
    table_name: str,
    mode: str = "overwrite",
    create_catalog_schema: bool = True
) -> str:
    """
    Write a Spark DataFrame to a Unity Catalog Delta table.
    
    Args:
        df (DataFrame): Spark DataFrame to write.
        catalog (str): Target Unity Catalog.
        schema (str): Target schema.
        table_name (str): Table name.
        mode (str): Write mode. Default: overwrite.
        create_catalog_schema (bool): Automatically create catalog/schema if missing.

    Returns:
        str: Fully-qualified table name.
    """

    if create_catalog_schema:
        ensure_catalog_and_schema(catalog, schema)

    full_table_name = f"{catalog}.{schema}.{table_name}"
    (
        df.write
          .format("delta")
          .mode(mode)
          .saveAsTable(full_table_name)
    )

    return full_table_name