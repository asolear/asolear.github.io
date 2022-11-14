var tileLayer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  'attribution': 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
});

var map = new L.Map('map', {
  'center': [37,-4],
  'zoom': 8,
  'layers': [tileLayer]
});

var marker;

map.on('click', function (e) {
  if (marker) {
    map.removeLayer(marker);
  }
  marker = new L.Marker(e.latlng).addTo(map);
});
