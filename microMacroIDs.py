

def MacrotopicIDMap(Macrotopic):
    # Dizionario che mappa i nomi dei macro argomenti ai loro ID
    print(Macrotopic)
    macro_topics = {
        'Diritto del mercato finanziario e degli intermediari': 1,
        'Nozioni di matematica finanza e di economia del mercato finanziario': 2,
        'Nozioni di diritto tributario riguardanti il mercato finanziario': 3,
        'Nozioni di diritto previdenziale e assicurativo': 4,
        'Nozioni di diritto privato e di diritto commerciale': 5
    }
    return macro_topics.get(Macrotopic, None) 

def microtopicIDmap(microtopic):
    print(microtopic)
    # Dizionario che mappa i nomi dei micro argomenti ai loro ID
    micro_topics = {
        'Abusi di mercato': 101,
        'Appello al pubblico risparmio': 102,
        'Attività dei consulenti finanziari': 103,
        'Disciplina dell\'Albo unico dei consulenti finanziari': 104,
        'Emittenti e società con azioni quotate': 105,
        'Gestione collettiva del risparmio': 106,
        'La normativa antiriciclaggio': 107,
        'Mercati degli strumenti finanziari': 108,
        'Organismo di vigilanza e tenuta dell\'albo unico dei consulenti finanziari': 109,
        'Promozione e collocamento a distanza e offerta fuori sede': 110,
        'Provvedimenti sanzionatori e cautelari nei confronti dei consulenti finanziari': 111,
        'Requisiti e deontologia dei consulenti finanziari': 112,
        'Servizi e attività di investimento': 113,
        'Trasparenza delle condizioni contrattuali e dei rapporti con i clienti': 114,
        'Vigilanza su mercati e intermediari': 115,
        'Analisi di scenario': 201,
        'Costruzione del portafoglio': 202,
        'Fondi comuni di investimento': 203,
        'Futures': 204,
        'Nozioni di matematica finanziaria': 205,
        'Opzioni': 206,
        'Strumenti derivati': 207,
        'Strumenti di mercato monetario': 208,
        'Strumenti e operatività': 209,
        'Swap': 210,
        'Titoli azionari': 211,
        'Titoli di credito': 212,
        'Titoli obbligazionari': 213,
        'Titoli strutturati': 214,
        'Valutazione delle obbligazioni': 215,
        'Aspetti del sistema tributario': 301,
        'La tassazione degli strumenti del risparmio gestito': 302,
        'La tassazione degli strumenti di investimento diretto': 303,
        'La tassazione indiretta dei redditi finanziari': 304,
        'Aspetti civilistici del contratto': 401,
        'Aspetti tecnici, attuariali e finanziari': 402,
        'Aspetti tributari': 403,
        'Gli intermediari assicurativi': 404,
        'I compiti dell\'Istituto per la vigilanza sulle assicurazioni': 405,
        'I principi assicurativi': 406,
        'Il TFR': 407,
        'La previdenza complementare': 408,
        'La previdenza pubblica': 409,
        'Le imprese di assicurazione': 410,
        'Tipologie di rami e polizze': 411,
        'Beni e diritti reali: nozione e disciplina': 501,
        'Conclusione, interpretazione e adempimento del contratto': 502,
        'Contratti tipici': 503,
        'Le obbligazioni: nozione e disciplina': 504,
        'L\'impresa: nozione e disciplina': 505,
        'Matrimonio, rapporti patrimoniali tra coniugi e impresa familiare': 506,
        'Risoluzione e invalidità del contratto': 507,
        'Scritture contabili e bilancio': 508,
        'Società di capitali: disciplina e organizzazione': 509,
        'Società di persone: disciplina e organizzazione': 510,
        'Titoli di credito': 511,
        'Vicende modificative della società e operazioni straordinarie': 512
    }
    return micro_topics.get(microtopic, None)  # Ritorna None se il micro argomento non è trovato
