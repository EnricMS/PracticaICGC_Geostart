<script>

	let { localitzacions, onSeleccionar } = $props();


</script>

<h2>Localitzacions</h2>

{#each localitzacions as localitzacioActual}

	<button onclick={ () => onSeleccionar(localitzacioActual)}>Localitat: {localitzacioActual.nom}</button>
{/each}
