'''
Write a Flask server application that returns a map of a Gale crater showing Curiosity's 
position on the Sol requested by the user 
Hints: 
    . Find the first location in locations.xml where startSol <= requested day <= endSol 
    . Use matplotlib.pyplot.savefig() to write to an io.BytesIo() buffer before converting to base64
'''