<script>
	import ResumCapes from '#lib/components/ResumCapes.svelte';
	import MapaJapo from '#lib/components/MapaJapo.svelte';
	import Localitzacions from '#lib/components/Localitzacions.svelte';

	const nomProjecte = 'GeoTrasteja';

	let capes = $state([]);
	let localitzacions = $state([]);
	let localitzacioSeleccionada = $state(null);

	let nomsPerceptibles = $derived(capesPerceptibles.map((capaActual) => capaActual.nom));

	let dadesCarregades = $state(false);

	let missatgeError = $state('');

	let nomBuscat = $state('');

	let carregant = $state(false);

	let capaTrobada = $derived(
		capes.find((capaActual) => capaActual.nom.toLowerCase() === nomBuscat.toLowerCase().trim())
	);

	let capesVisibles = $derived(capes.filter((capaActual) => capaActual.visible));

	let capesPerceptibles = $derived(
		capes.filter((capaActual) => capaActual.visible && capaActual.opacitat > 0)
	);

	function comptarCapesVisibles(capes) {
		let i = 0;

		for (const capaActual of capes) {
			if (capaActual.visible) {
				i++;
			}
		}

		return i;
	}

	function comptarCapesPerceptibles(capes) {
		let i = 0;

		for (const capaActual of capes) {
			if (capaActual.visible && capaActual.opacitat > 0) {
				i++;
			}
		}

		return i;
	}

	function obtenirNomCapesPerceptibles(capes) {
		const nomsPerceptibles = [];

		for (const capaActual of capes) {
			if (capaActual.visible && capaActual.opacitat > 0) {
				nomsPerceptibles.push(capaActual.nom);
			}
		}

		return nomsPerceptibles;
	}

	function seleccionarLocalitzacio (localitzacio){
		localitzacioSeleccionada = localitzacio ;
		
	}

	async function provarCarregaCapes() {
		carregant = true;
		missatgeError = '';

		try {
			const resposta = await fetch('/capes.json');

			if (!resposta.ok) {
				missatgeError = 'No s’han pogut carregar les capes';
				console.error('Error HTTP:', resposta.status);
				return;
			}

			const dades = await resposta.json();
			if (!Array.isArray(dades)) {
				missatgeError = 'Les dades rebudes no són una llista de capes';
				return;
			}
			for (const capaActual of dades) {
				if (capaActual === null || typeof capaActual !== 'object' || Array.isArray(capaActual)) {
					missatgeError = 'Una entrada de la llista no és un objecte capa';
					return;
				} else if (typeof capaActual.nom !== 'string') {
					missatgeError = 'Una capa no té un nom de text';
					return;
				} else if (capaActual.nom.trim() === '') {
					missatgeError = 'El nom conté un text buit';
					return;
				} else if (typeof capaActual.visible !== 'boolean') {
					missatgeError = 'La visibilitat de la capa no es un booleà';
					return;
				} else if (typeof capaActual.opacitat !== 'number') {
					missatgeError = 'L’opacitat d’una capa no és un número';
					return;
				} else if (capaActual.opacitat > 100 || capaActual.opacitat < 0) {
					missatgeError = 'L’opacitat d’una capa no és un número comprés entre 0 i 100';
					return;
				}
			}
			capes = dades;
			dadesCarregades = true;
		} catch (error) {
			missatgeError = 'Error de connexió o de lectura de les dades';
			console.error(error);
		} finally {
			carregant = false;
		}
	}

	async function carregarLocalitzacions() {
		const resposta = await fetch('/localitzacions.json');
		const dades = await resposta.json();
		localitzacions = dades;
	}
</script>

<h1>{nomProjecte}</h1>

<p>
	Pràctica per consolidar coneixements de Svelte, llibreries de mapes i desenvolupament frontend i
	backend.
</p>

<button onclick={provarCarregaCapes} disabled={carregant}>Provar carrega capes</button>
<button onclick={carregarLocalitzacions}>Provar carrega localitzacions {localitzacions.length}</button>

<Localitzacions localitzacions={localitzacions} />


{#if !dadesCarregades && !carregant}
	<p>Encara no s’han carregat les dades</p>
{:else if dadesCarregades && capes.length === 0}
	<p>La llista carregada és buida</p>
{/if}

{#if carregant === true}
	<p>Carregant capes...</p>
{/if}

{#if missatgeError !== ''}
	<p>{missatgeError}</p>
{/if}

<MapaJapo />

<h2>Controls de les capes</h2>

{#each capes as capaActual}
	<div>
		<h3>{capaActual.nom}</h3>
		<p>Opacitat: {capaActual.opacitat}%</p>

		<button
			onclick={() => {
				capaActual.opacitat = 100;
				capaActual.visible = true;
			}}
		>
			Restablir valors
		</button>

		<button
			onclick={() => {
				capaActual.visible = !capaActual.visible;
			}}
		>
			{#if capaActual.visible}
				Amagar
			{:else}
				Mostrar
			{/if}
		</button>

		{#if capaActual.visible}
			<label>
				Opacitat de {capaActual.nom}
				<input type="range" min="0" max="100" step="10" bind:value={capaActual.opacitat} />
			</label>
		{/if}
	</div>
{/each}

<h2>Controls globals</h2>

<button
	onclick={() => {
		for (const capaActual of capes) {
			capaActual.visible = false;
		}
	}}
>
	Amagar totes les capes
</button>

<button
	onclick={() => {
		for (const capaActual of capes) {
			capaActual.visible = true;
		}
	}}
>
	Mostrar totes les capes
</button>

<button
	onclick={() => {
		for (const capaActual of capes) {
			capaActual.visible = true;
			capaActual.opacitat = 100;
		}
	}}
>
	Restablir totes
</button>

<Localitzacions
localitzacions={localitzacions}
onSeleccionar={seleccionarLocalitzacio}
/>

<ResumCapes
	totalCapes={capes.length}
	totalVisibles={capesVisibles.length}
	totalPerceptibles={capesPerceptibles.length}
	{nomsPerceptibles}
/>

<h2>Cercador de capes</h2>

<div>
	<label>
		Nom de la capa:
		<input type="text" bind:value={nomBuscat} />
	</label>

	<p>Estàs buscant: {nomBuscat}</p>

	{#if nomBuscat.trim() === ''}
		<p>Escriu el nom d'una capa</p>
	{:else if capaTrobada !== undefined}
		<p>Capa trobada: {capaTrobada.nom}</p>

		{#if capaTrobada.visible}
			<p>Capa visible</p>
		{:else}
			<p>Capa oculta</p>
		{/if}

		<p>
			Opacitat de la capa:
			{capaTrobada.opacitat}%
		</p>
	{:else}
		<p>No s'ha trobat cap capa</p>
	{/if}
</div>
