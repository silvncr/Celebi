var location = window.location.href;
if (a === undefined) {
	window.location.href = location + "?a";
} else if (a === null) {

} else {
	document.getElementById("page") = '<html lang="en" dir="ltr"><head><meta charset="utf-8" http-equiv="refresh" content="0; url=turnipguy30.html"><link rel="icon" href="images/celebi.png"><title>'+a+' | Celebi</title><style>@import url("/styles/index.css");</style></head><body><h1>'+a+'</h1><img src="https://gpvc.arturio.dev/'+a+'"></body></html>';
};
submit.onClick = function() {
	window.location.href = location + "=" + document.getElementById("input").content;
};
