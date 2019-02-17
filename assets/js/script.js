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
    $.ajaxSetup({
	    type: "POST",
	    data: {},
	    dataType: 'json',
	    xhrFields: {
	       withCredentials: true
	    },
	    crossDomain: true,
	    contentType: 'application/json; charset=utf-8'
	});

    var query_param = getUrlVars()["serialNumber"];
    // var query_param = "hello"
	
	$.ajax({
    	//type:'get',
    	type:'post',
	  	url: "http://localhost:5000/queryresult",
	  	data: JSON.stringify({oi: query_param}),
	  	// data: JSON.stringify({oi: "herro2"}),
		success: function(response) {
	    // here you do whatever you want with the response variable
	    	console.log(response);
	    	console.dir(response);
	    	console.log(response["success"]);		// update status

	    	$("#responseTextArea").html(response);
		},
		error: function(request, status, error) {
			console.log("error ** + " + error);
		}
	});
});
