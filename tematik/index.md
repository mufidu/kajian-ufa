<script
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
</script>

-   Tematik 1 - Awal Kejayaan dan Keberhasilan Adalah Ujian

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%201%20-%20Awal%20Kejayaan%20dan%20Keberhasilan%20Adalah%20Ujian.mp3" type="audio/mpeg">
    </audio>

-   Tematik 2 - Efek Bermaksiat dan Kurang Istighfar

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%202%20-%20Efek%20Bermaksiat%20dan%20Kurang%20Istighfar.mp3" type="audio/mpeg">
    </audio>

-   Tematik 3 - Jaga Lisanmu, Lisan Punya Pengaruh Kuat Ke Hati

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%203%20-%20Jaga%20Lisanmu,%20Lisan%20Punya%20Pengaruh%20Kuat%20Ke%20Hati.mp3" type="audio/mpeg">
    </audio>

-   Tematik 4 - Qolbun Salim, Hati yang Selamat

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%204%20-%20Qolbun%20Salim,%20Hati%20yang%20Selamat.mp3" type="audio/mpeg">
    </audio>

-   Tematik 5 - Keutamaan Teman Shalih Bisa Memberi Syafaat Di Akhirat

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%205%20-%20Keutamaan%20Teman%20Shalih%20Bisa%20Memberi%20Syafaat%20Di%20Akhirat.mp3" type="audio/mpeg">
    </audio>

-   Tematik 6 - Awas Hoax dan Hati-hati Mendengar Kabar Berita - Part 1

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%206%20-%20Awas%20Hoax%20dan%20Hati-hati%20Mendengar%20Kabar%20Berita%20-%20Part%201.mp3" type="audio/mpeg">
    </audio>

-   Tematik 7 - Awas Hoax dan Hati-hati Mendengar Kabar Berita - Part 2

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%207%20-%20Awas%20Hoax%20dan%20Hati-hati%20Mendengar%20Kabar%20Berita%20-%20Part%202.mp3" type="audio/mpeg">
    </audio>

-   Tematik 8 - Aneh !! Ketika Ujian Datang Ada Golongan yang Menjauh Dari Allah

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%208%20-%20Aneh%20!!%20Ketika%20Ujian%20Datang%20Ada%20Golongan%20yang%20Menjauh%20Dari%20Allah.mp3" type="audio/mpeg">
    </audio>

-   Tematik 9 - Saatnya Deteksi Hati !

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%209%20-%20Saatnya%20Deteksi%20Hati%20!.mp3" type="audio/mpeg">
    </audio>

-   Tematik 10 - Hati-hati Jangan Kurangi Hak Orang Lain ! - Part-1

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2010%20-%20Hati-hati%20Jangan%20Kurangi%20Hak%20Orang%20Lain%20!%20-%20Part-1.mp3" type="audio/mpeg">
    </audio>

-   Tematik 11 - Hati-hati Jangan Kurangi Hak Orang Lain ! - Part-2

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2011%20-%20Hati-hati%20Jangan%20Kurangi%20Hak%20Orang%20Lain%20!%20-%20Part-2.mp3" type="audio/mpeg">
    </audio>

-   Tematik 12 - Saat Jalan Bertiga Bersama Kawan

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2012%20-%20Saat%20Jalan%20Bertiga%20Bersama%20Kawan.mp3" type="audio/mpeg">
    </audio>

-   Tematik 13 - MEMBOSANKAN! Saat Aku Mulai Malas Ketika Hati Naik Turun

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2013%20-%20MEMBOSANKAN!%20Saat%20Aku%20Mulai%20Malas%20Ketika%20Hati%20Naik%20Turun.mp3" type="audio/mpeg">
    </audio>

-   Tematik 14 - Ya Allah, Teguhkan Hatiku Diatas Agama-Mu

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2014%20-%20Ya%20Allah,%20Teguhkan%20Hatiku%20Diatas%20Agama-Mu.mp3" type="audio/mpeg">
    </audio>

-   Tematik 15 - Sunnah Bertakbir Di Bulan Dzulhijjah, Takbir Mutlaq dan Muqayyad

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2015%20-%20Sunnah%20Bertakbir%20Di%20Bulan%20Dzulhijjah,%20Takbir%20Mutlaq%20dan%20Muqayyad.mp3" type="audio/mpeg">
    </audio>

