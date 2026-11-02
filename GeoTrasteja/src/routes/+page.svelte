<script>

const nomProjecte = 'GeoTrasteja';

const capes = $state([
	{ nom: 'Ortofoto', visible: true, opacitat: 100 },
	{ nom: 'Geologia', visible: true, opacitat: 100 }
]);

let nomsPerceptibles = $derived(capesPerceptibles.map(capaActual => capaActual.nom));

let nomBuscat = $state('');

let capaTrobada = $derived(
	capes.find(capaActual =>
		capaActual.nom.toLowerCase() === nomBuscat.toLowerCase().trim()
	)
);

let capesVisibles = $derived(
	capes.filter(capaActual => capaActual.visible)
);

let capesPerceptibles = $derived(
	capes.filter(capaActual =>
		capaActual.visible && capaActual.opacitat > 0
	)
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


</script>

<h1>{nomProjecte}</h1>

<p>
	Pràctica per consolidar coneixements de Svelte, llibreries de mapes
	i desenvolupament frontend i backend.
</p>

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
				<input
					type="range"
					min="0"
					max="100"
					step="10"
					bind:value={capaActual.opacitat}
				/>
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

<h2>Resum</h2>

<p>Total de capes: {capes.length}</p>
<p>Capes visibles: {capesVisibles.length}</p>
<p>Capes perceptibles: {capesPerceptibles.length}</p>

{#each obtenirNomCapesPerceptibles(capes) as nomCapa}
	<p>Capa perceptible: {nomCapa}</p>
{:else}
	<p>No hi ha cap capa perceptible</p>
{/each}

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