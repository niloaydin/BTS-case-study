const ws = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@trade")

const chart = LightweightCharts.createChart(document.getElementById('chart'), { width: 400, height: 300 });
const lineSeries = chart.addLineSeries();


ws.onmessage = function (event) {
    var message = JSON.parse(event.data);
    lineSeries.setData([
        { time: message.T, value: message.p },
        { time: message.T, value: message.l }

    ]);
}
