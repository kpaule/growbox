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

    $('#flex_switch_light').change(function () {
        let status = this.checked ? 1 : 0;
        $.post(`/dashboard/led/${status}/`, function (data, status) {
            console.log("Data: " + data + "\nStatus: " + status);
        });
    });

    $('#flex_switch_pump').change(function () {
        let status = this.checked ? 1 : 0;
        $.post(`/dashboard/pump/${status}/`, function (data, status) {
            console.log("Data: " + data + "\nStatus: " + status);
        });
    });

    $('#flex_switch_heating').change(function () {
        let status = this.checked ? 1 : 0;
        $.post(`/dashboard/heating/${status}/`, function (data, status) {
            console.log("Data: " + data + "\nStatus: " + status);
        });
    });

    $('#flex_switch_fan').change(function () {
        let status = this.checked ? 1 : 0;
        $.post(`/dashboard/fan/${status}/`, function (data, status) {
            console.log("Data: " + data + "\nStatus: " + status);
        });
    });
});