-   Tematik 16 - Mencari Kawan Terbaik Saat Kita Terhempas

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2016%20-%20Mencari%20Kawan%20Terbaik%20Saat%20Kita%20Terhempas.mp3" type="audio/mpeg">
    </audio>

-   Tematik 17 - Jangan Modal Semangat! Hijrah dan Beramal Itu Bertahap

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2017%20-%20Jangan%20Modal%20Semangat!%20Hijrah%20dan%20Beramal%20Itu%20Bertahap.mp3" type="audio/mpeg">
    </audio>

-   Tematik 18 - Aneh, Banyak Orang Bodoh Berbicara Masalah Agama

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2018%20-%20Aneh,%20Banyak%20Orang%20Bodoh%20Berbicara%20Masalah%20Agama.mp3" type="audio/mpeg">
    </audio>

-   Tematik 19 - Jauhi Su_udzon dan Jangan Bawa Perkataan Saudaramu dengan Tafsir yang Buruk

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2019%20-%20Jauhi%20Su_udzon%20dan%20Jangan%20Bawa%20Perkataan%20Saudaramu%20dengan%20Tafsir%20yang%20Buruk.mp3" type="audio/mpeg">
    </audio>

-   Tematik 20 - Cara Deteksi Sinyal Keimanan Kita

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2020%20-%20Cara%20Deteksi%20Sinyal%20Keimanan%20Kita.mp3" type="audio/mpeg">
    </audio>

-   Tematik 21 - Ibadah Taubat, Ibadah Agung yang Dikerjakan Para Nabi dan Orang Shaleh

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2021%20-%20Ibadah%20Taubat,%20Ibadah%20Agung%20yang%20Dikerjakan%20Para%20Nabi%20dan%20Orang%20Shaleh.mp3" type="audio/mpeg">
    </audio>

-   Tematik 22 - Ujian Kesusahan dan Ujian Kesenangan

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2022%20-%20Ujian%20Kesusahan%20dan%20Ujian%20Kesenangan.mp3" type="audio/mpeg">
    </audio>

-   Tematik 23 - Semakin Tinggi Tingkat Iman, Semakin Tinggi Tingkat Ujiannya Part - 1

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2023%20-%20Semakin%20Tinggi%20Tingkat%20Iman,%20Semakin%20Tinggi%20Tingkat%20Ujiannya%20Part%20-%201.mp3" type="audio/mpeg">
    </audio>

-   Tematik 24 - Semakin Tinggi Tingkat Iman, Semakin Tinggi Tingkat Ujiannya Part - 2

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2024%20-%20Semakin%20Tinggi%20Tingkat%20Iman,%20Semakin%20Tinggi%20Tingkat%20Ujiannya%20Part%20-%202.mp3" type="audio/mpeg">
    </audio>

-   Tematik 25 - Sabar Akan Membahagiakanmu Bagaimanapun Kondisimu

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2025%20-%20Sabar%20Akan%20Membahagiakanmu%20Bagaimanapun%20Kondisimu.mp3" type="audio/mpeg">
    </audio>

-   Tematik 26 - Inilah Rahasia Keutamaan Sabar

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2026%20-%20Inilah%20Rahasia%20Keutamaan%20Sabar.mp3" type="audio/mpeg">
    </audio>

-   Tematik 27 - Sabar Setengah Iman, Sisanya Adalah Syukur

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2027%20-%20Sabar%20Setengah%20Iman,%20Sisanya%20Adalah%20Syukur.mp3" type="audio/mpeg">
    </audio>

-   Tematik 28 - Dalam Ketaatan Butuh Kesabaran

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2028%20-%20Dalam%20Ketaatan%20Butuh%20Kesabaran.mp3" type="audio/mpeg">
    </audio>

-   Tematik 29 - Kekuatan Sabar, Kisah Seorang Yang Memiliki Satu Kaki Bisa Berdiri Shalat Selama Lebih dari 2 Jam

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2029%20-%20Kekuatan%20Sabar,%20Kisah%20Seorang%20Yang%20Memiliki%20Satu%20Kaki%20Bisa%20Berdiri%20Shalat%20Selama%20Lebih%20dari%202%20Jam.mp3" type="audio/mpeg">
    </audio>

