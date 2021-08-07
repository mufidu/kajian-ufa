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
  border-left: 2px solid rgba(0, 0, 0, 0.33);
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
</script>

-   Muqaddimah 1- Silsilah Amalan Hati

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/e-Muqaddimah%201-%20silsilah-amalan-hati.mp3" type="audio/mpeg">

    Maaf, browser Anda tidak mendukung pemutaran audio.
    </audio>

-   Muqaddimah 2 - Silsilah Amalan Hati

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/e-Muqaddimah%202%20-%20silsilah-amalan-hati.mp3" type="audio/mpeg">

    </audio>

-   Materi 1 - Mempelajari Amalan Hati Part 1

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%201%20-%20Mempelajari%20Amalan%20Hati%20Part%201.mp3" type="audio/mpeg">

    </audio>

-   Materi 2 - Mempelajari Amalan Hati Part 2

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%202%20-%20Mempelajari%20Amalan%20Hati%20Part%202.mp3" type="audio/mpeg">

    </audio>

-   Materi 3 - Mempelajari Amalan Hati Part 3

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%203%20-%20Mempelajari%20Amalan%20Hati%20Part%203.mp3" type="audio/mpeg">

    </audio>

-   Materi 4 - Mempelajari Amalan Hati Part 4

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%204%20-%20Mempelajari%20Amalan%20Hati%20Part%204.mp3" type="audio/mpeg">

    </audio>

-   Materi 5 - Ikhlas part 1

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%205%20-%20%20ikhlas%20part%201.mp3" type="audio/mpeg">

    </audio>

-   Materi 6 Faidah Ikhlas seri 1

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%206%20faidah%20ikhlas%20seri%201.mp3" type="audio/mpeg">

    </audio>

-   Materi 7 Faidah Ikhlas 4

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%207%20faidah%20ikhlas%204.mp3" type="audio/mpeg">

    </audio>

-   Materi 8 Faidah Ikhlas 5

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%208%20faidah%20ikhlas%205.mp3" type="audio/mpeg">

    </audio>

-   Materi 9 Faidah Ikhlas 6

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%209%20Faidah%20Ikhlas%206.mp3" type="audio/mpeg">

    </audio>

-   Materi 10 Faidah Ikhlas 7 dan 8

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2010%20faidah%20ikhlas%207%20dan%208.mp3" type="audio/mpeg">

    </audio>

-   Materi 11 Faidah Ikhlas 9

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2011%20faidah%20ikhlas%209.mp3" type="audio/mpeg">

    </audio>

-   Materi 12 Bahaya Riya

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2012%20Bahaya%20Riya.mp3" type="audio/mpeg">

    </audio>

-   Materi 13 Sebab-sebab riya

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2013%20Sebab-sebab%20riya.mp3" type="audio/mpeg">

    </audio>

-   Materi 14 Tanda terjangkiti riya

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2014%20Tanda%20terjangkiti%20riya.mp3" type="audio/mpeg">

    </audio>

-   Materi 15 - Jihad melawan riya

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2015%20-%20jihad%20melawan%20riya.mp3" type="audio/mpeg">

    </audio>

-   Materi 16 - Nasib mujahid dan ustadz yang riya

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2016%20-%20nasib%20mujahid%20dan%20ustadz%20yang%20riya.mp3" type="audio/mpeg">

    </audio>

-   Materi 17 - Nasib donatur yang riya

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2017%20-%20nasib%20donatur%20yang%20riya.mp3" type="audio/mpeg">

    </audio>

-   Materi 18 - Mari melawan riya

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2018%20-%20mari%20melawan%20riya.mp3" type="audio/mpeg">

    </audio>

-   Materi 19 - Nasib Orang yang Riya di Dunia

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2019%20-%20Nasib%20Orang%20yang%20Riya%20di%20Dunia.mp3" type="audio/mpeg">

    </audio>

-   Materi 20 - Cara berjuang melawan riya

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2020%20-%20cara%20berjuang%20melawan%20riya.mp3" type="audio/mpeg">

    </audio>

-   Materi 21 - Doa terhindar dari riya

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2021%20-%20doa%20terhindar%20dari%20riya.mp3" type="audio/mpeg">

    </audio>

-   Materi 22 Doa Ketika Ketika Dipuji Agar Tidak Timbul Riya'

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2022%20Doa%20Ketika%20Ketika%20Dipuji%20Agar%20Tidak%20Timbul%20Riya_.mp3" type="audio/mpeg">

    </audio>

