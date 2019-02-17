function getUrlVars() {
	var vars = {};
	var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
	vars[key] = value;
	});
	return vars;
}

function process() {
	var first = getUrlVars()["serialNumber"]
	// processing here
	$("#responseTextArea").html(first);
}

$(document).ready(function() {
    process();
});
