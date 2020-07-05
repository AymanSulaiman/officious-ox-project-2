notebook = '''
<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>Data analysis for machine learning</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="New-data-Analytics-for-tvg_cd_data">New data Analytics for tvg_cd_data<a class="anchor-link" href="#New-data-Analytics-for-tvg_cd_data">&#182;</a></h1><p>This notebook is going to analyse the <code>tfg_cd_data.csv</code> file and observe how it can be used for machine learning application</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Importing the required modules</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">warnings</span>
<span class="n">warnings</span><span class="o">.</span><span class="n">filterwarnings</span><span class="p">(</span><span class="s1">&#39;ignore&#39;</span><span class="p">)</span>
<span class="o">%</span><span class="k">matplotlib</span> inline
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s1">&#39;tvg_cd_data.csv&#39;</span><span class="p">))</span>
<span class="n">df</span><span class="o">.</span><span class="n">tail</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[2]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>racedater</th>
      <th>tvgtrackcode</th>
      <th>race</th>
      <th>bettinginterestnumber</th>
      <th>horsename</th>
      <th>morninglineodds</th>
      <th>currentodds</th>
      <th>tvghorseweight</th>
      <th>tvghorsedamsirename</th>
      <th>tvghorseage</th>
      <th>...</th>
      <th>tvghorsenumberofwins</th>
      <th>tvghorsenumberofstarts</th>
      <th>tvghorsepowerrating</th>
      <th>tvghorseaveragespeed</th>
      <th>tvghorseaverageclassrating</th>
      <th>currentodds.1</th>
      <th>winpayout</th>
      <th>placepayout</th>
      <th>showpayout</th>
      <th>scratched</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2224</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>7</td>
      <td>out cold</td>
      <td>20.0</td>
      <td>SC</td>
      <td>123</td>
      <td>northern afleet</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>2</td>
      <td>69.8</td>
      <td>75</td>
      <td>81</td>
      <td>SC</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2225</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>8</td>
      <td>irish spirit</td>
      <td>3.0</td>
      <td>3</td>
      <td>123</td>
      <td>forest camp</td>
      <td>5</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>78.4</td>
      <td>89</td>
      <td>97</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2226</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>9</td>
      <td>alex's strike</td>
      <td>8.0</td>
      <td>4</td>
      <td>123</td>
      <td>smart strike</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>8</td>
      <td>84.4</td>
      <td>80</td>
      <td>87</td>
      <td>4</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2227</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>10</td>
      <td>heros reward</td>
      <td>10.0</td>
      <td>2</td>
      <td>118</td>
      <td>smart strike</td>
      <td>3</td>
      <td>...</td>
      <td>1</td>
      <td>3</td>
      <td>86.1</td>
      <td>77</td>
      <td>90</td>
      <td>2</td>
      <td>6.2</td>
      <td>4.2</td>
      <td>3.8</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2228</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>11</td>
      <td>nice of me</td>
      <td>20.0</td>
      <td>19</td>
      <td>123</td>
      <td>allen's prospect</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>7</td>
      <td>79.2</td>
      <td>74</td>
      <td>90</td>
      <td>19</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Going to draw some histograms for this dataset</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">column_list</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">columns</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">column_list</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;racedater&#39;, &#39;tvgtrackcode&#39;, &#39;race&#39;, &#39;bettinginterestnumber&#39;, &#39;horsename&#39;, &#39;morninglineodds&#39;, &#39;currentodds&#39;, &#39;tvghorseweight&#39;, &#39;tvghorsedamsirename&#39;, &#39;tvghorseage&#39;, &#39;tvghorsesex&#39;, &#39;tvghorsedaysoff&#39;, &#39;tvghorsenumberofwins&#39;, &#39;tvghorsenumberofstarts&#39;, &#39;tvghorsepowerrating&#39;, &#39;tvghorseaveragespeed&#39;, &#39;tvghorseaverageclassrating&#39;, &#39;currentodds.1&#39;, &#39;winpayout&#39;, &#39;placepayout&#39;, &#39;showpayout&#39;, &#39;scratched&#39;]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">tvghorseweight</span><span class="o">.</span><span class="n">min</span><span class="p">())</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">tvghorseweight</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>0
126
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Histogram-Analysis">Histogram Analysis<a class="anchor-link" href="#Histogram-Analysis">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df</span><span class="o">.</span><span class="n">tvghorseweight</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df</span><span class="o">.</span><span class="n">tvghorseage</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>There appears to be a huge amount of range, After inspecting the data on jupyter labs, there are horse called <code>(null)</code> so we shall get rid of them and find the true values</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_copy</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_copy</span> <span class="o">=</span> <span class="n">df_copy</span><span class="p">[</span><span class="n">df</span><span class="o">.</span><span class="n">tvghorsedamsirename</span> <span class="o">!=</span> <span class="s1">&#39;(null)&#39;</span><span class="p">]</span>
<span class="n">df_copy</span><span class="o">.</span><span class="n">tail</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[8]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>racedater</th>
      <th>tvgtrackcode</th>
      <th>race</th>
      <th>bettinginterestnumber</th>
      <th>horsename</th>
      <th>morninglineodds</th>
      <th>currentodds</th>
      <th>tvghorseweight</th>
      <th>tvghorsedamsirename</th>
      <th>tvghorseage</th>
      <th>...</th>
      <th>tvghorsenumberofwins</th>
      <th>tvghorsenumberofstarts</th>
      <th>tvghorsepowerrating</th>
      <th>tvghorseaveragespeed</th>
      <th>tvghorseaverageclassrating</th>
      <th>currentodds.1</th>
      <th>winpayout</th>
      <th>placepayout</th>
      <th>showpayout</th>
      <th>scratched</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2224</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>7</td>
      <td>out cold</td>
      <td>20.0</td>
      <td>SC</td>
      <td>123</td>
      <td>northern afleet</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>2</td>
      <td>69.8</td>
      <td>75</td>
      <td>81</td>
      <td>SC</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2225</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>8</td>
      <td>irish spirit</td>
      <td>3.0</td>
      <td>3</td>
      <td>123</td>
      <td>forest camp</td>
      <td>5</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>78.4</td>
      <td>89</td>
      <td>97</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2226</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>9</td>
      <td>alex's strike</td>
      <td>8.0</td>
      <td>4</td>
      <td>123</td>
      <td>smart strike</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>8</td>
      <td>84.4</td>
      <td>80</td>
      <td>87</td>
      <td>4</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2227</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>10</td>
      <td>heros reward</td>
      <td>10.0</td>
      <td>2</td>
      <td>118</td>
      <td>smart strike</td>
      <td>3</td>
      <td>...</td>
      <td>1</td>
      <td>3</td>
      <td>86.1</td>
      <td>77</td>
      <td>90</td>
      <td>2</td>
      <td>6.2</td>
      <td>4.2</td>
      <td>3.8</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2228</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>11</td>
      <td>nice of me</td>
      <td>20.0</td>
      <td>19</td>
      <td>123</td>
      <td>allen's prospect</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>7</td>
      <td>79.2</td>
      <td>74</td>
      <td>90</td>
      <td>19</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorseweight</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse weight histogram&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;weight (lb)&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorseage</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse age histogram&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;age (years)&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorsedaysoff</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse number of days off histogram&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;Number of days off&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorsenumberofwins</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse number of wins histogram&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;Number of wins&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorsepowerrating</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse power rating&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;horsepower&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorseaveragespeed</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse average speed&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;Speed (Beyer)&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorseaverageclassrating</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse average class rating&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;horse average class rating&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>There appears to be a consistant theme here, there is a value of zeros at the same count, lets get rid of them</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_copy</span> <span class="o">=</span> <span class="n">df_copy</span><span class="p">[</span><span class="n">df</span><span class="o">.</span><span class="n">tvghorseaverageclassrating</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">]</span>
<span class="n">df_copy</span><span class="o">.</span><span class="n">tail</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[16]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>racedater</th>
      <th>tvgtrackcode</th>
      <th>race</th>
      <th>bettinginterestnumber</th>
      <th>horsename</th>
      <th>morninglineodds</th>
      <th>currentodds</th>
      <th>tvghorseweight</th>
      <th>tvghorsedamsirename</th>
      <th>tvghorseage</th>
      <th>...</th>
      <th>tvghorsenumberofwins</th>
      <th>tvghorsenumberofstarts</th>
      <th>tvghorsepowerrating</th>
      <th>tvghorseaveragespeed</th>
      <th>tvghorseaverageclassrating</th>
      <th>currentodds.1</th>
      <th>winpayout</th>
      <th>placepayout</th>
      <th>showpayout</th>
      <th>scratched</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2224</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>7</td>
      <td>out cold</td>
      <td>20.0</td>
      <td>SC</td>
      <td>123</td>
      <td>northern afleet</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>2</td>
      <td>69.8</td>
      <td>75</td>
      <td>81</td>
      <td>SC</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2225</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>8</td>
      <td>irish spirit</td>
      <td>3.0</td>
      <td>3</td>
      <td>123</td>
      <td>forest camp</td>
      <td>5</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>78.4</td>
      <td>89</td>
      <td>97</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2226</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>9</td>
      <td>alex's strike</td>
      <td>8.0</td>
      <td>4</td>
      <td>123</td>
      <td>smart strike</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>8</td>
      <td>84.4</td>
      <td>80</td>
      <td>87</td>
      <td>4</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2227</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>10</td>
      <td>heros reward</td>
      <td>10.0</td>
      <td>2</td>
      <td>118</td>
      <td>smart strike</td>
      <td>3</td>
      <td>...</td>
      <td>1</td>
      <td>3</td>
      <td>86.1</td>
      <td>77</td>
      <td>90</td>
      <td>2</td>
      <td>6.2</td>
      <td>4.2</td>
      <td>3.8</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2228</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>11</td>
      <td>nice of me</td>
      <td>20.0</td>
      <td>19</td>
      <td>123</td>
      <td>allen's prospect</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>7</td>
      <td>79.2</td>
      <td>74</td>
      <td>90</td>
      <td>19</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Re-visualising</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorseweight</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse weight histogram&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;weight (lb)&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorseage</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse age histogram&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;age (years)&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorsedaysoff</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse number of days off histogram&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;Number of days off&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorsenumberofwins</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse number of wins histogram&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;Number of wins&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAYUAAAEWCAYAAACJ0YulAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAavUlEQVR4nO3de7hddX3n8ffHBLCoCJiAEGiDihfoUy+NeKvKCKPUCzCOWHy0ppYZekFbW5021NYyHZlBq63WSi0Va1QqpV5KvLTiUEBsKxiQooBIlFsghnhF7JQ2+J0/1u8sd072OdkJZ599krxfz3Oesy6/tfd3//Y++3PWb+29VqoKSZIAHjDpAiRJC4ehIEnqGQqSpJ6hIEnqGQqSpJ6hIEnqGQq7qCS3JDl20nVMSpJfSPK5Cd7/ryTZmOSeJA/bwdt4ZpIbx1BbJXnUDOtenuSiub5P7TwMBWmOJdkD+CPguVX14Kr61o7cTlVdXlWPmdvqtnmf51XVc7fVLsn7krxpPmrS/DIUNKskiyddw6TtQB8cCDwQuG4M5ezyfM1NlqGwa3tCkmuTfC/JXyd54NSKJP89ybok306yJsnBA+sqyWlJbgJuSuePk9zVbuvaJD/Z2u6V5K1JbmvDJe9O8mPDipka0mntv5Pk5iQ/O7B+iyGvJGck+WCbXt7qelWS29v2v5zkya2e7yb5063vMu9sNX8lyTEDKx6a5NwkG5LckeRNSRYN1PmP7TF/GzhjyGPZK8nbk9zZft7elj0amBry+W6Sfxiy7eokr2vTy9rj+tU2/6j2nCTJ0UnWT+uf1w97TpMsSfKJ1g/fTnJ5ktn+vo9NclPrx3clyeBzNNV5w573JKcCLwd+qw2Pfby1f1ySS1sN1yU5fqD2hyX5eJK7k3yh9ffnBtZv8Zpry97Rnuu7k1yV5JnTXht/k+SDSb6f5EtJHp3k9Fbv7Um2ucejrRkKu7aXAscBhwE/BfwCQJLnAP+nrT8IuBU4f9q2JwJPAY4Angs8C3g0sC/wc8DUkMib2/InAI8ClgFvnKWmp9C9aS4B3gKcO/WGNKKnAIe3Gt4OvAE4FjgSeGmSZ09r+/V2X78PfDTJ/m3damBzq/mJ7TH+tyHbHgCcOaSONwBPpXvcjweOAn63qr7aagHYt6qeM2Tby4Cj2/Sz2/1M1f0s4PKa+fwzQ59T4HXAemAp3Z7K7wCzncPmhcCTW+0vBZ43pM3Q572qzgHOA97ShsdelG7I7OPARXR99hrgvCRTw1/vAn4APBxY2X6mG3zNAXyBrn/3B/4K+JsM/GMDvAj4ALAf8EXg03TvacuAPwD+fJbHr5lUlT+74A9wC/CKgfm3AO9u0+fS/UFPrXsw8B/A8jZfwHMG1j8H+Crdm+ADBpaH7g/9kQPLngbcPENNvwCsG5jfu93XwwdqPnZg/RnAB9v08tZ22cD6bwE/NzD/EeC1A/d1J5CB9VcCP0/3pnkv8GMD614GXDKw7W3b6N+vAc8fmH8ecMu0WhfPsO0jge/SvYG9G/glYH1btxr4zTZ99NTyEZ7TPwAuBB41wmujgJ8ZmL8AWDXw2D832/Pe1r0PeNPA/DOBb0x7fXyoPYeL2uvrMQPr3jR1P8NeczPU/R3g8QOvjc8MrHsRcA+wqM0/pN3mvpP+W9zZftxT2LV9Y2D6X+ne/AEOpts7AKCq7qF7g1020P72gfX/APwp3X97G5Ock2Qfuv9K9wauakMG3wX+vi3fZk1V9a9t8sEztB1m48D0/xsyP3hbd1R7h2hupXvsPwHsAWwYqPvP6f7DnXI7s9uiDwdue5uq6mt0b2BPoHsz/QRwZ/uv+tl0exIzmek5/UNgHXBRkq8nWbWNMma6ncE6Z3rehzkYuL2qfjiw7Fa619RSYDFb9umw/t1iWZLXJbmhDV19F3go3V7flOnP/Ter6r6BeYY9Ls3OUNg93Un3xghAkgcBDwPuGGizxdBDVf1JVf003dDIo4H/AXyT7o/vyKrat/08tKp29A/xB3QhM+XhO3g7U5ZNG5r6cbrHfjvdnsKSgbr3qaojB9pu6/TBW/ThwG2P6jLgJcCeVXVHm38l3VDINdtxOwBU1fer6nVV9Qi6/5p/c/AYyo6a4XmHrfvnTuDQaccxfpzuNbWJbqjukIF1hw67u6mJdvzgt+mGtvarqn2B79HtnWqMDIXd018Br0ryhCR7Af8buKKqbhnWON3B3Ke0ceMfAP8G3Nf+K/wL4I+THNDaLksybHx6FNcAJyfZI8kKujfN++MA4Nfa7Z0EPA74VFVtoBv7fluSfZI8IMkjpx2P2JYPAb+bZGmSJXTHUT64HdtfBrwa+Gybv5RuHP5zA//tjizJC9tB6gB3A/e1nx020/PeVm8EHjHQ/IrW5rdafx9NF07nt8fzUeCMJHsneSxdAM7mIXRBsglYnOSNwEx7KZpDhsJuqKouBn6Pbgx+A90Y98mzbLIP3Zv/d+iGBL4FvLWt+226YYvPJ7kb+L/Ajn62/vdaLd8B/iddeN0fV9AdlP4m3cHil9SPvjPwSmBP4Pp2fx+mO+g+qjcBa4FrgS8BV7dlo7qM7o1vKhQ+R7eX9NkZt5jd4XR9fw/wz8DZVXXpDt7WlNme93OBI9rw299W1b8DxwM/S9ffZwOvrKqvtPavphv++QbdweEP0e2tzeTTwN/RHdO4lS6QtjWkpzmQLYdcJWn8kryZ7gMGwz6FpAlyT0HS2CV5bJKfat99OAo4BfjYpOvS1vzmoKT58BC6IaODgbuAt9F9hFYLjMNHkqSew0eSpN5OPXy0ZMmSWr58+aTLkKSdylVXXfXNqhr6JdOdOhSWL1/O2rVrJ12GJO1Uktw60zqHjyRJPUNBktQzFCRJPUNBktQzFCRJPUNBktQzFCRJPUNBktQzFCRJvZ36G8331/JVn9zhbW856wVzWIkkLQzuKUiSeoaCJKlnKEiSeoaCJKlnKEiSeoaCJKlnKEiSeoaCJKlnKEiSeoaCJKk31lBI8htJrkvy5SQfSvLAJPsn+UySm9rv/Qban55kXZIbkzxvnLVJkrY2tlBIsgz4NWBFVf0ksAg4GVgFXFxVhwMXt3mSHNHWHwkcB5ydZNG46pMkbW3cw0eLgR9LshjYG7gTOAFY3davBk5s0ycA51fVvVV1M7AOOGrM9UmSBowtFKrqDuCtwG3ABuB7VXURcGBVbWhtNgAHtE2WAbcP3MT6tmwLSU5NsjbJ2k2bNo2rfEnaLY1z+Gg/uv/+DwMOBh6U5BWzbTJkWW21oOqcqlpRVSuWLl06N8VKkoDxDh8dC9xcVZuq6j+AjwJPBzYmOQig/b6rtV8PHDqw/SF0w02SpHkyzlC4DXhqkr2TBDgGuAFYA6xsbVYCF7bpNcDJSfZKchhwOHDlGOuTJE0ztiuvVdUVST4MXA1sBr4InAM8GLggySl0wXFSa39dkguA61v706rqvnHVJ0na2lgvx1lVvw/8/rTF99LtNQxrfyZw5jhrkiTNzG80S5J6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqWcoSJJ6Yw2FJPsm+XCSryS5IcnTkuyf5DNJbmq/9xtof3qSdUluTPK8cdYmSdrauPcU3gH8fVU9Fng8cAOwCri4qg4HLm7zJDkCOBk4EjgOODvJojHXJ0kaMLZQSLIP8CzgXICq+veq+i5wArC6NVsNnNimTwDOr6p7q+pmYB1w1LjqkyRtbZx7Co8ANgF/meSLSd6T5EHAgVW1AaD9PqC1XwbcPrD9+rZsC0lOTbI2ydpNmzaNsXxJ2v2MMxQWA08C/qyqngj8gDZUNIMMWVZbLag6p6pWVNWKpUuXzk2lkiRgvKGwHlhfVVe0+Q/ThcTGJAcBtN93DbQ/dGD7Q4A7x1ifJGmasYVCVX0DuD3JY9qiY4DrgTXAyrZsJXBhm14DnJxkrySHAYcDV46rPknS1haP+fZfA5yXZE/g68Cr6ILogiSnALcBJwFU1XVJLqALjs3AaVV135jrkyQNGGsoVNU1wIohq46Zof2ZwJnjrEmSNDO/0SxJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6o0UCkkuHmWZJGnntni2lUkeCOwNLEmyH5C2ah/g4DHXJkmaZ7OGAvBLwGvpAuAqfhQKdwPvGmNdkqQJmDUUquodwDuSvKaq3jlPNUmSJmRbewoAVNU7kzwdWD64TVW9f0x1SZImYKRQSPIB4JHANcB9bXEBhoIk7UJGCgVgBXBEVdU4i5EkTdao31P4MvDwcRYiSZq8UfcUlgDXJ7kSuHdqYVUdP5aqdgLLV31yh7e95awXzGElkjR3Rg2FM8ZZhCRpYRj100eXjbsQSdLkjfrpo+/TfdoIYE9gD+AHVbXPuAqTJM2/UfcUHjI4n+RE4KixVCRJmpgdOktqVf0t8Jw5rkWSNGGjDh+9eGD2AXTfW/A7C5K0ixn100cvGpjeDNwCnDDn1UiSJmrUYwqvGnchkqTJG/UiO4ck+ViSu5JsTPKRJIeMuzhJ0vwa9UDzXwJr6K6rsAz4eFsmSdqFjBoKS6vqL6tqc/t5H7B0jHVJkiZg1FD4ZpJXJFnUfl4BfGuUDVv7Lyb5RJvfP8lnktzUfu830Pb0JOuS3Jjkedv/cCRJ98eoofCLwEuBbwAbgJcAox58/nXghoH5VcDFVXU4cHGbJ8kRwMnAkcBxwNlJFo14H5KkOTBqKPwvYGVVLa2qA+hC4oxtbdQORr8AeM/A4hOA1W16NXDiwPLzq+reqroZWIffmpakeTVqKPxUVX1naqaqvg08cYTt3g78FvDDgWUHVtWGdjsbgAPa8mXA7QPt1rdlW0hyapK1SdZu2rRpxPIlSaMYNRQeMG3sf3+28R2HJC8E7qqqq0a8jwxZttW3pqvqnKpaUVUrli71WLckzaVRv9H8NuCfknyY7o36pcCZ29jmGcDxSZ4PPBDYJ8kHgY1JDqqqDUkOAu5q7dcDhw5sfwhw54j1SZLmwEh7ClX1fuC/AhuBTcCLq+oD29jm9Ko6pKqW0x1A/oeqegXd9x1WtmYrgQvb9Brg5CR7JTkMOBy4cjsfjyTpfhh1T4Gquh64fg7u8yzggiSnALcBJ7Xbvy7JBe0+NgOnVdV9c3B/kqQRjRwK90dVXQpc2qa/BRwzQ7sz2fawlCRpTHboegqSpF2ToSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqSeoSBJ6hkKkqTevFyjWVtavuqTO7ztLWe9YA4rkaQtuacgSeoZCpKknqEgSeoZCpKknqEgSeoZCpKknqEgSeoZCpKknqEgSeoZCpKknqEgSeoZCpKknqEgSeoZCpKknqEgSeoZCpKknqEgSeoZCpKknqEgSeqNLRSSHJrkkiQ3JLkuya+35fsn+UySm9rv/Qa2OT3JuiQ3JnneuGqTJA03zj2FzcDrqupxwFOB05IcAawCLq6qw4GL2zxt3cnAkcBxwNlJFo2xPknSNGMLharaUFVXt+nvAzcAy4ATgNWt2WrgxDZ9AnB+Vd1bVTcD64CjxlWfJGlr83JMIcly4InAFcCBVbUBuuAADmjNlgG3D2y2vi2TJM2TsYdCkgcDHwFeW1V3z9Z0yLIacnunJlmbZO2mTZvmqkxJEmMOhSR70AXCeVX10bZ4Y5KD2vqDgLva8vXAoQObHwLcOf02q+qcqlpRVSuWLl06vuIlaTc0zk8fBTgXuKGq/mhg1RpgZZteCVw4sPzkJHslOQw4HLhyXPVJkra2eIy3/Qzg54EvJbmmLfsd4CzggiSnALcBJwFU1XVJLgCup/vk0mlVdd8Y65MkTTO2UKiqzzH8OAHAMTNscyZw5rhqkiTNzm80S5J6hoIkqWcoSJJ6hoIkqWcoSJJ6hoIkqTfO7yloDJav+uQOb3vLWS+Yw0ok7YrcU5Ak9QwFSVLPUJAk9QwFSVLPUJAk9QwFSVLPUJAk9QwFSVLPUJAk9QwFSVLPUJAk9QwFSVLPUJAk9QwFSVLPUJAk9QwFSVLPUJAk9QwFSVLPy3HuRu7PpTzBy3lKuwP3FCRJPUNBktQzFCRJPUNBktQzFCRJPUNBktTzI6ka2f35SKsfZ5V2Du4pSJJ6hoIkqWcoSJJ6HlPQvPB4hLRzcE9BktRzT0EL3v09kd/94V6KdjeGgjQmDplpZ7Tgho+SHJfkxiTrkqyadD2StDtZUHsKSRYB7wL+M7Ae+EKSNVV1/WQrk+bXpPYyvOaGFlQoAEcB66rq6wBJzgdOAAwFaUSTPAajnd9CC4VlwO0D8+uBpww2SHIqcGqbvSfJjffj/pYA37wf288X65xbI9eZN4+5km3bqfp0AfTXtuxU/TnG2/+JmVYstFDIkGW1xUzVOcA5c3JnydqqWjEXtzVO1jm3dpY6Yeep1Trn1iTrXGgHmtcDhw7MHwLcOaFaJGm3s9BC4QvA4UkOS7IncDKwZsI1SdJuY0ENH1XV5iSvBj4NLALeW1XXjfEu52QYah5Y59zaWeqEnadW65xbE6szVbXtVpKk3cJCGz6SJE2QoSBJ6u3yobCt02ak8ydt/bVJnjShOg9NckmSG5Jcl+TXh7Q5Osn3klzTft44oVpvSfKlVsPaIesn3qdJHjPQT9ckuTvJa6e1mVh/JnlvkruSfHlg2f5JPpPkpvZ7vxm2nbdTwcxQ5x8m+Up7bj+WZN8Ztp31dTIPdZ6R5I6B5/f5M2w76f7864Eab0lyzQzbzk9/VtUu+0N3sPprwCOAPYF/AY6Y1ub5wN/RfUfiqcAVE6r1IOBJbfohwFeH1Ho08IkF0K+3AEtmWb8g+nTa6+AbwE8slP4EngU8CfjywLK3AKva9CrgzTM8lllf0/NQ53OBxW36zcPqHOV1Mg91ngG8foTXxkT7c9r6twFvnGR/7up7Cv1pM6rq34Gp02YMOgF4f3U+D+yb5KD5LrSqNlTV1W36+8ANdN/w3hktiD4dcAzwtaq6dYI1bKGqPgt8e9riE4DVbXo1cOKQTUd5TY+1zqq6qKo2t9nP032faKJm6M9RTLw/pyQJ8FLgQ+O6/1Hs6qEw7LQZ099oR2kzr5IsB54IXDFk9dOS/EuSv0ty5LwW9iMFXJTkqnbakekWWp+ezMx/aAuhP6ccWFUboPsnAThgSJuF1re/SLdXOMy2Xifz4dVtmOu9MwzHLaT+fCawsapummH9vPTnrh4K2zxtxoht5k2SBwMfAV5bVXdPW3013RDI44F3An873/U1z6iqJwE/C5yW5FnT1i+YPm1fgjwe+JshqxdKf26PhdS3bwA2A+fN0GRbr5Nx+zPgkcATgA10QzPTLZj+BF7G7HsJ89Kfu3oojHLajAVzao0ke9AFwnlV9dHp66vq7qq6p01/CtgjyZJ5LpOqurP9vgv4GN0u+KAF06d0f0BXV9XG6SsWSn8O2Dg1zNZ+3zWkzYLo2yQrgRcCL6824D3dCK+TsaqqjVV1X1X9EPiLGe5/ofTnYuDFwF/P1Ga++nNXD4VRTpuxBnhl+8TMU4HvTe3Cz6c2nngucENV/dEMbR7e2pHkKLrn71vzVyUkeVCSh0xN0x10/PK0ZguiT5sZ//taCP05zRpgZZteCVw4pM3ETwWT5Djgt4Hjq+pfZ2gzyutkrKYdx/ovM9z/xPuzORb4SlWtH7ZyXvtz3EeyJ/1D90mYr9J9wuANbdkvA7/cpkN3YZ+vAV8CVkyozp+h2229Frim/Tx/Wq2vBq6j+4TE54GnT6DOR7T7/5dWy0Lu073p3uQfOrBsQfQnXVBtAP6D7r/VU4CHARcDN7Xf+7e2BwOfmu01Pc91rqMbh596nb57ep0zvU7muc4PtNfftXRv9ActxP5sy9839bocaDuR/vQ0F5Kk3q4+fCRJ2g6GgiSpZyhIknqGgiSpZyhIknqGgnZqSSrJ2wbmX5/kjDm67fcleclc3NY27uekdGfHvWQHtv2ncdSk3ZehoJ3dvcCLJ/xN5K0kWbQdzU8BfrWq/tP23k9VPX17t5FmYyhoZ7eZ7nq2vzF9xfT/9JPc034fneSyJBck+WqSs5K8PMmV7Xz1jxy4mWOTXN7avbBtvyjdNQW+0E629ksDt3tJkr+i+9LU9Hpe1m7/y0ne3Ja9ke6Li+9O8ofT2p+d5Pg2/bEk723TpyR505DHdGmSD6e71sF5A9/WPivJ9a3Wt+5YN2t3sXjSBUhz4F3AtUnesh3bPB54HN1pjL8OvKeqjkp3caPXAFMX5FkOPJvuxGqXJHkU8Eq6U3c8OclewD8muai1Pwr4yaq6efDOkhxMd+2Bnwa+Q3e2yxOr6g+SPIfuvP/TL5zyWbozZ66hO3Pn1GkbfobuFM/TPRE4ku7cPf8IPCPJ9XSneHhsVVVmuCCONMU9Be30qjub7PuBX9uOzb5Q3TUs7qU7vcHUm/qX6IJgygVV9cPqTmf8deCxdOedeWW6K2RdQXd6isNb+yunB0LzZODSqtpU3bUIzqO74MpsLgeemeQI4Hp+dMK8pwHDjiVcWVXrqzsB3DXtcdwN/BvwniQvBoaeq0iaYihoV/F2urH5Bw0s20x7jbehlD0H1t07MP3DgfkfsuUe9PTzwBTduZ1eU1VPaD+HVdVUqPxghvqGnaJ5VlV1B7AfcBzdXsPldBdhuae6CzFNN/iY7qO7Otpmur2Xj9BdtOfvt7cO7V4MBe0SqurbwAV0wTDlFrrhGuiuprXHDtz0SUke0I4zPAK4Efg08CvtVOckeXQ7c+VsrgCenWRJOwj9MuCyEe7/n+mGsqZC4fXt90jSXZ/jodWdGvy1dNcWkGbkMQXtSt5Gd+bTKX8BXJjkSrqzjs70X/xsbqR78z6Q7iyW/5bkPXRDM1e3PZBNDL90Zq+qNiQ5HbiEbq/hU1U17NTY010OPLeq1iW5Fdif7QgFuut9X5jkge1+tzogLw3yLKmSpJ7DR5KknqEgSeoZCpKknqEgSeoZCpKknqEgSeoZCpKk3v8HtTMLbV4aXP0AAAAASUVORK5CYII=
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorsepowerrating</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse power rating&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;horsepower&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorseaveragespeed</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse average speed&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;Speed (Beyer)&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">()</span>
<span class="n">n_bins</span> <span class="o">=</span> <span class="mi">20</span>
<span class="n">ax</span><span class="o">.</span><span class="n">hist</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="o">.</span><span class="n">tvghorseaverageclassrating</span><span class="p">,</span> <span class="n">bins</span><span class="o">=</span><span class="n">n_bins</span><span class="p">);</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s1">&#39;horse average class rating&#39;</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">&#39;horse average class rating&#39;</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">&#39;count&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Data looks a lot cleaner and useable</p>
<p>I will analyse the data further and apply a regression model to measure the, predict and contrast the data.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_copy</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s1">&#39;cleaned_tvg_cd_data.csv&#39;</span><span class="p">,</span><span class="n">index</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">x</span> <span class="o">=</span> <span class="nb">len</span><span class="p">([</span><span class="n">i</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">df_copy</span><span class="o">.</span><span class="n">columns</span><span class="p">])</span>
<span class="n">x</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[25]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>22</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Machine-Learning">Machine Learning<a class="anchor-link" href="#Machine-Learning">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">features</span> <span class="o">=</span> <span class="p">[</span>
    <span class="s1">&#39;tvghorseweight&#39;</span><span class="p">,</span> 
    <span class="s1">&#39;tvghorseage&#39;</span><span class="p">,</span> 
    <span class="s1">&#39;tvghorsedaysoff&#39;</span><span class="p">,</span> 
    <span class="s1">&#39;tvghorsenumberofwins&#39;</span><span class="p">,</span> 
    <span class="s1">&#39;tvghorsepowerrating&#39;</span><span class="p">,</span> 
    <span class="s1">&#39;tvghorseaverageclassrating&#39;</span>
<span class="p">]</span>
<span class="n">target</span> <span class="o">=</span> <span class="s1">&#39;tvghorseaveragespeed&#39;</span>

<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">features</span><span class="p">:</span>
    <span class="n">x</span><span class="o">=</span><span class="n">df_copy</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="n">y</span><span class="o">=</span><span class="n">df_copy</span><span class="p">[</span><span class="n">target</span><span class="p">]</span>
    <span class="n">m</span><span class="p">,</span> <span class="n">c</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">polyfit</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="s1">&#39;o&#39;</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">m</span><span class="o">*</span><span class="n">x</span> <span class="o">+</span> <span class="n">c</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="n">target</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="sa">f</span><span class="s1">&#39;</span><span class="si">{</span><span class="n">i</span><span class="si">}</span><span class="s1"> and </span><span class="si">{</span><span class="n">target</span><span class="si">}</span><span class="s1">&#39;</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAYYAAAEWCAYAAABi5jCmAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOydeZwUxfXAv29md2FBZEHxWuUyBqKiokRRjPFI1HiBV6JoYrxjTDySoBDvK6zBmJhDo8ZEo4LihfcVAY1GISAi8fp5obiiogIqLHu+3x/ds9s92z3Tc+3M7L7v57Ofnak+6lV1T72qeq9eiapiGIZhGAlixRbAMAzDKC1MMRiGYRg+TDEYhmEYPkwxGIZhGD5MMRiGYRg+TDEYhmEYPkwxuIjIj0Xk2WLL0d0RkbkiclKx5UiFiLwiInsWW450iIiKyNe6IJ89ReSDQudjdA0iMtR9dyrCzilrxSAiS0XkO8WWwyhfRORmEbncm6aq26jq3CKJlBfKQQEbpUtZK4ZSJZUmLgXEods/+1J/Dj2RcngmIhIvtgxFR1XL8g+4FWgDGoCvgHOAx4CfJZ23GDjM/bwv8AawGrgWeBo4yT32Y+BZ4CpgJfAu8D3PfTYDHgA+B94CTvYcuxi4G7gN+AI4CdgZWOB+/xi42nP+WOA/wCpXvj09x44HXgO+BN4BTvUcew04yPO9AvgU2DHCfecCVwDPuXX2tVR5udecAywHPnTLpMDX3GO93Lp63y3fX4Fqz7XjgZfc8r8N7O+RI1HnWwKzgc/cctwO1HjucS5Q78r3BrCPmx5Yt8BQV8YTXbmecdPvAj5yn/szwDZu+ilAM9CE8w496KYvBb7jebYzgX+6crwCjPHIuCOwyD12F3AncHnIO5uuvEuBXwEvu7LeCfT2HJ/keR4neJ9HUj5XAK3AOrdcf3afz1VJ590P/CJdOYA9gQ+AXwKfuDIc77lPf7d+VgDvAecDMc/v6jng9zi/nctx3r2n3TJ+CtzpuddI4En33DeA73uOHejK+AWwDLjYcyzdbz/VfW8GrgMeAdYA30mVl3vNj9yyfgZckPTOxIDJOO/9Z+77M9A91hunnfgM53f6X2Bjz29jKjDfrZv7E9dF+H33B25yn029W89x91gc57f6Kc7v/HScd6citH0tdgOfy5/3YXge1nOe71u7ldgL2NB9yIfhNKhn4jQKXsXQDJzsVuRpOD9AcY8/jaNMegM74PwIEg3Vxe61E9yXohp4Hvihe3w9YKz7udZ9KQ5wz/2u+32Q5+XfEhDg28BaOhr+C4Hbk34or0e871ycxnIbt/yVafLaH6cx3Qbog6OIvYrhDziKciDQD3gQmOppuFe7MsRc2UYGKIavuef0AgbhNNp/cI+NwPlBbuZp9Ld0P4fV7VBXxn8CfXEVFU4j2s/N5w/AS0mNwuVh75X7bNe59RrH+eG+4B6rwmkcznTr8zAcJROmGELL68l3Pk4nZCCO0v6J53l8DGzrlm06IYohuZ7d73u49Zl4nwfgdBA2S1cOHMXQAlzqHj8A510Z4B7/J04j1s99Bv8HnOj5XbUAP8d576qBGcB5OO9Gb2B399y+rozHu+fuiNOYbeORY5R73XZufUyI8NtPd9+bcd7XcR6ZUuW1NY7C3d2tu6twfv+Jd+Ys4AVgczf/64EZ7rFTcX4rfXDep52A9T3PrN7zjO8Bbov4+57l5tMX2AjnPTrVPfYT4HVgC5z3ag49TDH0w9H4Q9zvVwB/97w4z3vOFfdl8SqGtzzH+7iVt4lboa1AP8/xqcDNnsbjmSTZngEuATZMSj8XuDUp7XHguJAyzgLO9DQsXwJ93O+3AxdGua/70l2apj69ef0dt6H35K3uf3HreUvP8V2Bd93P1wO/j9JgJR2bACzy5PcJTu+tMmLdDnVlHJ6ijDXuOf3d7zeTXjH8y3Nsa6DB/bwHzg9ZPMefTb5fClnay+vJ91jP998Cf/U8jzrPsa+TmWIQnI7BHu73k4HZUcqB00g24GlI3GczFqdxawS29hw7FZjr+V29nyTbP4EbgM2T0n8A/Dsp7XrgopAy/iHxnpH6t5/yvu478M80z8qb14W4Db37vQ+OIk28M6/hdhrd75viKI4KnE7Kf4DtQp6Z9xlv7d43TorfN7Cx+wy8I/ajgTnu59m4HQz3+76kUQzdap5ZVb8EHgaOcpOOwmk8wekZLfOcqzjDYy8feY6vdT+u5177uXv/BO/haPEEy/BzIs6P93UR+a+IHOSmDwGOFJFViT+cnsemACLyPRF5QUQ+d48dgDPaQVXfwnnpDhaRPsAhOD3HtPcNkjFVXsn1lfR5EM6PYaEnr8fcdHAU6dukQUQ2EpE7RKReRL7AGWJ7y3oWTsP8iXveZmnqtpOsIhIXkToRedvNY6l7aEOi85Hn81qgtztXvhlQ775LnfLOpLwp8lrP/Zz8PN7LQP7E+34HToMBMBH/byNdOT5T1ZYA2TakY8ThlS3Vb+McHEU13/UAO8FNHwLskvQOH4PTOUNEdhGROSKyQkRW4/SEE+9Lqt9+yvsGyZgqLzq3JWtxeu8JhgD3efJ6DadjuTHOyPtx4A4R+VBEfisilSFyvIczQtuQ1L/vIe55yz3HrscZOXSSlwjvTrkrBg1ImwEcLSK74gxb57jpy3GGdoBjgPV+T8OHwEAR6edJG4zTywqURVXfVNWjcR7OlcDdIpIY0t6qqjWev76qWicivXCGj1fhzDvW4Mx7SnL5cObwX3UbUFLdN0jGCHn56gunsU/wKU4PchtPXv1VNdGILcOZokrHVFem7VR1feBYb1lVdbqq7o7z4qtbj6nqtlM5cRrA8Tgjj/44owo8+QS9Q1FZDtS671KCLcJOJk15I+TlvffgNOeH/TaOEJEhwC44zz9x70zK4eVTnN7wkCTZUv02PlLVk1V1M5zRxbWu2+0y4Omkd3g9VT3NvXQ6zvTlFqraH8du0um3EfDbT3ffTjKmySu5LakGNvBcuwzHPunNr7eq1qtqs6peoqpbA7sBB+HMZiRIfsbNOHWc6ve9DGfEsKHn2Pqquo1H3kzenbJXDB8Dw5PSHsF5SS/FMWq1uekPA6NEZILb2zsdf48hFFVdhjP8myoivUVkO5xe6+1h14jIsSIyyM1/lZvcitNLPFhE9nN7s71dP/HNcXpevXDsFy0i8j2cYZ+XO9y00+gYLZDmvkGky2smcLyIfMMdnVzoqY824Ebg9yKykVveWhHZzz3lJvfafUQk5h4bGSBDP5y52lUiUotjXE3U3wgR2dtVYOtwFFFrmroNoh/Oj+YznFHOb5KOB71DUXnezfdnIlIhIuNx7CthhJY3AjOBH4vI1u7zuCjN+Z3KpaqLcJ7334DHVTVRd5mWw3vPVle2K0Skn6t0foHzPgYiIkd63suVOI1yK/AQ8HUR+aGIVLp/3xSRb7jn9sMZua8TkZ1xlL6XsN9+uvsGkSqvu3F+a7uJSBXOtKZXQf3VrY8hbnkHuXWKiOwlIqPE8Xz6Aqfh9767x3qe8aXA3W4dh/6+VXU58ATwOxFZ3/3NbSki33bvORM4Q0Q2F5EBOIbxlJS7YpgKnO8On34FoKqNwL04PcT2hlNVPwWOxJm3/Qxn/m4BTqMRhaNxepsfAvfhzE8+meL8/YFXROQr4BrgKFVd5yqZ8cCvcX6ky3AaiJg7HD4D50GuxHkZH/De1H0JnsfpbdzpSQ+9b5Bw6fJS1UeBP+L0ut5y84SO+jrXTX/BnRb5F47BGFWdj2Po+z2OUe9p/D3KBJfgGAJX4yjuez3HegF1OL2lj3BGB792jwXWbVA5ceaz38Ppwb6KYxT0chOwtfsOzQq5RyCq2oRjqD0RR0Edi9MIhb1TqcqbLq9Hcea5Z+PU++w0l1yDMzpYKSJ/9KTPoPNvI9NyJPNznPn9d3BsE9NxbCJhfBOY5z6/B3DsWu+67+S+ONNAH+I89ytx3gWAnwKXisiXOB2Vmd6bpvjtp7tvEKF5qeorbpnvwOmNf4ljc0nU1zVuuZ5wr38BZ4QGTmf0bhyl8BrOb8OrRG/FsXl8hGMEP8PNM93v+0c4nb1XcX7Pd9MxjXwjzvTVYuBFIrx3CQ+FHoc4fvwfAMeo6px05/d03N7V/4BeSXPNhgcRmYdjMP5HsWXJhe5Sjq5ARNbDUahbqeq7OdxnLo4X0t/yJVu2lPuIISPcYViNOz3xa5zhX3IP0nARkUNFpModfl6J4+dvSsGDiHxbRDZxp2COw3FtfKzYcmVKdylHVyEiB4tIH9e2dRWwhA7HhrKnRykGHJfKt3GmJw7G8UtuKK5IJc2pOMPWt3HmQU9LfXqPZATOEH01zgKwI9zpvnKju5SjqxiPMy31IbAVznRmt5l+6bFTSYZhGEYwPW3EYBiGYaSh5ANapWLDDTfUoUOHFlsMwzCMsmLhwoWfquqgsONlrRiGDh3KggULii2GYRhGWSEiKVc/21SSYRiG4cMUg2EYhuHDFINhGIbhwxSDYRiG4cMUg2EYhuGjrL2SDMMwypFZi+qZ9vgbfLiqgc1qqpm03wgmjK5Nf2EXYYrBMAyjC5m1qJ4p9y6hodmJtl2/qoEp9y4BKBnlYIrBMAyjwHhHCDERWpNCETU0tzLt8Tc6KYZijSxMMRiGYRSQ5BFCslJI8OEqfzzPYo4sTDEYhmEUkGmPv9HeuKdis5rqtNc1NLcy5d6X+eXMxbSqEhfh6F224PIJo/IqsykGwzCMApI8Eghjr5H+0EVh1zU0t7V/blXlthfeB8ircjB3VcMwjAKSPBIIY87rK7K6DmDGvGUZyZQOGzEYhlHSlLprZzom7TeCSXctprkt9d439asaGFc3u72cfaqi99vD7BbZYorBMIySpRxcOyMh0U6rd6eP6iNOPyWIS8QMImKKwTCMkiXMABvk2plPoo5Sopw37fE3aG7NX4++D+s4vWIWd7V+m6W6KQBH77JF3u4PphgMwyhhwgywUQ262RB1lBL1vHzJupV8wMNVU6gSJ78YylWtE80ryTCMnsVmNdWB0yqZGGYzJeooJep5YWWIyvjYs1xTda0/cdefcdp3L+O0WGH8h8wryTCMkmXSfiOoroz70qor40zab0TB8ow6Sglr7JPTg8qQjjit1FX9jaW9J/qUwqlNZzNr/Kuw3xVQIKUANmIwDKOLOH/WEmbMW5bRwqxEz7srvZKijlLiAaEtEuleksuQytqwESu5o+oyhsc+ak9bRT/GN15KS/+hTBpvITEMwyhTko2yQzeo5rm3P28/nsnCrAmja7vUA2mvkYPaZUtO9xLmItqqytDJD7d/32qjvmzUr1fK6aRdY68wo+oKX9ojrTszf/RULj5sDE9nUoA8YFNJhmHklYRRtt7tHdevavApBS/5XpiVD+6c31kpBKVH9RB985M1IeVXfha/j6W9J/qUwkXNxzF03XR+2nwWt/73k6hi5xUbMRiGkVeixgaC/C/Myobk0Y0n4oSP5jZ8C9CyFb0vDVxfeTW7x1/xpU9ovJSX9Gu+tGLVjykGwzDySibumflemJUpQS6nqch2ARrA12UZj1RNoUI6NM9LbcP5cdO5rKJf4DXFqh9TDIZh5JVM3DPzuTDru1fP5c1P1rR/32qjvjz5iz07nZdub4R8c2js3/y+6jpf2l9bDuLKlqPQNLP5+V64FhWzMRiGkVfCXEzHbTmwvQccF+HYsYPztjArWSmAM7f/3avn+tKS7R+FUgoVtFBXcQNLe0/0KYWTmn7J0HXTqWuZGKgUClU/mWIjBsMwciLIDfXwnWp9aYfvVBupkcs2YF6yUghLz8T+kQ0b8zl3VV3C4FhHpNRPdX0ObbqEZbpxymtFYJP+vflwVQOb9O/NmCEDCyZnOgqmGETk78BBwCequq2bNhC4ExgKLAW+r6or3WNTgBOBVuAMVX28ULIZhpGeKI30+bOW+Fw7E26oMaDNk3bPwnrACS3tvR90+PfX9KlkdUMziSCk9asamHT3YiB/AfNyWYGcit1i/2N61W98aQ+17sIvm0+jkapI9xD8NoxiBgss5IjhZuDPwD89aZOBp1S1TkQmu9/PFZGtgaOAbYDNgH+JyNdVtXCq3TCMUKLGAQpzN0127GlobuX2F95vX9xVv6qBSXctBqE9wNzKtc2d7tPcqlzy4CslGklVOSN+H7+ovNuXekHzj7m1dd+M75YclbsrggWGUTDFoKrPiMjQpOTxwJ7u51uAucC5bvodqtoIvCsibwE7A88XSj7DKBVKcb+BqHGAMpmjTz4z3f4ECVaubfa5iSaPNNLFTfIuNssH67GWGyqvZrf4q770Qxov42XdMq95FTJYYCq62sawsaouB1DV5SKykZteC7zgOe8DN60TInIKcArA4MGDCyiqYRSeUt1vIGq8oLCwEPnGO8Uy6e7FoB2KpX5VA0JnxZNvRsj7PFo1hZh05LSo7Wv8uOkcVrNeQfIsZLDAVJSK8TnIWTfwOavqDcANAGPGjCn+6hjDyIFi7TeQjjCX05o+lb7e+9jhAwJX9XptDEBeG+6gvQ0K2RAcHnuG31X91Zd2XcvB/LblB2ndTXOhMi4FDRaYiq52V/1YRDYFcP8n1nt/AHgddjcHPuxi2QyjyynGfgNRCHI5rYwLX61r8YW6ePH91YFuqFf/YAdqa6oRoLammmPGDs44wmgxqaCFaRV/ZWnviT6lcKLrbnply9F5VQqVcel8tyJ2e7t6xPAAcBxQ5/6/35M+XUSuxjE+bwXM72LZDKPLyWW/gSA3USDjCKZBBEU1XdPYwqoGv4G4obmVpZ818PbUAzrJ9tHqdSjw0ep1AJ1cWEshHEYym/AZd/e6hM3l0/a0FdqfQ5su4QPdKMWV2SEQWrfNbdr9jM8iMgPH0LyhiHwAXISjEGaKyInA+8CRAKr6iojMBF4FWoDTzSPJ6AlM2m+Ez8YA0fYbCHMT9ZJJBNMoJDdcCZJHN1FdWEuJ3WNLuK1qqi/twdax/Kr5J5HdTTPFu4BtWIiBvNsZn1X16JBD+4ScfwVwRdAxw+iuZLvfQCZRSWfMW5axYsgkhlD/6krf96CQ1dDZhbX4KGdV3MNZFff6Us9vPp7bWr+b050TI6K4CGOHD+D5dz73uaPGBN8CtmLsVJeKUjE+G0aPJZv9BjLpcbeqdnL3TJdfJiuEixwHL2P6sZYbq37H2NhrvvSDGy9niQ7PSx7eqbVxdbM7rVFoU3zTRNmOHAuFKQbDKENi0nlBVCoyXVGbyRRG0MK0UuQb8h6P9priS3ux7WscH9HdNC6wSf/qdgUbdRV1FAeDYuxUlwpTDIZRZLJZ4NarIkZD2MYBaQhzh/UaszNlyymPtE+dlBpHxucyrfIGX9pfWg7hqpbvZ+RZ1Krw3OS9278Pn/JwoHKOJVVB1Gmirt6pLhWmGAyjiGS7wG1dCqXgnd8Oa+TTGYwzJZFPqRiVK2mhrvJGDo//25d+fNMk5rSNDrwm4SEUdSQwcZfBgXU2cRf/wtuoW4WWEqYYDKOIZLvALawBq62p9vVqx9XNDjyvf7V/oVqx103ki035jLt7XUytfNae9rHWcHjTJXygqRtir2ttFC6fMIp3V3zlW+A3bsuBjBky0Fe3axpbAq+f8/qKwPRSwBSDYRSRbBe4RTVWBp1XGRPWNHX4zRcq4mhXskdsMf+sutKXdn/rbkxqPpUmKkOu6kyqEc+4Lf1hsGctqufF91f70uYvXcn8d1f6wnWEUcrK2BSDYWRIVJtAlPPCev69K2O+efuxwwew9LMG372C9jxIvn+QUXNtU0vZGIxTo5xdcTdnVtznS/1184lMbw30is+ajftVceSYwb6RwNqmlk6jvaBwHWEUyxU1CqIlMieYDWPGjNEFCxYUWwyjB5FsEwCnpz71sFG+RjnsvMN3qvXtSbDXyEHcs7Ded15ynKEgKuPiCyQXdv+gSKTlPkLox1r+VnUVu8Re96Uf1Hg5/8uTu2mhCXpnuhIRWaiqY0KPm2IwjOiEzdlHndtPDiYX1JgvX92QkStqqvsHKZCuiERaCLaWpTzS69e+tP+2fZ0Tm37FFwWKbpovBvSppE9VRUm4okJ6xWBTSYaRAVFtAmHnJTfIDc2t3PdiPeua29qNn9kqhaD7d3Uk0kLw/fgcflt5oy/tTy0T+F3LkQQHZi4e8ZgTDC95JHfRwduUjCtqFEwxGEYGRPVJz2TKZk1TxzRSqbh7FhvH3fQGDo8/60v/cdM5zG3boUhSpScG/GDnLTpN55WTUoCuD7ttGGVNUDjqMG+g5PPy2betjJdWTzlfbManPN/rZ7zZ+0ftSmG5DmTcumsYum56SSsFcEYKDy1eXmwxcsZGDIaRAVFDFwSdN3SD6sBNbaJSERNa2zQv9yo1vh1bzC1J7qb3tY7j3OZTMnI3zYXEAre9Rg5ixvxltCbZZWJu/adjVUOzzxW4FHbkyxQzPhuGh0LuvxxmkM6EpXUHAh0hKMob5ZcVd/Hzilm+1MnNJ3FH694h1xSGuIgv8F2UvS6qKiRyWJJk54RiY8Znw4hILvsvR1Eo+VjQNHTywyW7yU1U1mcNN1VN45ux//OlH9j4G17RoUWRaezwAe2fZy2q556F9b4wH3fOXwbiD/3R0uYsFmyOMIoo5cVsQZhiMAyXbMNTRFUo+VpDUK5KYRtZysNJ7qbz2kZyctMv+YK+RZLK4ZUPv2z/HPQeBDX+za3ayQ01bPFgKS9mC8IUg2G4ZBueIqpCCQpP0RM4Kj6busq/+dKuaTmU37ccQam4m65qaM5qNLZqbTOLLty3/XvYwsZi7auQLaGKQUQGhh0DUNXuY/kyDLLfRSuqQgkySJf7KuQwqmhmWuX1jI//x5d+XNO5PN22fZfKUlsTfQ+FTEdjQaGzoXT2VciWVCOGhThrYQQYDKx0P9fg7Nc8rODSGUYXku0uWpkolOSY+0ND9votV2pZwb29LmJjWdWeVq8bcGTjRXzIhl0uT1zEZ/QdfekTWcWJqowJiH/BYNi7UUr7KmRL6DoGVR2mqsOBx4GDVXVDVd0AOAi4N+w6wyhXJoyuZepho6itqUZweppR4tlEXdvQndkztoilvSfyXO8z25XCPa27s9W6fzKu8U9FUQpAuzdRgosO3ibyGhDvezDtyO2ZdsT2Gb8b5Upad1XXrWmnpLQFqVydugpzVzWKQZAHEnSePrhw1hK+aOwYfazfK87Ll+zvu1c5jxiENn5VMZPTKx7wpZ/TfDIzW/fqcnn6VMZobNGULqZH77IFY4YMbH9WYa1fsvtqdyMf7qqfisj5wG04U0vHAp+lvsQwuoZCrjtI4PVpT17olPBAmnrYKN+UxXYXPeZTCgBfNLay3UWPdVIO5cb6fMU/qqaxU+xNX/r3Gqfymg4peP5hQQBHD65pD02+Sf/enTbRaVVt30kt8ayOufH5wIWCXvfVnkiUkBhHA4OA+9y/QW6aYRSVhAdIvdvzSzTSsxbV5y2PxJaXCaOkQqfVrwkPJC/JSiEsvW9VPPC8UmRbeYelvSfycu9T2pXCC23fYNS6vzF03fQuUQoQHgTwubc/970LYSvDZ8xb1v556WfBxuiw9J5C5JXPIrKeqn5VYHkywqaSejZRQ2DnQiYrjKN6v0TZk7mUOCb+L66o/Lsv7Q8th/GHlsMpFXfTTEk8q7DaF+Bdd5V5dyTnqSQR2Q34G7AeMFhEtgdOVdWf5k9Mw8icbNcdZELUhlvo2MYxqktkKSuFKpr5XeV1HBx/wZf+w6bJ/LttuyJJlT/SPaNyW5CWb6LYGH4P7Ac8AKCqi0Vkj4JKZRgRyHbdQSZE7dWXbhOfGZvLCu6rupBB0rGX8Qe6IUc2XsRyNiiiZF1HmEdZV9izSoVIYbdVdVlSUs9aummUJF3hJtpTjJB7x15kae+JPNvrzHalcHfrHmy17p/s3vjHklcKMekciry6Ms64LQcSFyc98T+MVG6oXWHPKiWijBiWudNJKiJVwBnAa7lkKiJnAyfhdLSWAMcDfYA7gaHAUuD7qroyl3yM7k2uq0yj9AC7sxFSaOOcijs5reJBX/qk5lO4q3XP4ggVkZrqSvr2qkjrMpz8PLO1S2UbR6tciaIYfgJcA9QCHwBPAKdnm6GI1OIol61VtUFEZgJHAVsDT6lqnYhMBiYD52abjxGNchseB8mbjaE5LPDdXQve54V3VpaVcThT+vMVN1f9ltGxt3zp+zfW8boOLpJUwYRtlXnQ9psy5/UVvnOjrDjOdnV7V9izSom0ikFVPwWOKUC+1SLSjDNS+BCYAuzpHr8FmIsphoKSS5jpYpBPecN6gMl+792JUfIOD/Y635f2n9atOaX5F3xFn6LIVF0Zo8ldlJaY6PHWetBWmXuNHMQ9C+uzeg+yHWV2hT2rlIjilfR14DpgY1XdVkS2Aw5R1cuzyVBV60XkKpx4Sw3AE6r6hIhsrKrL3XOWi8hGIfKcApwCMHhwafVuyo1yGx7nU97u2tML4sqKG/hBxVxf2tXNR/DH1kMpprtpZUyYeth27c8uaJqnuU2Z8/oK36hwXN3snN6DbGIZZTvSKFeiTCXdCEwCrgdQ1ZdFZDqQlWIQkQHAeJwgfKuAu0Tk2KjXq+oNwA3grGPIRgbDodyGx/mUtztHNgWoZh2v9T6hU/oxTVN4rm1UESQKIEknRX2+Yc+tkM+zu0RNjUoUxdBHVeeL36LfkkOe3wHeVdUVACJyL7Ab8LGIbOqOFjYFPskhDyMCxRoeZ2vXCJM3JsKwyQ9ndK/uujfCNvIuD/c6r1P6Po3TeFtLqxFrblVfLz/q+xhm+0nndZQr3SFqalSiuKt+KiJb4k79icgRwPIc8nwfGCsifcTRNvvgeDk9ABznnnMccH8OeRgRKEZU0Fzc/oLkBccWkOm9giKpljMnxx9iae+JPqWwUtdjxLqbGbpueskphQReRRD1fQyz/XQ3m1AxiTJiOB1n6makiNQD75KDMVpV54nI3cCLOCOPRe791wNmisiJOMrjyGzzMKJRjOFxLnaCZHljAT3HXGwkNdWVrGrIPFZ/sRDamFl1aae9k29q+R6XtfywSFJ1ECX0h7eXH/V9rA0ZWZS7ci8lMomV1DTW6LEAACAASURBVBeIqeqXaU/uIixWUvkxbPLDgauEs4lNk8u9grZgLBf68xW3VNWxQ+wdX/rEpl/zn7ZtiyRVZ5Z6nkGq8OJLM3zuYdtnduf9EfJNPmIlbQBcBOyOs8jtWeBSVbXQ211Aua0zSEc+7Rq53Cto5FLqbCdv80CvC3xp89tGcGrT2axk/SJJFUzyfH8+e/k9zRBcDKJs1PMk8AzOfgzgTCPtqarfKbBsaenuI4bu2DMKK9OOg/v7FpYdvcsWXD4htfdMLvcqpw1yfhh/gssqb/alXdV8JH9unUCpRjfdaqO+rG1qC117AM6zOnynWt8aBWvgu4Z8bNQzUFUv83y/XEQm5C6akY5yW2cQhaDe3tANqkM3VEmlHPJ5r1KjF01cXXktB8bn+9JLbboojLc+WdM+zVe/qoF7FtZ3UgK5LFQzCksUxTBHRI4CZrrfjwDKp7tVxpTbOgOINvWV7Pa35ZRHAu81Y96yjBvz598J35ylHBTDFvIx91ddwEDp2PpkadvG/KDpAj5mYBEly4zkeYiG5ta8L1QzCkcUxXAq8AvgVpxxawxYIyK/AFRVS2tysxtRbsvwsw1Zka37YVB+meZRKnw3toAbq672pd3Rsifnt5xAS6SfaemT3KEpx45PTyFKrKR+XSGI0ZlyW4af7dRXtguWMjUgJ3ZjK/RCqKgIbUypmMEpFf4B+NlNp3Ff27eKJFXh6F9dybi62e2jyZo+laxc29k9uFQ7Pj2JKF5J44CXVHWNG7piR+APqvp+waXr4ZSb90W2PcCjd9mi3Q6QnJ6KTEMglMrOaTV8yT+r6tgu9m57WrPGObDpN/yfpi5zuVIZE9Y0tbSvE6lf1UBlTKiMC82t/sippdrx6UlEGaNeB2zvbul5DnATzrTStwspmOFQTsvws536Ssz9z5i3zOdJNGbIQF8Ps5SVYhR2kLeY1etCX9q/W7flJ81ns4bS6CUn9kIOWjyYCQP6VNKnqmO/hLVNLZ1GB81tGrivQjk/4+5CFMXQoqoqIuOBa1T1JhE5Lu1VRo8jl6mvyyeM8hmHZy2q55d3LabVjcNfv6qBX961GCg/j5Xj4o9zSeUtvrTfNn+fa1vHU6ruprkoherKOBcdvI3vOQ0LcQ9e3dDMSxftm3VeRmGIohi+FJEpwA+Bb4lIHKgsrFhGOZLPqa/z7lvSrhQStLYp5923pCwUQy+auKbyL+wf/68v/eim83i+bZsiSZWebCKUxgQ27V+d8pmXmyNFTyeKYvgBMBE4QVU/EpHBwLTCimWUK/ma+lrTFGxUXtPUWtKL04bIR9xfdQE1sqY97Z22TTiq6QI+oXvuH92mpN1Fr9wcKXo6UbySPhKRe4Ct3KRPgfsKKpVhlBn7xf7L9VW/96VNb9mLC1pOoJXOEWHLCcHp2a9pbAkMMhglrEW5OVL0dKJ4JZ2Ms2PaQGBLnL2f/4oTLtvoIXR1zCah8yKpUkNo47yK2zmp4lFf+plNP+X+tt2LJFV+iYvw9tQDgPAQJFF7/Qve+5yPVq9DgY9Wr2PBe5+bYihRoobd3hmYB6Cqb4Ztu2l0T4qxN/QxYwcHurCWAgP4glur6tg2trQ9rVErOKjpN7ypmxdPsALgNULn0us/f9YS3/Ms11AlPYUoiqFRVZsSO7iJSAWl35kz8khXxGw65sbnfTGOxm05kHFbDvSlFZsd5f+4t9fFvrSnW7fjtOazWEvv4ghVYJKniYJsSFFGkzPmLQu8f7mEKulpRFEMT4vIr4FqEfku8FPgwcKKZZQSmSxcS24khm5Q3SnS6ZghA33n9KmK8eYna3z3KSWFcHz8US6qvNWXdmXzUVzXejCl6m6aD6JME0UdTdqua+VFFMUwGTgRWIITN+kR4G+FFMooLaK6GgY1Et7rEtMH0+e9T8ITNVP3yMoYNLdlWIAs6EUTf6r8E/vGF/rSj2o6nxfati68AEUgittpMt0xArARzSupDbjR/TN6IFFdDaPGLmrLoZPY0tax41ch3FaHynIeqLqA9WVte9rbbZtyVNP5rOim7qYJoridJmOB8LonUbySltDZprAaWABcbju5dX+iGh27ojGo6VOYtZX7xeZzfdUffGm3t+zDhS0/Ljl301R7KKe7Ji5CRVxobOk87BqQRd1GHU3aPs3lRZSppEeBVmC6+/0o9/8XwM3AwfkXy+gq8umGGtZI5JN1za3t8ZNyJUYb51fcxgkVj/nSz2g6nQfaxuV8/0ISF2jNQDckXE4BdrjkiUDFkM10f9TRpC1wKy+iKIZxqur9lSwRkedUdZwbbdUoU6IaDqOeF/Tjj0I8Jp3CX4TR0NyWs/IZyBfcVjWVrWPvddxXqzio6Qre1tKfF890tLDVRn1931cHLFJLlZ6KqKNJW+BWXkRRDOuJyC6qOg9ARHYG1nOPtRRMMqPgRDUcRj1vwuhaFrz3eXuU1DBEYDOPkTNsRW2+CXI3ndO6Pac3n1m27qbeKaJeFcLaAMv8OyvW+OwxMYL9zaPELQobYUZp4MspUnBPJ4piOAn4u4ish+Ob9wVwkoj0BaYWUjijsIT1vJPToxoYZy2q556F9Wl7tButV+UzchY69tGJ8Ue4oPI2X9rU5qO5vvUgyt3d1LvHxNrmMJdQ//cwp669Rg5KmVcxFjoaxSGKV9J/gVEi0h8QVV3lOTwz5DKjDIi6c1rYTlvJhuCoXkkff9nk+y6S3fx2KnrTyJ8q/8R34y/60r/feAHz9Rv5zaybMOf1FSmPm2tqzyHSZrIiciCwDdA7sQJaVS8toFxGFxB10VFYo93oMQTnYnjOp1IYJst5oOp8+kmHLG+21TKx6TxWUJO/jLohQSNA77RR2PM119TuRxR31b8CfYC9cBa2HQHML7BcRhcQ1YUwzCi5trmNte719asaihr47nuxeVxXdY0v7daW73Bxy3El525aqnhtDEHTRmHP1/ZU6H5EGTHspqrbicjLqnqJiPwOuDeXTEWkBkfJbIvzrp0AvAHcCQwFlgLfV9WVueTTk8jG7TSqC2HU0UAmSsE70uhTGQs0mqYjRhsXVNzK8RWP+9J/1vRzHmrb1X+u+BfWlUP01q4k+bkHTRspnevNXE67J7EI56xz/68Vkc2AZmBYjvleAzymqiOB7YHXcEJvPKWqWwFPud+NCCR6d/WrGlA6jIKzFtWnvG7C6FqmHjaK2ppqBGekMPWwUZ0USjqjZKbEXBkTsja3KrEMbMAbsJpHq87lnd7HtiuFNdqLfRqnMXTd9E5KATqvtu4uSsH77KKy1UZ9+cMPdkj53MOmhzQpz6D3xSh/oowYHnR7+NOAF3HejazDY4jI+sAewI8BVLUJaHL3lN7TPe0WYC5wbrb59CQKbRRMZ5TMhKCFWc1tSmUsfaiMneQN7ul1iS/tqdbR/Kz55zSUqbtprni9u7ac8kioM4F3gVuCVO9G2CixtqY647AZRvmRUjGISAynF78KuEdEHgJ6q+rqHPIcDqwA/iEi2wMLgTOBjVV1OYCqLg/b80FETsHZOIjBgwfnIEb3Idt4NVHdD/NpXAxbrRs+k6ScHH+Y8yqn+1KvaJ7Ija0HUu7upvlk7PABgVFpxw7PPMaTrVTu2aScSnID6P3O870xR6UAjjLaEbhOVUcDa8hg2khVb1DVMao6ZtCg/E5xlCthxr90RsFUI41M7lMIqlnHTZXTWNr7GJ9SOLLxQoaum86NAWsQkt1sywWhQ/a4CNWVUWZ4O7P0s2AFHpaeiqjTjEb3JMpU0hMicjhwr2peHAs/AD5IrKQG7sZRDB+LyKbuaGFT4JM85NUjyLZ3F3WB214jB3XZbmrD5UMerDqPvtLYnvZG2+Yc03Qen9K/S2ToahT/QrWGkIVqyYzbcqDve74jndpK5Z5LFMXwC6Av0CoiDbiOCaq6fjYZqupHIrJMREao6hs4e0e/6v4dB9S5/+/P5v49kWzj0ERd4JZPG0MYB8Ze4C9Vf/Sl3dyyL5e2/Ii2SD4SPW/Tl2GD1vN9jxrp1DDSIfkZBGSYqcgOOO6qVcA7wPE401ozgcHA+8CRqppyG68xY8boggULCixt9yVVKIramuqcF66lI0YbF1XcwnEVT/rST286g4fbxhYkz+5E8sY6e40cxD0L6zuNHG0KyEhGRBaq6piw41EWuAlwDDBMVS8TkS2ATVU160VuqvoSECTUPtne08icsAVuQsd0UqqFTQP6VNKnqiJjBbIhq7m96gpGxD5oT/tSqxnfdBnv6GZZlKT4JK+T6Ara1P+c7llYz+E71TLn9RUWwdTIiShTSdfixN3aG7gM+Ar4C/DNAspl5IHzZy1pj3QaF2Hs8AEs/azB18O8c/4ympNatOT2LWxh04HbbeqbZkoX8+ib8jp39fJHUnmydUd+3vxz1tErqzKWCr0rYgzo26u9bpevbuhyRdHQ3Mqc11dEcifN5z4cRvcjimLYRVV3FJFFAKq6UkSqCiyXkSPnz1riMxi3qvpcGetXNXDn/GWhkTaTSSxsCpu2CB8tKKfGH2JK5Qxf6mXNx3BT6wGEuZvGBCbuMtjX+21pbe0UgK9USA4Pkg8SNqBMVmlHMTRblFQjHVEUQ7OIxHHfTREZRHjkXqNEmDFvWdpzkkcKqUhe2DSubnbKSKrVrOPaymvYK77Yl35440Us1M7eUpUx/1qGXYcPZMyQgb4RSWNL+RuXk8tZFReaAhZ3JNd38uivqkJoCFj8EcXQbFFSjXREUQx/BO4DNhKRK3CC6J1fUKmMnMmnh06Q62tYz3RLqeehqvOolo6e/WttW3Bs06/5zHU3rYwLzZ7GMEbnBW7Pvf15pxFOdyC5nKqd6yOovi+fMIrLJ4xq/57c609cN3SD6vYV0HERjt5lC991kH+3VpuW6n5E2Y/hdhFZiGMYFmCCqr5WcMmMnMjFGFpTXUnfXhUpf+jJxuaDY//hT1V/9p3zj5b9uKzlh53cTXce6rd19OSwzc1tGqm+kwlyUR66QbVPmbaqtk8nepVDPt1abVqqexLFK+ka4E5V/UsXyGPkiV4VscCpBi+VMQGhU2/14kO2iRSZdfJdL3Je7GZ+WPEv37HTms7k0bZdQq994Z2Vvtg9hd7BrSvIJVrr6oZmXrpoX19aNr3w/wSEwwBnWtGrGPIZ7sKmpbonUaaSXgTOF5Gv40wp3amqtnigxFmXQikItDc2kMUG7V9+zN5PHcTrVe+0J32hfTik6TKW6qZpZeuOC9GSjfOZTH31r/bvhBelFx50ThjJ9Z3tgsgg8j0tZZQGUaaSbgFuEZGBwOHAlSIy2A2PbZQomUTHjNwgLH0Wbj4QgMSy9ydad+KM5p+VvbtprvStivPR6nUo8NHqdcSI7qGRHOIpSi886jaqEBxDKl/hLmy1dfckk2hdXwNG4myk83pBpDHyxqT9RlBd6d+5LKvpAlX499Vwcf92pQBwafMPGbpuOqc0/7KTUiiHYHbxmDhTaXm615qmVl+8o0zc9lYl7acdpReeyYjk6F22yECazMjbe2aUFFFsDFcChwFv44SsuMwNw22UMDlPFzR+BTN/BG8/5U8/4QkYvAuP182GgMbJuxo6bMIoWXGErcAuJK1tSiy7IKY+4iK0hlj5BYi5axHiIvSujLGmqXMvP7l3HaUXHhbnKjnPIK+kfJLPaSmjdIhiY3gX2FVVPy20MEZ+iTJdkGzkvGS3Cr7z9BHQ2hHdlI1HwY9mQd8N25PCIq6uXtvMyqQecDLJPdggY2gmUzHZksVuop1IZS/pFDU1QClA5x3yguqjMi6saWxh2OSH2aymOjRfhcBNeQqJRWHtfkSxMfxVRAaIyM7QsU2Wqj5TUMmMguM1YB4Se44/rvsLzPacsMtpsN8VEIt3ujYs4mqqtjasBxvU61y5pjGrfaALRcKwHAvpqUchrDTJdZlcHzV9KvlqXQurGhyFmyp+VSZbfBpGGFGmkk7C2WFtc+AlYCzwPE7sJCMipbgI6OrHXuV8vYFjevuni35deQ6/Oe+8lNdm6nUiwCb9ezNmyMDQuvDWR7YurEEuuPkgYbAfVgDX2vpVDYyrmx1aH+PqZncahYXFr7K5fSMfRJlKOhMnYN4LqrqXiIwELklzjeGh5BYBffkR3HwQzzS+2f4GrNK+jG+6jPd0E1gHv0lzi/7Vle092CgoTrkn3b0YtCMcRzZ1EffMoScHBgxywV3T2JKRrKnItNxRSI5mm1wfYUo42UW2FDobRvcgimJYp6rrRAQR6aWqr4uIdUsyoGQWAb37b7jlIF/SY63f5Mzm02mkIy5iFK+ibB2PgnryQXUxoE9loK1iQJ9KFl24b6d0L7MW1fu+H7T9pp32KciWfDtcBU0JJddHJq7HhpEPovhlfCAiNcAs4EkRuR/4sLBidS+KughIFZ65ynE39SqF/esYum46P2k+26cUINoCtFQG5sQ+wZmQXBcXHbwNlXH/XSrjwkUHb5PyPonRWb3rFeXdp8C7f/GxYwdn5KudINm1NBu8coTVtLc+ko3T6dINI1eiGJ8PdT9eLCJzgP7AYwWVqpsR1uOLibR7mWQyDRDJXtH4Fdx5LLwzx59+4r9gC2crjdq5s0N7oulItS1oohc7ri74/kEku2yGuUEm7htW9rDRWdA+BWOGDPTd/8PVDYH7SXhHULnuaBcUpTada2qYob8rtlw1eiZRppIQkd2BrVT1H27Y7VocN1YjAkHuh9DRM081z56sBIL2QfBd+8lr8NdvQZunZ7vJdvDDWdB3g7RyRTVgho0qWlXbG+7+1ZWdIodWxsVnY0jkGRYV1FsfUWw1YaOwdAZe6LyHRQKve22Ym24Uguo2yjOwsBNGV5N2NC0iFwHnAlPcpErgtkIK1d2YMLqWqYeNap9CCJrDT8wrewmaFrn9hfcDe8SLH7nBmS66dmyHUtj1Z3DhSvjJvzsphSC5amuqI+8PnMoOkZB3VUMzqGMXSNx/2hHbM+3I7X157ji4P8+9/bnP5/+2F97n/FlLfPdNZatJkBx3KEiuhEJJtkVcPmEUx44d3F62uAjHjh3sc699aPHyFLXiR4S0dRvlGYSFl7CwE0ahEE0znywiLwGjgRdVdbSb9rKqbtcF8qVkzJgxumBB+cXzGzb54cC5ZQHeresIO5FuKiZOK5dV/J2JFUnTRT+4Hb5xUKfzo7rMRjkvE3fSdEbSxEghmbiIb7FWWL15z6+IC40t0dY/JO9ZHWU6L5Nyj9tyYCePqWycDcL2XoiqxA0jGRFZqKpjwo5HmUpqUlUVkcQObn3zJl0PJWrgsbCpgo1YyR1VlzE89lF72ir6UXPGMzBweOA1UV1mo56XSRiLdFMeqaalvKSb329VpTWDXd5WelZp58OFONmN9sX3V+fFRdnCThhdTRTHjJkicj1QIyInA/8CbiysWIVl1qJ6xtXNZtjkhxlXN7vTlEKhiRp4LFlR7Bp7haW9JzK/9+ntSuGR1p3ZofVW5o6fF6oUINo0TCbnBZUhbHIp3ZRH2LRUcnpQnvkkqJzJDOgTPFXVtyrOJv17ty/ke+XDLyPVY1QmjK7lucl7827dgTw3eW9TCkZBSasYVPUq4G7gHmAEcKGq/qnQghWKoHn7oPnmQhJ1bt9pCGP8LH4fS3tPZEbVFe3Hfl9xEsPWTeeKvlO4+LCd0jYUUQ2YUc8LKsMxYwdnFWlz7PABkdKT84xKZTx6JNV0o5sgN9p4TGhqafO9U2GL4MxgbJQDUUJi9AVmq+qT7sK2ESJSqar5Xf7ZReSy2CyfYS3SBh5r/JIJL5/GhPjT4Glrn/7WDL69zwGcDZydQX5Rp68yia8fVIZkF9ChG1Tzy5mLOevOl0JjJS39LLixDEtPR2IjomxWQweVM/m5D92gD29+sqb9eFygKWIIDjMYG+VAFBvDM8C3RGQAzjTSAuAHwDGFFKxQZOv612VhLT5+Ff66O6hHeW22Ixx7D/QZyLezvG1U19Rct330Kotk98+wPYijPpMgI2wQxyR5EnllS3WvoHJG2SktqlIAW5RmlAdRbAyiqmtx9mT4k7vgbevCilU4snX9izr3njWL73DcTa/btUMp7HaG4256yhzoMzCn20edvsrFhTWZGfOWRUqP+kzS7VqWcC8dM2RgWhtS1HJmslNaFGxRmlEORBkxiIjsijNCODGD69LdNI4z+qhX1YPcrUPvxNkhbinwfVVdmWs+yWTbIy7IIqPWZnjobFh0qz/9qBkwMv8x9aPGzV/w3ue+bSoXvPd5VoohqrdR2DPZa+Qg36K0MI8kr5tvJiO7KPWRb5tAoW0MpRjF1yg/okZXnQLcp6qviMhwYE6aa6JwJvAaHdsHTwaeUtU6EZnsfj83D/n4yNb1L697237xIfx9f1j1Xkdanw3hpH/BwGGZ3y+PRJ3+iULYngHJZuCgZxK0wjvsft5nkO+AhVFDYCTbNTKxYeSLkovia5QtKRWD26s/WFUPSaSp6jvAGblkKiKbAwcCVwC/cJPHA3u6n28B5lIAxQDZ7TiV69w7AO/MhX+O96dtPQEOvR4qewdeEtQDhML5tKea/slUMfSpigduZdmnqrPLafIzGVc3u1MDH2UPgnyP7CbtN4JJdy32hfAIItmuEdWGkTg3H8+zZKL4GmVPSsWgqq0islMB8v0DcA7Qz5O2saoud/NdLiIbBV0oIqcApwAMHjy4AKIFk/UiI1V4+rcwN2mHgwOugp1PTnlpUA8wH/sZpCLq9E8U1oZsZRmW7iXbPQjyOrJLkDTEiYnzWJXMdqULel/y2cu3mEpGvogylbRIRB4A7gLaffRU9d5sMhSRg4BPVHWhiOyZ6fWqegNwAzghMbKRIVsyGmms+wLumAhL/+1PP2k2bB5N1wb1AKPuZ5AtqaKmZkoujXS2exDkZWTnYdrjb3Sq8zaNthdClPcln738gihFo0cSxStpIPAZzlaeB7t/nQPxRGcccIiILAXuAPYWkduAj0VkUwD3/yc55FE8Pn4FLq6Bui06lMJmO8I578LFqyMrBcisp5evXqE3kmiU9FREXeGdz2vz6VUFhe+Fh9kvsgntnUt9G4aXKPsxHJ/PDFV1Cm6kVnfE8CtVPVZEpgHHAXXu//vzmW/BeWk6zDrNnzbuTNjnYohlsyVMZrH/89UrTEyJzJi3rFMI7EzJJcZPrtfma0690L3wfI7QJoyuZcF7n/ue3eE75a8ujJ5DlOiqmwN/wunpK/AscKaqfpBz5h2K4SAR2QCYCQwG3geOVNXPU11f9Oiqrc3w4FnwUlIU8qPvgBHfy/n2QQbMsP0MyinSZjm5VIY9g75VFaxuaM5Z/lTRWpd6Iu1mK2u5vRtG15CP6Kr/AKYDR7rfj3XTvpurcKo6F8f7CFX9DNgn13t2Cavr4R/7wyrPhi19N4KTnoQBQ/OWTapdzMqlYU2m3Fwqk59BTZ9KvlrX4Yqaq/xhUWqj7KKXjHklGfkiimIYpKr/8Hy/WUTOKpRAJc3bs+HWQ/1p2xwGE64LdTfNlaDFZsk7m5UT5dh4eaemxtXN7rTfdS7y59NYbl5JRr6Iohg+FZFjgRnu96NxjNE9A1WYWwdP1/nTD/wdfPOkgmadz8VmpUK5N175lj+fey30r64MXFSXalc7wwgiimI4Afgz8HscG8N/3LTuzbrVMGMivPesP/3kOVC7Y5eIkM/FZlAac/vl7lJZCPnzZSwPs1dnYcc2ejhRvJLeBw5Jd1634aMlTnRTL5t/EybOzDmQXabkc7FZqczt53udQVdTyvInT3GlSzeMMKLsxzAIOBknuF37+aravUYNi26D+0/3p+3+C9j7gqzdTXMln66MpTK3n8qg7g2YV6oG9VLeZjOf74vRs4kylXQ/8G+cvRjyF3+4FGhpggfPgMUz/OkTZ8LX98trVufPWpLx2oCjd9nCZ2PwpmdKKc3tJ0+dlMpoJir5XCcRRjbTfvkcYRo9myiKoY+qFiSYXVH5+/7w/vMd39fbBE58AgYMyXtW2RqR87nYrJTn9ktlNFMqZKso8+n6avRsoiiGh0TkAFV9pODSdBVrPutQCtseAROuhYpeBcsuFyPy5RNG5cUDqavmxrPp6ZbSaKYUyFZRlrL9wygvQhWDiHxJR6TjX4tII9DsfldVXT/s2pKn7wZwwacQ7xo3vlIY4nfF3Hi2Pd1SHs0Ug2wVZSnbP4zyIlQxqGq/sGPdgi5SClA6RsFCz43nu6ebvINbIRRZKTSiyXKErUeIoii7wv5hdH+ieCUFOe2vBt5T1Zb8i9T9yKcRuZTJZ083aAe3fBqkS8XgHSRHZVyojEmneFg2JWR0FVFsDNcCOwJL3O+jgMXABiLyE1V9olDClQNRep35NCKXMrlMCUXZwS2fBulcDN75HGmE7bkxoE8lfaoqij6aMXomURTDUuBEVX0FQES2BiYBlwH3AmWvGLL9oWfS68yXETnf5LORK6e4P9neP+yZL3jvc+a8viLjegzLb9XaZhZduG/a6w2jEERZuTUyoRQAVPVVYLS793PZk/ih169qQOn4oc9aVJ/22lS9znIgl7IHkc9NcsJGGfkySGd7/7BnfvsL72dVj4Uup2FkQxTF8IaIXCci33b/rgX+T0R64XgplTW5NO7l7mZZCMU2YXQtz03em3frDuS5yXvnNPoo5G5k2d4/1V7UXqLW46T9Rjh7bHiojIvZE4yiEkUx/Bh4CzgLOBt4x01rBvYqlGBdRS6Ne7n39kpZseV7i8583T+TZxu5HpO1ii1UNopMFBvD/sCfVfV3Ace+yrM8XU4uBtNyX1BU6usH8ul6GWZLyfT+Qc9cCG7Lo9TjtMff8HkfgbM7X09d9W2UBlFGDIfgTB3dKiIHikgUZVI25DJlUehebaHpKZvH59OWEvTMjxk7OOt6LOVRm9FziRJ2+3gRqQS+B0wErhWRJ1W1sLvUdBG5rhYt5wVFPWWlbL5jMQU98zFDeNaHBAAADy5JREFUBmZVj6U+ajN6JqIRwzK4ymF/4HhgD1XdsJCCRWHMmDG6YMGCYothlDjDJj8cONUjwLt1B3a1OD6S3V/BGW2U08jTKD9EZKGqjgk7nnYqSUT2F5GbcQzQRwB/AzbJm4SGUWBK2Umg3Kcjje5JFHvB8Tj7PZ+qqo0AInIl0P1CcXdzSiU2UD6JUqZSdxIo5+lIo3sSRTFspaqzktK+hymGsqJUYgPlk6hl6im2FMPIF6nCbp8G/BQYLiIvew71A54rtGDdna7uvRdrM5xCljOTMlmv3DCik2rEMB14FJgKTPakf6mqnxdUqm5OMXrvxXCLLHQ5zdXTMApDqPFZVVer6lJVPVpV3/P8mVLIkWLEWCqGAbbQ5Sxlo3KxmLWonnF1sxk2+WHG1c3OOu6V0bOJssAtr4jIFiIyR0ReE5FXRORMN32giDwpIm+6/wd0tWxdRTF6usVYzFbocvaUBXpRyXdQRKPn0uWKAWgBfqmq3wDGAqe7obwnA0+p6lbAU/inr7oVxejpFsMtstDlNFdPP+Ue7dcoHbo8vIWqLgeWu5+/FJHXgFpgPLCne9otwFy6qedTsdwnu9oA2xXlLGWjclc7GJjNxcgXRY17JCJDgdHAPGBjV2mgqstFZKMiilZQeor7ZE8pZxDFcDCw8BpGvogcEiPvGYusBzwNXKGq94rIKlWt8Rxfqaqd7AwicgpwCsDgwYN3eu+997pMZsOIyri62YGNdG1NNc9N3rsgeVp4DSMqOYfEKARu3KV7gNtV9V43+WMR2dQ9vinwSdC1qnqDqo5R1TGDBg3qGoENI0OClEKq9HxgNhcjX3T5VJKICHAT8JqqXu059ABwHFDn/r+/q2UzjHwRF6E1YDQeFwk4O3+Uss3FKB+KYWMYB/wQWCIiL7lpv8ZRCDNF5ETgfeDIIshmGHkhSCmkSjeMUqIYXknP4kQ8DmKfrpTFMApFbYghuNYMwUYZUBQbg2F0d2zxnVHOdKttOg2jVOjJrrpG+WOKwTAKhBmCjXLFppIMwzAMH6YYDMMwDB+mGAzDMAwfphgMwzAMH6YYDMMwDB+mGAzDMAwfphgMwzAMH6YYDMMwDB+mGAzDMAwfphgMwzAMH6YYDMMwDB+mGAzDMAwfphgMwzAMH6YYDMMwDB+mGAzDMAwfphgMwzAMH6YYDMMwDB+mGAzDMAwfphgMwzAMH6YYDMMwDB+mGAzDMAwfphgMwzAMHxXFFsAwjMIya1E90x5/gw9XNbBZTTWT9hvBhNG1xRbLKGFMMRhGN2bWonqm3LuEhuZWAOpXNTDl3iUAphyMUEpuKklE9heRN0TkLRGZXGx5DKPQzFpUz7i62Qyb/DDj6mYza1F93u497fE32pVCgobmVqY9/kbe8jC6HyU1YhCROPAX4LvAB8B/ReQBVX21uJIZRmEodI/+w1UNGaUbBpTeiGFn4C1VfUdVm4A7gPFFlskwCkahe/Sb1VRnlG4YUHqKoRZY5vn+gZvWjoicIiILRGTBihUrulQ4w8g3he7RT9pvBNWVcV9adWWcSfuNyMv9je5JqSkGCUhT3xfVG1R1jKqOGTRoUBeJZRiFodA9+gmja5l62Chqa6oRoLammqmHjTLDs5GSkrIx4IwQtvB83xz4sEiyGEbBmbTfCJ+NAfLfo58wutYUgZERpaYY/gtsJSLDgHrgKGBicUUyjMKRaLBtnYFRSpSUYlDVFhH5GfA4EAf+rqqvFFkswygo1qM3So2SUgwAqvoI8Eix5TAMw+iplJrx2TAMwygyphgMwzAMH6YYDMMwDB+mGAzDMAwfoqrpzypRRGQFsAb4tNiy5MCGlLf8UP5lMPmLT7mXodzkH6KqoSuEy1oxAIjIAlUdU2w5sqXc5YfyL4PJX3zKvQzlLn8yNpVkGIZh+DDFYBiGYfjoDorhhmILkCPlLj+UfxlM/uJT7mUod/l9lL2NwTAMw8gv3WHEYBiGYeQRUwyGYRiGj7JSDCKyVESWiMhLIrLATRsoIk+KyJvu/wHFljMVIlIjIneLyOsi8pqI7FouZRCREW7dJ/6+EJGzykV+ABE5W0ReEZH/icgMEeldTvIDiMiZrvyviMhZblrJlkFE/i4in4jI/zxpofKKyBQReUtE3hCR/YojdQch8h/p1n+biIxJOr+k5M+GslIMLnup6g4en+HJwFOquhXwlPu9lLkGeExVRwLbA69RJmVQ1Tfcut8B2AlYC9xHmcgvIrXAGcAYVd0WJ7T7UZSJ/AAisi1wMs7+6NsDB4nIVpR2GW4G9k9KC5RXRLbGeSbbuNdcKyJxisvNdJb/f8BhwDPexBKVP2PKUTEkMx64xf18CzChiLKkRETWB/YAbgJQ1SZVXUUZlcHDPsDbqvoe5SV/BVAtIhVAH5wdAstJ/m8AL6jqWlVtAZ4GDqWEy6CqzwCfJyWHyTseuENVG1X1XeAtHCVYNILkV9XXVPWNgNNLTv5sKDfFoMATIrJQRE5x0zZW1eUA7v+NiiZdeoYDK4B/iMgiEfmbiPSlvMqQ4Chghvu5LORX1XrgKuB9YDmwWlWfoEzkd/kfsIeIbCAifYADcLbDLacyQLi8tcAyz3kfuGnlQrnLD5SfYhinqjsC3wNOF5E9ii1QhlQAOwLXqeponDhPpTTkj4SIVAGHAHcVW5ZMcOexxwPDgM2AviJybHGlygxVfQ24EngSeAxYDLQUVaj8IgFp5eRTX+7yA2WmGFT1Q/f/Jzhz2zsDH4vIpgDu/0+KJ2FaPgA+UNV57ve7cRRFOZUBHMX8oqp+7H4vF/m/A7yrqitUtRm4F9iN8pEfAFW9SVV3VNU9cKY43qTMykC4vB/gjIASbI4z3VculLv8QBkpBhHpKyL9Ep+BfXGG1Q8Ax7mnHQfcXxwJ06OqHwHLRGSEm7QP8CplVAaXo+mYRoLykf99YKyI9BERwan/1ygf+QEQkY3c/4NxDKAzKLMyEC7vA8BRItJLRIYBWwHziyBftpS7/A6qWhZ/OPPzi92/V4Dz3PQNcLwa3nT/Dyy2rGnKsQOwAHgZmAUMKKcy4BhsPwP6e9LKSf5LgNdxOhW3Ar3KSX63DP/G6VAsBvYp9WeAo7iWA804PeoTU8kLnAe8DbwBfK9E5T/U/dwIfAw8XqryZ/NnITEMwzAMH2UzlWQYhmF0DaYYDMMwDB+mGAzDMAwfphgMwzAMH6YYDMMwDB+mGIyccSPG/jSH67/KpzzdFRG5WUSOKEK+v076/p+ulsHoWkwxGPmgBshaMeSCGwyv6JRjBM0EEWT3KQZV3a2A4hglgCkGIx/UAVu6ezTcJSIHJA64vdzD3dXGM0XkZRG5U0TmeePYi8gVIrJYRF4QkY3dtCEi8pR7zVPuSt/EPa8WkTnAlSLybenYI2KRZ4X8JBH5r3v9JZ68ZrmBGF9JBGMUkdNE5Leec34sIn9yPx8rIvPd+1+faEhF5CsRuVRE5gG7isiFbn7/E5Eb3NXViMg3XRmeF5Fpibj+IhJ3vydkPNWT/zni7D2yWETqkis8RV5niMir7v3ucNM61Y+I7Ckic0RkOrAkRb3U4USjfUlEbk+U2/2/p4jMlY79RW73yHGAm/asiPxRRB7K4r0yikWxV9jZX/n/AUOB/7mfDwVucT9X4USarAZ+BVzvpm+LE/htjPtdgYPdz78Fznc/Pwgc534+AZjlfr4ZeAiIe84b535eDydY4b44G7QLTgfoIWAP95yB7v9qnBXQGwCDgLc8ZXoU2B0nzPWDQKWbfi3wI4/c3/dc4129e6unTP8DdnM/13nq6hRPWXvhrIgfhhOL6j9AnyR5bwaOSJPXh0Av93NNivrZEyeI47Bk+b314n7/Kul5f+X+3xNYjRMPKAY879ZZb/e5D3PPmwE8VOz31P6i/9mIwcg3jwJ7i0gvnAbuGVVtwGkw7gBQ1f/hhARJ0ITTcAMsxFE0ALsC093Pt7r3SHCXqra6n58DrhaRM3AawxYcxbAvsAh4ERiJE7cG4AwRWQy8gBPwbCtVXQG8IyJjRWQDYIR7331wNiX6r4i85H4f7t6nFbjHI9Ne7khoCbA3sI2I1AD9VDUxLz/dc/6+wI/c+87DUVBb4QT7+4eqrnXrK3kvg8C83PSXgdvFiRqbiLoaVD8A89XZMyBBp3oJyDeZ+ar6gaq2AS/hPLuRwDuee88Iu9goTUpiftboPqjqOhGZC+wH/ICORiEoHHGCZnW7ljiNbdh76Y3fssaTZ52IPIyzN8ELIvIdN7+pqnq99wYisidOw7urqq51Ze3tHr4T+D5OLKX7VFXdqZFbVHVKgDzrEspJRHrjjCbGqOoyEbnYvW+qcgvwc1V9PEnG/UkRqjlFXgAH4mwGdQhwgYhsE1I/4KnDNPWSikbP58SzS1VmowywEYORD74E+nm+3wEcD3wLSDR6z+I0uontD0dFuO9/cDYEAjjGvUcnRGRLVV2iqlfiTMeMdPM9QUTWc8+pFScqaX9gpdv4jQTGem51L85OYkfjKAlwArwdIR0RTQeKyJAAMRKN6KdunkcAqOpK4EsRSeRzlOeax4HTRKTSvffXxYkc/IQre59EnlHyEpEYsIXq/7d3By1RRlEYx/+P0UaE1u0iQciVX6F1m3YtCkoiMARzYxS48wO4KggjKPoELdSdbUKoUJjFYLhx1ia2KERbnBbnDrzvxIxGNGP6/HYzc4e598Jw7j33cN9YAx6TRQEjXeanU695+dnu4wltAVclXSmvb/3Bd+0U8I7B/lpE7En6UA5VV8gqljfAu4g4Ks2eA68lNcj0ToPMT/cyA7ySNEc++W6yS7tZSdfJFWsTWImIQ0nXgPVyHvoduEM+3Gaq9OMLmTZpj2NfUhMYj4iP5b2mpHnyyYFD5A2b00CrYw6+SVoiD3J3gE+Vj+8DS5J+AO8r435Jpl42ys5kF7gZEauSJoDPko6AZSqVQT1+6wLwVtIlctW+WNoudM4Pmaar6jov5FlNQ9JGRNz+ffrrIuJAWb68Kukr/+O10+ecb1e1vlBW8lwsqaZRciU+VgkcZ5akkYhoV/I8AS5HxKMBd+ufao+5BLxnwHZELA66X3Yy3jFYvwwDayUlIeDheQgKxQ1JT8n/Wwu4N9ju9MUDSXfJyrRN4MUx7e0U8Y7BzMxqfPhsZmY1DgxmZlbjwGBmZjUODGZmVuPAYGZmNb8AKan8IKdId/AAAAAASUVORK5CYII=
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="This-all-looks-good-for-the-machine-learning-model">This all looks good for the machine learning model<a class="anchor-link" href="#This-all-looks-good-for-the-machine-learning-model">&#182;</a></h3><p>We decided that the features to be:</p>
<ul>
<li>Weight</li>
<li>Age</li>
<li>Days Off</li>
<li>Number of Wins</li>
<li>Power Rating</li>
<li>Average Class Rating</li>
</ul>
<p>We wanted to know the Buyer speed so we have that as the target.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">features</span> <span class="o">=</span> <span class="p">[</span>
    <span class="s1">&#39;tvghorseweight&#39;</span><span class="p">,</span> 
    <span class="s1">&#39;tvghorseage&#39;</span><span class="p">,</span> 
    <span class="s1">&#39;tvghorsedaysoff&#39;</span><span class="p">,</span> 
    <span class="s1">&#39;tvghorsenumberofwins&#39;</span><span class="p">,</span> 
    <span class="s1">&#39;tvghorsepowerrating&#39;</span><span class="p">,</span> 
    <span class="s1">&#39;tvghorseaverageclassrating&#39;</span>
<span class="p">]</span>

<span class="n">target</span> <span class="o">=</span> <span class="s1">&#39;tvghorseaveragespeed&#39;</span>

<span class="n">X</span> <span class="o">=</span> <span class="n">df_copy</span><span class="p">[</span><span class="n">features</span><span class="p">]</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">df_copy</span><span class="p">[</span><span class="n">target</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>
<span class="n">X_train</span><span class="p">,</span> <span class="n">X_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.33</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># scaling the data</span>

<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">StandardScaler</span>
<span class="n">X_scaler</span> <span class="o">=</span> <span class="n">StandardScaler</span><span class="p">()</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">)</span>
<span class="n">y_scaler</span> <span class="o">=</span> <span class="n">StandardScaler</span><span class="p">()</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">y_train</span><span class="p">)</span>
<span class="n">X_train_scaled</span> <span class="o">=</span> <span class="n">X_scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">X_train</span><span class="p">)</span>
<span class="n">X_test_scaled</span> <span class="o">=</span> <span class="n">X_scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>
<span class="n">y_train_scaled</span> <span class="o">=</span> <span class="n">y_scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">y_train</span><span class="p">)</span>
<span class="n">y_test_scaled</span> <span class="o">=</span> <span class="n">y_scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">y_test</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LinearRegression</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">LinearRegression</span><span class="p">()</span>
<span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train_scaled</span><span class="p">,</span> <span class="n">y_train_scaled</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[30]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>LinearRegression()</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">predictions</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">)</span>
<span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train_scaled</span><span class="p">,</span> <span class="n">y_train_scaled</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_train_scaled</span><span class="p">),</span> <span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_train_scaled</span><span class="p">)</span> <span class="o">-</span> <span class="n">y_train_scaled</span><span class="p">,</span> <span class="n">c</span><span class="o">=</span><span class="s2">&quot;blue&quot;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;Training Data&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">),</span> <span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">)</span> <span class="o">-</span> <span class="n">y_test_scaled</span><span class="p">,</span> <span class="n">c</span><span class="o">=</span><span class="s2">&quot;orange&quot;</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">&quot;Testing Data&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">hlines</span><span class="p">(</span><span class="n">y</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">xmin</span><span class="o">=</span><span class="n">y_test_scaled</span><span class="o">.</span><span class="n">min</span><span class="p">(),</span> <span class="n">xmax</span><span class="o">=</span><span class="n">y_test_scaled</span><span class="o">.</span><span class="n">max</span><span class="p">())</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;Residual Plot&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Measuring the Linear Model</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="kn">import</span> <span class="n">mean_squared_error</span>

<span class="n">MSE_linear_regression</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">y_test_scaled</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
<span class="n">r2_linear_regression</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">,</span> <span class="n">y_test_scaled</span><span class="p">)</span>
<span class="c1">### END SOLUTION</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;MSE: </span><span class="si">{</span><span class="n">MSE_linear_regression</span><span class="si">}</span><span class="s2">, R2: </span><span class="si">{</span><span class="n">r2_linear_regression</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>MSE: 0.16302412817702236, R2: 0.8393376790850877
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Fitting, predicting and scoreing the Lasso Linear Model</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[33]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">Lasso</span>

<span class="c1">### BEGIN SOLUTION</span>
<span class="n">lasso</span> <span class="o">=</span> <span class="n">Lasso</span><span class="p">(</span><span class="n">alpha</span><span class="o">=.</span><span class="mi">01</span><span class="p">)</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train_scaled</span><span class="p">,</span> <span class="n">y_train_scaled</span><span class="p">)</span>

<span class="n">predictions</span> <span class="o">=</span> <span class="n">lasso</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">)</span>

<span class="n">MSE_lasso</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">y_test_scaled</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
<span class="n">r2_lasso</span> <span class="o">=</span> <span class="n">lasso</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">,</span> <span class="n">y_test_scaled</span><span class="p">)</span>
<span class="c1">### END SOLUTION</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;MSE: </span><span class="si">{</span><span class="n">MSE_lasso</span><span class="si">}</span><span class="s2">, R2: </span><span class="si">{</span><span class="n">r2_lasso</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>MSE: 0.164375594141657, R2: 0.8380057924438664
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Fitting, predicting and scoreing the Ridge Linear Model</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[34]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">Ridge</span>

<span class="c1">### BEGIN SOLUTION</span>
<span class="n">ridge</span> <span class="o">=</span> <span class="n">Ridge</span><span class="p">(</span><span class="n">alpha</span><span class="o">=.</span><span class="mi">01</span><span class="p">)</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train_scaled</span><span class="p">,</span> <span class="n">y_train_scaled</span><span class="p">)</span>

<span class="n">predictions</span> <span class="o">=</span> <span class="n">ridge</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">)</span>

<span class="n">MSE_ridge</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">y_test_scaled</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
<span class="n">r2_ridge</span> <span class="o">=</span> <span class="n">ridge</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">,</span> <span class="n">y_test_scaled</span><span class="p">)</span>
<span class="c1">### END SOLUTION</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;MSE: </span><span class="si">{</span><span class="n">MSE_ridge</span><span class="si">}</span><span class="s2">, R2: </span><span class="si">{</span><span class="n">r2_ridge</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>MSE: 0.16302432612175946, R2: 0.8393374840080692
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Fitting, predicting and scoreing the ElasticNet Model</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[35]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">ElasticNet</span>

<span class="c1">### BEGIN SOLUTION</span>
<span class="n">elasticnet</span> <span class="o">=</span> <span class="n">ElasticNet</span><span class="p">(</span><span class="n">alpha</span><span class="o">=.</span><span class="mi">01</span><span class="p">)</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train_scaled</span><span class="p">,</span> <span class="n">y_train_scaled</span><span class="p">)</span>

<span class="n">predictions</span> <span class="o">=</span> <span class="n">elasticnet</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">)</span>

<span class="n">MSE_elastic</span> <span class="o">=</span> <span class="n">mean_squared_error</span><span class="p">(</span><span class="n">y_test_scaled</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
<span class="n">r2_elastic</span> <span class="o">=</span> <span class="n">elasticnet</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">X_test_scaled</span><span class="p">,</span> <span class="n">y_test_scaled</span><span class="p">)</span>
<span class="c1">### END SOLUTION</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;MSE: </span><span class="si">{</span><span class="n">MSE_elastic</span><span class="si">}</span><span class="s2">, R2: </span><span class="si">{</span><span class="n">r2_elastic</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>MSE: 0.16379617411249137, R2: 0.8385768181424015
</pre>
</div>
</div>

</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>
'''
