class Friends:
    members = ["Ross", "Rachel", "Joey", "Phoebe", "Chandler", "Monica"]
    def __len__(self):
        return len(self.members)

my_friends = Friends()

print(my_friends)
print(len(my_friends))
