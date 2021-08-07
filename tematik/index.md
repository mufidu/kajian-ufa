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

-   Tematik 1 - Awal Kejayaan dan Keberhasilan Adalah Ujian

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%201%20-%20Awal%20Kejayaan%20dan%20Keberhasilan%20Adalah%20Ujian.mp3" type="audio/mpeg">
    Maaf, browser Anda tidak mendukung pemutaran audio.

    </audio>

-   Tematik 2 - Efek Bermaksiat dan Kurang Istighfar

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%202%20-%20Efek%20Bermaksiat%20dan%20Kurang%20Istighfar.mp3" type="audio/mpeg">

    </audio>

-   Tematik 3 - Jaga Lisanmu, Lisan Punya Pengaruh Kuat Ke Hati

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%203%20-%20Jaga%20Lisanmu,%20Lisan%20Punya%20Pengaruh%20Kuat%20Ke%20Hati.mp3" type="audio/mpeg">

    </audio>

-   Tematik 4 - Qolbun Salim, Hati yang Selamat

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%204%20-%20Qolbun%20Salim,%20Hati%20yang%20Selamat.mp3" type="audio/mpeg">

    </audio>

-   Tematik 5 - Keutamaan Teman Shalih Bisa Memberi Syafaat Di Akhirat

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%205%20-%20Keutamaan%20Teman%20Shalih%20Bisa%20Memberi%20Syafaat%20Di%20Akhirat.mp3" type="audio/mpeg">

    </audio>

-   Tematik 6 - Awas Hoax dan Hati-hati Mendengar Kabar Berita - Part 1

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%206%20-%20Awas%20Hoax%20dan%20Hati-hati%20Mendengar%20Kabar%20Berita%20-%20Part%201.mp3" type="audio/mpeg">

    </audio>

-   Tematik 7 - Awas Hoax dan Hati-hati Mendengar Kabar Berita - Part 2

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%207%20-%20Awas%20Hoax%20dan%20Hati-hati%20Mendengar%20Kabar%20Berita%20-%20Part%202.mp3" type="audio/mpeg">

    </audio>

-   Tematik 8 - Aneh !! Ketika Ujian Datang Ada Golongan yang Menjauh Dari Allah

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%208%20-%20Aneh%20!!%20Ketika%20Ujian%20Datang%20Ada%20Golongan%20yang%20Menjauh%20Dari%20Allah.mp3" type="audio/mpeg">

    </audio>

-   Tematik 9 - Saatnya Deteksi Hati !

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%209%20-%20Saatnya%20Deteksi%20Hati%20!.mp3" type="audio/mpeg">

    </audio>

-   Tematik 10 - Hati-hati Jangan Kurangi Hak Orang Lain ! - Part-1

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2010%20-%20Hati-hati%20Jangan%20Kurangi%20Hak%20Orang%20Lain%20!%20-%20Part-1.mp3" type="audio/mpeg">

    </audio>

-   Tematik 11 - Hati-hati Jangan Kurangi Hak Orang Lain ! - Part-2

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2011%20-%20Hati-hati%20Jangan%20Kurangi%20Hak%20Orang%20Lain%20!%20-%20Part-2.mp3" type="audio/mpeg">

    </audio>

-   Tematik 12 - Saat Jalan Bertiga Bersama Kawan

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2012%20-%20Saat%20Jalan%20Bertiga%20Bersama%20Kawan.mp3" type="audio/mpeg">

    </audio>

-   Tematik 13 - MEMBOSANKAN! Saat Aku Mulai Malas Ketika Hati Naik Turun

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2013%20-%20MEMBOSANKAN!%20Saat%20Aku%20Mulai%20Malas%20Ketika%20Hati%20Naik%20Turun.mp3" type="audio/mpeg">

    </audio>

-   Tematik 14 - Ya Allah, Teguhkan Hatiku Diatas Agama-Mu

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2014%20-%20Ya%20Allah,%20Teguhkan%20Hatiku%20Diatas%20Agama-Mu.mp3" type="audio/mpeg">

    </audio>

-   Tematik 15 - Sunnah Bertakbir Di Bulan Dzulhijjah, Takbir Mutlaq dan Muqayyad

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2015%20-%20Sunnah%20Bertakbir%20Di%20Bulan%20Dzulhijjah,%20Takbir%20Mutlaq%20dan%20Muqayyad.mp3" type="audio/mpeg">

    </audio>

-   Tematik 16 - Mencari Kawan Terbaik Saat Kita Terhempas

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2016%20-%20Mencari%20Kawan%20Terbaik%20Saat%20Kita%20Terhempas.mp3" type="audio/mpeg">

    </audio>

-   Tematik 17 - Jangan Modal Semangat! Hijrah dan Beramal Itu Bertahap

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2017%20-%20Jangan%20Modal%20Semangat!%20Hijrah%20dan%20Beramal%20Itu%20Bertahap.mp3" type="audio/mpeg">

    </audio>

-   Tematik 18 - Aneh, Banyak Orang Bodoh Berbicara Masalah Agama

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2018%20-%20Aneh,%20Banyak%20Orang%20Bodoh%20Berbicara%20Masalah%20Agama.mp3" type="audio/mpeg">

    </audio>

-   Tematik 19 - Jauhi Su_udzon dan Jangan Bawa Perkataan Saudaramu dengan Tafsir yang Buruk

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2019%20-%20Jauhi%20Su_udzon%20dan%20Jangan%20Bawa%20Perkataan%20Saudaramu%20dengan%20Tafsir%20yang%20Buruk.mp3" type="audio/mpeg">

    </audio>

-   Tematik 20 - Cara Deteksi Sinyal Keimanan Kita

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2020%20-%20Cara%20Deteksi%20Sinyal%20Keimanan%20Kita.mp3" type="audio/mpeg">

    </audio>

-   Tematik 21 - Ibadah Taubat, Ibadah Agung yang Dikerjakan Para Nabi dan Orang Shaleh

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2021%20-%20Ibadah%20Taubat,%20Ibadah%20Agung%20yang%20Dikerjakan%20Para%20Nabi%20dan%20Orang%20Shaleh.mp3" type="audio/mpeg">

    </audio>

-   Tematik 22 - Ujian Kesusahan dan Ujian Kesenangan

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2022%20-%20Ujian%20Kesusahan%20dan%20Ujian%20Kesenangan.mp3" type="audio/mpeg">

    </audio>

-   Tematik 23 - Semakin Tinggi Tingkat Iman, Semakin Tinggi Tingkat Ujiannya Part - 1

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2023%20-%20Semakin%20Tinggi%20Tingkat%20Iman,%20Semakin%20Tinggi%20Tingkat%20Ujiannya%20Part%20-%201.mp3" type="audio/mpeg">

    </audio>

-   Tematik 24 - Semakin Tinggi Tingkat Iman, Semakin Tinggi Tingkat Ujiannya Part - 2

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2024%20-%20Semakin%20Tinggi%20Tingkat%20Iman,%20Semakin%20Tinggi%20Tingkat%20Ujiannya%20Part%20-%202.mp3" type="audio/mpeg">

    </audio>

<br>

---