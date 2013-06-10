

// function timedRedirect() {
// 	setInterval(function(){
// 		window.location.href = "/main";
// 		//alert("Hello");
// 	}, 2000);
// }
$('btn').click(function(){
	var redirect = "/main";
	setTimeout(function(){
		window.location.href = redirect;
		//alert("Hello");
	}, 2000);
})