

function send_req( data, handler ){
	var myRequest = new Request({
		method: "GET",
		url: "ajax.html?" + data,
		onSuccess: function (responseText, responseXML){

			j_data = JSON.parse( responseText )
			if ( j_data["STATUS"] == "ERROR" )
				alert( j_data["VALUE"] )

			if ( handler ){
				handler()
			}
		}
	});
	myRequest.send();

}

function init (){

	send_req( "action=init", function() {
		location.reload()
	 })
}

function store_operator (){

	send_req( "action=set_operator&operator=" + parseInt(document.getElementById("operator").value) )
}

function store_operand (){

	send_req( "action=set_operand&operand=" + parseInt(document.getElementById("operand").value) )
}


function calc_value	(){

	var myRequest = new Request({
		method: "GET",
		url: "ajax.html?action=calc" ,
		onSuccess: function (responseText, responseXML){

			j_data = JSON.parse( responseText )
			if ( j_data["STATUS"] == "ERROR" )
				alert( j_data["VALUE"] )
			else
				document.getElementById("erg").value = j_data["ERG"];
		}
	});
	myRequest.send();

}


function store_value() {

	send_req( "action=store", function() {
		location.reload()
	 } )

}


































