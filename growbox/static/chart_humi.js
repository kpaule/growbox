function initHumidityChart(humi_floor_data, humi_floor_date) {
    var ctx = document.getElementById('humidityChart');
    var humidityChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: humi_floor_date,
            datasets: [{
                label: 'Humidity',
                data: humi_floor_data,
                borderWidth: 1
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
}