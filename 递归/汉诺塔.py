def move_tower(height, from_pole, with_pole, to_pole):
    if height>=1:
        move_tower(height-1, from_pole, to_pole, with_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, from_pole, to_pole)

def move_disk(fp,tp):
    print("moving disk from",fp,"to",tp)


move_tower(5,"A","B","C")

