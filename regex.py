import re
import os
import unicodedata
import sys
from microMacroIDs import macrotopic_id_map, microtopic_id_map



def path_checker(path):
    if len(path) > 255:
        print(f"Errore: Il percorso supera i 255 caratteri:\n{path}")
        sys.exit(-3)  
    

#questionPattern = r'(\d+)\n(.*?)Pratico: (SI|NO)' #qui vorrei: (numero)\n (quello che voglio io ) ('Pratico: ')[No SI] 
questionPattern= r'\n(\d+?)\n(.*?)\nA:\n(.*?)\nB:\n(.*?)\nC:\n(.*?)\nD:\n(.*?)\nLivello: ([12])\n[Ss]ub-contenuto: (.*?)\nPratico: [NS][OI]'
#questionPattern=r'(\d)'


def printMatch(match):
    numeroDomanda = escape_sql_value(match[0])
    testoDomanda = escape_sql_value(match[1].strip().replace("\n", " "))
    rispostaCorretta = escape_sql_value(match[2].strip().replace("\n", " "))
    distrattore1 = escape_sql_value(match[3].strip().replace("\n", " "))
    distrattore2 = escape_sql_value(match[4].strip().replace("\n", " "))
    distrattore3 = escape_sql_value(match[5].strip().replace("\n", " "))
    livello = escape_sql_value(match[6].strip())  # Assuming 'score' for now as there's no score from regex
    subContenuto = escape_sql_value(match[7].strip().replace("\n", ""))
    
    print("\n--------------- Debug Info ---------------")
    print(f"Numero Domanda: {numeroDomanda}")
    print(f"Testo Domanda: {testoDomanda}")
    print(f"Risposta Corretta: {rispostaCorretta}")
    print(f"Distrattore 1: {distrattore1}")
    print(f"Distrattore 2: {distrattore2}")
    print(f"Distrattore 3: {distrattore3}")
    print(f"Livello: {livello}")
    print(f"Sub-contenuto: {subContenuto}")
    print("-" * 48 + "\n")

#def clean_text(text):
 #   text = unicodedata.normalize('NFKC', text)
  #  text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Rimuove i caratteri non-ASCII
   # return text
   # ciao

def clean_text(text):
    text = text.encode('utf-8', 'replace').decode('utf-8')
    return text



def escape_sql_value(value):
    """ Escape single quotes in SQL value """
    return value.replace("'", "''")


def printDBEntryes(macroTPstr,microTPstr,nomeFileInput,nomeFileOutSQL):
    
    MacroTopicId = macrotopic_id_map(macroTPstr)
    microTopicId = microtopic_id_map(microTPstr)    

    if MacroTopicId is None :
        print("ERRORE: M acrotopic non trovato in "+{macroTPstr}+" "+{microTPstr})
        exit(-1)
    if microTopicId is None :
        print("ERRORE: microtopic non trovato in "+{macroTPstr}+" "+{microTPstr})
        exit(-2)



    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_txt_file_path = os.path.join(script_dir,nomeFileInput)
    path_checker(out_txt_file_path)
    out_SQL_file= os.path.join(script_dir, nomeFileOutSQL)
    path_checker(out_SQL_file)

    with open(out_txt_file_path, 'r', encoding='utf-8') as input_file:
        with open(out_SQL_file,'a',encoding='utf-8')as populateDB:
            populateDB.write("INSERT INTO ProgettoQuizDB.quiz (macroTopicId, microTopicId, question, correctAnswer, distractor1, distractor2, distractor3, score, subcontent) VALUES\n")
            contenuto = input_file.read()
            contenuto = clean_text(contenuto) 
            matches = re.findall(questionPattern,contenuto,re.DOTALL)
            if not matches:
                print("ERRORE: nessun match trovato")
                exit(-1)
            for i, match in enumerate(matches):
                #numeroDomanda = escape_sql_value(match[0])
                testoDomanda = escape_sql_value(match[1].strip().replace("\n", " "))
                rispostaCorretta = escape_sql_value(match[2].strip().replace("\n", " "))
                distrattore1 = escape_sql_value(match[3].strip().replace("\n", " "))
                distrattore2 = escape_sql_value(match[4].strip().replace("\n", " "))
                distrattore3 = escape_sql_value(match[5].strip().replace("\n", " "))
                livello = escape_sql_value(match[6].strip())  # Assuming 'score' for now as there's no score from regex
                subContenuto = escape_sql_value(match[7].strip().replace("\n", ""))

                
                # mettiao le , tra una entry e l'altra ed il ; alla fine
                if i < len(matches) - 1:
                    comma = ','
                else:
                    comma = ';'
                
                populateDB.write(f"({MacroTopicId}, {microTopicId}, '{testoDomanda}', '{rispostaCorretta}', '{distrattore1}', '{distrattore2}', '{distrattore3}', {livello}, '{subContenuto}'){comma}\n")


    #print("\n"+macroTPstr+" in "+microTPstr+" terminato con successo")
