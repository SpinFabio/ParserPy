import os
import fitz
import re
from regex import printDBEntryes
from microMacroIDs import microtopicIDmap, MacrotopicIDMap


nomeFileOutput = 'out.txt'
nomeDirectory = 'PutAllHere'

def clean_text(text):
    # Rimuove tutto tranne le lettere az, gli spazi e mantiene gli spazi solo interni
    cleaned_text = re.sub(r'[^a-zA-Z ]+', '', text)
    # Rimuove spazi multipli consecutivi con un singolo spazio
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    # Rimuove gli spazi all'inizio e alla fine della stringa
    cleaned_text = cleaned_text.strip()
    return cleaned_text

def estraiInfoDaPDF(file_path, output_file_path,MacroTP,microTP):
    try:
        doc = fitz.open(file_path)
        with open(output_file_path, 'a', encoding='utf-8') as output_file:
            for page in doc:
                text = page.get_text("text")
                output_file.write(text)
        MacroTopicId = microtopicIDmap(MacroTP)
        microTopicId = microtopicIDmap(microTP)

        print(MacroTP+" "+microTP)
        print(MacroTopicId+" "+microTopicId)


        if MacroTopicId is None :
            exit(-1)
        if microTopicId is None :
            exit(-2)

        #printDBEntryes(MacroTP,microTP,nomeDirectory,nomeFileOutput)
        


    except Exception as e:
        print(f"Errore nell'aprire o processare il file: {file_path}")
        print(f"Dettagli dell'errore: {e}")

def stampa_sottoalbero(root_dir, output_file_path):
    patternMacro = r'\d+_(.*)'  # Adjusted to capture entire macro topic name
    patternMicro = r'(.*?).pdf'  # Correct pattern for files

    for i, (root, dirs, files) in enumerate(os.walk(root_dir)):
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        stringa=os.path.basename(root)
        match = re.search(patternMacro, stringa)
        if match:
            MacroTP = match.group(1)
            MacroTP=clean_text(MacroTP)
            #print(f'{indent}{MacroTP}')
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                match = re.search(patternMicro, f)
                if match:
                    microTP = match.group(1)
                    microTP = clean_text(microTP)
                    #print(f'{subindent}{microTP}')
                    full_file_path = os.path.join(root, f)
                    estraiInfoDaPDF(full_file_path, output_file_path,MacroTP,microTP)
        else:
            print(f"{indent}ERRORE nella estrazione macrotopic numero {i+1}: {stringa}")

        

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    directory_radice = os.path.join(script_dir, nomeDirectory)
    output_file_path = os.path.join(script_dir, nomeFileOutput)
    # Pulisci il file di output all'inizio
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
    stampa_sottoalbero(directory_radice, output_file_path)
    print("Terminato")
