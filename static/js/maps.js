var map;
function initialize() {
  var mapOptions = {
    center: { lat: -34.397, lng: 150.644},
    zoom: 12
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
  var geocoder = new google.maps.Geocoder();


  var initialLocation;
  var siberia = new google.maps.LatLng(60, 105);
  var newyork = new google.maps.LatLng(40.69847032728747, -73.9514422416687);
  var browserSupportFlag =  new Boolean();
  // Try W3C Geolocation (Preferred)
  if(navigator.geolocation) {
      browserSupportFlag = true;
      navigator.geolocation.getCurrentPosition(function(position) {
        initialLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
        map.setCenter(initialLocation);
      }, function() {
        handleNoGeolocation(browserSupportFlag);
      });
    }
    // Browser doesn't support Geolocation
    else {
      browserSupportFlag = false;
      handleNoGeolocation(browserSupportFlag);
    }

    function handleNoGeolocation(errorFlag) {
      if (errorFlag == true) {
        alert("Geolocation service failed.");
        initialLocation = newyork;
      } else {
        alert("Your browser doesn't support geolocation. We've placed you in Siberia.");
        initialLocation = siberia;
      }
      map.setCenter(initialLocation);
    }

  geocoder.geocode({ 'address': "1185 York Rd. Warminster, PA 18974" }, function (results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        pt = results[0].geometry.location;
        console.log(pt);

        var myMarkerOpts = {
          position: pt,
          map: map
        };

        var marker = new google.maps.Marker(myMarkerOpts);
      }
  });
}
google.maps.event.addDomListener(window, 'load', initialize);