-   Tematik 30 - Lihatlah! Orang Kafir dan Pelaku Kemaksiatan Saja Bersabar

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2030%20-%20Lihatlah!%20Orang%20Kafir%20dan%20Pelaku%20Kemaksiatan%20Saja%20Bersabar.mp3" type="audio/mpeg">
    </audio>

-   Tematik 31 - Sabar Dalam Meninggalkan Kemaksiatan, Kisah Luar Biasa Nabi Yusuf

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2031%20-%20Sabar%20Dalam%20Meninggalkan%20Kemaksiatan,%20Kisah%20Luar%20Biasa%20Nabi%20Yusuf.mp3" type="audio/mpeg">
    </audio>

-   Tematik 32  - Inilah 3 Cara Bersabar Dalam Meninggalkan Kemaksiatan

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2032%20%20-%20Inilah%203%20Cara%20Bersabar%20Dalam%20Meninggalkan%20Kemaksiatan.mp3" type="audio/mpeg">
    </audio>

-   Tematik 33 - Sabar Pada Pukulan Pertama

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2033%20-%20Sabar%20Pada%20Pukulan%20Pertama.mp3" type="audio/mpeg">
    </audio>

-   Tematik 34 - Saat Musibah Akan Mengangkat Derajatmu

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2034%20-%20Saat%20Musibah%20Akan%20Mengangkat%20Derajatmu.mp3" type="audio/mpeg">
    </audio>

-   Tematik 35 - Saat Ujian Mendera Lihatlah Dibawahmu Dan Tetaplah Bersyukur

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2035%20-%20Saat%20Ujian%20Mendera%20Lihatlah%20Dibawahmu%20Dan%20Tetaplah%20Bersyukur.mp3" type="audio/mpeg">
    </audio>

-   Tematik 36 - Yang Terbaik Adalah Pilihan Allah

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2036%20-%20Yang%20Terbaik%20Adalah%20Pilihan%20Allah.mp3" type="audio/mpeg">
    </audio>

-   Tematik 37 - Buktikan Cintamu Kepada Nabi dengan Menjauhi Bid_ah

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2037%20-%20Buktikan%20Cintamu%20Kepada%20Nabi%20dengan%20Menjauhi%20Bid_ah.mp3" type="audio/mpeg">
    </audio>

-   Tematik 38 - Sekarang ya Rasulallah, Aku Lebih Mencintaimu Daripada Diriku Sendiri

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2038%20-%20Sekarang%20ya%20Rasulallah,%20Aku%20Lebih%20Mencintaimu%20Daripada%20Diriku%20Sendiri.mp3" type="audio/mpeg">
    </audio>

-   Tematik 39 - Seseorang Dikumpulkan Di Hari Kiamat Bersama dengan Orang yang Dicintainya

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2039%20-%20Seseorang%20Dikumpulkan%20Di%20Hari%20Kiamat%20Bersama%20dengan%20Orang%20yang%20Dicintainya.mp3" type="audio/mpeg">
    </audio>

-   Tematik 40 - Para Sahabat Lebih Tahu Cara Mencintai Nabi Muhammad

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2040%20-%20Para%20Sahabat%20Lebih%20Tahu%20Cara%20Mencintai%20Nabi%20Muhammad.mp3" type="audio/mpeg">
    </audio>

-   Tematik 41 - Dua Pilar Bukti Anda Mencintai Nabi Yaitu Kerinduan dan Ittiba_

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2041%20-%20Dua%20Pilar%20Bukti%20Anda%20Mencintai%20Nabi%20Yaitu%20Kerinduan%20dan%20Ittiba_.mp3" type="audio/mpeg">
    </audio>

-   Tematik 42 - Kenali Jasa Nabi Muhammad untuk Menumbuhkan Rasa Cintamu Padanya

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2042%20-%20Kenali%20Jasa%20Nabi%20Muhammad%20untuk%20Menumbuhkan%20Rasa%20Cintamu%20Padanya.mp3" type="audio/mpeg">
    </audio>

-   Tematik 43 - Cinta Luar Biasa

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2043%20-%20Cinta%20Luar%20Biasa.mp3" type="audio/mpeg">
    </audio>

