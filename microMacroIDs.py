import re
import unicodedata


def clean_text(text):
    # Normalizza il testo per decomporre i caratteri accentati
    text = unicodedata.normalize('NFKD', text)
    
    # Rimuovi i segni diacritici (accents) lasciando solo i caratteri "base"
    text = ''.join([char for char in text if not unicodedata.combining(char)])
    
    # Sostituisci l'apostrofo con uno spazio
    text = text.replace("'", " ")
    
    # Mantieni solo lettere (senza accenti), spazi, e rimuovi tutto il resto
    cleaned_text = re.sub(r'[^a-zA-Z ]+', '', text)
    
    # Rimuove spazi multipli consecutivi con un singolo spazio
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    
    # Rimuove eventuali spazi all'inizio e alla fine della stringa
    cleaned_text = cleaned_text.strip()
    
    # Converte tutto in minuscolo per uniformare il testo
    cleaned_text = cleaned_text.lower()
    
    return cleaned_text


def macrotopic_id_map(macrotopic):
    macro_topics = {
        'diritto del mercato': 1,
        'nozioni di matematica': 2,
        'nozioni di diritto tributario': 3,
        'nozioni di diritto previdenziale': 4,
        'nozioni di diritto privato': 5
    }
    
    macrotopic_cleaned = clean_text(macrotopic)
    
    return macro_topics.get(macrotopic_cleaned, None)



def microtopic_id_map(microtopic):
    micro_topics = {
        'abusi di mercato': 101,
        'appello al pubblico risparmio': 102,
        'attivita dei consulenti finanziari': 103,
        'disciplina dell albo unico dei consulenti finanziari': 104,
        'emittenti e societa con azioni quotate': 105,
        'gestione collettiva del risparmio': 106,
        'la normativa antiriciclaggio': 107,
        'mercati degli strumenti finanziari': 108,
        'organismo di vigilanza': 109,
        'promozione e collocamento a distanza': 110,
        'provvedimenti sanzionatori': 111,
        'requisiti e deontologia dei consulenti finanziari': 112,
        'servizi e attivita di investimento': 113,
        'trasparenza delle condizioni contrattuali': 114,
        'vigilanza su mercati e intermediari': 115,
        'analisi di scenario': 201,
        'costruzione del portafoglio': 202,
        'fondi comuni di investimento': 203,
        'futures': 204,
        'nozioni di matematica finanziaria': 205,
        'opzioni': 206,
        'strumenti derivati': 207,
        'strumenti di mercato monetario': 208,
        'strumenti e operativita': 209,
        'swap': 210,
        'titoli azionari': 211,
        'titoli di credito': 212,
        'titoli obbligazionari': 213,
        'titoli strutturati': 214,
        'valutazione delle obbligazioni': 215,
        'aspetti del sistema tributario': 301,
        'la tassazione degli strumenti del risparmio gestito': 302,
        'la tassazione degli strumenti di investimento diretto': 303,
        'la tassazione indiretta dei redditi finanziari': 304,
        'aspetti civilistici del contratto': 401,
        'aspetti tecnici attuariali e finanziari': 402,
        'aspetti tributari': 403,
        'gli intermediari assicurativi': 404,
        'i compiti dell istituto': 405,
        'i principi assicurativi': 406,
        'il tfr': 407,
        'la previdenza complementare': 408,
        'la previdenza pubblica': 409,
        'le imprese di assicurazione': 410,
        'tipologie di rami e polizze': 411,
        'beni e diritti reali nozione e disciplina': 501,
        'conclusione interpretazione': 502,
        'contratti tipici': 503,
        'le obbligazioni nozione e disciplina': 504,
        'l impresa nozione e disciplina': 505,
        'matrimonio rapporti patrimoniali': 506,
        'risoluzione e invalidita del contratto': 507,
        'scritture contabili e bilancio': 508,
        'societa di capitali disciplina e organizzazione': 509,
        'societa di persone disciplina e organizzazione': 510,
        'titoli di credito': 511,
        'vicende modificative della societa': 512
    }
    
    microtopic_cleaned = clean_text(microtopic)
    
    return micro_topics.get(microtopic_cleaned, None)
