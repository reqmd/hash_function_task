from hash_function_task import HashTable

ht = HashTable(size=30000)
ht.fill_random(num_items=30000, collision_keys=100)
uniformity = ht.check_bucket_uniformity()

print("Метрика:", uniformity["metric"])