-   Tematik 44 - Buktikan Cintamu Kepada Nabi dengan Mengikuti Sunnahnya

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2044%20-%20Buktikan%20Cintamu%20Kepada%20Nabi%20dengan%20Mengikuti%20Sunnahnya.mp3" type="audio/mpeg">
    </audio>

-   Tematik 45 - Semangat Beramal Ketika Mendengar Hadis Nabi

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2045%20-%20Semangat%20Beramal%20Ketika%20Mendengar%20Hadis%20Nabi.mp3" type="audio/mpeg">
    </audio>

-   Tematik 46 - Tinggalkan Apa yang Dilarang Nabi

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2046%20-%20Tinggalkan%20Apa%20yang%20Dilarang%20Nabi.mp3" type="audio/mpeg">
    </audio>

-   Tematik 47 - Mendahulukan Ucapan Nabi Daripada yang Lainnya

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2047%20-%20Mendahulukan%20Ucapan%20Nabi%20Daripada%20yang%20Lainnya.mp3" type="audio/mpeg">
    </audio>

-   Tematik 48 - Bersegeralah Beramal Shaleh untuk Bekal Akhirat

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2048%20-%20Bersegeralah%20Beramal%20Shaleh%20untuk%20Bekal%20Akhirat.mp3" type="audio/mpeg">
    </audio>

-   Tematik 49 - HASAD, Tenyata Ada 2 Orang yang Boleh Anda Hasadi

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2049%20-%20HASAD,%20Tenyata%20Ada%202%20Orang%20yang%20Boleh%20Anda%20Hasadi.mp3" type="audio/mpeg">
    </audio>

-   Tematik 50 - Berlombalah Dalam Beramal Karena Surga Bertingkat-tingkat

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2050%20-%20Berlombalah%20Dalam%20Beramal%20Karena%20Surga%20Bertingkat-tingkat.mp3" type="audio/mpeg">
    </audio>

-   Tematik 51 - Bersegera Dalam Kebajikan Doa Mudah Terkabul

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2051%20-%20Bersegera%20Dalam%20Kebajikan%20Doa%20Mudah%20Terkabul.mp3" type="audio/mpeg">
    </audio>

-   Tematik 52 -Terdepan dalam Ketaatan Ciri Sempurna Iman Seorang Hamba

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2052%20-Terdepan%20dalam%20Ketaatan%20Ciri%20Sempurna%20Iman%20Seorang%20Hamba.mp3" type="audio/mpeg">
    </audio>

-   Tematik 53 - Bersegeralah Beramal Shalih Sebelum Datang Fitnah Pada Dirimu

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2053%20-%20Bersegeralah%20Beramal%20Shalih%20Sebelum%20Datang%20Fitnah%20Pada%20Dirimu.mp3" type="audio/mpeg">
    </audio>

-   Tematik 54 - Manfaatkan Masa Mudamu Sebelum Masa Tuamu

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2054%20-%20Manfaatkan%20Masa%20Mudamu%20Sebelum%20Masa%20Tuamu.mp3" type="audio/mpeg">
    </audio>

-   Tematik 55 - Belajar Dermawan dalam Kondisi Kaya Atau Miskin

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2055%20-%20Belajar%20Dermawan%20dalam%20Kondisi%20Kaya%20Atau%20Miskin.mp3" type="audio/mpeg">
    </audio>

-   Tematik 56 - Manfaatkan Waktu Luang dan Jangan Tunda Peluang Beramal

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2056%20-%20Manfaatkan%20Waktu%20Luang%20dan%20Jangan%20Tunda%20Peluang%20Beramal.mp3" type="audio/mpeg">
    </audio>

-   Tematik 57 - Karena Iman yang Membedakan Antara yang Bersegera dan Menunda dalam Kebaikan

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2057%20-%20Karena%20Iman%20yang%20Membedakan%20Antara%20yang%20Bersegera%20dan%20Menunda%20dalam%20Kebaikan.mp3" type="audio/mpeg">
    </audio>

-   Tematik 58 - Kita Jadi Malu, Bagaimana Semangatnya Sahabat Berlomba-lomba Dalam Ketaatan

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2058%20-%20Kita%20Jadi%20Malu,%20Bagaimana%20Semangatnya%20Sahabat%20Berlomba-lomba%20Dalam%20Ketaatan.mp3" type="audio/mpeg">
    </audio>

