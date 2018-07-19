name = input(str("What is your name?"))
age = int(input("\nAh, good evening "+name+",and how old are you?"))

while age > 99:
  age = int(input("\nCome on now, "+name+", I find it hard to believe someone that old can even use a computer! \nPerhaps you can put your real age...?"))
years_until_100 = 100-age

print("\nExcellent. According to my calculations, that means you will reach 100 years of age in just",years_until_100,"years!")
print("\nIsn't that good news,"+name+"?")
wow = str(input("enter wow if impressed:"))

if wow in ['wow', 'wow!','WOW','Wow']:
 print("\nTell me a little more about how you feel,",name+":")
else:
 print("\nSigh. Kids these days.")
 print("\nTell me a little more about how you feel")

answer1 = input(str(print("\na) Yes, splendid news - I have years to eat cheese and drink wine and watch the world socially implode! \n\n b) Erm, no not really. I'd like a lot longer - I've only tried a handful of cheeses and I just need more time! \n\n c)Fuck off, I don't have to tell you anything. \n\nAnswer: ")))

if answer1 in ['a', 'A', 'a)', 'A)']:
 print("Exactly! Kudos on the positive outlook.")
elif answer1 in ['b', 'B', 'b)' 'B']:
 print("Don't worry",name,"there is plenty of time for that! I can help you find some good cheese. Don't cry buddy.")
elif answer1 in ['C','c','C)','c)']:
 print("Well. I mean, that's pretty rude. But fair enough - I'll take my prize of a lifetime supply of cheese and wine elsewhere. Dick.")
else:
 print("\nI don't think that was an option....")
