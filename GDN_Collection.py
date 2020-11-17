import csv
from c8 import C8Client

print("--- Connecting to C8")
client = C8Client(protocol='https', host='gdn1.macrometa.io', port=443,
                         email='teja@macrometa.io', password="Welcome123",
                         geofabric='_system')

collection_name = 'Data'
if client.has_collection(collection_name):
    print("Collection exists")
else:
    client.create_collection_kv(name=collection_name)

data = open("data.csv", 'r')
csv_file = csv.DictReader(data)
coll = client.get_collection(collection_name)


for row in csv_file:
    coll.insert(dict(row))
# client.insert_key_value_pair(collection_name, data1)
print("KV Pairs Inserted")
# # # Get KV count of a collection
print("Number of kv pairs in your collection: ",client.get_kv_count(collection_name))

#Delete Collection
#print("Collection Deleted: ",client.delete_collection_kv(collection_name))
