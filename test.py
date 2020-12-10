from mingus.containers import *
from mingus.midi import fluidsynth
import time
from mingus import midi
from mingus.midi.midi_file_out import write_NoteContainer

fluidsynth.init("/Users/Thomas_Stuart/PycharmProjects/MusFinalProject/all.sf2")
#fluidsynth.init("/Users/Thomas_Stuart/PycharmProjects/MusFinalProject/grandPiano.sf2")
#fluidsynth.init("/Users/Thomas_Stuart/PycharmProjects/MusFinalProject/AG.sf2")
#fluidsynth.init("/Users/Thomas_Stuart/PycharmProjects/MusFinalProject/EG.sf2")
#fluidsynth.init("/Users/Thomas_Stuart/PycharmProjects/MusFinalProject/bass.sf2")

# fluidsynth.set_instrument(1, 40) #guitar
# fluidsynth.set_instrument(1, 42) #guitar
# fluidsynth.set_instrument(1, 35) #horn

# fluidsynth.play_Note(Note("C-5"))
# time.sleep(1)
# fluidsynth.play_Note(Note("C-5"))
# time.sleep(1)
# fluidsynth.play_Note(Note("C-5"))
# time.sleep(1)
# fluidsynth.play_Note(Note("C-5"))
# time.sleep(1)
# fluidsynth.play_Note(Note("E-5"))
# time.sleep(1)
# fluidsynth.play_Note(Note("E-5"))
# time.sleep(1)
# fluidsynth.play_Note(Note("E-5"))
# time.sleep(1)
# fluidsynth.play_Note(Note("E-5"))

fluidsynth.set_instrument(1, 3) #piano
n = Note("C-5")
n.channel = 5
n.velocity = 50
fluidsynth.play_Note(n)

fluidsynth.set_instrument(1, 3) #piano
n = Note("D-5")
n.channel = 5
n.velocity = 50
fluidsynth.play_Note(n)

fluidsynth.set_instrument(1, 3) #piano
n = Note("E-5")
n.channel = 5
n.velocity = 50
fluidsynth.play_Note(n)

# fluidsynth.set_instrument(1, 40) #guitar
# n = Note("C-5")
# n.channel = 1
# n.velocity = 50
# fluidsynth.play_Note(n)

time.sleep(2)
fluidsynth.stop_Note(Note("C-5"), 1)

fluidsynth.set_instrument(1, 3) #piano
n = Note("E-5")
n.channel = 5
n.velocity = 50
fluidsynth.play_Note(n)

# fluidsynth.set_instrument(1, 35) #guitar
# n = Note("E-5")
# n.channel = 1
# n.velocity = 50
# fluidsynth.play_Note(n)

# nc = NoteContainer(["C-5", "C-5", "E-5"])
# write_NoteContainer("test.mid", nc)