-   Materi 23 - Menyembunyikan Amal Shaleh Agar Terhindar dari Riya

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2023%20%20-%20Menyembunyikan%20Amal%20Shaleh%20Agar%20Terhindar%20dari%20Riya.mp3" type="audio/mpeg">

    </audio>

-   Materi 24 - Poin Penting Menyembunyikan Amal Shaleh

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2024%20-%20Poin%20Penting%20Menyembunyikan%20Amal%20Shaleh.mp3" type="audio/mpeg">

    </audio>

-   Materi 25 - Riya Terselubung 1

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2025%20-%20Riya%20Terselubung%201.mp3" type="audio/mpeg">

    </audio>

-   Materi 26 - Riya Terselubung 2

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2026%20-%20Riya%20Terselubung%202.mp3" type="audio/mpeg">

    </audio>

-   Materi 27 - Sifat Ujub

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2027%20-%20Sifat%20Ujub.mp3" type="audio/mpeg">

    </audio>

-   Materi 28 - Perbedaan riya dan ujub

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2028%20-%20Perbedaan%20riya%20dan%20ujub.mp3" type="audio/mpeg">

    </audio>

-   Materi 29 - Bahaya Penyakit Ujub

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2029_Bahaya%20Penyakit%20Ujub.mp3" type="audio/mpeg">

    </audio>

-   Materi 30 - Cara melawan ujub 1

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2030_cara%20melawan%20ujub%201.mp3" type="audio/mpeg">

    </audio>

-   Materi 31 - Cara melawan ujub 2

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2031_cara%20melawan%20ujub%202.mp3" type="audio/mpeg">

    </audio>

-   Materi 32 - Cara melawan ujub 3

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2032_cara%20melawan%20ujub%203.mp3" type="audio/mpeg">

    </audio>

-   Materi 33 - Cara melawan ujub 4

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2033_cara%20melawan%20ujub%204.mp3" type="audio/mpeg">

    </audio>

-   Materi 34 - Model-model ujub 1 ujub dengan nasab

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2034%20model-model%20ujub%201%20ujub%20dengan%20nasab.mp3" type="audio/mpeg">

    </audio>

-   Materi 35 - Model-model ujub 2 ujub dengan penampilan

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2035%20model-model%20ujub%202%20ujub%20dengan%20penampilan.mp3" type="audio/mpeg">

    </audio>

-   Materi 36 - Model-model ujub 3 ujub dengan kekuatan dan kecerdasan

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2036_%20model-model%20ujub%203%20ujub%20dengan%20kekuatan%20dan%20kecerdasan.mp3" type="audio/mpeg">

    </audio>

-   Materi 37 - Model-model ujub 4 ujub dengan jumlah yang banyak dan harta

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2037%20model-model%20ujub%204%20ujub%20dengan%20jumlah%20yang%20banyak%20dan%20harta.mp3" type="audio/mpeg">

    </audio>

-   Materi 38 - Model-model ujub 5 ujub dengan berafiliasi kepada penguasa yang zalim

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2038%20model-model%20ujub%205%20ujub%20dengan%20berafiliasi%20kepada%20penguasa%20yang%20zalim.mp3" type="audio/mpeg">

    </audio>

-   Materi 39 - Tawakal Kepada Allah

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2039%20-%20Tawakal%20Kepada%20Allah.mp3" type="audio/mpeg">

    </audio>

-   Materi 40 - Keutamaan dan Urgensi Tawakal

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2040%20-%20Keutamaan%20dan%20Urgensi%20Tawakal.mp3" type="audio/mpeg">

    </audio>

-   Materi 41 - Tawakal Sebagai Pengumpul Keimanan2

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2041%20-%20Tawakal%20Sebagai%20Pengumpul%20Keimanan2.mp3" type="audio/mpeg">

    </audio>

-   Materi 42 - Doa Termasuk Bukti Tawakal

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2042%20-%20Doa%20Termasuk%20Bukti%20Tawakal.mp3" type="audio/mpeg">

    </audio>

-   Materi 43 - Rahasia Doa Nabi yang Mengandung Makna Tawakal

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2043%20-%20Rahasia%20Doa%20Nabi%20yang%20Mengandung%20Makna%20Tawakal.mp3" type="audio/mpeg">

    </audio>

-   Materi 44 - Tawakal Kunci Kemenangan

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2044%20-%20Tawakal%20Kunci%20Kemenangan.mp3" type="audio/mpeg">

    </audio>

