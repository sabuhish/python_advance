import requests

'''
error that happens in your program therefore it should stop you can except many types of errors
'''
# if input str, will give an error
number = input("Number here pls: ")

try:
    print(int(number) * 2) 
    
except ValueError:
    print("invalid operation, did not enter base 10 number, give a try")

except LookupError:
    print("look up error does not goes here, just more expect you can put in case.")


'''
this gonna work as well because program does not crash anymore
'''
print("Salam")

r = requests.get("https://fake.munisisazade.com/")

r_1 = requests.post("https://fake.munisisazade.com/", data= {"text": "Salam dunya"})

try:
    label = r_1.json()["label"]
    print(label)
    # JSONDecodeError as subclass of Valueerror we use Valueerror
except ValueError:
    print("could not decode the JSON reponse")
except KeyError:
    print("just in case if above exceptions does no raise")
