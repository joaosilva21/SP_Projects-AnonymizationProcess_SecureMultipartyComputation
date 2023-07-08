import random, math

def main():
    towrite_csv = ""
    i = 0
    s_ns = [-1]+[239000000 + (i+1)*37 for i in range(70001)]
    masculine = ["Aaron", "Ace", "Abraham", "Barry", "Bernard", "Billy", "Caleb", "Carson", \
                 "Cedric", "David", "Daniel", "Damien", "Eddie", "Edward", "Edgar", "Fabian", \
                 "Freddy", "Frank", "Gabriel", "Gerard", "Giovanni", "Harvey", "Herbert", "Howard", \
                 "Isaac", "Israel", "Ivan", "Jack", "Jamie", "James", "Kevin", "Kim", \
                 "Kenneth", "Leonard", "Lewis", "Lincoln", "Mark", "Mario", "Marcus", "Nelson", \
                 "Norman", "Nicolas", "Oliver", "Oswald", "Oscar", "Peter", "Phillipps", "Paul", \
                 "Ralph", "Ramsey", "Robert", "Sam", "Simon", "Shawn", "Taylor", "Tommy", \
                 "Vincent", "Vivian", "Ulysses", "Walker", "Willian", "Wallace", "Xavier"]
    feminine = ["Adriana", "Alexandra", "Alice", "Bella", "Barbara", "Beatrice", "Carly", "Carol", \
                "Clara", "Daisy", "Danielle", "Dora", "Ellen", "Emily", "Emma", "Fiona", \
                "Francie", "Florence", "Georgina", "Gwen", "Gloria", "Hannah", "Helena", "Hope", \
                "Isabela", "Ivy", "Jade", "Jana", "Jacinta", "Jasmine", "Katy", "Karoline", \
                "Kelly", "Lana", "Leila", "Lara", "Maria", "Madeleine", "Michelle", "Natalie", \
                "Nicola", "Noella", "Olivia", "Pamela", "Paula", "Penelope", "Patrice", "Rachel", \
                "Rebecca", "Rita", "Robin", "Sandra", "Sabrina", "Serena", "Teresa", "Trisha", \
                "Ursula", "Vanessa", "Victoria", "Velma", "Wanda", "Wendy", "Yasmin", "Zoe"]
    surnames = ["Smith", "Davies", "Nicholls", "Hamiton", "Henderson", "May", "Burton", "Newman", \
                "Kelly", "Bell", "Richards", "Webb", "Woods", "Burke", "Austin", "Arnold", \
                "Shaw", "Adams", "Hart", "Rogers", "Palmer", "Reed", "Murphy", "Johnston", \
                "Simpson", "Cox", "Carter", "Potter", "Newton", "Gregory", "Hunter", "Barber", \
                "Owen", "Holmes", "Woodward", "Stephens", "Slater", "Lowe", "Marsh", "Matthews", \
                "Green", "Murray", "Cross", "Ross", "Ward", "Turner", "West", "Knight", \
                "Robinson", "Brown", "Hall", "Hughes", "Wood", "Fox", "Jackson", "Andrews"]

    with open("cardio_train.csv", "r") as f:
        for l in f.readlines():
            l = l.split(";")
            if i == 0:
                l.insert(1, "social_number")
                l[0] = "name"
                towrite_csv += ";".join(l)
            else:
                if l[2] == "1":
                    l[0] = random.choice(feminine)
                else:
                    l[0] = random.choice(masculine)
                l[0] += " " + random.choice(surnames)
                l[1] = str(math.floor(int(l[1])/365))
                l[3] = str(random.randint(140, 160)) if int(l[3]) < 140 else l[3]
                l[4] = str(random.randint(60, 80)) if float(l[4]) < 60 else str(int(float(l[4])))
                l[5] = str(random.randint(120, 200)) if int(l[5]) > 270 or int(l[5]) < 60 else l[5] # sup
                l[6] = str(random.randint(60, 120)) if int(l[6]) > 270 or int(l[6]) < 60 else l[6] # inf

                if int(l[6]) > int(l[5]): 
                    l[6], l[5] = l[5], l[6]

                l.insert(1, str(s_ns[i]))
                towrite_csv += ";".join(l)
            i += 1
            #print(l)

    with open("new_new.csv", "w") as f2:
        f2.write(towrite_csv)

            

if __name__=="__main__":
    main()