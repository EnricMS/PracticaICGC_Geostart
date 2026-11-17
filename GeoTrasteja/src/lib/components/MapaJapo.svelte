<script>
import {onMount} from 'svelte';
import * as maplibregl from 'maplibre-gl';
import workerUrl from 'maplibre-gl/dist/maplibre-gl-worker.mjs?url';
import 'maplibre-gl/dist/maplibre-gl.css'

let contenidorMapa;

onMount(() => {
	maplibregl.setWorkerUrl(workerUrl);
	const mapa = new maplibregl.Map({
		container: contenidorMapa,
		style: 'https://demotiles.maplibre.org/style.json',
		center: [138, 37],
		zoom: 4
	});
	mapa.addControl(new maplibregl.NavigationControl(), 'top-right');
mapa.on('error', (event) => {
	console.error('Error del mapa:', event.error);
});
	return () => {
		mapa.remove();
	};
});
</script>



Kore wa Nihon chizu desu.

<div class="mapa" bind:this={contenidorMapa}></div>

<style>
	.mapa {
		margin-inline: auto;
		width: 70%;
		height: 600px;
	}
</style>
