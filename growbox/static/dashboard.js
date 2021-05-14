function getMetricsNow() {
    $.getJSON("/dashboard/now/", function (metric) {
        console.log(metric);
        $("#temperature_air").text(metric.temperature_air.toFixed(3))
        $("#temperature_ground").text(metric.temperature_ground.toFixed(3))
        $("#humidity_air").text(metric.humidity_air.toFixed(3))
        $("#humidity_ground").text(metric.humidity_ground.toFixed(3))

        $("#flex_switch_light").prop("checked", metric.light)
        $("#flex_switch_pump").prop("checked", metric.pump)
        $("#flex_switch_heating").prop("checked", metric.heating)
        $("#flex_switch_fan").prop("checked", metric.fan)
    });
}

function initAvgDay() {
    $.getJSON("/dashboard/day/", function (metrics) {
        console.log(metrics);
        var humidity_air = [];
        var humidity_ground = [];
        var temperature_air = [];
        var temperature_ground = [];
        var date = [];

        for (var key in metrics) {
            metric = metrics[key]
            humidity_air.push(metric.humidity_air)
            humidity_ground.push(metric.humidity_ground)
            temperature_air.push(metric.temperature_air)
            temperature_ground.push(metric.temperature_ground)
            date.push(metric.date_start)
        }
        humidity_air.reverse()
        humidity_ground.reverse()
        temperature_air.reverse()
        temperature_ground.reverse()
        date.reverse()

        var ctx = $('#humidityChart');
        graph = new Chart(ctx, {
            type: 'line',
            data: {
                labels: date,
                datasets: [{
                    label: 'Air Humidity',
                    data: humidity_air,
                    borderWidth: 1,
                    backgroundColor: 'rgb(0, 0, 255)',
                    borderColor: 'rgb(0, 0, 255)'
                }, {
                    label: 'Soil Humidity ',
                    data: humidity_ground,
                    borderWidth: 1,
                    backgroundColor: 'rgb(0, 191, 255)',
                    borderColor: 'rgb(0, 191, 255)'
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
        ctx.data('graph', graph);

        var ctx = $('#temperatureChart');
        graph = new Chart(ctx, {
            type: 'line',
            data: {
                labels: date,
                datasets: [{
                    label: 'Air Temperature',
                    data: temperature_air,
                    borderWidth: 1,
                    backgroundColor: 'rgb(255, 0, 0)',
                    borderColor: 'rgb(255, 0, 0)'
                }, {
                    label: 'Soil Temperature',
                    data: temperature_ground,
                    borderWidth: 1,
                    backgroundColor: 'rgb(255, 140, 0)',
                    borderColor: 'rgb(255, 140, 0)'
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
        ctx.data('graph', graph);
    });
}

function updateAvgDay() {
    $.getJSON("/dashboard/day/", function (metrics) {
        console.log(metrics);
        var humidity_air = [];
        var humidity_ground = [];
        var temperature_air = [];
        var temperature_ground = [];
        var date = [];

        for (var key in metrics) {
            metric = metrics[key]
            humidity_air.push(metric.humidity_air)
            humidity_ground.push(metric.humidity_ground)
            temperature_air.push(metric.temperature_air)
            temperature_ground.push(metric.temperature_ground)
            date.push(metric.date_start)
        }
        humidity_air.reverse()
        humidity_ground.reverse()
        temperature_air.reverse()
        temperature_ground.reverse()
        date.reverse()

        var graph = $('#humidityChart').data('graph');
        humidityChart.data = {
            labels: date,
            datasets: [{
                data: humidity_air
            }, {
                data: humidity_ground
            }]
        };
        graph.update();

        var graph = $('#temperatureChart').data('graph');
        humidityChart.data = {
            labels: date,
            datasets: [{
                data: temperature_air
            }, {
                data: temperature_ground
            }]
        };
        graph.update();
    });
}

$(document).ready(function () {
    var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
    var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList;
    var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent;
    let recognition = new SpeechRecognition();
    let speechRecognitionList = new SpeechGrammarList();
    let colors = ['light on', 'light off', 'pump on', 'pump off', 'heating on', 'heating off', 'fan on', 'fan off'];
    let grammar = '#JSGF V1.0; grammar colors; public <color> = ' + colors.join(' | ') + ' ;';
    speechRecognitionList.addFromString(grammar, 1);
    recognition.grammars = speechRecognitionList;
    recognition.continuous = false;
    recognition.lang = 'en-US';
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    getMetricsNow();
    initAvgDay();
    setInterval(function () {
        getMetricsNow();
        updateAvgDay();
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

    $('#speech-rec').click(function () {
        recognition.start();
        console.log('Ready to receive a color command.');
        recognition.onresult = function (event) {
            let command = event.results[0][0].transcript
            let led_checkbox = document.getElementById("flex_switch_light");
            let pump_checkbox = document.getElementById("flex_switch_pump");
            let heating_checkbox = document.getElementById("flex_switch_heating");
            let fan_checkbox = document.getElementById("flex_switch_fan");
            console.log('Transcript: ' + command);
            console.log('Confidence: ' + event.results[0][0].confidence);
            switch (command) {
                case "light on":
                    led_checkbox.checked = true;
                    $.post(`/dashboard/led/1/`, function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                    });
                    break;
                case "light off":
                    led_checkbox.checked = false;
                    $.post(`/dashboard/led/0/`, function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                    });
                    break;
                case "pump on":
                    pump_checkbox.checked = true;
                    $.post(`/dashboard/pump/1/`, function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                    });
                    break;
                case "pump off":
                    pump_checkbox.checked = false;
                    $.post(`/dashboard/pump/0/`, function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                    });
                    break;
                case "heating on":
                    heating_checkbox.checked = true;
                    $.post(`/dashboard/heating/1/`, function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                    });
                    break;
                case "heating off":
                    heating_checkbox.checked = false;
                    $.post(`/dashboard/heating/0/`, function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                    });
                    break;
                case "fan on":
                    fan_checkbox.checked = true;
                    $.post(`/dashboard/fan/1/`, function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                    });
                    break;
                case "fan off":
                    fan_checkbox.checked = false;
                    $.post(`/dashboard/fan/0/`, function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                    });
                    break;
            }
        }
        recognition.onspeechend = function () {
            recognition.stop();
        }
        recognition.onnomatch = function (event) {
            console.log('Command not recognized');
        }
        recognition.onerror = function (event) {
            console.log('Error occurred in recognition: ' + event.error);
        }
    });
});
