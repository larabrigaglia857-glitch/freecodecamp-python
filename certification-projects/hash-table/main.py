class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, my_string = ""):
        hashed_value = 0
        for character in my_string:
            hashed_value += ord(character)
        return hashed_value

    def add(self, key, value):
        hashed_value = self.hash(key)
        if hashed_value not in self.collection:
            self.collection[hashed_value] = {}
        self.collection[hashed_value][key] = value
        return self.collection

    def remove(self, key):
        hashed_value = self.hash(key)
        if hashed_value in self.collection:
            if key in self.collection[hashed_value]:
                del self.collection[hashed_value][key]
        return self.collection

    def lookup(self, key):
        hashed_value = self.hash(key)
        if hashed_value in self.collection and key in self.collection[hashed_value]:
            return self.collection[hashed_value][key]
        return None

my_hash_table = HashTable()
print(my_hash_table.hash("golf"))
print(my_hash_table.hash("sport"))
print(my_hash_table.hash("dear"))
print(my_hash_table.hash("friend"))
print(my_hash_table.hash("read"))
print(my_hash_table.hash("book"))
print(my_hash_table.add("golf", "sport"))
print(my_hash_table.add("dear", "friend"))
print(my_hash_table.add("read", "book"))
#print(my_hash_table.add("fcc", "book"))
print(my_hash_table.lookup("golf"))
print(my_hash_table.lookup("cfc"))