-   Tematik 59 - Nabi Bersegera dalam Kebaikan, dan Sedikit Nasehat Untuk Kita Di Zaman Gadget Ini

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2059%20-%20Nabi%20Bersegera%20dalam%20Kebaikan,%20dan%20Sedikit%20Nasehat%20Untuk%20Kita%20Di%20Zaman%20Gadget%20Ini.mp3" type="audio/mpeg">
    </audio>

-   Tematik 60 - Makanlah Dari yang Halal Dan Jangan Ikuti Langkah-langkah Setan

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2060%20-%20Makanlah%20Dari%20yang%20Halal%20Dan%20Jangan%20Ikuti%20Langkah-langkah%20Setan.mp3" type="audio/mpeg">
    </audio>

-   Tematik 61 - Hukum Asal Makanan Halal Kecuali Apa yang Telah Diharamkan Oleh Syariat

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2061%20-%20Hukum%20Asal%20Makanan%20Halal%20Kecuali%20Apa%20yang%20Telah%20Diharamkan%20Oleh%20Syariat.mp3" type="audio/mpeg">
    </audio>

-   Tematik 62 - Tragis, Gara-gara Harta Haram Amal Shalihpun Tidak Diterima

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2062%20-%20Tragis,%20Gara-gara%20Harta%20Haram%20Amal%20Shalihpun%20Tidak%20Diterima.mp3" type="audio/mpeg">
    </audio>

-   Tematik 63 - Orang Kaya Posisinya Paling Rendah Di Akhirat, Kecuali dari Harta yang Halal dan Digunakan Untuk Sedekah

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2063%20-%20Orang%20Kaya%20Posisinya%20Paling%20Rendah%20Di%20Akhirat,%20Kecuali%20dari%20Harta%20yang%20Halal%20dan%20Digunakan%20Untuk%20Sedekah.mp3" type="audio/mpeg">
    </audio>

-   Tematik 64 - Kisah Abu Bakar Memuntahkan Makanan Syubhat

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2064%20-%20Kisah%20Abu%20Bakar%20Memuntahkan%20Makanan%20Syubhat.mp3" type="audio/mpeg">
    </audio>

-   Tematik 65 - Kisah Ulama - Gara-gara Delima Dijodohkan Dengan Putri Majikan

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2065%20-%20Kisah%20Ulama%20-%20Gara-gara%20Delima%20Dijodohkan%20Dengan%20Putri%20Majikan.mp3" type="audio/mpeg">
    </audio>

-   Tematik 66 - Kisah Masa Kecil Imam Bukhari, Ayahnya Tidak Memberikan Makan Dari Harta Haram

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2066%20-%20Kisah%20Masa%20Kecil%20Imam%20Bukhari,%20Ayahnya%20Tidak%20Memberikan%20Makan%20Dari%20Harta%20Haram.mp3" type="audio/mpeg">
    </audio>

-   Tematik 67 - Jujurlah Dalam Berdagang, Ada Keberkahan Hartamu Disana

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2067%20-%20Jujurlah%20Dalam%20Berdagang,%20Ada%20Keberkahan%20Hartamu%20Disana.mp3" type="audio/mpeg">
    </audio>

-   Tematik 68 - Hati-hati Fitnah Aurot dan Lawan Jenis

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2068%20-%20Hati-hati%20Fitnah%20Aurot%20dan%20Lawan%20Jenis.mp3" type="audio/mpeg">
    </audio>

-   Tematik 69 - Kisah Taubatnya Penyihir Fir_aun

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2069%20-%20Kisah%20Taubatnya%20Penyihir%20Fir_aun.mp3" type="audio/mpeg">
    </audio>

-   Tematik 70 - Kisah Taubatnya Pembunuh 100 Nyawa

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2070%20-%20Kisah%20Taubatnya%20Pembunuh%20100%20Nyawa.mp3" type="audio/mpeg">
    </audio>