-   Materi 45 - Tawakal untuk Perdamaian, Ibadah dan Menghadapi Musibah

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2045%20-%20Tawakal%20untuk%20Perdamaian,%20Ibadah%20dan%20Menghadapi%20Musibah.mp3" type="audio/mpeg">

    </audio>

-   Materi 46 - Tawakal Akan Mendapat Pahala Besar, Tawakal Sebagai Benteng dari Godaan Setan, Tawakal Sebab Dicintai Allah

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2046%20-%20Tawakal%20Akan%20Mendapat%20Pahala%20Besar,%20Tawakal%20Sebagai%20Benteng%20dari%20Godaan%20Setan,%20Tawakal%20Sebab%20Dicintai%20Allah.mp3" type="audio/mpeg">

    </audio>

-   Materi 47 - Tawakal Sebab Datangkan Rezeki

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2047%20-%20Tawakal%20Sebab%20Datangkan%20Rezeki.mp3" type="audio/mpeg">

    </audio>

-   Materi 48 - Bertawakallah Kepada Allah, Jangan Bertawakal Kepada Materi

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2048%20-%20Bertawakallah%20Kepada%20Allah,%20Jangan%20Bertawakal%20Kepada%20Materi.mp3" type="audio/mpeg">

    </audio>

-   Materi 49 - Hakikat Tawakal

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2049%20-%20Hakikat%20Tawakal.mp3" type="audio/mpeg">

    </audio>

-   Materi 50 - Salah dalam Memahami Tawakal

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2050%20-%20Salah%20dalam%20Memahami%20Tawakal.mp3" type="audio/mpeg">

    </audio>

-   Materi 51 - Diantara Tawakal Terlarang Adalah Memakai Jimat

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2051%20-%20Diantara%20Tawakal%20Terlarang%20Adalah%20Memakai%20Jimat.mp3" type="audio/mpeg">

    </audio>

-   Materi 52 - Tathoyyur Bentuk Tawakal Terlarang

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2052%20-%20Tathoyyur%20Bentuk%20Tawakal%20Terlarang.mp3" type="audio/mpeg">

    </audio>

-   Materi 53 - Ujub Bentuk Tawakal Terlarang

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2053%20-%20Ujub%20Bentuk%20Tawakal%20Terlarang.mp3" type="audio/mpeg">

    </audio>

-   Materi 54 -Makna Tawadhu'

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2054%20-Makna%20Tawadhu_.mp3" type="audio/mpeg">

    </audio>

-   Materi 55 - Perkataan Ulama Tentang Tawadhu'

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2055%20-%20Perkataan%20Ulama%20Tentang%20Tawadhu_.mp3" type="audio/mpeg">

    </audio>

-   Materi 56 - Perkataan Ulama Tentang Tawadhu' (Part2)

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2056%20-%20%20Perkataan%20Ulama%20Tentang%20Tawadhu_%20(Part2).mp3" type="audio/mpeg">

    </audio>

-   Materi 57 - Tawadhu' Sifat 'Ibadurrahman

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2057%20-%20Tawadhu_%20Sifat%20_Ibadurrahman.mp3" type="audio/mpeg">

    </audio>

-   Materi 58 - Sikap Orang yang Tawadhu' Terhadap Dunia

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2058%20-%20Sikap%20Orang%20yang%20Tawadhu_%20Terhadap%20Dunia.mp3" type="audio/mpeg">

    </audio>

-   Materi 59 - Tawadhu' Kasih Sayang Terhadap Sesama

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2059%20-%20Tawadhu_%20Kasih%20Sayang%20Terhadap%20Sesama.mp3" type="audio/mpeg">

    </audio>

-   Materi 60 - Tawadhu' Kepada Orang Tua

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2060%20-%20Tawadhu_%20Kepada%20Orang%20Tua.mp3" type="audio/mpeg">

    </audio>

-   Materi 61 - Hamba yang Tawadhu' Akan Diangkat Derajatnya Oleh Allah

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2061%20-%20Hamba%20yang%20Tawadhu_%20Akan%20Diangkat%20Derajatnya%20Oleh%20Allah.mp3" type="audio/mpeg">

    </audio>

-   Materi 62 - Sifat Tawadhu' Tidak Dzalim Kepada yang Lain

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2062%20-%20Sifat%20Tawadhu_%20Tidak%20Dzalim%20Kepada%20yang%20Lain.mp3" type="audio/mpeg">

    </audio>

