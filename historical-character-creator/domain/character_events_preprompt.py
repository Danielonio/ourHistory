characterEventsPreprompt: str = '''
I want to know 5 important key events in the life of a known historical character.
Answer me in JSON format like so: 

{"name": n,"events":  [{"date": d, "description": des, "place": p }}]}

where n is the complete name of the character,
d is the date in which the event took place in ISO format, 
des is a description of the event the character was involved with 
and p is the name of the place it happenned. p must be in JSON format with this properties
name: n, coordinates: c, where n is the current name of the place, and c are the coordenates of the place in JSON format like so
{"latitude": x, "longitude": y}.

The events in the array should be ordered by the date field.
The first event in the array has to be the day the character was born.
The last event in the array has to be the day the character died.

The name of the character you have to inform about is: 
'''
