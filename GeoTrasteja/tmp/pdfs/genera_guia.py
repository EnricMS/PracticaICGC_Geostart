from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output/pdf/GeoTrasteja_guia_de_repas_2026-11-07.pdf'
for name, file in [('Body','arial.ttf'),('Bold','arialbd.ttf'),('Code','consola.ttf')]:
    pdfmetrics.registerFont(TTFont(name, 'C:/Windows/Fonts/'+file))
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TextCat', fontName='Body', fontSize=11, leading=16, spaceAfter=10))
styles.add(ParagraphStyle(name='TitleCat', fontName='Bold', fontSize=27, leading=32, textColor=colors.HexColor('#12394a'), spaceAfter=18))
styles.add(ParagraphStyle(name='HeadCat', fontName='Bold', fontSize=16, leading=21, textColor=colors.HexColor('#126c78'), spaceBefore=12, spaceAfter=10))
styles.add(ParagraphStyle(name='CodeCat', fontName='Code', fontSize=9, leading=13, backColor=colors.HexColor('#edf3f5'), borderPadding=10, spaceBefore=7, spaceAfter=15))
story=[]
def p(t): story.append(Paragraph(t,styles['TextCat']))
def h(t): story.append(Paragraph(t,styles['HeadCat']))
def code(t): story.append(Preformatted(t.strip('\n'),styles['CodeCat']))
def page(n,t):
    if story: story.append(PageBreak())
    p('GEOTRASTEJA · QUADERN DE REPÀS · '+str(n))
    story.append(Paragraph(t,styles['TitleCat']))

page(1,'JavaScript i Svelte, pas a pas')
p('Guia personal de teoria i exemples a partir de la pràctica de GeoTrasteja. Preparada per a Enric Miralles · Actualització del 7 de novembre de 2026.')
p('Objectiu: entendre què fa cada peça del codi i poder tornar-la a escriure amb autonomia. Els exemples se centren en capes de mapa: nom, visibilitat i opacitat. Encara no hem connectat aquests controls a un mapa real.')
h('Com llegir aquest quadern')
p('Dedica un descans a una secció. Abans de mirar l’explicació d’un exemple, intenta anticipar què mostrarà o què passarà en fer clic. No cal memoritzar cada símbol de cop: relaciona’l amb la seva funció.')
h('Recorregut de lectura')
for t in ['2. Entorn, terminal i servidor local','3. Anatomia del component i HTML','4. Variables, valors i expressions','5. Estat reactiu i actualització de pantalla','6. Funcions, esdeveniments i funcions fletxa','7. Condicionals: JavaScript i Svelte','8. Opacitat, lliscadors i vinculació','9. Objectes i propietats','10. Arrays i accés per posició','11. Repetir la interfície amb each','12. Exemple integrat de les capes','13. Errors habituals i com llegir-los','14. React, SvelteKit i vocabulari de consulta']:
    p(t)
p('Ampliacions: 15-21. Accions globals, comptadors i cerca. 22-29. $derived, find, filter i map. 30-32. Organització i components. 33-35. JSON, HTTP i fetch. 36-37. Errors i estats. 38-41. Validació i càrrega integrada. 42-43. Missatges, proves i repàs. Els exemples antics es conserven com a etapes, no per acumular-los al component.')

page(2,'L’entorn i la terminal')
p('<b>Node.js</b> permet executar JavaScript fora del navegador. <b>npm</b> gestiona dependències i executa les ordres definides al projecte. Una dependència és un paquet de codi que utilitza el projecte.')
code('node -v\nnpm -v\nnpx sv create .')
p('<b>npx</b> executa una eina d’un paquet npm; pot descarregar-la si cal. <b>sv</b> és la CLI de Svelte; <b>create</b> crea un projecte i <b>.</b> indica la carpeta actual. Vam triar SvelteKit minimal, JavaScript amb JSDoc, Prettier, ESLint i npm.')
p('<b>JSDoc</b> permet descriure tipus amb comentaris mantenint sintaxi JavaScript. <b>Prettier</b> formata el codi; <b>ESLint</b> detecta determinats problemes. No substitueixen entendre ni provar el programa.')
h('Iniciar el projecte')
code('cd .\u005cGeoTrasteja\nnpm run dev\n# Opcional: obrir també el navegador\nnpm run dev -- --open')
p('Executa npm run dev des de la carpeta que conté <b>package.json</b>. Aquest fitxer descriu el projecte, les dependències i els scripts. L’ordre inicia el servidor de desenvolupament; obre l’adreça que indiqui la terminal. Ctrl+C l’atura.')
p('<b>localhost</b> fa referència al teu ordinador. El port identifica el servei concret. Desa els canvis perquè l’entorn de desenvolupament els apliqui; molts canvis es reflecteixen automàticament al navegador.')
h('Dos errors que hem vist')
p('<b>ENOENT / no es troba package.json:</b> érem a la carpeta superior, no dins de GeoTrasteja. Primer cal entrar al projecte amb cd.')
p('<b>JSON enganxat a PowerShell:</b> una configuració com editor.inlineSuggest.enabled pertany a la configuració de l’editor. No és una ordre de terminal ni codi del component.')
p('Un avís de nova versió de npm no implica que la instal·lació hagi fallat. Chart.js serveix per a gràfics i no era necessari en aquesta pràctica.')

page(3,'Un component .svelte')
p('Un <b>component</b> és una peça de la interfície amb dades, comportament i presentació. En un fitxer .svelte poden conviure JavaScript, plantilla i estils. A SvelteKit, <b>src/routes/+page.svelte</b> defineix la pàgina d’aquella ruta.')
code('''<script>
  const nomProjecte = 'GeoTrasteja';
</script>

<h1>{nomProjecte}</h1>
<p>Pràctica de desenvolupament web i mapes.</p>''')
p('El bloc <b>script</b> conté JavaScript. La part de sota és la <b>plantilla</b>: HTML amb sintaxi de Svelte. Les variables del script estan disponibles en aquesta plantilla perquè formen part del mateix component: no cal importar-les entre les dues parts.')
h('HTML que hem utilitzat')
p('<b>&lt;h1&gt;</b>: títol principal. <b>&lt;p&gt;</b>: paràgraf. <b>&lt;button&gt;</b>: botó. <b>&lt;a href="..."&gt;</b>: enllaç, amb l’adreça a l’atribut href. <b>&lt;input&gt;</b>: control de formulari.')
code('<p>Text del paràgraf</p>\n<a href="https://svelte.dev">Documentació</a>')
p('Una <b>etiqueta d’obertura</b> inicia l’element i una <b>etiqueta de tancament</b> el tanca. Els atributs van a l’etiqueta d’obertura. Per exemple, onclick pertany a &lt;button ...&gt;, no al text entre les etiquetes.')
h('Text i expressions')
code('<p>El projecte és {nomProjecte}.</p>')
p('El text normal s’escriu directament. Les claus indiquen que Svelte ha d’avaluar una expressió JavaScript i utilitzar-ne el valor. Un comentari de plantilla s’escriu amb &lt;!-- comentari --&gt;.')

page(4,'Variables i expressions')
code("const nomProjecte = 'GeoTrasteja';\nconst nombreCapes = 3;\nlet visible = true;")
p('Una <b>variable</b> associa un nom a un valor. Una <b>declaració</b> crea aquesta associació. Una <b>assignació</b> estableix o canvia el valor amb =.')
p('<b>const</b> impedeix reassignar el nom. <b>let</b> permet reassignar-lo. Un <b>string</b> és text entre cometes; un <b>number</b> és un número; un <b>boolean</b> és true o false, sense cometes.')
code("'GeoTrasteja'  // text\n100           // número\ntrue          // booleà\n'false'       // text, no és el booleà false")
h('Expressió i instrucció')
p('Una <b>expressió</b> produeix un valor: nombreCapes + 1 dona 4 si nombreCapes val 3. Una <b>instrucció</b> executa una acció o controla el flux: per exemple, una assignació o un if.')
code('<p>El projecte té {nombreCapes} capes.</p>\n<p>Amb una capa més: {nombreCapes + 1}.</p>')
p('Sumar dins de les claus no modifica nombreCapes. Per modificar una variable cal assignar el resultat: opacitat = opacitat - 10.')
h('Operadors essencials')
p('<b>=</b> assigna. <b>===</b> compara valor i tipus. <b>!</b> nega un valor lògic. <b>&lt;</b> i <b>&gt;</b> comparen números. <b>+</b> suma números; <b>-</b> resta. <b>&amp;&amp;</b> i <b>||</b> combinen expressions amb curtcircuit; no calen per agrupar instruccions seguides.')
code('!true   // false\n!false  // true\nvisible = !visible; // inverteix el booleà')
p('JavaScript distingeix majúscules: capaVisible, capavisible i opcaitat són noms diferents. Un error de nom pot trencar el programa encara que la idea sigui correcta.')

