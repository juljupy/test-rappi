$(document).ready(function(){
    $('.calendar').fullCalendar({
    	events: {
	        url: '/horarios',
	        type: 'GET',
	        error: function() {
	            alert('there was an error while fetching events!');
	        }
	    }
    });
});