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

1. Q & A - Hukum Menjadi Admin Dakwah Instagram dan Youtube

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/1.%20Q%20_%20A%20-%20Hukum%20Menjadi%20Admin%20Dakwah%20Instagram%20dan%20Youtube.mp3" type="audio/mpeg">
    </audio>

2. Q & A - Aku Takut Meninggalkan Pekerjaan Haram, Karena Takut Jatuh Miskin

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/2.%20Q%20_%20A%20-%20Aku%20Takut%20Meninggalkan%20Pekerjaan%20Haram,%20Karena%20Takut%20Jatuh%20Miskin.mp3" type="audio/mpeg">
    </audio>

3. Q & A - Hukum Aborsi janin

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/3.%20Q%20_%20A%20-%20Hukum%20Aborsi%20janin.mp3" type="audio/mpeg">
    </audio>

4. Q & A - Orang Tua Menolak Menikahkan Anaknya Dengan Alasan Belum Selesai Kuliah

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/4.%20Q%20_%20A%20-%20Orang%20Tua%20Menolak%20Menikahkan%20Anaknya%20Dengan%20Alasan%20Belum%20Selesai%20Kuliah.mp3" type="audio/mpeg">
    </audio>

5. Q & A - Tidak Bisa Memaafkan Karena Sakit Hati Dipecat Juragan

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/5.%20Q%20_%20A%20-%20Tidak%20Bisa%20Memaafkan%20Karena%20Sakit%20Hati%20Dipecat%20Juragan.mp3" type="audio/mpeg">
    </audio>

6. Q & A - Hukum Menceraikan Istri yang Susah Dinasihati

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/6.%20Q%20_%20A%20-%20Hukum%20Menceraikan%20Istri%20yang%20Susah%20Dinasihati.mp3" type="audio/mpeg">
    </audio>

7. Q & A - Hukum Membaca Surat Al-Kahfi Di Hari Jumat

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/7.%20Q%20_%20A%20-%20Hukum%20Membaca%20Surat%20Al-Kahfi%20Di%20Hari%20Jumat.mp3" type="audio/mpeg">
    </audio>

8. Q & A - Bagaimanakah Nasib Janda Kelak Di Surga

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/8.%20Q%20&%20A%20-%20Bagaimanakah%20Nasib%20Janda%20Kelak%20Di%20Surga.mp3" type="audio/mpeg">
    </audio>

9. Q & A - Apakah Suami Akan Tetap Mencintai Istrinya Tatkala Masuk Surga

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/9.%20Q%20&%20A%20-%20Apakah%20Suami%20Akan%20Tetap%20Mencintai%20Istrinya%20Tatkala%20Masuk%20Surga.mp3" type="audio/mpeg">
    </audio>

10. Q & A - Ibuku Pernah Selingkuh, Haruskah Aku Tetap Berbakti Padanya

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/10.%20Q%20&%20A%20-%20Ibuku%20Pernah%20Selingkuh,%20Haruskah%20Aku%20Tetap%20Berbakti%20Padanya.mp3" type="audio/mpeg">
    </audio>

11. Q & A - Kenapa Perceraian Ada di Tangan Laki-laki

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/11.%20Q%20_%20A%20-%20Kenapa%20Perceraian%20Ada%20di%20Tangan%20Laki-laki.mp3" type="audio/mpeg">
    </audio>

12. Q & A - Kapan Istri Boleh Minta Cerai Secara Syar_i

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/12.%20Q%20_%20A%20-%20Kapan%20Istri%20Boleh%20Minta%20Cerai%20Secara%20Syar_i.mp3" type="audio/mpeg">
    </audio>

13. Q & A - Kiat Menghindari Konflik dengan Mertua

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/13.%20Q%20_%20A%20-%20Kiat%20Menghindari%20Konflik%20dengan%20Mertua.mp3" type="audio/mpeg">
    </audio>

14. Q & A - Hukum Makan Harta Haram dan Memanfaatkan Anak Yatim Untuk Donasi

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/14.%20Q%20_%20A%20-%20Hukum%20Makan%20Harta%20Haram%20dan%20Memanfaatkan%20Anak%20Yatim%20Untuk%20Donasi.mp3" type="audio/mpeg">
    </audio>

15. Q & A - Apakah Makanan Haram Berdampak Buruk Kepada Anak Kita

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/15.%20Q%20_%20A%20-%20Apakah%20Makanan%20Haram%20Berdampak%20Buruk%20Kepada%20Anak%20Kita.mp3" type="audio/mpeg">
    </audio>

16. Q & A - Hukum Orang Tua Kerja di Tempat Haram

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/16.%20Q%20_%20A%20-%20Hukum%20Orang%20Tua%20Kerja%20di%20Tempat%20Haram.mp3" type="audio/mpeg">
    </audio>

