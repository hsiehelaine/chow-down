var keylist = [];

function getUrlVars() {
	var vars = {};
	var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
	vars[key] = value;
	});
	return vars;
}


function toggle_display(div) {
	var i;
	for (i = 0; i < keylist.length; i++) {
		var x = document.getElementById(keylist[i]);
		if (keylist[i] == div) {
			x.style.display = "block";
		} else {
			x.style.display = "none";
		}
		
	}
} 

function convertNull(value) {
    return (value == null) ? "Not Available" : value
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
    var query_param2 = getUrlVars()["selection"];
    $.ajax({
    	type:'post',
	  	url: "http://localhost:5000/queryresult",
	  	data: JSON.stringify({srl: query_param, srt: query_param2}),
	  	contentType: 'application/json',
		success: function(response) {
	    	var json_obj = $.parseJSON(response);

	    	var left="<ol>";
	    	var right="";
	    	keylist = [];
	    	
          for (var key in json_obj) 
          {
             	keylist.push(key);
             	var entry = JSON.parse(json_obj[key]);

             	left += "<li onclick='toggle_display(&quot;" + key + "&quot;)' class='pointer'>" + key + "</li>";
                right += "<div id='" + key + "' hidden>";
                right += "<div id='right-text'>" + key + "</div> </br>";
                right += "<div> Rating: " + convertNull(entry[0]) + "</div>";
                right += "<div> Calories: " + convertNull(entry[1]) + "</div>";
                right += "<div> Protein: " + convertNull(entry[2]) + "</div>";
                right += "<div> Fat: " + convertNull(entry[3]) + "</div>";
                right += "<div> Sodium: " + convertNull(entry[4]) + "</div>";
            	right += "</div>";
          }
   	  left+="</ol>";

	  $("#responseTextAreaLeft").html(left);
	  $("#responseTextAreaRight").html(right);

	  },
	  error: function(request, status, error) {
		console.log("error ** + " + error);
	  }

	
	});
});

