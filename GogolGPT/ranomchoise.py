import os, random, shutil

for i in range(6847):
	img = random.choice(os.listdir("images")) 
	shutil.move(f'images/{img}', "empty/")

print(img)
