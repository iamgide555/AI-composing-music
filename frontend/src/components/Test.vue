<template>
    <div>
        Hi <br>
    </div>
</template>
<script>
/* eslint-disable */
import WebMidi from 'webmidi'
 export default {
     created() {
         if (navigator.requestMIDIAccess) {
            console.log('This browser supports WebMIDI!');
        } else {
            console.log('WebMIDI is not supported in this browser.');
        }
        WebMidi.enable(function () {
            // Viewing available inputs and outputs
            console.log(WebMidi.inputs);
            console.log(WebMidi.outputs);
            WebMidi.outputs[0].playNote("C3");
        })
     }
 }
</script>
