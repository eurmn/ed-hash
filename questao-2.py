class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def hash_function1(self, key):
        return hash(key) % self.size

    def hash_function2(self, key):
        return (hash(key) * 2) % self.size

    def set_val(self, key, val):
        hashed_key1 = self.hash_function1(key)
        hashed_key2 = self.hash_function2(key)
        bucket1 = self.hash_table[hashed_key1]
        bucket2 = bucket1[hashed_key2]
        found_key = False
        for index, record in enumerate(bucket2):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket2[index] = (key, val)
        else:
            bucket2.append((key, val))

    def get_val(self, key):
        hashed_key1 = self.hash_function1(key)
        hashed_key2 = self.hash_function2(key)
        bucket1 = self.hash_table[hashed_key1]
        bucket2 = bucket1[hashed_key2]
        for index, record in enumerate(bucket2):
            record_key, record_val = record
            if record_key == key:
                return record_val
        return None

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = HashTable(10)

# Inserindo valores
hash_table.set_val('nome1', 'valor1')
hash_table.set_val('nome2', 'valor2')
hash_table.set_val('nome3', 'valor3')

# Obtendo valores
print(hash_table.get_val('nome1'))  # valor1
print(hash_table.get_val('nome2'))  # valor2
print(hash_table.get_val('nome3'))  # valor3

# Imprimindo a tabela hash
print(hash_table)