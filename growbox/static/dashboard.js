function getMetricsNow() {
    $.getJSON("/dashboard/now/", function (metric) {
        console.log(metric);
        $("#temperature_air").text(metric.temperature_air)
        $("#temperature_ground").text(metric.temperature_ground)
        $("#humidity_air").text(metric.humidity_air)
        $("#humidity_ground").text(metric.humidity_ground)

        $("#flex_switch_light").prop("checked", metric.light)
        $("#flex_switch_pump").prop("checked", metric.pump)
        $("#flex_switch_heating").prop("checked", metric.heating)
        $("#flex_switch_fan").prop("checked", metric.fan)
    });
}

$(document).ready(function () {
    getMetricsNow();
    setInterval(function () {
        getMetricsNow();
    }, 5000);
});
