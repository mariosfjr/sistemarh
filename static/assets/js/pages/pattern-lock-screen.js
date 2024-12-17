
    function updateClock ( )
 	{
 	var currentTime = new Date ( );
  	var currentHours = currentTime.getHours ( );
  	var currentMinutes = currentTime.getMinutes ( );

  	currentMinutes = ( currentMinutes < 10 ? "0" : "" ) + currentMinutes;
  	var timeOfDay = ( currentHours < 12 ) ? "AM" : "PM";
  	currentHours = ( currentHours > 12 ) ? currentHours - 12 : currentHours;
  	currentHours = ( currentHours == 0 ) ? 12 : currentHours;
  	var currentTimeString = currentHours + ":" + currentMinutes + " " + timeOfDay;
  	  	
   	$("#time").html(currentTimeString);
   	  	
 }

$(document).ready(function(){
    var lock = new PatternLock("#patternContainer");
    lock.checkForPattern("321478965", function() {
        window.location.href = "index.html";
    });
    setInterval('updateClock()', 1000);
    
    var objToday = new Date(),
                weekday = new Array('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'),
                dayOfWeek = weekday[objToday.getDay()],
                dayOfMonth = objToday.getDate(),
                months = new Array('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'),
                curMonth = months[objToday.getMonth()],
                curYear = objToday.getFullYear();
var today = dayOfWeek + "<br>" + curMonth + " " + dayOfMonth + ", " + curYear;

  
   	$("#date").html(today);
});