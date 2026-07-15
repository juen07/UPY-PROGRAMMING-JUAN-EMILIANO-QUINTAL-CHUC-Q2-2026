class NotVerbError(Exception):
	pass

class NotLowercase(Exception):
	pass

class NotSpace(Exception):
	pass

#Required structures
pronouns = ["Yo", "Tu", "Él", "Nosotros", "Vosotros", "ellos"]

endings = {
	"ar": ["o", "as", "a", "amos", "ais", "an"],
	"er": ["o", "es", "e", "emos", "eis", "en"],
	"ir": ["o", "es", "e", "imos", "is", "en"]
}

verb = input("Write a spanish verb (ar/er/ir): ")

try:
	stem = verb[:-2]
	ending = verb[-2:]

	if not verb.islower():
		raise  NotLowercase()
	
	elif any(c.isspace() for c in verb):
		raise NotSpace()
	
	elif not verb.isalpha() or ending not in endings.keys():
	    raise NotVerbError()

except NotVerbError:
	print("El verbo debe terminar en ar, er, ir")

except NotLowercase:
	print("El verbo debe estar en minúsculas")

except NotSpace:
	print("El verbo no debe tener espacios extra")
	
else:
    conjugations = endings[ending]
    for index, pronoun  in enumerate(conjugations):
        conjugation = stem + pronoun
        termination = pronouns[index]	
        print(f"{termination} {conjugation}") 
	

