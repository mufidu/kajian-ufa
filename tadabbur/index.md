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

-   1 TQ - Hikmah Doa Nabi Zakaria

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/1%20TQ%20-%20Hikmah%20Doa%20Nabi%20Zakaria.mp3" type="audio/mpeg">
    Maaf, browser Anda tidak mendukung pemutaran audio.
    </audio>

-   2 TQ - Allah Menghancurkan Kesombongan Kaum Durhaka 'Ad

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/2%20TQ%20-%20Allah%20Menghancurkan%20Kesombongan%20Kaum%20Durhaka%20_Ad.mp3" type="audio/mpeg">

    </audio>

-   3 TQ - HIkmah Surat Ath Tholaq - Antara Perceraian dan Takwa

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/3%20TQ%20-%20HIkmah%20Surat%20Ath%20Tholaq%20-%20Antara%20Perceraian%20dan%20Takwa.mp3" type="audio/mpeg">

    </audio>

-   4 TQ - Mahalnya Hidayah Kisah 2 Wanita Istri Dari Seorang Nabi

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/4%20TQ-%20Mahalnya%20Hidayah%20Kisah%202%20Wanita%20IStri%20Dari%20Seorang%20Nabi.mp3" type="audio/mpeg">

    </audio>

-   5 TQ - Sabar Hanya Berlaku Di Dunia, Tapi Tidak di Neraka

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/5%20TQ%20-%20Sabar%20Hanya%20Berlaku%20Di%20Dunia,%20Tapi%20Tidak%20di%20Neraka.mp3" type="audio/mpeg">

    </audio>

-   6 TQ - Kiat Terhindar Dari Maksiat dengan Mengingat Nikmat dari Allah

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/6%20TQ%20-%20Kiat%20Terhindar%20Dari%20Maksiat%20dengan%20Mengingat%20Nikmat%20dari%20Allah.mp3" type="audio/mpeg">

    </audio>

-   7 TQ - Hikmah Kisah Nabi Ya_qub Ketika Terkena Musibah

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/7%20TQ%20-%20Hikmah%20Kisah%20Nabi%20Ya_qub%20Ketika%20Terkena%20Musibah.mp3" type="audio/mpeg">

    </audio>

-   8 TQ - Menggabungkan Taqwa dan Sabar untuk Meraih Kesuksesan Dunia dan Akhirat

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/8%20TQ%20-%20Menggabungkan%20Taqwa%20dan%20Sabar%20untuk%20Meraih%20Kesuksesan%20Dunia%20dan%20Akhirat.mp3" type="audio/mpeg">

    </audio>

-   9 TQ - Tingkatan Manusia di Dunia dan Akhirat

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/9%20TQ%20-%20Tingkatan%20Manusia%20di%20Dunia%20dan%20Akhirat.mp3" type="audio/mpeg">

    </audio>

-   10 TQ - Berpikir Dahulu Sebelum Berbicara

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/10%20TQ%20-%20Berpikir%20Dahulu%20Sebelum%20Berbicara.mp3" type="audio/mpeg">

    </audio>

-   11 TQ - Program Setan Membuka Aurot Anak Adam

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/11%20TQ%20-%20Program%20Setan%20Membuka%20Aurot%20Anak%20Adam.mp3" type="audio/mpeg">

    </audio>

-   12 TQ - Amal Kebaikan Akan Menghapuskan Dosa Kecil

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/12%20TQ%20-%20Amal%20Kebaikan%20Akan%20Menghapuskan%20Dosa%20Kecil.mp3" type="audio/mpeg">

    </audio>

-   13 TQ - Catatlah Utang Piutangmu !!

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/13%20TQ%20-%20Catatlah%20Utang%20Piutangmu%20!!.mp3" type="audio/mpeg">

    </audio>

-   14 TQ - NIkmat Persaudaraan

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/14%20TQ%20-%20NIkmat%20Persaudaraan.mp3" type="audio/mpeg">

    </audio>

-   15 TQ - Amalan Saat Kita Terbangun Dari Tidur

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/15%20TQ%20-%20Amalan%20Saat%20Kita%20Terbangun%20Dari%20Tidur.mp3" type="audio/mpeg">

    </audio>

-   16 TQ - Bersyukur Kepada Allah, Bersyukur Kepada Orang Tua

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/16%20TQ%20-%20Bersyukur%20Kepada%20Allah,%20Bersyukur%20Kepada%20Orang%20Tua.mp3" type="audio/mpeg">

    </audio>

-   17 TQ - Rumahku Istanaku, Rumahku Tempat Ibadahku

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/17%20TQ%20-%20Rumahku%20Istanaku,%20Rumahku%20Tempat%20Ibadahku.mp3" type="audio/mpeg">

    </audio>

-   18 TQ - Hati-hati Dengan Hasad, Bisa Menghalangi dari Hidayah

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/18%20TQ%20-%20Hati-hati%20Dengan%20Hasad,%20Bisa%20Menghalangi%20dari%20Hidayah.mp3" type="audio/mpeg">

    </audio>

-   19 TQ - Kembalilah! Jangan Berputus AsaTerhadap Kasih Sayang Allah

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/19%20TQ%20-%20Kembalilah!%20Jangan%20Berputus%20AsaTerhadap%20Kasih%20Sayang%20Allah.mp3" type="audio/mpeg">

    </audio>

-   20 TQ - Janji Allah Ketika Seorang Hamba Bertakwa

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/20%20TQ%20-%20Janji%20Allah%20Ketika%20Seorang%20Hamba%20Bertakwa.mp3" type="audio/mpeg">

    </audio>

-   21 TQ - Saudaraku, Jagalah Keluarga Kita dari Api Neraka

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/21%20TQ%20-%20Saudaraku,%20Jagalah%20Keluarga%20Kita%20dari%20Api%20Neraka.mp3" type="audio/mpeg">

    </audio>

-   22 TQ - Sombong, Saat Merasa Dirinya Sudah Cukup

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/22%20TQ%20-%20Sombong,%20Saat%20Merasa%20Dirinya%20Sudah%20Cukup.mp3" type="audio/mpeg">

    </audio>

-   23 TQ - Kisah Yusuf dengan Wanita-wanita Istana

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/23%20TQ%20-%20Kisah%20Yusuf%20dengan%20Wanita-wanita%20Istana.mp3" type="audio/mpeg">

    </audio>

-   24 TQ - Sifat Al-Abrar dan Muqarrabun

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/24%20TQ%20-%20Sifat%20Al-Abrar%20dan%20Muqarrabun.mp3" type="audio/mpeg">

    </audio>

-   25 TQ - Kiat Lari Dari Maksiat Faidah Dari Kisah Nabi Yusuf

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/25%20TQ%20-%20Kiat%20Lari%20Dari%20Maksiat%20Faidah%20Dari%20Kisah%20Nabi%20Yusuf.mp3" type="audio/mpeg">

    </audio>

-   26 TQ - Janji Iblis Menghiasi Kemaksiatan dengan Keindahan

    <audio controls preload="none">

    <source src="https://mufidu.github.io/kajian-ufa/tadabbur/Audio%20-%20Tadabbur%20Quran/26%20TQ%20-%20Janji%20Iblis%20Menghiasi%20Kemaksiatan%20dengan%20Keindahan.mp3" type="audio/mpeg">

    </audio>

<br>

---