-   Tematik 71 - Kisah Pemilik Onta dan Allah Bergembira dengan Hamba yang Bertobat

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2071%20-%20Kisah%20Pemilik%20Onta%20dan%20Allah%20Bergembira%20dengan%20Hamba%20yang%20Bertobat.mp3" type="audio/mpeg">
    </audio>

-   Tematik 72 - Ayat-ayat yang Memberikan Pengharapan Kepada Seorang Hamba

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2072%20-%20Ayat-ayat%20yang%20Memberikan%20Pengharapan%20Kepada%20Seorang%20Hamba.mp3" type="audio/mpeg">
    </audio>

-   Tematik 73 - Khianatnya Hati Saat Menunda-nunda Taubat, Akhirnya Su_ul Khatimah

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2073%20-%20Khianatnya%20Hati%20Saat%20Menunda-nunda%20Taubat,%20Akhirnya%20Su_ul%20Khatimah.mp3" type="audio/mpeg">
    </audio>

-   Tematik 74 - Saat Mata Berkhianat, Allah Perintahkan Hamba Bertobat

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2074%20-%20Saat%20Mata%20Berkhianat,%20Allah%20Perintahkan%20Hamba%20Bertobat.mp3" type="audio/mpeg">
    </audio>

-   Tematik 75 - Beda Kita dengan Salafus Shaleh

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2075%20-%20Beda%20Kita%20dengan%20Salafus%20Shaleh.mp3" type="audio/mpeg">
    </audio>

-   Tematik 76 - Kita Mengaku Cinta Kepada Allah ﷻ, Tapi Perkaranya Apakah Kita Benar-Benar Dicintai Allah ﷻ

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2076%20-%20Kita%20Mengaku%20Cinta%20Kepada%20Allah%20ﷻ,%20Tapi%20Perkaranya%20Apakah%20Kita%20Benar-Benar%20Dicintai%20Allah%20ﷻ.mp3" type="audio/mpeg">
    </audio>

-   Tematik 77 - Kesalahan Argumen dalam Beragama Menganggap Wali Adalah Maksum

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2077%20-%20Kesalahan%20Argumen%20dalam%20Beragama%20Menganggap%20Wali%20Adalah%20Maksum.mp3" type="audio/mpeg">
    </audio>

-   Tematik 78 - Kesalahan Dalam Beragama Mendahulukan Akal Daripada Dalil

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2078%20-%20Kesalahan%20Dalam%20Beragama%20Mendahulukan%20Akal%20Daripada%20Dalil.mp3" type="audio/mpeg">
    </audio>

-   Tematik 79 - Diantara Kesalahan Dalam Beragama Mengikuti Ijtihad Ulama yang Salah

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2079%20-%20Diantara%20Kesalahan%20Dalam%20Beragama%20Mengikuti%20Ijtihad%20Ulama%20yang%20Salah.mp3" type="audio/mpeg">
    </audio>

-   Tematik 80 - Diantara Kesalahan Dalam Beragama Berdalil dengan Mimpi

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2080%20-%20Diantara%20Kesalahan%20Dalam%20Beragama%20Berdalil%20dengan%20Mimpi.mp3" type="audio/mpeg">
    </audio>

-   Tematik 81 - Diantara Kesalahan Argumentasi Beragama Menjadikan Keberhasilan Sebagai Dalil

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2081%20-%20Diantara%20Kesalahan%20Argumentasi%20Beragama%20Menjadikan%20Keberhasilan%20Sebagai%20Dalil.mp3" type="audio/mpeg">
    </audio>

-   Tematik 82 - Diantara Kesalahan Argumentasi Beragama Menjadikan Kekayaan Barometer Kebenaran

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2082%20-%20Diantara%20Kesalahan%20Argumentasi%20Beragama%20Menjadikan%20Kekayaan%20Barometer%20Kebenaran.mp3" type="audio/mpeg">
    </audio>

-   Tematik 83 - Diantara Kesalahan Beragama Memotong-motong Ayat untuk Dijadikan Dalil

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2083%20-%20Diantara%20Kesalahan%20Beragama%20Memotong-motong%20Ayat%20untuk%20Dijadikan%20Dalil.mp3" type="audio/mpeg">
    </audio>

