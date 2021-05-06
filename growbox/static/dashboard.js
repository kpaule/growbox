$(document).ready(function() {
    console.log( "ready!" );
    
    $.getJSON("/dashboard/now/", function(metric) {
        console.log( metric );
        $("#temperature_air").text(metric.temperature_air)
        $("#temperature_ground").text(metric.temperature_ground)
        $("#humidity_air").text(metric.humidity_air)
        $("#humidity_ground").text(metric.humidity_ground)
    });
});