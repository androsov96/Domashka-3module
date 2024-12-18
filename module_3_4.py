def single_root_words(root_world, *other_worlds):
    same_words = []
    for i in other_worlds:
        if root_world.lower() in i.lower():
            same_words.append(i)
        if i.lower() in root_world.lower():
            same_words.append(i)
    return same_words

print(single_root_words('Rich', 'Richiest', 'orichalcum', 'cheers', 'RichIes'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
