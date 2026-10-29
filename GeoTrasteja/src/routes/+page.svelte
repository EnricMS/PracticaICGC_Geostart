<script>
	const nomProjecte = 'GeoTrasteja';
	const nombreCapes = 3;
	const capa = $state({ nom: 'Ortofoto', visible: true, opacitat: 100 });
	const capes = $state([
		{ nom: 'Ortofoto', visible: true, opacitat: 100 },
		{ nom: 'Geologia', visible: false, opacitat: 70 }
	]);
	
	let nomBuscat = $state('');

	function alternarVisibilitat() {
		capa.visible = !capa.visible;
	}

	capes[1].nom;

	function comptarCapesVisibles(capes) {
		let i = 0;

		for (const capaActual of capes) {
			if (capaActual.visible === true) {
				i++;
			}
		}
		return i;
	}

	function comptarCapesPerceptibles(capes) {
		let i = 0;
		for (const capaActual of capes) {
			if (capaActual.visible === true && capaActual.opacitat > 0) {
				i++;
			}
		}
		return i;
	}

	function obtenirNomCapesPerceptibles(capes) {
		const capesVisibles = [];
		for (const capaActual of capes) {
			if (capaActual.visible === true && capaActual.opacitat > 0) {
				capesVisibles.push(capaActual.nom);
			}
		}
		return capesVisibles;
	}

function buscarCapaNom(capes, nomBuscat) {
  for (const nomCerca of capes) {
    if (nomBuscat.toLowerCase().trim() === nomCerca.nom.toLowerCase()) {
      return nomCerca;
    }
  }
  return null;
}

const capaTrobada = buscarCapaNom(capes, 'Geologia');

if (capaTrobada !== null) {
  console.log(capaTrobada.opacitat);
}

</script>

<h1>{nomProjecte}</h1>

<p>
	Pràctica per a consolidar coneixements de Svelte, llibreries de mapes juntament amb programació i
	desenvolupament Front i back end per a aplicacions
</p>

<p>El projecte té {nombreCapes} capes</p>
<p>Si afegim una capa, en tindrem {nombreCapes + 1}.</p>

{#if capa.visible}
	La capa es visible
{:else}
	La capa es oculta
{/if}

<button onclick={alternarVisibilitat}> Canviar visibilitat </button>

<button onclick={() => (capa.visible = !capa.visible)}>
	{#if capa.visible}
		Amaga
	{:else}
		Mostra{/if}
</button>

<button onclick={() => (capa.visible = true)}>Mostrar Capa</button>
<button onclick={() => (capa.visible = false)}>Amagar Capa</button>

<button
	onclick={() => {
		if (capa.opacitat > 0) {
			capa.opacitat = capa.opacitat - 10;
		}
	}}>Reduir Opacitat Capa</button
>

<p>Opacitat: {capa.opacitat}%</p>

<input type="range" min="0" max="100" step="10" bind:value={capa.opacitat} />

<button
	onclick={() => {
		if (capa.opacitat < 100) {
			capa.opacitat = capa.opacitat + 10;
		}
	}}>Augmentar Opacitat Capa</button
>

<button
	onclick={() => {
		capa.opacitat = 100;
		capa.visible = true;
	}}>Restablir Opacitat</button
>

<p>{capa.nom}</p>

<button onclick={() => (capa.visible = !capa.visible)}>Alternar Visibilitat Capes</button>

<!-- <p>{capes[1].nom}</p> -->

{#each capes as capaActual}
	{#if capaActual.visible}
		Capa visible
	{:else}
		Capa oculta{/if}
	<button
		onclick={() => {
			capaActual.visible = !capaActual.visible;
		}}>Alternar Visibilitat</button
	>
	<p>{capaActual.nom} --- Opacitat: {capaActual.opacitat}%</p>
{/each}

{#each capes as capaActual}
	<p>{capaActual.nom} --- Opacitat: {capaActual.opacitat}%</p>
	<button
		onclick={() => {
			capaActual.opacitat = 100;
			capaActual.visible = true;
		}}>Restablir valors</button
	>
	<button
		onclick={() => {
			capaActual.visible = !capaActual.visible;
		}}
	>
		{#if capaActual.visible}
			Amagar
		{:else}
			Mostrar
		{/if}</button
	>
	{#if capaActual.visible}
		<input type="range" min="0" max="100" step="10" bind:value={capaActual.opacitat} />
	{/if}
{/each}

<button
	onclick={() => {
		for (const capaActual of capes) {
			capaActual.visible = false;
		}
	}}>Amagar totes les capes</button
>

<button
	onclick={() => {
		for (const capaActual of capes) {
			capaActual.visible = true;
		}
	}}>Mostrar totes les capes</button
>

<button
	onclick={() => {
		for (const capaActual of capes) {
			capaActual.visible = true;
			capaActual.opacitat = 100;
		}
	}}>Restablir totes</button
>

<p>Capes visibles {comptarCapesVisibles(capes)}</p>
<p>Capes perceptibles {comptarCapesPerceptibles(capes)}</p>

{#each obtenirNomCapesPerceptibles(capes) as NomCapaPerceptible}
	<p>Capa perceptible: {NomCapaPerceptible}</p>
{:else}
	<p>No hi ha cap capa perceptible</p>
{/each}


<div>
<p>Cerca:</p>
	<input type="text" bind:value ={nomBuscat}/>
	<p>Estàs buscant: {nomBuscat}</p>
	{#if (nomBuscat.trim() === '') } Escriu el nom d'una capa{:else if buscarCapaNom(capes, nomBuscat) !== null} 
		Capa trobada{:else}No s'ha trobat cap capa 
	{/if}
</div>
