def tq():
  import os

  files = os.listdir("../tadabbur/Audio - Tadabbur Quran")
  files.sort(key=lambda x: int(x.split(' ')[0]))

  file1 = open("../tadabbur/index.md", "w")
  file1.write('''<script
            async
            defer
            data-website-id="ef6464b6-bb4f-4a9d-8888-331c55a5b959"
            src="https://um.mufidu.com/umami.js"
></script>
<style>
#yptd {
  z-index: 9999999999;
  position: fixed;
  bottom: 1rem;
  left: 1rem;
  font: 16px Helvetica, Arial, sans-serif;
  -webkit-text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;

  box-shadow: 0 0.5rem 1rem rgba(0,0,0, 0.2);
}
#yptd * {
  margin: 0;
}
#yptd a {
  border-radius: 5px;
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  float: left;
  margin: 0 0.5em 0 0;
  padding: 0.25em 1.0em;
  font-weight: bold;
  color: #FFF;
  background-color: #a19c9d;
}
#yptd a em {
  font-size: 0.90em;
}
#yptd a:hover,
#yptd a:focus,
#yptd a:active {
  outline: 0;
  color: #a19c9d;
  background-color: #FFF;
  text-decoration: none;
}
#yptd span {
  border-radius: 3px;
  -moz-border-radius: 3px;
  -webkit-border-radius: 3px;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  float: left;
  display: block;
  margin: 0.5em;
  padding: 0em 0.5em;
  width: 2.5em;
  border-bottom: 2px solid rgba(0, 0, 0, 0.25);
  text-decoration: none;
  color: #000;
  background-color: #FFF;
  cursor: pointer;
  text-align: center;
}
#yptd span em {
  font-size: 0.75em;
  vertical-align: middle;
}
#yptd span:hover,
#yptd span:focus,
#yptd span:active {
  color: #a19c9d;
}
#yptd-bar {
  border-radius: 3px 3px 0 0;
  -moz-border-radius: 3px 3px 0 0;
  -webkit-border-radius: 3px 3px 0 0;
  height: 2.25em;
  background-color: #a19c9d;
}
#yptd-bar:after {
  content: "";
  display: block;
  clear: both;
}
#yptd-controls {
  float: right;
  height: 2.25em;
}
#yptd-box {
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  display: block;
  float: left;
  width: 4.0em;
  min-width: 4.0em;
  padding: 0 0.5em;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.15);
}
#yptd-in {
  width: 100%;
  height: 100%;
  border: 0;
  text-align: center;
  vertical-align: middle;
  font: 14px Helvetica, Arial, sans-serif;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 14px;
  color: #FFF;
  background-color: transparent;
}
#yptd-bottom {
  padding: 0.75em;
  font-size: 0.75em;
  vertical-align: middle;
  background-color: rgba(0, 0, 0, 0.8);
}
#yptd-bottom:after {
  content: "";
  display: block;
  clear: both;
}
#yptd-pit {
  position: relative;
  float: right;
  padding: 0.25em 0;
}
#yptd-pit label {
  margin-right: 0.5em;
  color: #FFF;
}
#yptd-pit em {
  display: none;
}
#yptd-pit input {
  float: right;
}
#yptd-pit:hover em,
#yptd-pit:focus em,
#yptd-pit:active em {
  display: block;
  position: absolute;
  top: -2.5em;
  left: 0;
  padding: 0.5em;
  white-space: pre;
  font-size: 0.8em;
  background-color: #a19c9d;
}
</style>

<div id="yptd">
    <div id="yptd-bar">
        <div id="yptd-controls">
            <span id="yptd-dwn">-</span>
            <div id="yptd-box">
                <input id="yptd-in" type="text" value="1.0">
            </div>
            <span id="yptd-up">+</span>
        </div>
    </div>
</div>

<script>
    /**
* yuptude v1
* yuptude is a tiny bookmarklet that you can use to speed up or slow down videos in your browser.
*/

//Speed at which to play 
var s = 1.0;
//Pitch shifting off/on
var p = false;
//Videos on the page
var videos;
//Individual video element
var v;
//Speed value from manual input field
var inputval;
//Container for yuptude widget

var ytw = dg("yptd");
var yts = dg("yptd-style");
var yti_in = dg("yptd-in");
var yti_off = dg("yptd-off");
var yti_pit = dg("yptd-pin");
var yti_up = dg("yptd-up");
var yti_dwn = dg("yptd-dwn");

//getElementById helper function
function dg(ID) {
return document.getElementById(ID);
}

//Update the speed variable when the input field changes
yti_in.addEventListener("input", yte_in);
function yte_in() {
s = dg("yptd-in").value;
}

//Increase video playback speed up to the standard cutoff of 4.0
yti_up.addEventListener("click", yte_up);
function yte_up() {
inputval = document.getElementById("yptd-in").value;
inputval = inputval ? parseFloat(inputval) : 1;
inputval = (inputval <= 3.9 ? inputval + 0.1 : inputval);

    s = dg("yptd-in").value = inputval.toFixed(1);

}

//Decrease video playback speed down to the standard cutoff of 0.5
yti_dwn.addEventListener("click", yte_dwn);
function yte_dwn() {
inputval = dg("yptd-in").value;
inputval = inputval ? parseFloat(inputval) : 1;
inputval = (inputval >= 0.6 ? inputval - 0.1 : inputval);

    s = dg("yptd-in").value = inputval.toFixed(1);

}

//Apply speed & pitch changes with a running internal to catch videos that are
//appended to the page or loaded after yuptude starts.
var interval = setInterval(function() { apply() }, 100);

function apply(ns) {
videos = document.querySelectorAll("audio");
for(var i = 0; i < videos.length; i++) {
v = videos[i];
if(v && v.readyState >= 2) {
v.playbackRate = (ns || (s || 1));
v.mozPreservesPitch = v.webkitPreservesPitch = v.preservePitch = !p;
}
}
}
</script>\n\n''')
  file1.close()

  for file in files:
      judul = '-   {}'.format(file.replace('.mp3', ''))
      judul = judul + "\n\n"
      judul = judul + '    <audio controls preload="none">'
      judul = judul + "\n" + "\n"
      judul = judul + '    <source src="/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/{}" type="audio/mpeg">'.format(file.replace(" ", "%20"))
      judul = judul + "\n"
      judul = judul + "    </audio>"
      judul = judul + "\n\n"
      print(judul)
      file1 = open("../tadabbur/index.md", "a")
      file1.write(judul)
      file1.close()

  file1 = open("../tadabbur/index.md", "a")
  file1.write("---\n")
  file1.close()