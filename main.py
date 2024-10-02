import os
import fitz
import re
from regex import printDBEntryes,path_checker


nomeFileOutput = 'out.txt'
nomeDirectory = 'PutAllHere'
nomeFileOutSQL='populateDB.sql'


def estraiInfoDaPDF(file_name,file_path, output_file_path,macroTPstr,microTPstr):
    try:
        doc = fitz.open(file_path)
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for page in doc:
                text = page.get_text("text")
                output_file.write(text)


        printDBEntryes(macroTPstr,microTPstr,nomeFileOutput,nomeFileOutSQL)
        
    except Exception as e:
        print(f"Errore nell'aprire o processare il file: {file_name}")
        print(f"Dettagli dell'errore: {e}")




def percorri_sottoalbero(root_dir, output_file_path):

    patternMacro = r'(.*)\d+_(.*)'
    patternMicro = r'(.*?).pdf'

    for root, _, files in os.walk(root_dir):
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        directory_name=os.path.basename(root)
        macroTP = re.findall(patternMacro,root,re.DOTALL)
        print(f'{indent}{directory_name}')

        if macroTP:    
            macroTPstr=macroTP[0][1]
            subindent = ' ' * 4 * (level + 1)

            for file_name in files:
                microTP = re.findall(patternMicro,file_name ,re.DOTALL)
                microTPstr=microTP[0]
                full_file_path = os.path.join(root, file_name)

                    
                print(f'{subindent}{microTPstr}')
                estraiInfoDaPDF(file_name,full_file_path, output_file_path,macroTPstr,microTPstr)
        
        

if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    directory_radice = os.path.join(script_dir, nomeDirectory)
    output_file_path = os.path.join(script_dir, nomeFileOutput)
    out_SQL_file= os.path.join(script_dir, nomeFileOutSQL)

    # Pulisci il file di output all'inizio
    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    if os.path.exists(out_SQL_file):
        os.remove(out_SQL_file)

    percorri_sottoalbero(directory_radice, output_file_path)
    print("Terminato")