-   Materi 63 - Hamba yang Tawadhu Akan Terkenal Di Hari Kiamat Dengan Memakai Baju Keimanan Terindah

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2063%20-%20Hamba%20yang%20Tawadhu%20Akan%20Terkenal%20Di%20Hari%20Kiamat%20Dengan%20Memakai%20Baju%20Keimanan%20Terindah.mp3" type="audio/mpeg">

    </audio>

-   Materi 64 - Hamba yang Tawadhu Akan Diangkat Derajat Oleh Allah

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2064%20-%20Hamba%20yang%20Tawadhu%20Akan%20Diangkat%20Derajat%20Oleh%20Allah.mp3" type="audio/mpeg">

    </audio>

-   Materi 65 - Hamba yang Tawadhu' Tetap Menjaga Izzah Tanpa Harus Menghinakan Diri

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2065%20-%20Hamba%20yang%20Tawadhu_%20Tetap%20Menjaga%20Izzah%20Tanpa%20Harus%20Menghinakan%20Diri.mp3" type="audio/mpeg">

    </audio>

-   Materi 66 - Pengaruh Pakaian Terhadap Tawadhu'

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2066%20-%20Pengaruh%20Pakaian%20Terhadap%20Tawadhu_.mp3" type="audio/mpeg">

    </audio>

-   Materi 67 - Tawadhu' Terhadap Makanan

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2067%20-%20Tawadhu_%20Terhadap%20Makanan.mp3" type="audio/mpeg">

    </audio>

-   Materi 68 - Tawadhu' Terhadap Orang Miskin

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2068%20-%20Tawadhu_%20Terhadap%20Orang%20Miskin.mp3" type="audio/mpeg">

    </audio>

-   Materi 69 - Tawadhu' Tidak Merasa Besar Diri Dihadapan Orang Lain

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2069%20-%20Tawadhu_%20Tidak%20Merasa%20Besar%20Diri%20Dihadapan%20Orang%20Lain.mp3" type="audio/mpeg">

    </audio>

-   Materi 70 - Tawadhu' Ketika Berkunjung dan Menghadiri Undangan

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2070%20-%20Tawadhu_%20Ketika%20Berkunjung%20dan%20Menghadiri%20Undangan.mp3" type="audio/mpeg">

    </audio>

-   Materi 71 - Tawadhu' Terhadap Anak Kecil

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2071%20-%20Tawadhu_%20Terhadap%20Anak%20Kecil.mp3" type="audio/mpeg">

    </audio>

-   Materi 72 - Tawadhu' Kepada Orang yang Dibawahnya Tanpa Pilih-pilih Menyapa dan Mengucapkan Salam

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2072%20-%20Tawadhu_%20Kepada%20Orang%20yang%20Dibawahnya%20Tanpa%20Pilih-pilih%20Menyapa%20dan%20Mengucapkan%20Salam.mp3" type="audio/mpeg">

    </audio>

-   Materi 73- Tawadhu'nya Nabi Saat Kondisi Perang Khondaq

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2073-%20%20Tawadhu_nya%20Nabi%20Saat%20Kondisi%20Perang%20Khondaq.mp3" type="audio/mpeg">

    </audio>

-   Materi 74- Tawadhu'nya Nabi Kepada Istri dan Keluarga

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2074-%20%20Tawadhu_nya%20Nabi%20Kepada%20Istri%20dan%20Keluarga.mp3" type="audio/mpeg">

    </audio>

-   Materi 75- Tawadhu'nya Nabi Kepada Anak Kecil

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2075-%20%20Tawadhu_nya%20Nabi%20Kepada%20Anak%20Kecil.mp3" type="audio/mpeg">

    </audio>

-   Materi 76- Tawadhu'nya Nabi Kepada Orang Lemah

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2076-%20%20Tawadhu_nya%20Nabi%20Kepada%20Orang%20Lemah.mp3" type="audio/mpeg">

    </audio>

-   Materi 77- Tawadhu'nya Nabi Kepada Bawahannya

    <audio controls preload="metadata">

    <source src="https://mufidu.github.io/kajian-ufa/silsilah-hati/Audio%20-%20Silsilah%20Hati/Materi%2077-%20%20Tawadhu_nya%20Nabi%20Kepada%20Bawahannya.mp3" type="audio/mpeg">

    </audio>

<br>

---
