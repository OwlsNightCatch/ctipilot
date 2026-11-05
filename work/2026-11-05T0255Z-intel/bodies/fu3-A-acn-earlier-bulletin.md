---
title: Misure urgenti di verifica e mitigazione per operatori della distribuzione alimentare e della filiera del freddo
url: https://www.acn.gov.it/portale/w/misure-urgenti-di-verifica-e-mitigazione-per-operatori-della-distribuzione-alimentare-e-della-filiera-del-freddo
hostname: acn.gov.it
description: L’Agenzia per la Cybersicurezza Nazionale richiama l’attenzione delle organizzazioni operanti nei settori della grande distribuzione organizzata (GDO), della logistica alimentare, della refrigerazione industriale e dei servizi di manutenzione connessi, alla luce del recente incidente informatico che ha colpito numerose catene di supermercati francesi.
sitename: ACN
date: "2026-10-13"
fingerprint: efb9f419e70905b1
---
## Misure urgenti di verifica e mitigazione per operatori della distribuzione alimentare e della filiera del freddo

**Bollettino**

BL01/261013/CSIRT-ITA

## Sintesi

L’Agenzia per la Cybersicurezza Nazionale richiama l’attenzione delle organizzazioni operanti nei settori della grande distribuzione organizzata (GDO), della logistica alimentare, della refrigerazione industriale e dei servizi di manutenzione connessi, alla luce del recente incidente informatico che ha colpito numerose catene di supermercati francesi.

Tramite lo sfruttamento di installazioni obsolete, interfacce di amministrazione esposte direttamente su Internet e carenze nei meccanismi di autenticazione, l’attacco ha consentito l’attivazione remota dei cicli di sbrinamento e la modifica dei parametri operativi degli impianti, causando l’interruzione della catena del freddo e ingenti danni economici.

## Descrizione e potenziali impatti

La gestione della filiera del freddo dipende dall’interazione tra infrastrutture informatiche aziendali, apparati di regolazione e piattaforme di supervisione. Le verifiche devono considerare sia la sicurezza dei singoli componenti sia i collegamenti attraverso i quali utenti, applicazioni e manutentori possono accedere alle funzioni di controllo degli impianti.

### Sistemi IT — Information Technology

I sistemi IT comprendono le risorse dedicate all’elaborazione, alla conservazione e allo scambio delle informazioni, quali postazioni di lavoro, server, servizi di identità e applicativi gestionali e logistici. La compromissione di queste risorse può comportare accessi non autorizzati ai dati e interruzioni dei servizi aziendali. In presenza di collegamenti non adeguatamente segregati, un sistema IT compromesso può inoltre costituire un punto di accesso agli ambienti di controllo degli impianti. Le relative funzionalità amministrative devono pertanto essere raggiungibili attraverso opportune reti di amministrazione e gestione, separate dalle reti utilizzate per le ordinarie attività degli utenti.

### Sistemi OT — Operational Technology

I sistemi OT comprendono hardware e software che monitorano o controllano processi fisici. Nella filiera del freddo vi rientrano controllori della refrigerazione, sensori, attuatori e sistemi che regolano temperature, compressori e cicli di sbrinamento. La loro compromissione può incidere direttamente sul funzionamento degli impianti e sulle condizioni di conservazione delle merci. La protezione deve tenere conto dei requisiti di sicurezza e continuità operativa, prevedendo la segregazione dalle reti IT, la limitazione delle comunicazioni e il controllo degli accessi tecnici e di manutenzione.

### Sistemi SCADA — Supervisory Control and Data Acquisition

I sistemi SCADA rientrano nell’ambito OT e svolgono funzioni di supervisione, acquisizione dei dati e controllo dei processi, anche distribuiti su più impianti. Consentono, in funzione della configurazione, di visualizzare temperature e allarmi, modificare parametri e inviare comandi. La compromissione di una piattaforma centralizzata può quindi produrre effetti su più apparecchiature o siti. I sistemi SCADA devono essere collocati in segmenti di rete protetti, consentendo esclusivamente le comunicazioni necessarie con controllori, postazioni degli operatori e sistemi autorizzati. Non tutti gli impianti di refrigerazione dispongono di uno SCADA: le verifiche devono includere anche controllori autonomi, interfacce uomo-macchina (HMI) e altre piattaforme di telecontrollo.

### Esposizione delle interfacce e conseguenze operative

