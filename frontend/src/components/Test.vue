<template>
    <div>
        Hi <br>
        {{midiTest}}
    </div>
</template>
<script>
/* eslint-disable */
import WebMidi from 'webmidi'
 export default {
     computed: {
         midiTest() {
            var timeUsed = 0;
            var startTime = 0;
            var stopTime = 0;
            var correctChord = [60, 64, 67, 70]; // C7 chord starting on middle C
            var activeChord = [];
            var correctNoteSequence = [60, 65, 69, 65, 69, 67, 65, 62, 60]; // Amazing Grace in F
            var activeNoteSequence = [];
            var currentStep = 0;
            navigator.requestMIDIAccess()
                .then(onMIDISuccess, onMIDIFailure);

            function onMIDISuccess(midiAccess) {
                for (var input of midiAccess.inputs.values())
                    input.onmidimessage = getMIDIMessage;
                var inputs = midiAccess.inputs;
                var outputs = midiAccess.outputs;
            }
            function getMIDIMessage(message) {
                var command = message.data[0];
                var note = message.data[1];
                var velocity = (message.data.length > 2) ? message.data[2] : 0; // a velocity value might not be included with a noteOff command
                 switch (command) {
                    case 144: // note on
                        if (velocity > 0) {
                            noteOn(note);
                        }
                        break;
                    case 128: // note off
                        noteOff(note);
                        break;
                    // we could easily expand this switch statement to cover other types of commands such as controllers or sysex
                }
            }

            function noteOn(note) {
                console.log(note)
                startTimer()
                // console.log("In NoteOn")
                // switch(currentStep) {
                //     // If the game hasn't started yet.
                //     // The first noteOn message we get will run the first sequence
                //     case 0: 
                //         // Run our start up sequence
                //         runSequence('gamestart');
                //         // Increment the currentStep so this is only triggered once
                //         currentStep++;
                        
                //         break;
                //      // The first lock - playing a correct sequence
                //     case 1:
                //         console.log("NoteOn case 1")
                //         activeNoteSequence.push(note);

                //         // when the array is the same length as the correct sequence, compare the two
                //         if (activeNoteSequence.length == correctNoteSequence.length) {
                //             var match = true;
                //             for (var index = 0; index < activeNoteSequence.length; index++) {
                //                 if (activeNoteSequence[index] != correctNoteSequence[index]) {
                //                     match = false;
                //                     break;
                //                 }
                //             }
                            
                //         }
                //         if (match) {
                //             // Run the next sequence and increment the current step
                //             runSequence('lock1');
                //             currentStep++;
                //         } else {
                //             // Clear the array and start over
                //             activeNoteSequence = [];
                //         }
                //     break;
                //     case 2:
                //         // add the note to the active chord array
                //         activeChord.push(note);

                //         // If the array is the same length as the correct chord, compare
                //         if (activeChord.length == correctChord.length) {
                //             var match = true;
                //             for (var index = 0; index < activeChord.length; index++) {
                //                 if (correctChord.indexOf(activeChord[index]) < 0) {
                //                     match = false;
                //                     break;
                //                 }
                //             }

                //             if (match) {
                //                 runSequence('lock2');
                //                 currentStep++;
                //             }
                //         }
                //     break;
                // }
            }

            function noteOff(note) {
                console.log(note)
                stopTimer()
                // console.log("In NoteOff")
                // switch(currentStep) {
                //     case 2:
                //         // Remove the note value from the active chord array
                //         activeChord.splice(activeChord.indexOf(note), 1);
                //         break;
                // }
            }

            function startTimer() {
                startTime = new Date();
                console.log(startTime)
            }
            function stopTimer() {
                stopTime = new Date();
                timeUsed = stopTime - startTime;
                console.log(stopTime)
                console.log("Time Used:" + timeUsed/1000)
            }
            function onMIDIFailure() {
                console.log('Could not access your MIDI devices.');
            }
         },
         webmidiTest() {
             // Enable WebMidi.js
            WebMidi.enable(function (err) {

            if (err) {
                console.log("WebMidi could not be enabled.", err);
            }

            // Viewing available inputs and outputs
            console.log(WebMidi.inputs);
            console.log(WebMidi.outputs);

            // Display the current time
            console.log(WebMidi.time);

            // Retrieving an output port/device using its id, name or index
            // var output = WebMidi.getOutputById("123456789");
            var output = WebMidi.getOutputByName("MIDIOUT2 (Launchkey MIDI)");
            // output = WebMidi.outputs[0];

            // Play a note on all channels of the selected output
            output.playNote("C3");

            // Play a note on channel 3
            output.playNote("Gb4", 3);

            // Play a chord on all available channels
            output.playNote(["C3", "D#3", "G3"]);

            // Play a chord on channel 7
            output.playNote(["C3", "D#3", "G3"], 7);

            // Play a note at full velocity on all channels)
            output.playNote("F#-1", "all", {velocity: 1});

            // Play a note on channel 16 in 2 seconds (relative time)
            output.playNote("F5", 16, {time: "+2000"});

            // Play a note on channel 1 at an absolute time in the future
            output.playNote("F5", 16, {time: WebMidi.time + 3000});

            // Play a note for a duration of 2 seconds (will send a note off message in 2 seconds). Also use
            // a low attack velocity
            output.playNote("Gb2", 10, {duration: 2000, velocity: 0.25});

            // Stop a playing note on all channels
            output.stopNote("C-1");

            // Stopping a playing note on channel 11
            output.stopNote("F3", 11);

            // Stop a playing note on channel 11 and use a high release velocity
            output.stopNote("G8", 11, {velocity: 0.9});

            // Stopping a playing note in 2.5 seconds
            output.stopNote("Bb2", 11, {time: "+2500"});

            // Send polyphonic aftertouch message to channel 8
            output.sendKeyAftertouch("C#3", 8, 0.25);

            // Send pitch bend (between -1 and 1) to channel 12
            output.sendPitchBend(-1, 12);

            // You can chain most method calls
            output.playNote("G5", 12)
                .sendPitchBend(-0.5, 12, {time: 400}) // After 400 ms.
                .sendPitchBend(0.5, 12, {time: 800})  // After 800 ms.
                .stopNote("G5", 12, {time: 1200});    // After 1.2 s.

            // Retrieve an input by name, id or index
            var input = WebMidi.getInputByName("MIDIIN2 (Launchkey MIDI)");
            console.log(input)
            // Listen for a 'note on' message on all channels
            input.addListener('noteon', "all",
                function (e) {
                console.log("Received 'noteon' message (" + e.note.name + e.note.octave + ").");
                }
            );

            // Listen to pitch bend message on channel 3
            input.addListener('pitchbend', 3,
                function (e) {
                console.log("Received 'pitchbend' message.", e);
                }
            );

            // Listen to control change message on all channels
            input.addListener('controlchange', "all",
                function (e) {
                console.log("Received 'controlchange' message.", e);
                }
            );

            // Check for the presence of an event listener (n such cases, you cannot use anonymous functions).
            function test(e) { console.log(e); }
            input.addListener('programchange', 12, test);
            console.log("Has event listener: ", input.hasListener('programchange', 12, test));

            // Remove a specific listener
            input.removeListener('programchange', 12, test);
            console.log("Has event listener: ", input.hasListener('programchange', 12, test));

            // Remove all listeners of a specific type on a specific channel
            input.removeListener('noteoff', 12);

            // Remove all listeners for 'noteoff' on all channels
            input.removeListener('noteoff');

            // Remove all listeners on the input
            input.removeListener();

            });
         },
         test() {
             var a = 0
             WebMidi.enable(function(err) {
                while(a== 0){
                    console.log("inwhile")
                    WebMidi.inputs[0].addListener('pitchbend', "all", function(e) {
                        console.log("In la")
                        console.log("Pitch value: " + e.value);
                        a = 1;
                        });
                }
            });
         }
     },
    //  created() {
    //      if (navigator.requestMIDIAccess) {
    //         console.log('This browser supports WebMIDI!');
    //     } else {
    //         console.log('WebMIDI is not supported in this browser.');
    //     }
    //     WebMidi.enable(function () {
    //         // Viewing available inputs and outputs
    //         console.log(WebMidi.inputs);
    //         console.log(WebMidi.outputs);
    //         WebMidi.outputs[1].playNote("C3");
    //     })
    //  }
 }
</script>
