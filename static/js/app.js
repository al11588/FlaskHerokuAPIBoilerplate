$(function (){
	var $boilerplatecode = $('#boilerplatecode');
	$.ajax({
		type:'GET',
		url: 'http://127.0.0.1:5000/0/', // Change url for Heroku: https://example.herokuapp.com/0/
		success: function(boilerplatecode) {
			$.each(boilerplatecode, function(i, code){
				$boilerplatecode.text( boilerplatecode.text);
			});
		}
	});
});
