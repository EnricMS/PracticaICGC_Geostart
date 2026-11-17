
<script>
  let { totalCapes, totalVisibles, totalPerceptibles, nomsPerceptibles } = $props();
  
</script>

<h2>Resum de les capes</h2>

{#if totalPerceptibles === totalCapes && totalCapes > 0}
Totes les capes són perceptibles
{/if}

{#each nomsPerceptibles as nomCapa}
	<p>Capa perceptible: {nomCapa}</p>
{:else}
	<p>No hi ha cap capa perceptible</p>
{/each}

<p>Total de capes: {totalCapes}</p>
<p>Total de capes visibles: {totalVisibles}</p>
<p>Total de capes perceptibles: {totalPerceptibles}</p>

{#if totalVisibles < totalCapes}
<p>Hi ha capes amagades</p>
{/if}

<p>Capes amagades: {totalCapes - totalVisibles}</p>
<p>Capes activades però no perceptibles: {totalVisibles - totalPerceptibles}</p>