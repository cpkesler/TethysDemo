require(["esri/map", "dojo/domReady!"], function(Map) {
  var map = new Map("map", {
    center: [-86.5, 33],
    zoom: 6,
    basemap: "topo"
  });
});