17. Q & A - Haruskah Bertanya Kehalalan Makanan Kepada Penjual

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/17.%20Q%20_%20A%20-%20Haruskah%20Bertanya%20Kehalalan%20Makanan%20Kepada%20Penjual.mp3" type="audio/mpeg">
    </audio>

18. Q & A - Hukum Ditraktir Makanan Oleh Kawan yang Bekerja di Tempat Haram

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/18.%20Q%20_%20A%20-%20Hukum%20Ditraktir%20Makanan%20Oleh%20Kawan%20yang%20Bekerja%20di%20Tempat%20Haram.mp3" type="audio/mpeg">
    </audio>

19. Q & A - Hukum Berziarah Ke Kuburan Wali dan Orang Shalih

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/19.%20Q%20_%20A%20-%20Hukum%20Berziarah%20Ke%20Kuburan%20Wali%20dan%20Orang%20Shalih.mp3" type="audio/mpeg">
    </audio>

20. Q & A - Bagaimana Sikap yang Benar Ketika Pelaku Kemaksiatan Meninggal Dunia

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/20.%20Q%20_%20A%20-%20Bagaimana%20Sikap%20yang%20Benar%20Ketika%20Pelaku%20Kemaksiatan%20Meninggal%20Dunia.mp3" type="audio/mpeg">
    </audio>

21. Q & A - Bingung Sesama Dai Saling Bantah-Bantahan

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/21.%20Q%20_%20A%20-%20Bingung%20Sesama%20Dai%20Saling%20Bantah-Bantahan.mp3" type="audio/mpeg">
    </audio>

22. Q & A - Hukum Mendengar Ceramah Dari Banyak Dai

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/22.%20Q%20_%20A%20-%20Hukum%20Mendengar%20Ceramah%20Dari%20Banyak%20Dai.mp3" type="audio/mpeg">
    </audio>

23. Q & A - Apakah Orang yang Menunda Tobat Tidak Akan Diberi Petunjuk Lagi Oleh Allah

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/23.%20Q%20_%20A%20-%20Apakah%20Orang%20yang%20Menunda%20Tobat%20Tidak%20Akan%20Diberi%20Petunjuk%20Lagi%20Oleh%20Allah.mp3" type="audio/mpeg">
    </audio>

24. Q & A - Bagaimana Menyikapi Perbedaan dan Perdebatan di Sosial Media Saat ini

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/24.%20Q%20_%20A%20-%20Bagaimana%20Menyikapi%20Perbedaan%20dan%20Perdebatan%20di%20Sosial%20Media%20Saat%20ini.mp3" type="audio/mpeg">
    </audio>

25. Q & A - Sikap Kita Kepada Orang Tua yang Berbeda Kepemahaman Agamanya

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/25.%20Q%20_%20A%20-%20Sikap%20Kita%20Kepada%20Orang%20Tua%20yang%20Berbeda%20Kepemahaman%20Agamanya.mp3" type="audio/mpeg">
    </audio>

26. Q & A - Hukum Wanita Memakai Minyak Wangi

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/26.%20Q%20_%20A%20-%20Hukum%20Wanita%20Memakai%20Minyak%20Wangi.mp3" type="audio/mpeg">
    </audio>

27. Q & A - Hukum Memakai Sepatu Berbahan Kulit Babi

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/27.%20Q%20_%20A%20-%20Hukum%20Memakai%20Sepatu%20Berbahan%20Kulit%20Babi.mp3" type="audio/mpeg">
    </audio>

28. Q & A - Istri Dilarang Suami Ikut Kajian Sunnah

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/28.%20Q%20_%20A%20-%20Istri%20Dilarang%20Suami%20Ikut%20Kajian%20Sunnah.mp3" type="audio/mpeg">
    </audio>

29. Q & A - Bolehkah Wanita Menampakkan Rambut Kepada Saudara Ipar Laki-laki

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/29.%20Q%20_%20A%20-%20Bolehkah%20Wanita%20Menampakkan%20Rambut%20Kepada%20Saudara%20Ipar%20Laki-laki.mp3" type="audio/mpeg">
    </audio>

30. Q & A - Apakah Ada Kewajiban Mendakwahi Tetangga

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/30.%20Q%20_%20A%20-%20Apakah%20Ada%20Kewajiban%20Mendakwahi%20Tetangga.mp3" type="audio/mpeg">
    </audio>

31. Q & A - Suami tidak Memberi Nafkah Bolehkah Istri Tidak Taat Pada Suami

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/31.%20Q%20_%20A%20-%20Suami%20tidak%20Memberi%20Nafkah%20Bolehkah%20Istri%20Tidak%20Taat%20Pada%20Suami.mp3" type="audio/mpeg">
    </audio>

