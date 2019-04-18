<template>
    <div>
        Hi <br>
        {{midiTest}}
        {{notes}} <br>
        {{velocities}} <br>
        {{duration}} <br>
        {{offset}}
    </div>
</template>
<script>
/* eslint-disable */
import WebMidi from 'webmidi'
 export default {
     data() {
         return {
             notes: [],
             velocities: [],
             duration: [],
             offset: [],
             chordCheck: 0,
             currentNote: [],
             timeUsed: [],
             startTime: [],
             stopTime: [],
             currentVelocity: [],
             allNote : {36: 'C1', 48: 'C2', 60: 'C3', 72: 'C4', 37: 'C#1', 49: 'C#2', 61: 'C#3', 73: 'C#4', 38: 'D1', 50: 'D2', 62: 'D3', 74: 'D4', 39: 'D#1', 51: 'D#2', 63: 'D#3', 75: 'D#4', 40: 'E1', 52: 'E2', 64: 'E3', 76: 'E4', 41: 'F1', 53: 'F2', 65: 'F3', 77: 'F4', 42: 'F#1', 54: 'F#2', 66: 'F#3', 78: 'F#4', 43: 'G1', 55: 'G2', 67: 'G3', 79: 'G4', 44: 'G#1', 56: 'G#2', 68: 'G#3', 80: 'G#4', 45: 'A1', 57: 'A2', 69: 'A3', 81: 'A4', 46: 'A#1', 58: 'A#2', 70: 'A#3', 82: 'A#4', 47: 'B1', 59: 'B2', 71: 'B3', 83: 'B4', 84: 'C5'},
         }
     },
     methods: {
        onMIDISuccess(midiAccess) {
            for (var input of midiAccess.inputs.values())
                input.onmidimessage = this.getMIDIMessage;
            var inputs = midiAccess.inputs;
            var outputs = midiAccess.outputs;
        },
        getMIDIMessage(message) {
            var command = message.data[0];
            var note = message.data[1];
            var velocity = (message.data.length > 2) ? message.data[2] : 0; // a velocity value might not be included with a noteOff command
            switch (command) {
                case 144: // note on
                    if (velocity > 0) {
                        this.currentNote.push(this.allNote[note]);
                        this.noteOn(this.allNote[note]);
                        this.currentVelocity[this.allNote[note]] = velocity;
                    }
                    break;
                case 128: // note off
                    this.notes.push(this.allNote[note])
                    this.velocities.push(this.currentVelocity[this.allNote[note]])
                    this.noteOff(this.allNote[note],this.currentVelocity[this.allNote[note]]);
                    this.duration.push(this.timeUsed[this.allNote[note]]*2)
                    // if(this.offset.length == 0)
                    // {
                    //     this.offset.push(1)
                    // }
                    // else
                    // {
                    //     var a = this.currentNote[0]
                    //     console.log((this.startTime[this.allNote[note]] - this.startTime[a])/1000*2);
                    //     console.log(this.startTime[this.allNote[note]]);
                    //     console.log(this.startTime[1]);           
                    //     this.offset.push(
                    //         (this.startTime[this.allNote[note]] - this.startTime[a])/1000*2
                    //     )
                    // }
                    var popNote = this.currentNote;
                    this.currentNote = [];
                    for(var i=0;i<popNote.length;i++)
                    {
                        if(popNote[i] != this.allNote[note])
                        {
                            this.currentNote.push(popNote[i])
                        }
                        else
                        {
                            var previousNote = popNote[i];
                        }
                    }
                    
                    // console.log(this.allNote[note]," : ",this.currentNote);
                    break;
                // we could easily expand this switch statement to cover other types of commands such as controllers or sysex
            }
            if(this.currentNote.length == 0)
            {
                this.chordCheck = 3
            }
        },
        noteOn(note) {
            this.startTimer(note)
        },
        noteOff(note,velocity) {
            this.stopTimer(note,velocity)
        },

        startTimer(note) {
            this.startTime[note] = new Date();
        },
        stopTimer(note,velocity) {
            this.stopTime[note] = new Date();
            this.timeUsed[note] = (this.stopTime[note] - this.startTime[note])/1000;
            this.showData(note,velocity,this.timeUsed[note]);
        },
        showData(note,velocity,timeUsed) {
            console.log(note,velocity,timeUsed*2);
            console.log("Time Used:" + timeUsed,"s.");
        },
        onMIDIFailure() {
            console.log('Could not access your MIDI devices.');
        },
     },
     computed: {
         midiTest() {
            navigator.requestMIDIAccess()
                .then(this.onMIDISuccess, this.onMIDIFailure);
         },
     },
 }
</script>