page(5,'Estat reactiu amb $state')
p('L’<b>estat</b> són les dades que poden canviar mentre utilitzem la interfície. La <b>reactivitat</b> connecta aquests canvis amb el contingut que veiem.')
code('''<script>
  let capaVisible = $state(true);
  let opacitat = $state(100);
</script>

<p>Opacitat: {opacitat}%</p>''')
p('En aquest component de Svelte 5 fem servir <b>$state</b>, una runa reconeguda pel compilador, per declarar estat reactiu. No l’hem d’importar. Quan un esdeveniment modifica opacitat, Svelte actualitza els fragments que en depenen.')
p('Una variable let ordinària permet reassignacions de JavaScript, però en aquest component amb runes no declara per si sola estat reactiu. Per això vam passar de let opacitat = 100 a let opacitat = $state(100).')
h('Desar codi no és clicar un control')
p('Canviar una constant al fitxer i desar provoca una actualització de desenvolupament. Canviar l’estat amb un botó passa durant l’execució de l’aplicació: és el comportament que estem programant per a l’usuari.')
h('La cadena que ja hem construït')
code('Clic -> funció -> canvi d’estat -> pantalla actualitzada')
p('No cal buscar manualment el paràgraf al DOM i canviar-ne el text. El <b>DOM</b> és la representació dels elements de la pàgina que gestiona el navegador; Svelte genera el codi necessari per actualitzar-lo.')
p('Aquests valors no es desen permanentment per si sols. Recarregar la pàgina crea una nova instància amb els valors inicials, tret que programem persistència.')

page(6,'Funcions i clics')
p('Una <b>funció</b> agrupa instruccions que s’executen quan es crida. Definir-la i cridar-la són accions diferents. Un <b>paràmetre</b> és un nom d’entrada de la funció; un argument és el valor que li passem en cridar-la.')
code('''function alternarVisibilitat() {
  capaVisible = !capaVisible;
}

// A la plantilla:
<button onclick={alternarVisibilitat}>Alternar</button>''')
p('<b>onclick</b> rep una funció: el gestor de l’esdeveniment. Sense parèntesis passem la funció perquè s’executi en fer clic. Escriure onclick={alternarVisibilitat()} la cridaria en avaluar l’atribut, no reservaria la crida per al clic.')
h('La mateixa acció amb una funció fletxa')
code('''<button onclick={() => capaVisible = !capaVisible}>
  Alternar
</button>''')
p('<b>()</b> indica que no declarem paràmetres. <b>=&gt;</b> introdueix el cos. Aquesta funció és anònima: l’hem escrit directament a l’atribut. Amb una sola expressió podem ometre les claus del cos.')
code('''<button onclick={() => {
  opacitat = 100;
  capaVisible = true;
}}>
  Restablir
</button>''')
p('Amb diverses instruccions fem servir un únic cos amb claus i separem les instruccions amb punt i coma. No utilitzem &amp;&amp; per unir dos blocs. A onclick={...}, les claus exteriors són de Svelte; les de després de =&gt; delimiten el cos JavaScript.')
p('<b>return</b> retorna un resultat i acaba l’execució de la funció. <b>console.log</b> mostra informació a la consola, però no substitueix retornar un valor. En aquests gestors només necessitem modificar l’estat.')

page(7,'Dos contextos per al if')
h('Plantilla: decidir què es mostra')
code('''{#if capaVisible}
  <p>La capa és visible.</p>
{:else}
  <p>La capa està oculta.</p>
{/if}''')
p('<b>#</b> obre un bloc; <b>:</b> introdueix una branca alternativa; <b>/</b> tanca el bloc. Són marques de Svelte, no la sintaxi if de JavaScript. Si no hi ha else i la condició és falsa, no es crea el contingut del bloc.')
h('Funció: decidir què s’executa')
code('''<button onclick={() => {
  if (opacitat > 0) {
    opacitat = opacitat - 10;
  }
}}>
  Reduir opacitat
</button>''')
p('Aquí som dins del cos d’una funció JavaScript, encara que visualment estigui a la plantilla. Per això utilitzem if (...) { ... }, sense #. El context del codi determina la sintaxi, no només la presència del bloc script.')
h('Consultar no és assignar')
code('''{#if capaVisible}           <!-- correcte -->
{#if capaVisible === true}  <!-- també correcte -->

<!-- Incorrecte per consultar: -->
{#if capaVisible = true}''')
p('L’última expressió assigna true i produeix true; no compara. A més, modifica estat mentre Svelte renderitza. En mode runes aquesta mutació durant l’avaluació de la plantilla pot provocar un error d’estat insegur. Un 500 és el símptoma al servidor; el missatge concret explica la causa.')
p('El gestor del clic modifica les dades. El condicional de la plantilla consulta les dades per decidir què mostrar.')

page(8,'Lliscadors i opacitat')
code('''<p>Opacitat: {opacitat}%</p>
<input type="range" min="0" max="100"
  step="10" bind:value={opacitat} />''')
p('<b>type="range"</b> crea un lliscador. <b>min</b> i <b>max</b> en delimiten els valors seleccionables; <b>step</b> estableix els salts. Aquest input no necessita etiqueta de tancament.')
p('<b>bind:value</b> crea una vinculació en dos sentits: moure el lliscador actualitza la variable; modificar la variable actualitza el control. En un input numèric o range, Svelte tracta el valor vinculat com a número.')
h('Botons amb condicions')
code('''<button onclick={() => {
  if (opacitat < 100) {
    opacitat = opacitat + 10;
  }
}}>Augmentar</button>''')
p('Si comencem a 100 i només fem salts de 10, amb els dos botons protegits i el lliscador només arribem a 0, 10, 20... 100. La comprovació és suficient per a aquestes regles actuals.')
p('Si més endavant el valor pogués ser 95, comprovar opacitat &lt; 100 i sumar 10 donaria 105. Cal revisar la validació quan canvien les entrades permeses. Els límits HTML del lliscador no són una validació general de totes les assignacions JavaScript.')
h('Dos conceptes independents')
p('<b>visible</b> indica si volem mostrar la capa. <b>opacitat</b> indica el grau de transparència. Una capa amb visible a true i opacitat 0 pot estar activada però no ser perceptible. De moment mostrem valors; encara no afecten cap mapa real.')

page(9,'Objectes: agrupar propietats')
p('Un <b>objecte</b> agrupa valors amb nom. Cada parella nom: valor és una propietat. Això permet mantenir juntes les dades d’una mateixa capa.')
code("const capa = $state({\n  nom: 'Ortofoto',\n  visible: true,\n  opacitat: 100\n});")
p('Les claus defineixen l’objecte, els dos punts separen el nom de la propietat del valor, i les comes separen les propietats. $state rep l’objecte dins dels seus parèntesis.')
code("capa.nom       // 'Ortofoto'\ncapa.visible   // true\ncapa.opacitat  // 100")
p('El <b>punt</b> accedeix a una propietat. capa és tot l’objecte; capa.visible és només el valor de la seva propietat visible. No són intercanviables.')
h('Modificar l’objecte reactiu')
code('''<button onclick={() => capa.visible = !capa.visible}>
  Alternar
</button>
<p>Opacitat: {capa.opacitat}%</p>
<input type="range" min="0" max="100" step="10"
  bind:value={capa.opacitat} />''')
p('$state fa reactives les propietats d’aquest objecte simple. <b>const és vàlid</b>: podem modificar capa.visible; el que const impedeix és reassignar capa a un altre objecte.')
p('Quan migrem de variables independents a un objecte, tots els controls han de consultar i modificar les mateixes propietats. Si el lliscador modifica opacitat però el paràgraf llegeix capa.opacitat, treballen amb dades diferents.')
p('Un cop feta la migració, eliminem les antigues declaracions que ja no utilitzem. Això redueix les confusions sobre quina dada controla cada element.')

