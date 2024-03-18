<script lang="ts">
	import { onMount } from 'svelte';
	import markers from '$lib/markers.json';
	import { scaleLinear } from 'd3-scale';
	let L;

	onMount(async () => {
		L = (await import('leaflet')).default;

		const map = L.map('map', {
			center: [39.8283, -98.5795],
			zoom: 5,
			minZoom: 3,
			zoomSnap: 0.1
		});

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors | Data from <a href="https://en.wikipedia.org/wiki/List_of_North_American_settlements_by_year_of_foundation" target="_blank">Wikipedia</a> and <a href="https://simplemaps.com/data/us-cities> target="_blank">SimpleMaps</a>'
    }).addTo(map);
  
		const minYear = 1521;
		const maxYear = 1917;

		const colorScale = scaleLinear().domain([minYear, maxYear]).range(['red', 'yellow']);

		markers.forEach((marker) => {
			const markerColor = colorScale(marker.year);
			const markerIcon = L.divIcon({
				className: 'custom-icon',
				html: `<svg height="50" width="50">
          <circle cx="25" cy="25" r="5" stroke="black" stroke-width="1" fill="${markerColor}" />
        </svg>`,
				iconSize: [50, 50]
			});

			L.marker([marker.lat, marker.lng], { icon: markerIcon })
				.bindPopup(`${marker.city}, ${marker.year}`)
				.openPopup()
				.addTo(map);
		});
	});
</script>

<svelte:head>
	<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
</svelte:head>

<main>
	<div class="cont">
		<div id="map" />
	</div>
</main>

<style>
	main {
		height: 100vh;
		width: 100vw;
		padding: 0;
		background-color: var(--light);
	}
	#map {
		height: 100%;
		width: 100%;
	}
	.cont {
		width: 100%;
		height: 100%;
	}
</style>
