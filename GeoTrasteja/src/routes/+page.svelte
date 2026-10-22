<script>
const nomProjecte = 'GeoTrasteja';
const nombreCapes = 3;
let capaVisible = $state(true); 

function alternarVisibilitat () {
  capaVisible = !capaVisible;
}

</script>

<h1>{nomProjecte}</h1>

<p>Pràctica per a consolidar coneixements de Svelte, llibreries de mapes juntament amb programació i desenvolupament Front i back end per a aplicacions </p>

<p>El projecte té {nombreCapes} capes</p>
<p>Si afegim una capa, en tindrem {nombreCapes + 1}.</p>

{#if capaVisible}
  La capa es visible
{/if}


<button onclick={alternarVisibilitat}>
  Canviar visibilitat
</button>