page(10,'Arrays: una llista de capes')
p('Un <b>array</b> és una llista ordenada d’elements. S’escriu amb claudàtors i els seus elements se separen amb comes. Pot contenir objectes.')
code("const capes = $state([\n  { nom: 'Ortofoto', visible: true, opacitat: 100 },\n  { nom: 'Geologia', visible: false, opacitat: 70 }\n]);")
p('Llegim els embolcalls de fora cap a dins: $state(...) declara l’estat; [...] conté la llista; cada {...} representa una capa. Els valors de l’objecte necessiten noms de propietat.')
h('Les posicions comencen a zero')
code("capes[0]           // tot l’objecte Ortofoto\ncapes[1]           // tot l’objecte Geologia\ncapes[1].nom       // 'Geologia'\ncapes[0].opacitat  // 100\ncapes.length       // 2")
p('Primer seleccionem l’objecte per la posició de l’array, després la propietat pel nom. No parlem de la primera posició d’un objecte per obtenir-ne el nom: utilitzem .nom.')
h('Consultar, recórrer i afegir')
p('Si coneixem la posició, l’accés directe és suficient. Un bucle és útil per processar diversos elements. <b>push()</b> afegeix un element al final d’un array: no serveix per consultar un nom existent.')
code('''for (const capaActual of capes) {
  console.log(capaActual.nom);
}''')
p('Aquest for...of és JavaScript: recorre els objectes. const declara la variable de cada iteració. Si una funció retorna dins del bucle, s’acaba tota la funció, no només aquella volta. Per mostrar elements a la plantilla farem servir each.')

page(11,'Una interfície per cada capa')
code('''{#each capes as capaActual}
  <p>{capaActual.nom} - Opacitat: {capaActual.opacitat}%</p>
{/each}''')
p('<b>{#each}</b> repeteix un fragment de plantilla per cada element de l’array. <b>as capaActual</b> dona un nom temporal a l’element que estem representant. No crea un nou objecte independent: accedim a la capa corresponent de l’array.')
p('Aquest nom està disponible dins del bloc. Hem triat capaActual, però podríem escollir un altre nom coherent. Si posem el paràgraf dins del bloc, es crea un paràgraf per capa. Si envoltem el bloc amb un únic paràgraf, tot queda dins d’aquell paràgraf.')
h('Cada botó controla la seva capa')
code('''{#each capes as capaActual}
  <p>{capaActual.nom}</p>
  {#if capaActual.visible}
    <p>Capa visible</p>
  {:else}
    <p>Capa oculta</p>
  {/if}
  <button onclick={() => {
    capaActual.visible = !capaActual.visible;
  }}>Alternar visibilitat</button>
{/each}''')
p('Cada funció utilitza la capa de la seva iteració. El clic a Geologia modifica Geologia, mentre Ortofoto conserva el seu estat. El condicional només consulta visible; l’assignació és dins del gestor del clic.')
p('El mateix principi s’aplica al lliscador: vincular-lo a capaActual.opacitat permet controlar cada capa de manera independent.')

page(12,'Exemple integrat de referència')
p('Aquest exemple reuneix el que hem construït. Inclou el lliscador per fila, el següent pas de pràctica. Llegeix-lo de dalt a baix i identifica dades, consulta d’estat i modificació d’estat.')
code('''<script>
  const nomProjecte = 'GeoTrasteja';
  const capes = $state([
    { nom: 'Ortofoto', visible: true, opacitat: 100 },
    { nom: 'Geologia', visible: false, opacitat: 70 }
  ]);
</script>

<h1>{nomProjecte}</h1>

{#each capes as capaActual}
  <section>
    <h2>{capaActual.nom}</h2>

    {#if capaActual.visible}
      <p>Capa visible</p>
    {:else}
      <p>Capa oculta</p>
    {/if}

    <button onclick={() => {
      capaActual.visible = !capaActual.visible;
    }}>
      {#if capaActual.visible}
        Amaga
      {:else}
        Mostra
      {/if}
    </button>

    <p>Opacitat: {capaActual.opacitat}%</p>
    <label>
      Opacitat de {capaActual.nom}
      <input type="range" min="0" max="100" step="10"
        bind:value={capaActual.opacitat} />
    </label>
  </section>
{/each}''')
p('section agrupa el contingut de cada capa; h2 n’és el subtítol. label dona una etiqueta al control que conté. Són elements HTML de suport a l’exemple, no funcions noves de Svelte.')

page(13,'Llegir errors sense perdre el fil')
p('Un error no vol dir que tota la idea sigui incorrecta. Localitza el fragment concret i distingeix un error de sintaxi, de nom o de comportament.')
h('Expected token &gt;')
code('''<!-- Incorrecte: falta embolcallar el JavaScript -->
<button onclick= () => { opacitat = 100 }>

<!-- Correcte -->
<button onclick={() => { opacitat = 100; }}>
  Restablir
</button>''')
p('El parser intenta entendre l’etiqueta i troba símbols inesperats. Revisa les claus exteriors de l’atribut i el tancament de l’etiqueta. El lloc assenyalat pot ser posterior al símbol que falta.')
h('500 / Internal server error')
p('És una resposta d’error del servidor. No explica per si sola què falla. Llegeix el missatge de la terminal: fitxer, línia, columna i descripció. En aquesta pràctica vam trobar assignacions dins de condicionals de plantilla.')
h('La pantalla no reflecteix el canvi')
p('Comprova que has desat; que has declarat l’estat amb $state; i que el control i el text utilitzen la mateixa dada. Per exemple, capa.opacitat i opacitat són expressions diferents.')
h('Objecte i array confosos')
p('[...] és una llista. {...} amb parelles propietat: valor és un objecte. A ["Ortofoto", true, 100] els valors no tenen noms de propietat; no és l’objecte de capa que necessitem.')
h('Rutina de comprovació')
p('1. Desa el fitxer. 2. Llegeix el primer error concret. 3. Revisa noms i delimitadors. 4. Canvia una cosa cada vegada. 5. Prova el cas normal i els límits. Si demanes ajuda, comparteix el codi actual i l’error actual.')

page(14,'Situar els conceptes')
h('Svelte i React')
p('Tots dos permeten construir interfícies amb components, estat i propietats. A React és habitual declarar estat amb useState i modificar-lo amb la funció actualitzadora. A Svelte 5 hem declarat estat amb $state i l’hem modificat amb assignacions.')
p('React fa servir JSX i expressions JavaScript com map o &amp;&amp; per representar llistes i condicionals. Svelte ofereix blocs de plantilla com each i if. Svelte compila els components a codi d’actualització del DOM; React renderitza i reconcilia els resultats. Cap d’aquestes descripcions implica recarregar tota la pàgina amb cada clic.')
h('Svelte i SvelteKit')
p('<b>Svelte</b> aporta el model de components i la sintaxi reactiva. <b>SvelteKit</b> hi afegeix l’estructura d’aplicació: rutes, càrrega de dades i funcionalitats de servidor. Encara no hem programat una API en aquest projecte.')
p('Hem esmentat components amb propietats, estils locals, valors derivats i transicions com a funcionalitats que treballarem més endavant. No cal considerar-les practicades ni dominades encara.')
h('Petit diccionari')
for t in ['<b>Propietat:</b> dada amb nom dins d’un objecte. <b>Índex:</b> posició d’un element dins d’un array.', '<b>Esdeveniment:</b> acció com un clic. <b>Gestor:</b> funció que respon a l’esdeveniment.', '<b>Renderitzar:</b> generar o actualitzar la representació de la interfície. <b>Vincular:</b> connectar un control amb una dada.', '<b>CLI:</b> eina de línia d’ordres. <b>Script npm:</b> ordre definida al package.json. <b>Backend:</b> part que s’executa al servidor. <b>Frontend:</b> interfície i lògica del navegador.']:
    p(t)
h('Preguntes per repassar de memòria')
p('Quina diferència hi ha entre = i ===? Per què no cridem directament la funció a onclick? Què conté capes[1]? On va el if de JavaScript? Què actualitza bind:value? Per què const permet canviar una propietat?')
p('Material basat en el diàleg i en els exemples treballats. La prioritat és poder explicar cada línia i reconstruir-la, no copiar el fragment complet.')

page(15,'Accions sobre totes les capes')
p('Un control dins del bloc each actua sobre l’objecte de la seva fila. Un control global, fora del bloc, necessita recórrer l’array per modificar cada objecte.')
code('''<button onclick={() => {
  for (const capaActual of capes) {
    capaActual.visible = false;
  }
}}>Amagar totes les capes</button>

<button onclick={() => {
  for (const capaActual of capes) {
    capaActual.visible = true;
    capaActual.opacitat = 100;
  }
}}>Restablir totes</button>''')
p('El for...of recorre els elements. A cada volta, capaActual conté una de les capes. Aquesta variable és local al bucle: no és la mateixa variable que la del each, encara que es diguin igual.')
h('Per què capes.visible = false no ho fa?')
p('capes és un array, no un objecte capa. Assignar capes.visible afegiria una propietat a l’array, però no canviaria visible dels objectes que conté. Cal accedir a cada element i modificar-ne la propietat.')
h('Dues instruccions, un sol cos')
p('Dins del cos de la funció podem escriure diverses instruccions amb punt i coma. L’operador coma també pot avaluar diverses expressions, però separar les assignacions en instruccions és més clar. No necessitem &amp;&amp; per executar-les seguides.')
p('El botó Restablir de cada fila va dins del each i fora del if que amaga el lliscador: així continua disponible quan la capa està oculta. El botó Restablir totes va fora del each per no repetir-lo a cada fila.')

