
tones=['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

class key_sig():

    def __init__(self,root):                                    #   initialize by getting the index of the root note
        for index,tone in enumerate(tones):                     #   enumerate so we can loop through the notes to find starting point
            if tone==root:                                      #   self.root is the index of the root, not the letter note
                self.root=index
                break                                           #   once we find it, break out of the loop
    
    def major_scale(self):                                      #   maj scale function. we use the half_steps list to increment.
        half_steps=[2,2,1,2,2,2,1,1]                            #   these are the #'s of half steps between notes in every major scale
        self.maj_scale=[]                                       #   create empty list to append
        interval=0
        for step in range(len(half_steps)):                     #   the loop increments by 1 so we just make sure it gets all the way through the half_steps
            self.maj_scale.append(tones[self.root+interval])
            interval+=half_steps[step]
        return self.maj_scale

    def minor_scale(self):
        half_steps=[2,1,2,2,1,2,2,1]
        self.min_scale=[]
        interval=0
        for step in range(len(half_steps)):
            self.min_scale.append(tones[self.root+interval])
            interval+=half_steps[step]
        return self.min_scale


Key_of_A=key_sig(root='A')
print("A Major Scale: ", Key_of_A.major_scale())
print("A Minor Scale: ", Key_of_A.minor_scale())



Key_of_G_Sharp=key_sig(root='G#')
print("G# Major Scale: ", Key_of_G_Sharp.major_scale())
print("G# Minor Scale: ", Key_of_G_Sharp.minor_scale())

