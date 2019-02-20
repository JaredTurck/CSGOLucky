(function() {
	document.getElementById("steamAccountName").value = {usrnme};
	document.getElementById("steamPassword").value = {passwd};
	document.getElementById("SteamLogin").click();

	var error_text_1 = "The account name or password that you have entered is incorrect."
	if (document.getElementById("error_display").innerText.indexOf(error_text_1) >= 0) {
		return true;
	}
	
	var error_text_2 = "There was a problem communicating with the Steam servers"
	if (document.getElementsByClassName("newmodal_content_border")[0] !== undefined) {
		if (document.getElementsByClassName("newmodal_content_border")[0].innerText.indexOf(error_text_2) >= 0) {
			return true;
		}
	}
	
		
	return false;
	
})();