page(16,'Comptar sense modificar')
p('Una funció de consulta llegeix les dades i retorna un resultat. Per comptar, inicialitzem un acumulador numèric a zero, recorrem l’array i l’incrementem quan es compleix la condició.')
code('''function comptarCapesVisibles(capes) {
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
    if (capaActual.visible && capaActual.opacitat > 0) {
      i++;
    }
  }
  return i;
}''')
p('<b>i++</b> incrementa i en una unitat. let i; començaria amb undefined i no serviria per al recompte. El return va després del bucle perquè necessitem revisar totes les capes.')
code('''<p>Capes visibles: {comptarCapesVisibles(capes)}</p>
<p>Perceptibles: {comptarCapesPerceptibles(capes)}</p>''')
p('Les crides de la plantilla llegeixen estat reactiu a través de les funcions. El recompte es pot actualitzar quan canvia la visibilitat o, en el segon cas, l’opacitat. Les funcions no han de modificar l’estat mentre calculen el resultat.')
h('Visible i perceptible no són el mateix')
p('Amb Ortofoto visible a opacitat 0 i Geologia visible a 70: <b>2 visibles, 1 perceptible</b>. Si amaguem Geologia: <b>1 visible, 0 perceptibles</b>. Si després pugem Ortofoto a 30: <b>1 visible, 1 perceptible</b>. Aquí visible és la propietat d’activació del nostre model.')

page(17,'Construir un array de noms')
p('El patró del comptador també permet acumular dades en un array. Ara el resultat no serà un número, sinó una llista de textos.')
code('''function obtenirNomCapesPerceptibles(capes) {
  const capesVisibles = [];
  for (const capaActual of capes) {
    if (capaActual.visible && capaActual.opacitat > 0) {
      capesVisibles.push(capaActual.nom);
    }
  }
  return capesVisibles;
}''')
p('Conservem el nom de funció utilitzat al projecte; obtenirNomsCapesPerceptibles seria més precís perquè retorna diversos noms. capesVisibles conté textos, no objectes: nomsPerceptibles seria també un nom més descriptiu per a aquest array local.')
h('El destinatari de push')
p('<b>arrayDestinatari.push(valor)</b> afegeix el valor a l’array. capaActual.nom és un text i no és on hem de cridar push. const impedeix reassignar l’array, però permet afegir-hi elements.')
code('''{#each obtenirNomCapesPerceptibles(capes) as nomCapa}
  <p>Capa perceptible: {nomCapa}</p>
{:else}
  <p>No hi ha cap capa perceptible</p>
{/each}''')
p('La funció <b>retorna un array</b>; no es converteix en un array. each recorre aquest resultat. nomCapa rep cada text, no l’índex. No cal assignar-li valors manualment dins del bloc.')
p('Si retorna ["Ortofoto", "Geologia"], es creen dos paràgrafs. Si retorna [], s’executa la branca else del each. Aquesta branca correspon a una llista buida, no a una condició falsa de cada element.')

page(18,'Cercar i retornar un objecte')
code('''function buscarCapaNom(capes, nomBuscat) {
  for (const nomCerca of capes) {
    if (nomBuscat === nomCerca.nom) {
      return nomCerca;
    }
  }
  return null;
}''')
p('capes i nomBuscat són <b>paràmetres</b>. Quan cridem buscarCapaNom(capes, "Geologia"), passem arguments concrets. nomCerca conté un objecte capa, encara que el seu nom pugui fer pensar que és un text; capaActual seria més descriptiu.')
p('Comparem el text buscat amb la propietat nom. Comparar nomBuscat amb l’objecte complet no comprova el seu nom. nom i Nom són propietats diferents.')
h('Retorn anticipat')
p('return nomCerca acaba tota la funció en trobar una coincidència. return null va després del bucle. Si el poséssim a l’else de la primera comparació, buscar Geologia s’aturaria en veure que Ortofoto no coincideix. Sense un retorn final explícit, la funció retornaria undefined quan no troba res.')
code('''const capaTrobada = buscarCapaNom(capes, 'Geologia');
if (capaTrobada !== null) {
  console.log(capaTrobada.opacitat);
}''')
p('Retornem l’objecte complet, que ja inclou opacitat. No cal posar l’opacitat a zero ni retornar-la per separat. <b>return objecte, numero</b> utilitza l’operador coma i retorna només l’última expressió, no dos resultats.')
h('Identitat i abast')
p('L’objecte retornat és el mateix element que hi ha a l’array; no n’hem creat una còpia. nomCerca només existeix dins del bucle de la funció: la plantilla no pot utilitzar aquesta variable local. Ha d’utilitzar el resultat retornat.')

page(19,'Escriure i normalitzar textos')
code('''// Dins del script:
let nomBuscat = $state('');

<!-- A la plantilla: -->
<input type="text" bind:value={nomBuscat} />
<p>Estàs buscant: {nomBuscat}</p>''')
p('bind:value reassigna nomBuscat quan escrivim: per això el text reactiu necessita let. Amb const no podem reassignar-lo. És diferent de modificar una propietat d’un objecte declarat amb const.')
h('Dos mètodes de string')
code("'GEOLOGIA'.toLowerCase() // 'geologia'\n' Geologia '.trim()    // 'Geologia'\n' Geo logia '.trim()   // 'Geo logia'")
p('<b>toLowerCase()</b> retorna el text en minúscules. <b>trim()</b> elimina espais dels extrems, no els interiors. Cap dels dos modifica el string original. Els parèntesis executen el mètode: sense (), toLowerCase fa referència a la funció, no al resultat.')
code('''function buscarCapaNom(capes, nomBuscat) {
  for (const nomCerca of capes) {
    if (nomBuscat.toLowerCase().trim() ===
        nomCerca.nom.toLowerCase()) {
      return nomCerca;
    }
  }
  return null;
}''')
p('Convertim els dos costats a minúscules i netegem els extrems de l’entrada. Així " GEOLOGIA " troba Geologia. No elimina accents ni espais interiors; tampoc fa una cerca parcial.')
p('Per detectar una entrada buida o només amb espais, comprovem <b>nomBuscat.trim() === \'\'</b>. En canvi, \'\'.trim() continua sent buit i no neteja el que ha escrit l’usuari.')

page(20,'Mostrar el resultat de la cerca')
code('''<div>
  <p>Cerca:</p>
  <input type="text" bind:value={nomBuscat} />
  <p>Estàs buscant: {nomBuscat}</p>

  {#if nomBuscat.trim() === ''}
    <p>Escriu el nom d'una capa</p>
  {:else if buscarCapaNom(capes, nomBuscat) !== null}
    <p>Capa trobada</p>

    {#if buscarCapaNom(capes, nomBuscat).visible}
      <p>Capa visible</p>
    {:else}
      <p>Capa oculta</p>
    {/if}

    <p>Opacitat de la capa:
      {buscarCapaNom(capes, nomBuscat).opacitat}%
    </p>
  {:else}
    <p>No s'ha trobat cap capa</p>
  {/if}
</div>''')
p('L’ordre importa: primer tractem l’entrada buida, després una coincidència i, al final, l’absència de coincidències. else sempre va al final. Dins d’un else if no afegim unes altres claus al voltant de la variable.')
p('<b>!== null</b> comprova que hi ha un objecte. No comparem el resultat amb nomBuscat: un objecte no és el mateix que el text d’entrada. Accedim a les propietats només dins de la branca on la cerca ha trobat una capa.')
p('Quan cerquem Geologia i en modifiquem l’opacitat amb el lliscador, el resultat també canvia. La cerca llegeix les dades reactives actuals i retorna el mateix objecte de l’array.')
p('Aquesta versió repeteix la cerca en diverses expressions. És la versió treballada fins ara; el següent pas serà representar el resultat amb un valor derivat, sense repetir totes aquestes crides.')

