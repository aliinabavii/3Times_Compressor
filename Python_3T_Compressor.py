import subprocess
import os

# Check if WinRAR is installed in the default path
winrar_path = "C:\\Program Files\\WinRAR\\WinRAR.exe"

if not os.path.exists(winrar_path):
    print("WinRAR not found on this system. Please install WinRAR.")
else:
    while True:
        # Get the path of the file dropped onto the program
        file_to_compress = input("Drag and drop a file here (or type 'q' to quit): ").strip('"')

        if file_to_compress.lower() == 'q':
            break

        # Get the directory of the file
        file_directory = os.path.dirname(file_to_compress)
        file_name = os.path.basename(file_to_compress)

        # Check if the file exists
        if not os.path.exists(file_to_compress):
            print("File not found.")
        else:
            # Change the current working directory to the file's directory
            os.chdir(file_directory)

            # Ask the user to choose between RAR or ZIP compression
            compression_format = input("Choose the compression format (RAR or ZIP): ").lower()

            if compression_format not in ['rar', 'zip']:
                print("Invalid compression format. Please choose RAR or ZIP.")
            else:
                # Compress the file into the specified format using WinRAR
                subprocess.run([winrar_path, "a", f"{file_name}.{compression_format}", file_name, f"-af{compression_format}"])
                subprocess.run([winrar_path, "a", f"{file_name}1.{compression_format}", f"{file_name}.{compression_format}", f"-af{compression_format}"])
                subprocess.run([winrar_path, "a", f"{file_name}_cmp3.{compression_format}", f"{file_name}1.{compression_format}", f"-af{compression_format}"])
                
                
                os.remove(f"{file_name}.{compression_format}")
                os.remove(f"{file_name}1.{compression_format}")
        

                print("File compressed successfully.")