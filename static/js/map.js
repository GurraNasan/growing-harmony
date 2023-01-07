function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 11,
        center: {
            lat: 59.01,
            lng: 18
        }
    });
    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    var locations = [ 
    {lat: 59.03942229246411, lng: 18.01422054105957 },
    {lat: 59.00877639554074, lng: 17.966252069894995},      
    ];

    var markers = locations.map((location, i) => {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    const markerCluster = new markerClusterer.MarkerClusterer({ map, markers });

}