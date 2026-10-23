<script>
const nomProjecte = 'GeoTrasteja';
const nombreCapes = 3;
const capa = $state({nom:'Ortofoto', visible: true, opacitat: 100});

function alternarVisibilitat () {
  capa.visible = !capa.visible;
}

</script>

<h1>{nomProjecte}</h1>

<p>Pràctica per a consolidar coneixements de Svelte, llibreries de mapes juntament amb programació i desenvolupament Front i back end per a aplicacions </p>

<p>El projecte té {nombreCapes} capes</p>
<p>Si afegim una capa, en tindrem {nombreCapes + 1}.</p>

{#if capa.visible}
  La capa es visible
 {:else}
 La capa es oculta 
{/if}

<button onclick={alternarVisibilitat}>
  Canviar visibilitat
</button>

<button onclick= {() => capa.visible = !capa.visible}> 
  {#if capa.visible} Amaga {:else} Mostra{/if}
</button>


<button onclick={() => capa.visible = true }>Mostrar Capa</button>
<button onclick={() => capa.visible = false }>Amagar Capa</button>


<button  onclick = {() => {if (capa.opacitat > 0){ capa.opacitat = capa.opacitat - 10}}}>Reduir Opacitat Capa</button>

<p>Opacitat: {capa.opacitat}%</p>

<input type="range" min="0" max="100" step="10" bind:value={capa.opacitat} />

<button  onclick = {() => {if (capa.opacitat < 100){ capa.opacitat = capa.opacitat + 10}}}>Augmentar Opacitat Capa</button>

<button onclick= {() => {capa.opacitat = 100; capa.visible = true }}>Restablir Opacitat</button>

<p>{capa.nom}</p>

<button onclick={() => capa.visible = !capa.visible}>Alternar Visibilitat Capes</button>
