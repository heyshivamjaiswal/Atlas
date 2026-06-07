from pymilvus import (
    connections,
    Collection,
    CollectionSchema,
    FieldSchema,
    DataType
)

connections.connect(
    alias="default",
    host="localhost",
    port="19530"
)