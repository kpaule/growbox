function initTemperatureChart(temp_floor_data, temp_floor_date) {
    var ctx = document.getElementById('temperatureChart');
    var temperatureChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: temp_floor_date,
            datasets: [{
                label: 'Temperature',
                data: temp_floor_data,
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