-   Tematik 84 - Diantara Kesalahan Beragama Berdalil dengan Ayat Mutasyabihat untuk Menjatuhkan yang Muhkam

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2084%20-%20Diantara%20Kesalahan%20Beragama%20Berdalil%20dengan%20Ayat%20Mutasyabihat%20untuk%20Menjatuhkan%20yang%20Muhkam.mp3" type="audio/mpeg">
    </audio>

-   Tematik 85 - Diantara Kesalahan Beragama Berdalil dengan Mayoritas Kebanyakan Orang

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2085%20-%20Diantara%20Kesalahan%20Beragama%20Berdalil%20dengan%20Mayoritas%20Kebanyakan%20Orang.mp3" type="audio/mpeg">
    </audio>

-   Tematik 86 - Diantara Kesalahan Beragama, Berdalil dengan Mengikuti Nenek Moyang

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2086%20-%20Diantara%20Kesalahan%20Beragama,%20Berdalil%20dengan%20Mengikuti%20Nenek%20Moyang.mp3" type="audio/mpeg">
    </audio>

-   Tematik 87 - Diantara Kesalahan Beragama, Berdalil Hadis Dhaif dan Maudhu_

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2087%20-%20Diantara%20Kesalahan%20Beragama,%20Berdalil%20Hadis%20Dhaif%20dan%20Maudhu_.mp3" type="audio/mpeg">
    </audio>

-   Tematik 88 - Diantara Kesalahan Beragama, Berdalil Istilah Palsu yang Mengatasnamakan Syariat

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2088%20-%20Diantara%20Kesalahan%20Beragama,%20Berdalil%20Istilah%20Palsu%20yang%20Mengatasnamakan%20Syariat.mp3" type="audio/mpeg">
    </audio>

-   Tematik 89 - Diantara Kesalahan Beragama, Berdalil dengan Karomah Seseorang

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2089%20-%20Diantara%20Kesalahan%20Beragama,%20Berdalil%20dengan%20Karomah%20Seseorang.mp3" type="audio/mpeg">
    </audio>

-   Tematik 90 - Diantara Kesalahan Beragama, Mencampur Kebenaran dengan Kebatilan

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2090%20-%20Diantara%20Kesalahan%20Beragama,%20Mencampur%20Kebenaran%20dengan%20Kebatilan.mp3" type="audio/mpeg">
    </audio>

-   Tematik 91 - Diantara Kesalahan Beragama, Menetapkan Hukum Dengan Memahami Dalil Sepihak

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2091%20-%20Diantara%20Kesalahan%20Beragama,%20Menetapkan%20Hukum%20Dengan%20Memahami%20Dalil%20Sepihak.mp3" type="audio/mpeg">
    </audio>

-   Tematik 92 - Diantara Kesalahan Beragama, Berdalil dengan Pengalaman Tertentu

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2092%20-%20Diantara%20Kesalahan%20Beragama,%20Berdalil%20dengan%20Pengalaman%20Tertentu.mp3" type="audio/mpeg">
    </audio>

-   Tematik 93 - Diantara Kesalahan Beragama, Hanya Berdalil dengan Hadis Mutawatir dan Menolak Hadis Ahad

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2093%20-%20Diantara%20Kesalahan%20Beragama,%20Hanya%20Berdalil%20dengan%20Hadis%20Mutawatir%20dan%20Menolak%20Hadis%20Ahad.mp3" type="audio/mpeg">
    </audio>

-   Tematik 94 - Diantara Kesalahan Beragama, Berdalil Karena Senioritas Umur Lebih Tua

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2094%20-%20Diantara%20Kesalahan%20Beragama,%20Berdalil%20Karena%20Senioritas%20Umur%20Lebih%20Tua.mp3" type="audio/mpeg">
    </audio>

-   Tematik 95 - Diantara Kesalahan Beragama, Berdalil dengan Perkataan Ahli Filsasat

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2095%20-%20Diantara%20Kesalahan%20Beragama,%20Berdalil%20dengan%20Perkataan%20Ahli%20Filsasat.mp3" type="audio/mpeg">
    </audio>

-   Tematik 96 - Diantara Kesalahan Beragama, Berdalil dengan Perkataan Imam Madzhab

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2096%20-%20Diantara%20Kesalahan%20Beragama,%20Berdalil%20dengan%20Perkataan%20Imam%20Madzhab.mp3" type="audio/mpeg">
    </audio>