page(21,'Repàs i punt de continuació')
h('Què hem incorporat des del primer quadern')
p('Accions globals amb for...of; comptadors; condicions amb &amp;&amp;; acumulació de noms amb push; each sobre el resultat d’una funció; else per a l’array buit; cerca amb retorn d’objecte o null; abast de variables; entrada de text amb bind; comparacions, normalització i condicionals imbricats.')
h('Comprova-ho abans de mirar la resposta')
p('1. Una capa visible amb opacitat 0: compta com a perceptible? 2. Què fa push i sobre quin valor es crida? 3. Per què return null no va a l’else del bucle de cerca? 4. Què retorna trim en un text amb espais interiors? 5. Per què nomCerca no està disponible a la plantilla? 6. Per què nomBuscat es declara amb let?')
h('Respostes breus')
p('1. No; sí que compta com a visible. 2. Afegeix un element al final de l’array destinatari. 3. Hem de revisar totes les capes abans de descartar la cerca. 4. Conserva els espais interiors. 5. Té abast local al bucle de la funció. 6. La vinculació reassigna el text amb cada entrada.')
h('Un petit recorregut de comprovació')
p('Cerca " GEOLOGIA "; canvia’n l’opacitat; amaga-la; deixa una altra capa activada amb opacitat 0; comprova els dos comptadors i la llista de noms; escriu un nom inexistent; buida l’entrada amb espais. Cada control ha de consultar i modificar les dades que li corresponen.')
h('Continuació en aquesta edició')
p('Les pàgines següents incorporen $derived i els mètodes find, filter i map, que ja hem introduït i practicat. Les funcions amb bucles de les pàgines anteriors es conserven per entendre la seva equivalència amb aquestes alternatives.')
p('Encara queden components i propietats, i dades asíncrones amb async/await i fetch. El canvi del each perquè recorri nomsPerceptibles és el punt exacte pendent de pràctica; la nova versió s’inclou al final com a referència.')

page(22,'Netejar abans de continuar')
p('Els exemples de cada etapa no s’han d’acumular indefinidament. Vam acabar amb un objecte capa independent, un array capes, controls duplicats i dues declaracions de capaTrobada. La neteja va deixar un únic array com a font de dades.')
h('Una font de dades, diversos resultats')
code("const nomProjecte = 'GeoTrasteja';\nconst capes = $state([\n  { nom: 'Ortofoto', visible: true, opacitat: 100 },\n  { nom: 'Geologia', visible: true, opacitat: 100 }\n]);\nlet nomBuscat = $state('');")
p('Les dues capes comencen ara visibles i amb opacitat 100. visible i opacitat continuen sent propietats independents. El total de capes es mostra amb capes.length, no amb un número fix.')
h('Declaracions que no podem duplicar')
p('No podem declarar let capaTrobada i const capaTrobada en el mateix àmbit. L’exemple antic de cerca fixa de Geologia es va eliminar en introduir el resultat derivat de la cerca de l’usuari.')
p('En substituir un fragment, cal conservar nomProjecte i capes al principi del script. Els valors derivats necessiten les dades originals. Si eliminem una funció, també hem d’eliminar o substituir totes les crides que encara la utilitzen.')
h('Noms coherents amb la plantilla')
p('Si la plantilla consulta capaTrobada, guardar el resultat amb el nom capa no la connecta automàticament. Si mostra capesVisibles.length, hem de declarar capesVisibles. Els noms han de coincidir exactament.')
p('Quan un resultat ja es calcula amb find o filter i no queden crides a la funció anterior, podem retirar la funció antiga. Els bucles continuen sent útils per entendre i explicar el procés.')

page(23,'$derived: un resultat que depèn de dades')
p('<b>$state</b> declara les dades reactives que modifiquem. <b>$derived</b> expressa un càlcul a partir de dades reactives i manté el resultat coherent amb les dependències que consulta.')
code('''let nomBuscat = $state('');
let capaTrobada = $derived(buscarCapaNom(capes, nomBuscat));''')
p('La cerca continua sent una funció. $derived en utilitza el resultat: un objecte capa o null en aquesta versió amb buscarCapaNom. Si escrivim Geologia, el resultat és el seu objecte; si escrivim Ortofoto, passa a ser l’objecte d’Ortofoto.')
h('Per què una assignació ordinària no és equivalent?')
code('''// Càlcul executat en inicialitzar aquesta variable:
let resultat = buscarCapaNom(capes, nomBuscat);

// Resultat derivat de les dades reactives consultades:
let resultatReactiu = $derived(buscarCapaNom(capes, nomBuscat));''')
p('Svelte segueix les lectures reactives síncrones durant el càlcul, també dins de les funcions cridades. Quan una dependència canvia, invalida el resultat i el recalcula quan es torna a consultar. No vol dir que es recalculi per qualsevol canvi de tota l’aplicació.')
h('Consultar el resultat pel seu nom')
code('''{:else if capaTrobada !== null}
  <p>{capaTrobada.nom}</p>
  <p>Opacitat: {capaTrobada.opacitat}%</p>''')
p('Evitem repetir la cerca en cada expressió. El símbol % és text de la plantilla: no canvia el número de la propietat. Podem aplicar el mateix patró a un recompte amb $derived(comptarCapesVisibles(capes)).')
p('El càlcul derivat ha de consultar dades sense modificar estat. En aquesta pràctica el tractem com un resultat calculat; les accions de l’usuari modifiquen les dades originals amb $state.')

page(24,'find: trobar un element')
p('<b>find()</b> recorre l’array i retorna el primer element per al qual la funció de comprovació dona un valor cert. Si no el troba, retorna <b>undefined</b>.')
code("const capa = capes.find(\n  capaActual => capaActual.nom === 'Geologia'\n);")
p('capaActual és un paràmetre que rep un objecte cada vegada. Posar-li el nom nom no faria que rebés un text: el contingut depèn dels elements de l’array. Per obtenir-ne el text del nom, accedim a .nom.')
h('Funció de comprovació')
code("capaActual => capaActual.nom === 'Geologia'")
p('La funció fletxa retorna directament el booleà de la comparació. No cal if. Si afegim claus al cos i volem aquest resultat, hem d’escriure return: amb el cos d’expressió el retorn és implícit.')
code('''let capaTrobada = $derived(
  capes.find(capaActual =>
    capaActual.nom.toLowerCase() ===
    nomBuscat.toLowerCase().trim()
  )
);''')
p('Aquesta declaració substitueix el derived que cridava buscarCapaNom. No l’afegim com una segona declaració amb el mateix nom. Conserva el comportament de cerca exacta, ignorant majúscules i espais als extrems de l’entrada.')
h('Canvia el cas de resultat absent')
p('La nostra funció retornava null; find retorna undefined. Per això la plantilla ha de comprovar <b>capaTrobada !== undefined</b>. undefined és el nom exacte, no undefinied. El resultat trobat és l’objecte complet, no només el nom.')

page(25,'filter: seleccionar diversos elements')
p('<b>filter()</b> crea un nou array amb tots els elements que compleixen la comprovació. Si no n’hi ha cap, retorna <b>[]</b>. No retorna undefined ni un recompte.')
code('''let capesVisibles = $derived(
  capes.filter(capaActual => capaActual.visible)
);

let capesPerceptibles = $derived(
  capes.filter(capaActual =>
    capaActual.visible && capaActual.opacitat > 0
  )
);''')
p('capaActual.visible i capaActual.visible === true són equivalents per als booleans del nostre model. La condició de perceptibilitat exigeix les dues propietats amb &amp;&amp;. El plural del nom recorda que el resultat és una llista.')
h('Comptar el resultat')
code('''<p>Capes visibles: {capesVisibles.length}</p>
<p>Capes perceptibles: {capesPerceptibles.length}</p>''')
p('length és la quantitat d’elements de l’array. Mostrar {capesVisibles} no és el mateix que mostrar-ne la longitud. CapesVisibles amb majúscula inicial seria una altra variable.')
h('Dos errors que hem corregit')
p('<b>capes.filter(capaActual =&gt; capes.visible)</b> consulta l’array, no l’objecte actual. La propietat s’ha de llegir des de capaActual. <b>... =&gt; if (...)</b> no és una expressió vàlida: podem retornar directament la condició.')
p('filter no modifica l’array original: crea un nou array que conté referències als objectes seleccionats. No fa còpies independents de cada capa. $derived en manté la selecció actualitzada quan canvien les dades que consulta.')

