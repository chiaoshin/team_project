
// 設定一地圖，定位在#map，先定位在center座標，zoom定位【已設定好經緯度】
var map = L.map('map', {
    center: [23.6978,120.9605],
    zoom: 7
});

// 【圖資設定】
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