L’esposizione diretta su Internet delle funzionalità di amministrazione e controllo può agevolare l’individuazione delle risorse e i tentativi di accesso non autorizzato. Vulnerabilità, configurazioni non sicure e credenziali predefinite o compromesse possono consentire di utilizzare funzioni destinate esclusivamente agli operatori e ai manutentori.

La compromissione può permettere la modifica delle temperature impostate, della durata e della frequenza dei cicli di sbrinamento, delle soglie di allarme e delle modalità di notifica. L’alterazione dei dati visualizzati o la disabilitazione degli allarmi possono inoltre ritardare l’individuazione delle anomalie. I possibili impatti comprendono interruzioni della catena del freddo, deterioramento delle merci, indisponibilità degli impianti, sospensione delle attività e costi di ripristino.

La sola presenza di una pagina di autenticazione o di un certificato HTTPS non garantisce la sicurezza del sistema esposto. HTTPS protegge le comunicazioni, ma non impedisce lo sfruttamento di vulnerabilità applicative o l’utilizzo di credenziali compromesse.

La rimozione dell’esposizione pubblica deve pertanto essere accompagnata dalla segregazione delle reti e dalla protezione dei percorsi di amministrazione. L’accesso a una VPN o alla rete interna non deve consentire di raggiungere indiscriminatamente tutti i sistemi: le autorizzazioni devono limitare le risorse e le operazioni disponibili in funzione delle effettive esigenze.

## Azioni immediate

Si raccomanda di avviare immediatamente le seguenti attività, dando priorità alla rimozione delle esposizioni e alla verifica dell’integrità dei parametri operativi. Gli interventi devono essere coordinati tra responsabili della sicurezza informatica, responsabili degli impianti e manutentori, evitando interruzioni non controllate della refrigerazione.

**1. Identificazione dei sistemi e delle esposizioni**

- Censire controllori, sistemi SCADA, HMI, gateway OT/IoT, piattaforme di monitoraggio e servizi di teleassistenza, indicando ubicazione, responsabile, produttore, modello, versione e stato di supporto.
- Verificare la presenza di sistemi di gestione centralizzata della refrigerazione e dei relativi servizi di accesso remoto, indipendentemente dal produttore.
- Individuare console, API amministrative, servizi di accesso remoto e protocolli di controllo raggiungibili da Internet, verificando firewall, NAT, inoltro delle porte ed eventuali collegamenti autonomi, inclusi router cellulari e connessioni predisposte dai manutentori.
- Ricostruire i collegamenti tra reti IT, reti OT, piattaforme SCADA e reti di amministrazione e gestione, comprese le connessioni tra sedi, punti vendita e fornitori.
- Privilegiare l’esame delle configurazioni, degli inventari e del traffico già disponibile. Eventuali scansioni attive sui dispositivi OT devono essere preventivamente valutate e concordate con i responsabili degli impianti.

**2. Segregazione delle reti e protezione delle funzioni amministrative**

- Rimuovere l’esposizione diretta su Internet delle interfacce amministrative e dei servizi di controllo OT, intervenendo sui collegamenti di rete senza interrompere indiscriminatamente il funzionamento degli impianti.
- Segregare gli ambienti OT dalle reti IT aziendali, dalle reti degli utenti e dalle reti per ospiti, mediante separazione logica e filtraggio e, ove necessario, separazione fisica.
- Predisporre opportune reti di amministrazione e gestione, accessibili esclusivamente da postazioni e utenti autorizzati, evitando che le console amministrative siano raggiungibili dalle ordinarie postazioni di lavoro.
- Applicare regole di firewall che neghino le comunicazioni non espressamente autorizzate, consentendo soltanto sorgenti, destinazioni, servizi e porte necessari. La sola suddivisione in VLAN non sostituisce il filtraggio tra i segmenti.
- Limitare anche le comunicazioni in uscita dagli ambienti OT e dai sistemi di gestione, verificando che siano necessarie e autorizzate.
- Qualora la rimozione dell’esposizione non sia immediatamente attuabile, restringere temporaneamente l’accesso a indirizzi IP fidati, rafforzare il monitoraggio e definire tempi e responsabilità per la messa in sicurezza.

**3. Accessi remoti, VPN e protezione delle comunicazioni**