page(26,'map: transformar cada element')
p('<b>map()</b> crea un nou array amb el resultat de transformar cada element. En el nostre cas, transformem objectes capa en textos amb els seus noms.')
code('''let nomsPerceptibles = $derived(
  capesPerceptibles.map(capaActual => capaActual.nom)
);''')
p('capesPerceptibles ja conté només els objectes perceptibles. map retorna la propietat nom de cadascun: per exemple, ["Ortofoto", "Geologia"]. El resultat té un element per cada element de l’array d’entrada.')
h('No cal push ni un comptador')
p('En la funció anterior creàvem un array buit i hi fèiem push dins del bucle. map ja crea l’array de resultats. La funció fletxa decideix quin valor hi va a cada posició; aquí és capaActual.nom.')
code('''// Expressió de transformació:
capesPerceptibles.map(capaActual => capaActual.nom)

// Guardar un resultat calculat una vegada:
const noms = capesPerceptibles.map(capaActual => capaActual.nom);''')
p('No escrivim const capesPerceptibles.map(...): const necessita un nom de variable i una assignació. Per mantenir aquesta transformació reactiva al component, fem servir la declaració amb $derived de dalt.')
h('Canvi de la plantilla: següent exercici pendent')
code('''{#each nomsPerceptibles as nomCapa}
  <p>Capa perceptible: {nomCapa}</p>
{:else}
  <p>No hi ha cap capa perceptible</p>
{/each}''')
p('Aquesta és la substitució de referència del bloc que encara cridava obtenirNomCapesPerceptibles(capes). El punt pendent de pràctica és fer aquest canvi, provar-lo i retirar la funció antiga si ja no s’utilitza.')

page(27,'Les dades i els resultats, junts')
p('Aquesta és la nova base de referència del script. Conserva les dades originals i declara els resultats una sola vegada. La funció de noms anterior deixa de ser necessària quan la plantilla ja utilitza nomsPerceptibles.')
code('''<script>
  const nomProjecte = 'GeoTrasteja';
  const capes = $state([
    { nom: 'Ortofoto', visible: true, opacitat: 100 },
    { nom: 'Geologia', visible: true, opacitat: 100 }
  ]);

  let nomBuscat = $state('');

  let capaTrobada = $derived(
    capes.find(capaActual =>
      capaActual.nom.toLowerCase() ===
      nomBuscat.toLowerCase().trim()
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

  let nomsPerceptibles = $derived(
    capesPerceptibles.map(capaActual => capaActual.nom)
  );
</script>''')
p('<b>Cadena de dependències:</b> capes alimenta el filtre; capesPerceptibles alimenta map; nomsPerceptibles alimenta each. Els controls continuen modificant les propietats dels objectes de capes, com abans.')

page(28,'La plantilla amb els resultats derivats')
p('Fragments de referència del resum i del cercador. Els botons globals, els controls per capa i els lliscadors es mantenen com ja els havíem construït; no cal reescriure’ls per utilitzar aquests resultats.')
code('''<h2>Resum</h2>
<p>Total de capes: {capes.length}</p>
<p>Capes visibles: {capesVisibles.length}</p>
<p>Capes perceptibles: {capesPerceptibles.length}</p>

{#each nomsPerceptibles as nomCapa}
  <p>Capa perceptible: {nomCapa}</p>
{:else}
  <p>No hi ha cap capa perceptible</p>
{/each}

<h2>Cercador de capes</h2>
<label>
  Nom de la capa:
  <input type="text" bind:value={nomBuscat} />
</label>

{#if nomBuscat.trim() === ''}
  <p>Escriu el nom d'una capa</p>
{:else if capaTrobada !== undefined}
  <p>Capa trobada: {capaTrobada.nom}</p>
  {#if capaTrobada.visible}
    <p>Capa visible</p>
  {:else}
    <p>Capa oculta</p>
  {/if}
  <p>Opacitat: {capaTrobada.opacitat}%</p>
{:else}
  <p>No s'ha trobat cap capa</p>
{/if}''')
p('El if protegeix l’accés a les propietats quan find no ha trobat cap objecte. Aquests fragments corresponen a la versió amb find: no s’hi ha de conservar la comprovació antiga de null.')

page(29,'Triar el mètode i explicar el resultat')
h('Quina pregunta vols respondre?')
p('<b>find:</b> quin és el primer element que compleix això? Retorna un element o undefined. <b>filter:</b> quins elements ho compleixen? Retorna un array amb zero o més elements. <b>map:</b> en què vull transformar cada element? Retorna un array de resultats de la mateixa longitud.')
p('La funció que passem a un mètode s’anomena també callback: el mètode la crida per als elements. No és un tipus nou de funció; aquí la definim amb una funció fletxa.')
h('Exercicis mentals amb dues capes')
p('1. Ortofoto visible a 0 i Geologia visible a 100: quina longitud tenen els dos filtres? 2. Quin resultat produeix map sobre les perceptibles? 3. Què dona find si busquem Relleu? 4. Si amaguem totes, què mostra el each dels noms? 5. Quina diferència hi ha entre capaTrobada i capaTrobada.nom?')
h('Respostes')
p('1. capesVisibles.length és 2 i capesPerceptibles.length és 1. 2. ["Geologia"]. 3. undefined. 4. El missatge alternatiu perquè l’array és buit. 5. El primer és un objecte o undefined; la propietat nom, quan existeix la capa, és un text.')
h('Comprovar la migració')
p('Conserva nomProjecte i capes. Declara cada resultat una vegada. Fes coincidir els noms del script i la plantilla. Amb find comprova undefined. No retiris una funció mentre encara hi hagi crides. Prova entrada buida, nom inexistent, majúscules, espais i canvis de visibilitat i opacitat.')
h('On reprendrem la pràctica')
p('En aquesta edició ja hem continuat: el resum és un component amb propietats i les dades es carreguen des d’un JSON amb validació i gestió d’errors. Les pàgines següents incorporen aquest treball i indiquen el nou punt de continuació.')

page(30,'Com s’organitza GeoTrasteja')
p('La pàgina té una font principal de dades: capes. Els botons i lliscadors en modifiquen els objectes. Els valors derivats consulten aquest estat i la plantilla en mostra els resultats.')
code('''capes: array d’objectes de les capes
  -> capesVisibles: array d’objectes filtrats
  -> capesPerceptibles: array d’objectes filtrats
       -> nomsPerceptibles: array de textos

nomBuscat + capes -> capaTrobada: objecte o undefined''')
p('capaActual és un nom temporal dins de cada bucle o callback, no una variable global que emmagatzemi totes les capes. Al each de capes representa un objecte; al each de nomsPerceptibles, nomCapa representa un text.')
h('Fitxers amb responsabilitats diferents')
p('<b>src/routes/+page.svelte:</b> estat, càrrega, validació, resultats derivats i controls. <b>src/lib/components/ResumCapes.svelte:</b> mostra els recomptes i els noms que rep. <b>static/capes.json:</b> dades inicials servides com a recurs estàtic.')
p('Els controls de pantalla modifiquen l’estat en memòria, no el fitxer JSON. Tornar a carregar correctament el fitxer substitueix capes pels seus valors, i pot restablir canvis fets amb els controls.')
h('Condicions del resum')
code('''{#if totalCapes > 0 && totalPerceptibles === totalCapes}
  <p>Totes les capes són perceptibles</p>
{/if}

{#if totalVisibles < totalCapes}
  <p>Hi ha capes amagades</p>
{/if}''')
p('Amb 3 visibles i 2 perceptibles no hi ha necessàriament cap capa amagada: una pot tenir opacitat 0. Per dir que totes són perceptibles, exigim també que existeixi almenys una capa, perquè 0 === 0 és cert.')

page(31,'Components, imports i propietats')
p('Un component separat no accedeix automàticament a les variables de la pàgina. Les <b>props</b> són dades d’entrada que li passa el component pare. totalCapes és un nom escollit per nosaltres, no una paraula especial de Svelte.')
code('''// Dins del script de +page.svelte:
import ResumCapes from '#lib/components/ResumCapes.svelte';

<!-- A la plantilla de la pàgina: -->
<ResumCapes
  totalCapes={capes.length}
  totalVisibles={capesVisibles.length}
  totalPerceptibles={capesPerceptibles.length}
  {nomsPerceptibles}
/>''')
p('El projecte ha indicat que el seu àlies és <b>#lib</b>, que apunta a src/lib. L’exemple anterior amb $lib no funcionava en aquest entorn; fem servir l’àlies que ha indicat el compilador. Una ruta relativa des de routes seria ../lib/components/ResumCapes.svelte.')
p('import dona un nom al component importat i &lt;ResumCapes /&gt; el mostra en aquell punt. {nomsPerceptibles} és una abreviatura de nomsPerceptibles={nomsPerceptibles}.')
h('Rebre les props en el component')
code('''<script>
  let {
    totalCapes,
    totalVisibles,
    totalPerceptibles,
    nomsPerceptibles
  } = $props();
</script>''')
p('$props() rep les dades d’entrada; les claus extreuen les propietats pel seu nom. Es fa una sola crida a $props() per component. Els noms han de coincidir amb els de la crida: totalVisibbles no és totalVisibles.')
p('Els tres totals són números: la pàgina ja ha calculat .length. nomsPerceptibles és un array de textos. No fem totalCapes.length, perquè el total no és un array.')

