import os 
import sys

def analizar_archivo(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            Lineas = len(lines)
            Palabras = sum(len(line.split()) for line in lines)
            Pythons = sum(line.lower().count('python') for line in lines)
            
            return Lineas, Palabras, Pythons
    except Exception:
        print(f"Error en el analisis del archivo {file_path}: {Exception}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <directorio>")
        sys.exit(1)

    directory = sys.argv[1]
    
    if not os.path.exists(directory):
        print(f"El directorio {directory} no existe.")
        sys.exit(1)

    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    
    if not txt_files:
        with open(os.path.join(directory, 'informe.txt'), 'w', encoding='utf-8') as analisis:
            analisis.write("No se encontraron archivos de texto.\n")
        print("No se encontraron archivos de texto.")
        return

    report_path = os.path.join(directory, 'informe.txt')
    with open(report_path, 'w', encoding='utf-8') as analisis:
        for txt_file in txt_files:
            file_path = os.path.join(directory, txt_file)
            analysis = analizar_archivo(file_path)
            if analysis:
                Lineas, Palabras, Pythons = analysis
                analisis.write(f"Archivo analizado: {txt_file}\n")
                analisis.write(f"Cantidad de líneas: {Lineas}\n")
                analisis.write(f"Cantidad total de palabras: {Palabras}\n")
                analisis.write(f"Cantidad de veces que aparece 'Python': {Pythons}\n")
                analisis.write("\n")
    print(f"El informe se genero en {report_path}")

if __name__ == "__main__":
    main()
