
tones=['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

class key_sig():

    def __init__(self,rootnote):                                    
        self.rootnote=[index for index,tone in enumerate(tones) if tone==rootnote][0]

    def major_scale(self):                                      #   maj scale function. we use the half_steps list to increment.
        half_steps=[2,2,1,2,2,2,1,1]                            #   these are the #'s of half steps between notes in every major scale
        self.maj_scale=[]                                       #   create empty list to append
        interval=0
        for step in range(len(half_steps)):                     #   the loop increments by 1 so we just make sure it gets all the way through the half_steps
            self.maj_scale.append(tones[self.rootnote+interval])
            interval+=half_steps[step]
        return self.maj_scale

    def minor_scale(self):
        half_steps=[2,1,2,2,1,2,2,1]
        self.min_scale=[]
        interval=0
        for step in range(len(half_steps)):
            self.min_scale.append(tones[self.rootnote+interval])
            interval+=half_steps[step]
        return self.min_scale

    def M_chords(self):
        self.key_chords=[]
        self.scale=self.maj_scale+self.maj_scale 
        for i in range(0,7):
            self.chord=[self.scale[i]]
            self.chord.append(self.scale[i+2])
            self.chord.append(self.scale[i+4])
            self.key_chords.append(tuple(self.chord))                       
        return self.key_chords

    def m_chords(self):
        self.key_chords=[]
        self.scale=self.min_scale+self.min_scale 
        for i in range(0,7):
            self.chord=[self.scale[i]]
            self.chord.append(self.scale[i+2])
            self.chord.append(self.scale[i+4])
            self.key_chords.append(tuple(self.chord))                       
        return self.key_chords

Key_of_A=key_sig(rootnote='A')
print("A Major Scale: ", Key_of_A.major_scale())
print("A Minor Scale: ", Key_of_A.minor_scale())
print("Chords in A Major: ", Key_of_A.M_chords())
print("Chords in A Minor: ", Key_of_A.m_chords())


Key_of_G_Sharp=key_sig(rootnote='G#')
print("G# Major Scale: ", Key_of_G_Sharp.major_scale())
print("G# Minor Scale: ", Key_of_G_Sharp.minor_scale())