page(32,'El component de resum complet')
code('''<script>
  let {
    totalCapes, totalVisibles,
    totalPerceptibles, nomsPerceptibles
  } = $props();
</script>

<h2>Resum de les capes</h2>

{#if totalCapes > 0 && totalPerceptibles === totalCapes}
  <p>Totes les capes són perceptibles</p>
{/if}

<p>Total de capes: {totalCapes}</p>
<p>Total de capes visibles: {totalVisibles}</p>
<p>Total de capes perceptibles: {totalPerceptibles}</p>

{#each nomsPerceptibles as nomCapa}
  <p>Capa perceptible: {nomCapa}</p>
{:else}
  <p>No hi ha cap capa perceptible</p>
{/each}

{#if totalVisibles < totalCapes}
  <p>Hi ha capes amagades</p>
{/if}''')
p('El resum rep resultats ja calculats, no l’array complet de capes. Si afegim Relleu a les dades, la pàgina recalcula i el component rep els nous valors sense haver-ne de canviar el codi.')
p('Vam retirar els paràgrafs i la llista duplicats de la pàgina quan els vam traslladar al component. Cal moure, no copiar indefinidament. El each ara recorre nomsPerceptibles, no crida l’antiga funció que rebia capes.')
p('Amb Ortofoto, Geologia i Relleu visibles a 100 hi ha 3 visibles i 3 perceptibles. Si posem Relleu a 0, continuen sent 3 visibles però passen a 2 perceptibles.')

page(33,'JSON: dades, sense declaracions')
p('<b>JSON</b> és un format de text per representar dades. No hi escrivim const, let, funcions ni $state. Els noms de propietats i els strings utilitzen cometes dobles; números i booleans, no.')
code('''[
  {
    "nom": "Ortofoto",
    "visible": true,
    "opacitat": 100
  },
  {
    "nom": "Geologia",
    "visible": true,
    "opacitat": 100
  },
  {
    "nom": "Relleu",
    "visible": true,
    "opacitat": 100
  }
]''')
p('Les claus agrupen cada objecte. Les comes separen propietats i objectes; no posem una coma després de l’últim element. Els dos punts van fora de les cometes: "nom": "Ortofoto".')
p('Desem aquest text a <b>static/capes.json</b>. Amb el servidor local, es consulta a <b>/capes.json</b>, sense /static. La carpeta static no forma part del camí públic: el seu contingut es serveix des de l’arrel de l’aplicació.')
p('Veure aquest recurs al navegador comprova que existeix i és accessible. Encara no significa que l’estat capes del component l’hagi llegit: això ho programem amb fetch.')

page(34,'HTTP, endpoint i API')
p('El navegador és un client que fa una petició HTTP al servidor. <b>GET</b> és el mètode habitual per demanar un recurs. La resposta conté un estat, capçaleres i un cos amb el contingut.')
p('Un <b>endpoint</b> és un punt concret on el client pot fer una petició. Una <b>API</b> defineix la interfície de comunicació: operacions disponibles, entrades i respostes. Pot tenir un endpoint o diversos.')
h('El nostre recurs és estàtic')
p('GET /capes.json és un punt d’accés a dades, però en aquesta pràctica en diem recurs estàtic: el servidor retorna el fitxer que hem desat. Encara no hem escrit una funció de servidor pròpia per preparar la resposta.')
p('Un futur GET /api/capes podria executar codi de servidor que llegeixi dades, filtri o retorni errors. Tots dos recursos podrien retornar el mateix JSON. /api és una convenció del camí, no el que crea una API.')
h('Resposta i contingut no són el mateix')
code('''const resposta = await fetch('/capes.json');
const dades = await resposta.json();''')
p('<b>resposta</b> és l’objecte HTTP retornat per fetch. <b>dades</b> és el resultat d’interpretar el cos com a JSON; en el nostre fitxer és un array d’objectes. La constant dades no conté una funció: conté el resultat de cridar .json().')
p('L’extensió .json de l’adreça no converteix automàticament el contingut en dades JavaScript. resposta.json() no demana al servidor que canviï el format; llegeix i interpreta la resposta rebuda. resposta.text() la llegiria com a text i resposta.blob() com a dades de tipus Blob.')
p('json() retorna l’estructura que hi hagi al document: també podria ser un objecte, un número o null. Per això més endavant validem que sigui un array de capes.')

page(35,'async, await i la primera prova')
code('''async function provarCarregaCapes() {
  const resposta = await fetch('/capes.json');
  const dades = await resposta.json();
  console.log(dades);
}

<!-- A la plantilla: -->
<button onclick={provarCarregaCapes}>Provar càrrega</button>''')
p('<b>async</b> permet utilitzar await en aquesta funció i fa que la funció retorni una promesa. Una <b>promesa</b> representa un resultat que pot arribar més endavant o fallar. <b>await</b> espera aquest resultat dins de la funció sense bloquejar tota la interfície.')
p('El primer await espera la resposta HTTP. El segon espera la lectura i interpretació del cos. Són dos passos i produeixen dos valors diferents; separar-los ens permet revisar l’estat HTTP abans de llegir el JSON.')
h('Veure el resultat al navegador')
p('console.log(dades) apareix a la pestanya Console de les eines de desenvolupament del navegador quan cliquem el botó. Un resultat com (3) [{...}, {...}, {...}] es pot desplegar. Els avisos d’altres scripts no són necessàriament la sortida de la nostra funció.')
h('Connectar-lo als controls')
code('''// Estat inicial, fora de la funció:
let capes = $state([]);

// Després de llegir i validar les dades:
capes = dades;''')
p('Fem servir let perquè reassignem l’array complet. La primera versió amb const permetia modificar propietats però no substituir capes. No declarem capes dues vegades: substituïm la declaració antiga.')
p('La constant local dades guarda el resultat de la lectura. L’assignació capes = dades connecta aquest resultat amb l’estat que utilitzen els controls, els derived i el component. Llegim l’assignació de dreta a esquerra.')

page(36,'Errors HTTP i excepcions')
code('''const resposta = await fetch('/capes.json');

if (!resposta.ok) {
  missatgeError = 'No s’han pogut carregar les capes';
  console.error('Error HTTP:', resposta.status);
  return;
}''')
p('fetch no rebutja automàticament una resposta 404. resposta.ok indica si l’estat és dins del rang d’èxit 200-299. resposta.status dona el codi. ! nega el booleà; return acaba la funció abans de llegir el cos com a JSON.')
h('try, catch i finally')
code('''try {
  // Petició, comprovacions i lectura.
} catch (error) {
  // Error de xarxa o interpretació del JSON.
} finally {
  // Finalització tant en cas d’èxit com d’error.
}''')
p('Si la xarxa falla, fetch pot rebutjar la promesa. Si arriba una resposta correcta però el JSON està mal format, és resposta.json() el que falla. Tots dos errors arriben al catch d’aquesta funció.')
p('Un return dins del try també passa pel finally abans de sortir. Això permet posar carregant = false en un sol lloc, inclosos els errors HTTP i els retorns de validació. Aquesta explicació es refereix al flux normal de la funció, no a tancar el navegador a mitja execució.')
p('console.error mostra informació a la consola per al desenvolupador. missatgeError guarda un text reactiu que podem mostrar a l’usuari. Són dues responsabilitats diferents.')

page(37,'Estats de càrrega i error')
code('''let capes = $state([]);
let carregant = $state(false);
let missatgeError = $state('');
let dadesCarregades = $state(false);''')
p('<b>carregant:</b> hi ha una petició en curs. <b>missatgeError:</b> text de l’últim error d’aquest intent. <b>dadesCarregades:</b> hi ha hagut almenys una càrrega correcta en aquesta instància de la pàgina. <b>capes:</b> última llista acceptada.')
code('''<button onclick={provarCarregaCapes} disabled={carregant}>
  Provar càrrega
</button>

{#if carregant}
  <p>Carregant capes...</p>
{/if}

{#if missatgeError !== ''}
  <p>{missatgeError}</p>
{/if}''')
p('disabled rep un booleà: desactiva el botó durant la càrrega. Al principi de la funció posem carregant a true i buidem missatgeError per netejar un error anterior. El finally torna carregant a false.')
p('Un fitxer local pot carregar molt ràpid; el missatge pot durar tan poc que no el percebem. Cal distingir el comportament de l’estat del temps que triga la petició.')
p('No reiniciem dadesCarregades al principi de cada intent: recorda si ja tenim una càrrega correcta. Si una recàrrega falla, conservem les dades acceptades anteriorment i mostrem el nou error.')

