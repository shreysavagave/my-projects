questions = ["what is the capital of india",
              " what is capital of maharashtra ",
              "who won icc cricket world cup 2011",
              "shrey is in love with"]
options = [ ["a.mumbai", "b.delhi","c.kolkata","d.chennai"],
["a.kolhapur", "b.nashik","c.mumbai","d.pune"] ,
["a.austrialia","b.india","c.pakistan","d.austrialia"],
["aishwarya","kartina","shreya","disha"]]

answers = ["b","a","b","a"]
money = ["10 lakhs ","25 lakhs","50 lakhs","1crore"]
level = [ 1,2,3,4,5,6]


print("\n welcome to shrey savagave's kaun banega karode pati\n ")

for i in range (0,len(questions)):
    print(" level ",level[i])
    print("\n question for rupees ",money[i])
    print("\n", questions[i])
    print("\n",options[i])
    p = input("enter ans\t")
    if(p == answers[i]) :
        print("\n correct answer you won rupees",money[i] ) 
    elif(level[i]>=level[2]):
        print("\n wrong answer you take rupees",money[i-1])
        break
    else:
        print("\n wrong answer you lost")
        break

    if(level[i]==level[3]):
             print("congratulations you become crore pati")