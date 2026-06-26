#Required structures
pronouns = ["Yo", "Tu", "Él", "Nosotros", "Vosotros", "ellos"]

endings = {
	"ar": ["o", "as", "a", "amos", "ais", "an"],
	"er": ["o", "es", "e", "emos", "eis", "en"],
	"ir": ["o", "es", "e", "imos", "is", "en"]
}

verb = input("Write a spanish verb (ar/er/ir): ")

stem = verb[:-2]
ending = verb[-2:]

conjugations = endings[ending]
for index, pronoun  in enumerate(conjugations):
	conjugation = stem + pronoun
	termination = pronouns[index]	
	print(f"{termination} {conjugation}") 
	