-   Tematik 97 - Ilmu Allah yang Maha Luas, Sedangkan Makhluk Sangat Terbatas

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2097%20-%20Ilmu%20Allah%20yang%20Maha%20Luas,%20Sedangkan%20Makhluk%20Sangat%20Terbatas.mp3" type="audio/mpeg">
    </audio>

-   Tematik 98 - Nasihat Bagi Perokok

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2098%20-%20Nasihat%20Bagi%20Perokok.mp3" type="audio/mpeg">
    </audio>

-   Tematik 99 - Dosa Berubah Jadi Pahala dengan Taubat

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%2099%20-%20Dosa%20Berubah%20Jadi%20Pahala%20dengan%20Taubat.mp3" type="audio/mpeg">
    </audio>

-   Tematik 100 - 4 Syarat Tobat Diterima oleh Allah

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%20100%20-%204%20Syarat%20Tobat%20Diterima%20oleh%20Allah.mp3" type="audio/mpeg">
    </audio>

-   Tematik 101 -  Tobat dari Dosa yang Disadari dan Tidak Disadari

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%20101%20-%20%20Tobat%20dari%20Dosa%20yang%20Disadari%20dan%20Tidak%20Disadari.mp3" type="audio/mpeg">
    </audio>

-   Tematik 102 - Bertobatlah Sebelum Azal Menjemput

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%20102%20-%20Bertobatlah%20Sebelum%20Azal%20Menjemput.mp3" type="audio/mpeg">
    </audio>

-   Tematik 103 - Manusia Tidak Lepas Dari Kesalahan, Manusia Terbaik Adalah yang Istighfar dan Bertobat

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%20103%20-%20Manusia%20Tidak%20Lepas%20Dari%20Kesalahan,%20Manusia%20Terbaik%20Adalah%20yang%20Istighfar%20dan%20Bertobat.mp3" type="audio/mpeg">
    </audio>

-   Tematik 104 - Jangan Kau Cela Masa

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%20104%20-%20Jangan%20Kau%20Cela%20Masa.mp3" type="audio/mpeg">
    </audio>

-   Tematik 105 - Ketika Manusia Terlalu Banyak Teori Tentang Kebahagiaan

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%20105%20-%20Ketika%20Manusia%20Terlalu%20Banyak%20Teori%20Tentang%20Kebahagiaan.mp3" type="audio/mpeg">
    </audio>

-   Tematik 106 - Letak Kebahagiaan Sebenarnya

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%20106%20-%20Letak%20Kebahagiaan%20Sebenarnya.mp3" type="audio/mpeg">
    </audio>

-   Tematik 107 - Semakin Bertauhid dan Ikhlas Semakin Dia Bahagia

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%20107%20-%20Semakin%20Bertauhid%20dan%20Ikhlas%20Semakin%20Dia%20Bahagia.mp3" type="audio/mpeg">
    </audio>

-   Tematik 108 - Media Sosial Menjadi Tumbal Kebahagiaan Manusia Saat Ini

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%20108%20-%20Media%20Sosial%20Menjadi%20Tumbal%20Kebahagiaan%20Manusia%20Saat%20Ini.mp3" type="audio/mpeg">
    </audio>

-   Tematik 109 - Menjadi Tumbal Media Sosial Untuk Kebahagiaan Manusia Saat Ini Bag-2

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%20109%20-%20Menjadi%20Tumbal%20Media%20Sosial%20Untuk%20Kebahagiaan%20Manusia%20Saat%20Ini%20Bag-2.mp3" type="audio/mpeg">
    </audio>

-   Tematik 110 -  Ciptakan Surga di Rumah

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%20110%20-%20%20Ciptakan%20Surga%20di%20Rumah.mp3" type="audio/mpeg">
    </audio>

-   Tematik 111 - Saudarakau Saatnya Engkau Berdzikir dan Berkhalwat dengan Allah

    <audio controls preload="none">

    <source src="/kajian-ufa/tematik/Audio%20-%20Tematik/Tematik%20111%20-%20Saudarakau%20Saatnya%20Engkau%20Berdzikir%20dan%20Berkhalwat%20dengan%20Allah.mp3" type="audio/mpeg">
    </audio>

---
