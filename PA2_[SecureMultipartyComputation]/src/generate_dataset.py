import sys, random, math, copy

music_genre = ["Jazz", "Rock", "Hip Hop", "Blues", "Classic", \
               "Eletronic", "Pop", "Kpop", "Jpop", "Country", \
               "R&B", "Funk", "Reggae", "Alternative", "Folk"]

artists = ["artist1", "artist2", "artist3", "artist4", "artist5", "artist6", \
           "artist7", "artist8", "artist9", "artist10", "artist11", "artist12", \
           "artist13", "artist14", "artist15", "artist16", "artist17", "artist18"]

def clear_songs(csv_file):
    i=0
    towrite_csv = ""
    with open(csv_file, "r") as f:
        for l in f.readlines():
            l=l.split(",")

            if i !=0:
                if i<2000:
                    towrite_csv+=l[0]+","+l[1]+","+str(math.floor(int(l[2])/1000))+","+random.choice(music_genre) \
                               +","+l[4]+","+str(random.randint(1,5))+"\n"
                else:
                    towrite_csv+=l[0]+","+l[1][:-1]+","+str(random.randint(180, 300))+","+random.choice(music_genre) \
                               +","+str(random.randint(1999,2023))+","+str(random.randint(1,5))+"\n"

            i+=1

    with open("new_new.csv", "w") as f2:
        f2.write(towrite_csv)

def gen_data(n):
    size = 2000000-1 # change, regarding the size of your original dataset
    if n > (size+1)/2:
        print("Error: use a <n> lower than", (size+1)/2)

    n_intersets = random.randint(math.floor(n*0.3), math.floor(n*0.7))
    print(n_intersets)
    data = []
    part1 = []; part2 = []

    with open("new_new.csv", "r") as f:
        data = copy.deepcopy(f.readlines())
        index = 0;
        fin = (n-n_intersets)*2 + n_intersets
        while(index < fin):
            if n_intersets > 0:
                part1.append(data[index]); part2.append(data[index])
                n_intersets -=1
                index += 1
            else:
                part1.append(data[index])
                index += 1
                part2.append(data[index])
                index += 1
            
        random.shuffle(part1)
        random.shuffle(part2)

    with open("part1.csv", "w") as f2:
        f2.write("".join(part1))

    with open("part2.csv", "w") as f3:
        f3.write("".join(part2))

def gen_first_data(n):
    size = 2000000-1 # change, regarding the size of your original dataset
    if n > (size+1)/2:
        print("Error: use a <n> lower than", (size+1)/2)

    n_intersets = random.randint(math.floor(n*0.3), math.floor(n*0.7))
    data = []
    part1 = []; part2 = []

    with open("new_new.csv", "r") as f:
        data = copy.deepcopy(f.readlines())
        for i in range(n):
            if n_intersets > 0:
                index = random.randint(0, size)
                part1.append(data[index]); part2.append(data[index])
                data.remove(data[index])
                n_intersets -=1
                size -= 1
            else:
                index = random.randint(0, size)
                part1.append(data[index])
                data.remove(data[index])
                size -= 1

                index = random.randint(0, size)
                part2.append(data[index])
                data.remove(data[index])
                size -= 1
            
        random.shuffle(part1)
        random.shuffle(part2)

    with open("part1.csv", "w") as f2:
        f2.write("".join(part1))

    with open("part2.csv", "w") as f3:
        f3.write("".join(part2))

def new(n):
    with open("new_new.csv", "w") as f4:
        for i in range(n):
            f4.write(random.choice(artists)+",music"+str(i+1)+"\n")

if __name__=="__main__":
    if(len(sys.argv)==3):
        if(sys.argv[1]=="-s"):
            clear_songs(sys.argv[2])
        elif(sys.argv[1]=="-g"):
            gen_data(int(sys.argv[2]))
        elif(sys.argv[1]=="-n"):
            new(int(sys.argv[2]))
    else:
        print("Number of arguments invalid\nUsage:\n" + \
              "\tpython generate_dataset.py -g <size of datasets>\n" + \
              "\tpython generate_dataset.py -s <csv file to use>\n" + \
              "\tpython generate_dataset.py -n <size of dataset>\n")