32. Q & A - Tips Agar Pasangan Kenal Hidayah Sunnah

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/32.%20Q%20_%20A%20-%20Tips%20Agar%20Pasangan%20Kenal%20Hidayah%20Sunnah.mp3" type="audio/mpeg">
    </audio>

33. Q & A - Seorang Istri Sedekah Dengan Harta Pribadi

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/33.%20Q%20_%20A%20-%20Seorang%20Istri%20Sedekah%20Dengan%20Harta%20Pribadi.mp3" type="audio/mpeg">
    </audio>

34. Q & A - Hukum Memakai Khadam Jin Muslim

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/34.%20Q%20_%20A%20-%20Hukum%20Memakai%20Khadam%20Jin%20Muslim.mp3" type="audio/mpeg">
    </audio>

35. Q & A - Hukum Bermakmum di Belakang Imam yang Suka Melakukan Kesyirikan

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/35.%20Q%20_%20A%20-%20Hukum%20Bermakmum%20di%20Belakang%20Imam%20yang%20Suka%20Melakukan%20Kesyirikan.mp3" type="audio/mpeg">
    </audio>

36. Q & A -Hukum Poligami dan Maksud Adil dalam Poligami

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/36.%20Q%20_%20A%20-Hukum%20Poligami%20dan%20Maksud%20Adil%20dalam%20Poligami.mp3" type="audio/mpeg">
    </audio>

37. Q & A - Hibah Orang Tua Kepada Anaknya Tidak Adil

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/37.%20Q%20_%20A%20-%20Hibah%20Orang%20Tua%20Kepada%20Anaknya%20Tidak%20Adil.mp3" type="audio/mpeg">
    </audio>

38. Q & A - Hukum Kloset WC Kamar Mandi Menghadap Kiblat

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/38.%20Q%20_%20A%20-%20Hukum%20Kloset%20WC%20Kamar%20Mandi%20Menghadap%20Kiblat.mp3" type="audio/mpeg">
    </audio>

39. Q & A - Hukum Hukum Memelihara Burung dan Kucing

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/39.%20Q%20_%20A%20-%20Hukum%20Hukum%20Memelihara%20Burung%20dan%20Kucing.mp3" type="audio/mpeg">
    </audio>

40. Q & A - Bagaimana Cara Mengetahui Musibah Itu Sebagai Penggugur Dosa Atau Untuk Pengangkat Derajat_

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/40.%20Q%20_%20A%20-%20Bagaimana%20Cara%20Mengetahui%20Musibah%20Itu%20Sebagai%20Penggugur%20Dosa%20Atau%20Untuk%20Pengangkat%20Derajat_.mp3" type="audio/mpeg">
    </audio>

41. Q & A - Hukum Sesaji dengan Alasan Sedekah Memberi Makan Hewan

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/41.%20Q%20_%20A%20-%20Hukum%20Sesaji%20dengan%20Alasan%20Sedekah%20Memberi%20Makan%20Hewan.mp3" type="audio/mpeg">
    </audio>

42. Q & A - Hukum Nadhor dengan Beberapa Calon Wanita Sekaligus

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/42.%20Q%20_%20A%20-%20Hukum%20Nadhor%20dengan%20Beberapa%20Calon%20Wanita%20Sekaligus.mp3" type="audio/mpeg">
    </audio>

43. Q & A - Hukum Membatalkan Shalat Ketika Ada Kebakaran Atau Gempa

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/43.%20Q%20_%20A%20-%20Hukum%20Membatalkan%20Shalat%20Ketika%20Ada%20Kebakaran%20Atau%20Gempa.mp3" type="audio/mpeg">
    </audio>

44. Q & A - Antara Pelit dan Sederhana

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/44.%20Q%20_%20A%20-%20Antara%20Pelit%20dan%20Sederhana.mp3" type="audio/mpeg">
    </audio>

45. Q & A - Hukum Anak Laki-laki Memandikan Jenazah Ibunya

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/45.%20Q%20_%20A%20-%20Hukum%20Anak%20Laki-laki%20Memandikan%20Jenazah%20Ibunya.mp3" type="audio/mpeg">
    </audio>

46. Q & A - Hukum Makanan Mengandung Rum, Atau Sedikit Alkohol

    <audio controls preload="none">

    <source src="/kajian-ufa/q-a/Audio%20-%20Q%20_%20A/46.%20Q%20_%20A%20-%20Hukum%20Makanan%20Mengandung%20Rum,%20Atau%20Sedikit%20Alkohol.mp3" type="audio/mpeg">
    </audio>

---