- Consentire l’amministrazione remota attraverso VPN aziendali o altre soluzioni di accesso controllato, mantenute aggiornate e protette con autenticazione a più fattori.
- Configurare gli accessi VPN affinché ciascun utente o manutentore possa raggiungere esclusivamente i sistemi necessari, attraverso le reti di amministrazione e gestione e, ove previsto, sistemi intermedi dedicati (jump host).
- Limitare gli accessi dei fornitori alle risorse e ai periodi autorizzati, registrando le attività e revocando le abilitazioni al termine dell’intervento.
- Qualora l’esposizione pubblica di un servizio web risulti strettamente necessaria, documentarne la motivazione e limitarne le funzionalità esposte. Utilizzare esclusivamente HTTPS con configurazioni TLS aggiornate e certificati validi, non scaduti, corrispondenti al nome del servizio e rilasciati da autorità di certificazione riconosciute dai client.
- Mantenere le funzionalità amministrative separate dal servizio pubblico e accessibili attraverso i canali protetti. Il ricorso a HTTPS non sostituisce VPN, autenticazione robusta, aggiornamenti e restrizioni di accesso.
- Disabilitare l’amministrazione tramite HTTP e altri protocolli non cifrati. Per componenti legacy che non supportano protocolli sicuri, confinare le comunicazioni in segmenti protetti in attesa della sostituzione.

**4. Verifica degli account e delle autenticazioni**

- Verificare tutti gli account amministrativi, tecnici e di manutenzione, disabilitando quelli inutilizzati, non riconosciuti o non più autorizzati.
- Sostituire le credenziali predefinite, deboli o riutilizzate e procedere con priorità alla rotazione delle credenziali associate a sistemi esposti o sospetti. Coordinare le modifiche agli account di servizio per evitare interruzioni delle integrazioni.
- Imporre l’autenticazione a più fattori sugli accessi remoti. Se il dispositivo OT non la supporta, applicarla sul sistema che ne media l’accesso.
- Utilizzare account individuali e privilegi limitati alle attività necessarie, distinguendo, ove possibile, le autorizzazioni di consultazione da quelle di modifica dei parametri.
- In caso di sospetta sottrazione delle credenziali, verificare e revocare anche sessioni, token e altri strumenti di accesso ancora validi.

**5. Verifica dei parametri e ricerca di possibili compromissioni**

- Confrontare le configurazioni correnti con quelle autorizzate, verificando temperature impostate, cicli di sbrinamento, programmi orari, soglie di allarme, destinatari delle notifiche e modalità di funzionamento.
- Verificare le temperature effettive e il funzionamento degli allarmi, ricorrendo, ove disponibili, anche a strumenti indipendenti dalla piattaforma di supervisione.
- Analizzare i log disponibili, estendendo la ricerca agli ultimi 90 giorni ove conservati, senza ritardare le verifiche immediate in caso di copertura inferiore.
- Ricercare accessi da sorgenti insolite, autenticazioni anomale, modifiche ai parametri, creazione di account, variazioni dei privilegi, disabilitazione degli allarmi e attività non riconducibili a interventi autorizzati.
- Correlare gli eventi dei controllori e delle piattaforme SCADA con quelli di VPN, firewall, sistemi di identità e strumenti di teleassistenza.
- Preservare log, configurazioni e altri elementi utili all’analisi prima di operazioni che possano cancellarli, compatibilmente con la messa in sicurezza degli impianti.

**6. Aggiornamento e dismissione dei dispositivi fuori supporto**

- Verificare con produttori e fornitori le versioni installate, gli aggiornamenti disponibili e le date di fine supporto, individuando i dispositivi a fine vita (End of Life, EOL) o che non ricevono più aggiornamenti di sicurezza.
- Applicare con priorità i correttivi disponibili, previa verifica della compatibilità e dell’impatto sui processi OT, predisponendo copie delle configurazioni e procedure di ripristino.
- Disattivare e dismettere i dispositivi EOL o fuori supporto non necessari, pianificando la sostituzione di quelli ancora impiegati nei processi operativi.
- Qualora la disattivazione immediata non sia compatibile con la sicurezza e la continuità degli impianti, isolare i dispositivi in segmenti dedicati, rimuoverne l’accessibilità diretta da Internet e consentire esclusivamente le comunicazioni indispensabili con sistemi autorizzati.
- Disabilitare sui dispositivi da sostituire i servizi non necessari, limitarne rigorosamente l’amministrazione e rafforzare il monitoraggio fino alla dismissione.
- Formalizzare un piano di sostituzione con responsabili e scadenze. L’isolamento costituisce una misura temporanea e non ripristina il supporto del produttore né elimina le vulnerabilità presenti.

## Misure di rafforzamento della postura

Si raccomanda di completare il riesame delle protezioni e formalizzare un piano per gli interventi che richiedano tempi più lunghi:

- Verifica della segregazione: controllare l’effettiva applicazione delle regole tra reti IT, ambienti OT, piattaforme SCADA e reti di amministrazione e gestione. Rimuovere collegamenti non autorizzati e regole eccessivamente permissive.
- Protezione della gestione centralizzata: limitare i privilegi con cui operatori e piattaforme possono intervenire su più siti; verificare che la compromissione di un singolo punto vendita o account non consenta accessi indiscriminati agli altri impianti.
- Controllo dei fornitori: riesaminare tutti i collegamenti di teleassistenza, compresi agenti software e connessioni avviate dall’interno verso servizi esterni, individuando responsabilità, autorizzazioni e modalità di revoca.
- Gestione di VPN e certificati: verificare aggiornamenti, configurazioni, account autorizzati e registrazione degli accessi sui gateway VPN; predisporre il monitoraggio della scadenza e il rinnovo dei certificati impiegati dai servizi web e dai canali di accesso remoto.
- Monitoraggio OT: predisporre controlli compatibili con gli impianti per rilevare connessioni inattese, modifiche ai parametri e anomalie di processo; verificare sincronizzazione temporale, conservazione dei log e recapito degli allarmi al personale incaricato.
- Backup e ripristino: verificare la disponibilità di copie protette delle configurazioni, dei programmi dei controllori e dei dati necessari al recupero delle piattaforme di supervisione. Testare il ripristino in condizioni compatibili con la continuità operativa.
- Continuità della catena del freddo: verificare procedure locali o manuali di emergenza, ove tecnicamente previste e sicure, e soluzioni alternative per la conservazione delle merci. Individuare il personale autorizzato ad attivarle e i relativi contatti.
- Risposta agli incidenti: effettuare un’esercitazione che coinvolga sicurezza informatica, responsabili degli impianti, manutentori, logistica e responsabili della sicurezza alimentare.
- Gestione continuativa: includere refrigerazione, climatizzazione (HVAC) e sistemi di gestione degli edifici nei programmi aziendali di inventario, gestione delle vulnerabilità, aggiornamento e controllo delle modifiche, monitorando anche lo stato di supporto e l’avanzamento delle sostituzioni.

## Gestione delle anomalie e segnalazione

Qualora siano rilevati accessi anomali, modifiche non autorizzate ai parametri degli impianti o altri indicatori di compromissione, si raccomanda di attivare tempestivamente le procedure di gestione degli incidenti e di effettuare immediata segnalazione all’Agenzia per la Cybersicurezza Nazionale tramite i canali istituzionali del CSIRT Italia.

Le attività di contenimento devono essere coordinate con i responsabili degli impianti, isolando i sistemi interessati e limitando gli accessi sospetti, nel rispetto delle condizioni operative di sicurezza. Riavvii, ripristini di fabbrica e riconfigurazioni devono essere pianificati con il supporto del produttore o del manutentore, preservando ove possibile gli elementi utili all’analisi.

Per i dispositivi coinvolti, il ripristino deve comprendere la verifica degli account, la rotazione dei segreti, l’applicazione dei correttivi e il recupero di configurazioni affidabili. Prima della riattivazione degli accessi remoti devono essere verificati il corretto funzionamento dell’impianto, l’integrità dei parametri, l’efficacia degli allarmi e la rimozione delle condizioni che hanno consentito l’accesso.

In presenza di anomalie termiche, la valutazione delle merci interessate deve essere affidata ai responsabili competenti secondo le procedure di sicurezza alimentare: il ripristino della temperatura non dimostra, da solo, il mantenimento delle condizioni di conservazione.

Le finestre temporali indicate costituiscono obiettivi operativi raccomandati per le attività di verifica e mitigazione e non sostituiscono gli obblighi di notifica applicabili.

| Titolo della tabella |  |  | 
|---|---|---|
| Versione | Note | Data | 
|---|---|---|
| 1.0 | Pubblicato il 13-10-2026 | 13/10/2026 | 
| 1.1 | Riproposto in primo piano a seguito dei recenti eventi rilevati sul territorio nazionale. | 03/11/2026 | 
| 1.2 | Riproposto in primo piano a seguito degli ulteriori eventi rilevati sul territorio nazionale. | 04/11/2026 | 

## Criticità

Alto (89.97)

## Argomenti

## Data pubblicazione

13/10/26 ore 12:44

## Data Ultimo Aggiornamento

04/11/26 ore 18:37