page(38,'Validar la forma de les dades')
p('Interpretar JSON i validar dades són passos diferents. Un document pot ser JSON vàlid i, tot i així, no tenir l’estructura que necessita el nostre programa.')
code('''const dades = await resposta.json();

if (!Array.isArray(dades)) {
  missatgeError = 'Les dades rebudes no són una llista de capes';
  return;
}''')
p('<b>Array.isArray(dades)</b> retorna un booleà. És una comprovació de JavaScript, no un mètode de resposta. Un objecte aïllat amb nom, visible i opacitat es rebutja aquí perquè esperem una llista.')
h('Protegir cada entrada abans de consultar propietats')
code('''for (const capaActual of dades) {
  if (
    capaActual === null ||
    typeof capaActual !== 'object' ||
    Array.isArray(capaActual)
  ) {
    missatgeError = 'Una entrada no és un objecte capa';
    return;
  }
  // Després comprovem les seves propietats.
}''')
p('typeof s’escriu davant del valor, no com una propietat .typeof. Rebutgem null perquè no podem accedir a null.nom; typeof null dona object, de manera que necessita la comprovació explícita. Els arrays també tenen typeof object, per això els descartem amb Array.isArray.')
p('|| expressa que n’hi ha prou amb una causa d’invalidesa. L’ordre de validació protegeix els accessos següents i ens permet mostrar un missatge concret, en lloc de caure en un error genèric de lectura.')

page(39,'Validar propietats, tipus i rangs')
code('''if (typeof capaActual.nom !== 'string') {
  missatgeError = 'Una capa no té un nom de text';
  return;
} else if (capaActual.nom.trim() === '') {
  missatgeError = 'El nom conté un text buit';
  return;
} else if (typeof capaActual.visible !== 'boolean') {
  missatgeError = 'La visibilitat no és un booleà';
  return;
} else if (typeof capaActual.opacitat !== 'number') {
  missatgeError = 'L’opacitat no és un número';
  return;
} else if (capaActual.opacitat > 100 || capaActual.opacitat < 0) {
  missatgeError = 'L’opacitat ha d’estar entre 0 i 100';
  return;
}''')
p('Primer exigim que el nom sigui string; només després podem fer trim. Un nom amb espais és text, però el rebutgem si queda buit en retallar els extrems. La comprovació no reescriu ni normalitza el nom desat.')
p('"true" és text; true és booleà. "100" és text; 100 és número. El tipus correcte encara no garanteix el rang correcte: 120 és un número, però queda fora de 0 a 100. Els extrems 0 i 100 estan permesos.')
h('Acceptar la llista sencera')
p('capes = dades va després de totes les validacions i fora del bucle. Si una capa és incorrecta, return acaba tota la càrrega i capes conserva el valor anterior. No acceptem la primera capa i després rebutgem només la segona: la substitució és conjunta.')
p('És una validació bàsica per al nostre fitxer: no és un esquema universal. Per exemple, encara no comprovem noms duplicats ni totes les particularitats dels números en altres orígens de dades.')

page(40,'Càrrega integrada: primera part')
p('Referència completa en dues pàgines. Les declaracions d’estat de la pàgina 37 van fora de la funció. El bucle d’aquesta pàgina continua amb les comprovacions de propietats de la pàgina següent.')
code('''async function provarCarregaCapes() {
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
      if (
        capaActual === null ||
        typeof capaActual !== 'object' ||
        Array.isArray(capaActual)
      ) {
        missatgeError = 'Una entrada no és un objecte capa';
        return;
      }

      // Continua amb les validacions de la pàgina següent.''')
p('Les claus obertes continuen expressament a la pàgina 41. No enganxis aquesta primera meitat tota sola com si fos una funció completa.')

page(41,'Càrrega integrada: continuació')
code('''      if (typeof capaActual.nom !== 'string') {
        missatgeError = 'Una capa no té un nom de text';
        return;
      } else if (capaActual.nom.trim() === '') {
        missatgeError = 'El nom conté un text buit';
        return;
      } else if (typeof capaActual.visible !== 'boolean') {
        missatgeError = 'La visibilitat no és un booleà';
        return;
      } else if (typeof capaActual.opacitat !== 'number') {
        missatgeError = 'L’opacitat no és un número';
        return;
      } else if (
        capaActual.opacitat > 100 || capaActual.opacitat < 0
      ) {
        missatgeError = 'L’opacitat ha d’estar entre 0 i 100';
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
}''')
p('dadesCarregades = true és imprescindible: assignar dades a capes no modifica automàticament aquest altre booleà. Vam detectar aquest oblit perquè el missatge inicial continuava apareixent després de carregar correctament.')
p('Si dades és [], el bucle no fa cap volta i la llista es considera vàlida. S’assigna l’array buit i es registra una càrrega correcta, cosa diferent de no haver carregat mai.')

page(42,'Mai carregat o llista buida?')
code('''<button onclick={provarCarregaCapes} disabled={carregant}>
  Provar càrrega
</button>

{#if !dadesCarregades && !carregant}
  <p>Encara no s’han carregat les dades</p>
{:else if dadesCarregades && capes.length === 0}
  <p>La llista carregada és buida</p>
{/if}

{#if carregant}
  <p>Carregant capes...</p>
{/if}

{#if missatgeError !== ''}
  <p>{missatgeError}</p>
{/if}''')
p('Amb capes = [] tot sol no sabem si falta carregar o si el resultat vàlid és buit. dadesCarregades aporta aquesta informació. Abans del primer èxit és false; després d’un èxit és true, encara que la llista no tingui elements.')
p('Aquesta és la versió treballada. Els blocs són independents: abans del primer èxit pot aparèixer el missatge inicial juntament amb un error. Si ja hi havia una llista buida acceptada i recarreguem, el text de llista buida pot coexistir amb Carregant. La llista continua sent l’últim resultat correcte.')
p('El resum rep recomptes zero quan l’array és buit i mostra que no hi ha capes perceptibles. La condició totalCapes > 0 evita afirmar que totes són perceptibles abans de tenir capes.')

page(43,'Proves i repàs per aquesta nit')
h('Casos que hem comprovat')
p('<b>Fitxer correcte:</b> carrega tres capes i actualitza controls i resum. <b>Ruta inexistent:</b> resposta 404, missatge HTTP i botó actiu al final. <b>JSON mal format:</b> error de lectura al catch. <b>Objecte en lloc d’array:</b> missatge de llista incorrecta.')
p('<b>Nom numèric o buit:</b> rebutjat. <b>visible com a text:</b> rebutjat. <b>Opacitat fora del rang:</b> rebutjada. <b>Entrada null:</b> rebutjada abans d’accedir a propietats. <b>[]:</b> càrrega correcta amb llista buida. Després de cada prova recuperem les dades vàlides.')
h('Explica el recorregut sense mirar el codi')
p('Clic -> carregant true i error buit -> fetch -> estat HTTP -> lectura JSON -> validació d’array -> validació de cada capa -> assignació a capes -> dadesCarregades true -> finally -> carregant false. Si es produeix una excepció dins del try, catch prepara el missatge abans del finally.')
h('Sis preguntes de repàs')
p('1. Què rep ResumCapes? 2. Què diferencia resposta de dades? 3. Un 404 entra automàticament al catch? 4. S’executa finally després d’un return dins del try? 5. Per què typeof precedeix trim? 6. Què passa si la segona capa és invàlida?')
h('Respostes breus')
p('1. Tres números i un array de noms. 2. L’objecte HTTP i el contingut interpretat. 3. No; revisem resposta.ok. 4. Sí. 5. Hem de comprovar que el valor és text abans de cridar un mètode de text. 6. Retornem abans d’assignar i conservem capes anterior.')
h('Punt exacte de continuació')
p('La càrrega, la validació i els missatges han funcionat en les proves. Queda l’exercici curt al resum: mostrar quantes capes estan amagades amb les propietats que ja rep el component, sense cap funció ni prop nova. Després continuarem la preparació del mapa. Encara no hem connectat MapLibre ni programat un endpoint propi en GeoTrasteja.')

def footer(canvas, doc):
    canvas.setStrokeColor(colors.HexColor('#b8d1d7'))
    canvas.line(42,43,553,43)
    canvas.setFont('Body',8)
    canvas.setFillColor(colors.HexColor('#46616b'))
    canvas.drawString(42,29,'GeoTrasteja · Guia de repàs · Actualitzat el 07/11/2026')
    canvas.drawRightString(553,29,str(doc.page))
doc=SimpleDocTemplate(str(OUT),pagesize=(595.28,841.89),rightMargin=42,leftMargin=42,topMargin=38,bottomMargin=57,title='GeoTrasteja - Guia de repàs de JavaScript i Svelte',author='Material personal de repàs per a Enric Miralles')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)
